#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sqlite3
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path

KINDS = {"status", "blocker", "request", "handoff", "impact_notice"}


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def parse_iso(s: str) -> datetime:
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    dt = datetime.fromisoformat(s)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def connect(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA synchronous=FULL;")
    return conn


def init_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS coord_events (
          seq INTEGER PRIMARY KEY AUTOINCREMENT,
          event_id TEXT UNIQUE NOT NULL,
          at TEXT NOT NULL,
          job_id TEXT NOT NULL,
          session_key TEXT NOT NULL,
          agent_id TEXT NOT NULL,
          subagent_id TEXT,
          kind TEXT NOT NULL,
          summary TEXT NOT NULL,
          refs_json TEXT,
          ttl_days INTEGER NOT NULL DEFAULT 7,
          non_sensitive INTEGER NOT NULL DEFAULT 1,
          supersedes_event_id TEXT,
          idempotency_key TEXT UNIQUE
        );
        CREATE INDEX IF NOT EXISTS idx_coord_kind_at ON coord_events(kind, at DESC);
        CREATE INDEX IF NOT EXISTS idx_coord_job_at ON coord_events(job_id, at DESC);
        """
    )
    conn.commit()


def emit_event(conn: sqlite3.Connection, payload: dict) -> dict:
    kind = payload["kind"]
    if kind not in KINDS:
        raise ValueError(f"invalid kind: {kind}")
    if not payload.get("safety", {}).get("non_sensitive", False):
        raise ValueError("shared coordination events must be non-sensitive")

    event_id = payload.get("event_id") or f"coord:{uuid.uuid4()}"
    with conn:
        if payload.get("idempotency_key"):
            hit = conn.execute(
                "SELECT event_id FROM coord_events WHERE idempotency_key = ?",
                (payload["idempotency_key"],),
            ).fetchone()
            if hit:
                return {"status": "duplicate", "event_id": hit[0]}

        conn.execute(
            """
            INSERT INTO coord_events(
              event_id, at, job_id, session_key, agent_id, subagent_id, kind, summary,
              refs_json, ttl_days, non_sensitive, supersedes_event_id, idempotency_key
            ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                event_id,
                payload.get("at") or now_iso(),
                payload["job_id"],
                payload["session_key"],
                payload.get("actor", {}).get("agent_id", "unknown"),
                payload.get("actor", {}).get("subagent_id"),
                kind,
                payload["summary"][:400],
                json.dumps(payload.get("refs", []), separators=(",", ":")),
                int(payload.get("ttl_days", 7)),
                1,
                payload.get("supersedes_event_id"),
                payload.get("idempotency_key"),
            ),
        )
    return {"status": "ok", "event_id": event_id}


def active_events(conn: sqlite3.Connection):
    rows = conn.execute(
        """
        SELECT event_id, at, job_id, session_key, agent_id, kind, summary, refs_json, ttl_days, supersedes_event_id
        FROM coord_events
        WHERE non_sensitive = 1
        ORDER BY at DESC, seq DESC
        """
    ).fetchall()
    out = []
    now = datetime.now(timezone.utc)
    superseded = {r[9] for r in rows if r[9]}
    for r in rows:
        event_id, at, job_id, session_key, agent_id, kind, summary, refs_json, ttl_days, _sup = r
        if event_id in superseded:
            continue
        if parse_iso(at) + timedelta(days=int(ttl_days)) < now:
            continue
        out.append(
            {
                "event_id": event_id,
                "at": at,
                "job_id": job_id,
                "session_key": session_key,
                "agent_id": agent_id,
                "kind": kind,
                "summary": summary,
                "refs": json.loads(refs_json or "[]"),
            }
        )
    return out


def render_workboard(events: list[dict], out_path: Path, max_items: int = 20) -> dict:
    latest_by_job: dict[str, dict] = {}
    blockers = []
    requests = []
    notable = []

    for e in events:
        if e["kind"] in {"status", "handoff"} and e["job_id"] not in latest_by_job:
            latest_by_job[e["job_id"]] = e
        if e["kind"] == "blocker":
            blockers.append(e)
        if e["kind"] == "request":
            requests.append(e)
        if e["kind"] in {"blocker", "request", "impact_notice"}:
            notable.append(e)

    def fmt(e: dict) -> str:
        refs = f" | refs: {', '.join(e['refs'])}" if e.get("refs") else ""
        return f"- [{e['at']}] ({e['job_id']}/{e['kind']}) {e['summary']}{refs}"

    lines = [
        "# WORKBOARD.md (Generated)",
        "",
        "Non-authoritative projection from coordination events.",
        "",
        "## Current Active Intents (by job)",
    ]
    if latest_by_job:
        for job in sorted(latest_by_job.keys()):
            lines.append(fmt(latest_by_job[job]))
    else:
        lines.append("- none")

    lines += ["", "## Open Blockers"]
    lines += [fmt(e) for e in blockers[:max_items]] or ["- none"]

    lines += ["", "## Open Cross-Job Requests"]
    lines += [fmt(e) for e in requests[:max_items]] or ["- none"]

    lines += ["", "## Recent Notable Events"]
    lines += [fmt(e) for e in notable[:max_items]] or ["- none"]
    lines.append("")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")
    return {
        "status": "ok",
        "path": str(out_path),
        "active_jobs": len(latest_by_job),
        "blockers": len(blockers),
        "requests": len(requests),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("command", choices=["init", "emit", "project"])
    ap.add_argument("--db", default="os/runtime/tde_state.sqlite")
    ap.add_argument("--payload-json", default="{}")
    ap.add_argument("--out", default="governance/WORKBOARD.md")
    args = ap.parse_args()

    conn = connect(Path(args.db))
    init_schema(conn)

    if args.command == "init":
        print(json.dumps({"status": "ok", "db": args.db}))
    elif args.command == "emit":
        payload = json.loads(args.payload_json)
        print(json.dumps(emit_event(conn, payload)))
    elif args.command == "project":
        print(json.dumps(render_workboard(active_events(conn), Path(args.out))))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

TASK_RE = re.compile(r"^- \[(?P<mark> |x)\] (?P<id>[A-Z][A-Z0-9-]+) \| (?P<title>.+)$")
SECTIONS = ["Inbox", "Triage", "Active", "Waiting", "Done"]


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def connect(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA synchronous=FULL;")
    return conn


def init_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS events (
          seq INTEGER PRIMARY KEY AUTOINCREMENT,
          event_id TEXT UNIQUE,
          at TEXT NOT NULL,
          type TEXT NOT NULL,
          payload_json TEXT NOT NULL,
          prev_hash TEXT,
          hash TEXT
        );

        CREATE TABLE IF NOT EXISTS actions (
          action_id TEXT PRIMARY KEY,
          idempotency_key TEXT UNIQUE NOT NULL,
          request_hash TEXT NOT NULL,
          state TEXT NOT NULL,
          response_json TEXT,
          created_at TEXT NOT NULL,
          updated_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS tasks (
          task_id TEXT PRIMARY KEY,
          title TEXT NOT NULL,
          status TEXT NOT NULL,
          checked INTEGER NOT NULL DEFAULT 0,
          version INTEGER NOT NULL DEFAULT 0,
          source TEXT,
          updated_at TEXT NOT NULL,
          metadata_json TEXT
        );
        """
    )
    conn.commit()


def parse_tasks_md(path: Path) -> list[dict]:
    lines = path.read_text(encoding="utf-8").splitlines()
    current = None
    out = []
    for raw in lines:
        if raw.startswith("## "):
            sec = raw[3:].strip()
            current = sec if sec in SECTIONS else None
            continue
        if not current:
            continue
        m = TASK_RE.match(raw.strip())
        if not m:
            continue
        out.append(
            {
                "task_id": m.group("id"),
                "title": m.group("title"),
                "status": current,
                "checked": 1 if m.group("mark") == "x" else 0,
            }
        )
    return out


def import_tasks(conn: sqlite3.Connection, tasks_path: Path) -> dict:
    parsed = parse_tasks_md(tasks_path)
    by_id = {row["task_id"]: row for row in parsed}  # last occurrence wins
    now = now_iso()
    with conn:
        conn.execute("DELETE FROM tasks")
        for row in by_id.values():
            conn.execute(
                """
                INSERT INTO tasks(task_id,title,status,checked,version,source,updated_at,metadata_json)
                VALUES(?,?,?,?,0,?,?,?)
                """,
                (row["task_id"], row["title"], row["status"], row["checked"], str(tasks_path), now, "{}"),
            )
    return {"imported": len(by_id), "raw_rows": len(parsed)}


def export_tasks(conn: sqlite3.Connection, out_path: Path) -> dict:
    rows = conn.execute(
        "SELECT task_id,title,status,checked FROM tasks ORDER BY status, task_id"
    ).fetchall()
    by = {s: [] for s in SECTIONS}
    for tid, title, status, checked in rows:
        mark = "x" if checked else " "
        if status in by:
            by[status].append(f"- [{mark}] {tid} | {title}")

    lines = ["# TASKS.md (Generated from tde_state_store)", ""]
    for s in SECTIONS:
        lines.append(f"## {s}")
        lines.extend(by[s])
        lines.append("")

    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return {"exported": len(rows), "path": str(out_path)}


def status_fingerprint(items: list[dict]) -> str:
    payload = json.dumps(sorted(items, key=lambda x: (x["status"], x["task_id"])), separators=(",", ":"))
    return hashlib.sha256(payload.encode()).hexdigest()


def _next_event_hash(conn: sqlite3.Connection, payload: dict) -> tuple[str | None, str]:
    prev = conn.execute("SELECT hash FROM events ORDER BY seq DESC LIMIT 1").fetchone()
    prev_hash = prev[0] if prev else None
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    base = (prev_hash or "") + raw
    curr = hashlib.sha256(base.encode()).hexdigest()
    return prev_hash, curr


def record_shadow_tick(conn: sqlite3.Connection, tick_id: str, artifact: dict) -> dict:
    now = now_iso()
    with conn:
        # durable action ledger entry for this tick
        request_hash = hashlib.sha256(json.dumps(artifact, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        conn.execute(
            """
            INSERT OR REPLACE INTO actions(action_id,idempotency_key,request_hash,state,response_json,created_at,updated_at)
            VALUES(?,?,?,?,?,?,?)
            """,
            (
                f"shadow:{tick_id}",
                f"shadow:{tick_id}",
                request_hash,
                artifact.get("status", "unknown"),
                json.dumps({"outcomes": artifact.get("outcomes"), "fail_closed": artifact.get("fail_closed")}),
                now,
                now,
            ),
        )

        # append event for tick summary
        summary = {
            "tick_id": tick_id,
            "status": artifact.get("status"),
            "outcomes": artifact.get("outcomes", {}),
            "claim_count": len(artifact.get("claimed", [])),
            "mutation_count": len(artifact.get("mutations", [])),
            "fail_closed": artifact.get("fail_closed", False),
        }
        prev_hash, curr_hash = _next_event_hash(conn, summary)
        conn.execute(
            """
            INSERT INTO events(event_id,at,type,payload_json,prev_hash,hash)
            VALUES(?,?,?,?,?,?)
            """,
            (
                f"evt:{tick_id}:summary",
                now,
                "job_tick_summary",
                json.dumps(summary, separators=(",", ":")),
                prev_hash,
                curr_hash,
            ),
        )

    return {"action_id": f"shadow:{tick_id}", "event_id": f"evt:{tick_id}:summary"}


def parity_check(conn: sqlite3.Connection, tasks_path: Path) -> dict:
    raw_file_items = parse_tasks_md(tasks_path)
    by_id = {row["task_id"]: row for row in raw_file_items}
    file_items = list(by_id.values())
    db_rows = conn.execute("SELECT task_id,title,status,checked FROM tasks").fetchall()
    db_items = [
        {"task_id": tid, "title": title, "status": status, "checked": checked}
        for tid, title, status, checked in db_rows
    ]
    f1 = status_fingerprint(file_items)
    f2 = status_fingerprint(db_items)
    return {
        "match": f1 == f2,
        "file_fingerprint": f1,
        "db_fingerprint": f2,
        "file_count": len(file_items),
        "db_count": len(db_items),
        "raw_file_rows": len(raw_file_items),
        "duplicate_rows": max(0, len(raw_file_items) - len(file_items)),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("command", choices=["init", "import-tasks", "export-tasks", "parity", "record-shadow-tick"])
    ap.add_argument("--db", default="os/runtime/tde_state.sqlite")
    ap.add_argument("--tasks", default="TASKS.md")
    ap.add_argument("--out", default="os/runtime/TASKS_from_db.md")
    ap.add_argument("--tick-id", default="shadow-tick")
    ap.add_argument("--artifact-json", default="{}")
    args = ap.parse_args()

    conn = connect(Path(args.db))
    init_schema(conn)

    if args.command == "init":
        print(json.dumps({"status": "ok", "db": args.db}))
    elif args.command == "import-tasks":
        print(json.dumps(import_tasks(conn, Path(args.tasks))))
    elif args.command == "export-tasks":
        print(json.dumps(export_tasks(conn, Path(args.out))))
    elif args.command == "parity":
        print(json.dumps(parity_check(conn, Path(args.tasks))))
    elif args.command == "record-shadow-tick":
        payload = json.loads(args.artifact_json)
        print(json.dumps(record_shadow_tick(conn, args.tick_id, payload)))


if __name__ == "__main__":
    main()

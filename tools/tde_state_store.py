#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

TASK_RE = re.compile(r"^- \[(?P<mark> |x)\] (?P<id>[A-Z][A-Z0-9-]+) \| (?P<title>.+)$")
SECTIONS = ["Inbox", "Triage", "Active", "Waiting", "Done"]
SUPPORTED_ACTIVATION_RULES = {"all_predecessors_done"}
CHAIN_METADATA_KEYS = {
    "depends_on",
    "activation_rule",
    "objective_id",
    "stage_id",
    "chain_policy",
    "activated_by",
    "activated_at",
}


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


def _safe_load_metadata(raw: str | None) -> dict[str, Any]:
    if not raw:
        return {}
    try:
        parsed = json.loads(raw)
    except Exception:
        return {}
    return parsed if isinstance(parsed, dict) else {}


def validate_chain_metadata(metadata: dict[str, Any]) -> tuple[bool, str | None]:
    if not isinstance(metadata, dict):
        return False, "metadata_not_object"

    chain = {k: metadata.get(k) for k in CHAIN_METADATA_KEYS if k in metadata}
    if not chain:
        return True, None

    depends_on = chain.get("depends_on")
    if depends_on is not None:
        if not isinstance(depends_on, list) or any(not isinstance(x, str) or not x.strip() for x in depends_on):
            return False, "invalid_depends_on"

    activation_rule = chain.get("activation_rule")
    if activation_rule is not None and activation_rule not in SUPPORTED_ACTIVATION_RULES:
        return False, "unsupported_activation_rule"

    objective_id = chain.get("objective_id")
    if objective_id is not None and (not isinstance(objective_id, str) or not objective_id.strip()):
        return False, "invalid_objective_id"

    stage_id = chain.get("stage_id")
    if stage_id is not None and (not isinstance(stage_id, str) or not stage_id.strip()):
        return False, "invalid_stage_id"

    chain_policy = chain.get("chain_policy")
    if chain_policy is not None and not isinstance(chain_policy, dict):
        return False, "invalid_chain_policy"

    activated_by = chain.get("activated_by")
    if activated_by is not None and (not isinstance(activated_by, str) or not activated_by.strip()):
        return False, "invalid_activated_by"

    activated_at = chain.get("activated_at")
    if activated_at is not None:
        if not isinstance(activated_at, str) or not activated_at.strip():
            return False, "invalid_activated_at"
        try:
            datetime.fromisoformat(activated_at)
        except Exception:
            return False, "invalid_activated_at"

    return True, None


def import_tasks(conn: sqlite3.Connection, tasks_path: Path, preserve_metadata: bool = True) -> dict:
    parsed = parse_tasks_md(tasks_path)
    by_id = {row["task_id"]: row for row in parsed}  # last occurrence wins
    now = now_iso()
    existing_meta: dict[str, str] = {}
    if preserve_metadata:
        existing_meta = {
            tid: meta or "{}"
            for tid, meta in conn.execute("SELECT task_id, metadata_json FROM tasks").fetchall()
        }

    with conn:
        conn.execute("DELETE FROM tasks")
        for row in by_id.values():
            metadata_json = existing_meta.get(row["task_id"], "{}")
            metadata = _safe_load_metadata(metadata_json)
            ok, reason = validate_chain_metadata(metadata)
            if not ok:
                raise ValueError(f"invalid_preserved_metadata:{row['task_id']}:{reason}")
            conn.execute(
                """
                INSERT INTO tasks(task_id,title,status,checked,version,source,updated_at,metadata_json)
                VALUES(?,?,?,?,0,?,?,?)
                """,
                (row["task_id"], row["title"], row["status"], row["checked"], str(tasks_path), now, json.dumps(metadata, separators=(",", ":"))),
            )
    return {"imported": len(by_id), "raw_rows": len(parsed), "preserved_metadata": preserve_metadata}


def read_tasks(conn: sqlite3.Connection, section: str | None = None) -> list[dict]:
    rows = conn.execute(
        "SELECT task_id,title,status,checked,version,updated_at,metadata_json FROM tasks ORDER BY task_id"
    ).fetchall()
    out = []
    for tid, title, status, checked, version, updated_at, metadata_json in rows:
        if section and status != section:
            continue
        metadata = _safe_load_metadata(metadata_json)
        out.append(
            {
                "task_id": tid,
                "title": title,
                "status": status,
                "checked": checked,
                "version": version,
                "updated_at": updated_at,
                "metadata": metadata,
                "metadata_json": json.dumps(metadata, separators=(",", ":")),
            }
        )
    return out


def update_task_metadata(conn: sqlite3.Connection, task_id: str, metadata_patch: dict[str, Any], replace: bool = False) -> dict:
    row = conn.execute("SELECT metadata_json FROM tasks WHERE task_id=?", (task_id,)).fetchone()
    if not row:
        raise KeyError(f"task_not_found:{task_id}")
    current = {} if replace else _safe_load_metadata(row[0])
    candidate = metadata_patch if replace else {**current, **metadata_patch}
    ok, reason = validate_chain_metadata(candidate)
    if not ok:
        raise ValueError(f"invalid_chain_metadata:{reason}")
    now = now_iso()
    with conn:
        conn.execute(
            "UPDATE tasks SET metadata_json=?, version=version+1, updated_at=? WHERE task_id=?",
            (json.dumps(candidate, separators=(",", ":")), now, task_id),
        )
    return {"task_id": task_id, "metadata": candidate, "updated_at": now}


def apply_ready_promotions(conn: sqlite3.Connection, promotions: list[dict[str, Any]]) -> dict[str, Any]:
    if not promotions:
        return {"applied": 0, "task_ids": []}
    now = now_iso()
    applied = []
    with conn:
        for item in promotions:
            row = conn.execute("SELECT status, metadata_json FROM tasks WHERE task_id=?", (item["task_id"],)).fetchone()
            if not row:
                continue
            status, metadata_json = row
            if status == "Active" or status == "Done":
                continue
            metadata = _safe_load_metadata(metadata_json)
            metadata["activated_by"] = item.get("activated_by")
            metadata["activated_at"] = item.get("activated_at") or now
            conn.execute(
                "UPDATE tasks SET status='Active', version=version+1, updated_at=?, metadata_json=? WHERE task_id=?",
                (now, json.dumps(metadata, separators=(",", ":")), item["task_id"]),
            )
            applied.append(item["task_id"])
    return {"applied": len(applied), "task_ids": applied}


def apply_low_risk_writeback_db(conn: sqlite3.Connection, claimed_ids: list[str], tick_id: str) -> dict:
    """Canonical DB write-back: move claimed tasks from Active -> Waiting and persist tick metadata."""
    if not claimed_ids:
        return {"applied": False, "reason": "no_tasks_or_no_claims", "moved": []}

    rows = conn.execute(
        f"SELECT task_id, metadata_json FROM tasks WHERE status='Active' AND task_id IN ({','.join('?' for _ in claimed_ids)})",
        claimed_ids,
    ).fetchall()
    if not rows:
        return {"applied": False, "reason": "no_active_claims_to_move", "moved": []}

    now = now_iso()
    moved = []
    with conn:
        for task_id, metadata_json in rows:
            metadata = _safe_load_metadata(metadata_json)
            metadata["last_tick_id"] = tick_id
            history = metadata.get("tick_history") or []
            if tick_id not in history:
                history = (history + [tick_id])[-10:]
            metadata["tick_history"] = history
            conn.execute(
                """
                UPDATE tasks
                SET status='Waiting', version=version+1, updated_at=?, metadata_json=?
                WHERE task_id=? AND status='Active'
                """,
                (now, json.dumps(metadata, separators=(",", ":")), task_id),
            )
            moved.append(task_id)

    return {
        "applied": True,
        "reason": None,
        "moved": moved,
        "targetSection": "Waiting",
    }


def export_tasks(conn: sqlite3.Connection, out_path: Path) -> dict:
    rows = conn.execute(
        "SELECT task_id,title,status,checked,metadata_json FROM tasks ORDER BY status, task_id"
    ).fetchall()
    by = {s: [] for s in SECTIONS}
    metadata_count = 0
    for tid, title, status, checked, metadata_json in rows:
        mark = "x" if checked else " "
        if status not in by:
            continue
        by[status].append(f"- [{mark}] {tid} | {title}")
        metadata = _safe_load_metadata(metadata_json)
        chain_metadata = {k: metadata[k] for k in CHAIN_METADATA_KEYS if k in metadata}
        if chain_metadata:
            metadata_count += 1
            by[status].append(f"  <!-- tde:metadata {json.dumps(chain_metadata, sort_keys=True)} -->")

    lines = ["# TASKS.md (Generated from tde_state_store)", ""]
    for s in SECTIONS:
        lines.append(f"## {s}")
        lines.extend(by[s])
        lines.append("")

    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return {"exported": len(rows), "path": str(out_path), "metadata_projected": metadata_count}


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

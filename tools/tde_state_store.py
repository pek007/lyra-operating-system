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
    ap.add_argument("command", choices=["init", "import-tasks", "export-tasks", "parity"])
    ap.add_argument("--db", default="os/runtime/tde_state.sqlite")
    ap.add_argument("--tasks", default="TASKS.md")
    ap.add_argument("--out", default="os/runtime/TASKS_from_db.md")
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


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
generate_tasks_view.py — Generate TASKS.md from tde_state.sqlite.

Usage:
    python3 tools/generate_tasks_view.py [--db PATH] [--out PATH] [--no-done]

TASKS.md is a generated artifact. Do not edit it manually.
Edit source data via TDE tools or direct DB writes.
"""

import argparse
import datetime
import json
import sqlite3
from pathlib import Path

DEFAULT_DB = Path(__file__).parent.parent / "os/runtime/tde_state.sqlite"
DEFAULT_OUT = Path(__file__).parent.parent / "TASKS.md"

# Canonical status ordering and display labels
STATUS_ORDER = ["Inbox", "Triage", "Active", "Waiting", "Done"]
# DB values are mixed-case; normalise to canonical
STATUS_ALIASES = {
    "inbox": "Inbox",
    "triage": "Triage",
    "active": "Active",
    "waiting": "Waiting",
    "done": "Done",
}


def normalise_status(raw: str) -> str:
    return STATUS_ALIASES.get(raw.lower(), raw)


def checkbox(status: str) -> str:
    return "[x]" if status == "Done" else "[ ]"


def format_metadata_comment(meta_json: str) -> str:
    if not meta_json:
        return ""
    try:
        meta = json.loads(meta_json)
    except (json.JSONDecodeError, TypeError):
        return ""
    if not meta:
        return ""
    return f"\n  <!-- tde:metadata {json.dumps(meta, separators=(',', ':'))} -->"


def load_tasks(db_path: Path) -> list[dict]:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    rows = cur.execute(
        "SELECT task_id, title, status, metadata_json, updated_at FROM tasks ORDER BY updated_at DESC"
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def bucket_tasks(tasks: list[dict]) -> dict[str, list[dict]]:
    buckets: dict[str, list[dict]] = {s: [] for s in STATUS_ORDER}
    for t in tasks:
        canonical = normalise_status(t["status"])
        if canonical not in buckets:
            buckets[canonical] = []
        buckets[canonical].append(t)
    return buckets


def render(buckets: dict[str, list[dict]], include_done: bool, generated_at: str) -> str:
    lines = [
        "# TASKS.md",
        "",
        "> **Generated artifact** — do not edit manually.",
        f"> Source: `os/runtime/tde_state.sqlite` | Generated: {generated_at}",
        "> To regenerate: `python3 tools/generate_tasks_view.py`",
        "",
    ]

    for section in STATUS_ORDER:
        if section == "Done" and not include_done:
            lines.append(f"## Done\n\n_(omitted — run without `--no-done` to include)_\n")
            continue

        items = buckets.get(section, [])
        lines.append(f"## {section}")

        if not items:
            lines.append("_(none)_")
            lines.append("")
            continue

        for t in items:
            cb = checkbox(section)
            task_id = t["task_id"]
            title = t["title"].rstrip(".")
            meta_comment = format_metadata_comment(t.get("metadata_json"))
            entry = f"- {cb} {task_id} | {title}{meta_comment}"
            lines.append(entry)

        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Generate TASKS.md from TDE SQLite state.")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB, help="Path to tde_state.sqlite")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT, help="Output path for TASKS.md")
    parser.add_argument("--no-done", action="store_true", help="Omit Done section from output")
    parser.add_argument("--stdout", action="store_true", help="Print to stdout instead of file")
    args = parser.parse_args()

    if not args.db.exists():
        raise FileNotFoundError(f"DB not found: {args.db}")

    tasks = load_tasks(args.db)
    buckets = bucket_tasks(tasks)
    generated_at = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    output = render(buckets, include_done=not args.no_done, generated_at=generated_at)

    if args.stdout:
        print(output)
    else:
        args.out.write_text(output, encoding="utf-8")
        total = sum(len(v) for v in buckets.values())
        print(f"Written {args.out} ({total} tasks, generated at {generated_at})")


if __name__ == "__main__":
    main()

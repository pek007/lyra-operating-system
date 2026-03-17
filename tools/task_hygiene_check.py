#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

OPEN_TASK_RE = re.compile(r"^- \[ \] ([A-Z]+-[0-9]{4}-[0-9]{3,}|IMP-AUTO-[0-9]{8}-[0-9]{2}) \|\s*(.+)$")


def normalize_intent(title: str) -> str:
    t = title.lower().strip()
    t = re.sub(r"`[^`]+`", "", t)
    t = re.sub(r"\([^)]*\)", "", t)
    t = re.sub(r"[^a-z0-9]+", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def check(file_path: Path) -> list[str]:
    errors: list[str] = []
    open_ids: dict[str, int] = {}
    intents: dict[str, tuple[str, int]] = {}

    lines = file_path.read_text(encoding="utf-8", errors="replace").splitlines()
    for i, line in enumerate(lines, start=1):
        m = OPEN_TASK_RE.match(line)
        if not m:
            continue
        task_id, title = m.group(1), m.group(2)
        if task_id in open_ids:
            errors.append(f"line {i}: duplicate open task ID {task_id} (first at line {open_ids[task_id]})")
        else:
            open_ids[task_id] = i

        intent = normalize_intent(title)
        if not intent:
            continue
        prior = intents.get(intent)
        if prior:
            prior_id, prior_line = prior
            if prior_id != task_id:
                errors.append(
                    f"line {i}: duplicate open task intent with {prior_id} (line {prior_line}) -> '{title}'"
                )
        else:
            intents[intent] = (task_id, i)

    return errors


def main() -> int:
    ap = argparse.ArgumentParser(description="Check generated TDE task projection hygiene")
    ap.add_argument("--file", default="os/runtime/TASKS_from_db.md")
    args = ap.parse_args()

    path = Path(args.file)
    if not path.exists():
        print(f"Missing file: {path}")
        return 2

    errors = check(path)
    if errors:
        print("TASKS hygiene check failed:")
        for e in errors:
            print(f"- {e}")
        return 1

    print("OK: generated TDE task projection open-task IDs and intents are unique")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

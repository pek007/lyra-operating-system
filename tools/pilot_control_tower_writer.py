#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

SECTIONS = ["Active", "Waiting", "Done"]


def count_sections(tasks_path: Path) -> dict[str, int]:
    lines = tasks_path.read_text(encoding="utf-8").splitlines()
    current = None
    out = {k: 0 for k in SECTIONS}
    for line in lines:
        if line.startswith("## "):
            sec = line[3:].strip()
            current = sec if sec in SECTIONS else None
            continue
        if current and re.match(r"^- \[[ x]\] ", line.strip()):
            out[current] += 1
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="os/runtime/tde_state.sqlite")
    ap.add_argument("--tasks", default="TASKS.md")
    ap.add_argument("--session-key", default="control_tower:main")
    ap.add_argument("--job-id", default="HEAD_OF_CONTROL_TOWER")
    ap.add_argument("--agent-id", default="lyra-main")
    ap.add_argument("--idempotency-key", default="pilot:control_tower:latest")
    args = ap.parse_args()

    counts = count_sections(Path(args.tasks))
    ts = datetime.now(timezone.utc).isoformat()
    summary = (
        f"Control Tower status at {ts}: Active={counts['Active']}, "
        f"Waiting={counts['Waiting']}, Done={counts['Done']}"
    )

    payload = {
        "artifactType": "coord_status_event",
        "schemaVersion": "1.0.0",
        "at": ts,
        "job_id": args.job_id,
        "session_key": args.session_key,
        "actor": {"agent_id": args.agent_id},
        "kind": "status",
        "summary": summary,
        "refs": ["TASKS.md"],
        "ttl_days": 7,
        "safety": {"non_sensitive": True},
        "idempotency_key": args.idempotency_key,
    }

    cmd = [
        "python3",
        "tools/coordination_workboard.py",
        "emit",
        "--db",
        args.db,
        "--payload-json",
        json.dumps(payload),
    ]
    out = subprocess.check_output(cmd, text=True)
    print(out.strip())


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Run docs/task hygiene checks as a single fail-fast command.

This restores the historical entrypoint used by runbooks and task evidence.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


COMMANDS = [
    ["python3", "tools/task_hygiene_check.py", "--file", "TASKS.md"],
    ["python3", "tools/markdown_link_check.py", "--changed-only"],
]


def run(cmd: list[str]) -> int:
    print(f"$ {' '.join(cmd)}")
    proc = subprocess.run(cmd, cwd=ROOT)
    return proc.returncode


def main() -> int:
    for cmd in COMMANDS:
        rc = run(cmd)
        if rc != 0:
            return rc
    print("Docs hygiene bundle passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())

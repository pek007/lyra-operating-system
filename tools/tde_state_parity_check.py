#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess


def run(cmd: list[str]) -> dict:
    out = subprocess.check_output(cmd, text=True)
    return json.loads(out)


def main() -> None:
    run(["python3", "tools/tde_state_store.py", "init"])
    imported = run(["python3", "tools/tde_state_store.py", "import-tasks"])
    parity = run(["python3", "tools/tde_state_store.py", "parity"])
    run(["python3", "tools/tde_state_store.py", "export-tasks"])

    if not parity.get("match"):
        raise SystemExit(f"[FAIL] parity mismatch: {parity}")

    print(f"[PASS] state parity ok (imported={imported.get('imported')}, count={parity.get('db_count')})")


if __name__ == "__main__":
    main()

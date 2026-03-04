#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path


def main() -> None:
    target = Path("tools/tde_job_tick_runner.py")
    text = target.read_text(encoding="utf-8")

    required = [
        "binding_unresolved_fail_closed",
        '"binding_status": "unproven"',
        '"writeback": {"applied": False, "reason": "binding_unresolved_fail_closed", "moved": []}',
    ]

    missing = [frag for frag in required if frag not in text]
    if missing:
        raise SystemExit(f"[FAIL] missing fail-closed binding guard fragments: {missing}")

    print("[PASS] binding fail-closed guard fragments present")


if __name__ == "__main__":
    main()

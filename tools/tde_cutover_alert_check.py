#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


def main() -> None:
    p = Path("knowledge/evidence/metrics/2026-03-04__tde-db-cutover-readiness-report-v1.json")
    if not p.exists():
        raise SystemExit("[FAIL] readiness report missing")

    r = json.loads(p.read_text(encoding="utf-8"))
    checks = r.get("checks", {})
    verdict = r.get("verdict", "NO_GO")
    consecutive = int(checks.get("parity_consecutive_failures", 0))
    threshold = int(checks.get("parity_threshold", 3))

    if consecutive >= threshold:
        raise SystemExit(f"[ALERT] consecutive parity failures {consecutive} >= threshold {threshold}")

    print(f"[PASS] cutover alert check ok (verdict={verdict}, consecutive={consecutive}/{threshold})")


if __name__ == "__main__":
    main()

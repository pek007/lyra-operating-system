#!/usr/bin/env python3
from __future__ import annotations

import glob
import json
from pathlib import Path


def _resolve_report_path() -> Path:
    latest = Path("knowledge/evidence/metrics/tde-db-cutover-readiness-report-latest.json")
    if latest.exists():
        return latest
    files = sorted(glob.glob("knowledge/evidence/metrics/*__tde-db-cutover-readiness-report-v1.json"))
    if files:
        return Path(files[-1])
    raise SystemExit("[FAIL] readiness report missing")


def main() -> None:
    p = _resolve_report_path()
    r = json.loads(p.read_text(encoding="utf-8"))
    checks = r.get("checks", {})
    verdict = r.get("verdict", "NO_GO")
    consecutive = int(checks.get("parity_consecutive_failures", 0))
    threshold = int(checks.get("parity_threshold", 3))

    if consecutive >= threshold:
        raise SystemExit(f"[ALERT] consecutive parity failures {consecutive} >= threshold {threshold}")

    print(f"[PASS] cutover alert check ok (verdict={verdict}, consecutive={consecutive}/{threshold}, report={p})")


if __name__ == "__main__":
    main()

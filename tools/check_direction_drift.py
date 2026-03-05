#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT_PATH = ROOT / "os/runtime/effective_direction_snapshot.json"
BASELINE_PATH = ROOT / "governance/effective_direction_baseline.json"
REPORT_PATH = ROOT / "os/runtime/effective_direction_drift_report.json"


def run_snapshot() -> dict:
    out = subprocess.check_output(["python3", "tools/gen_effective_direction_snapshot.py"], cwd=ROOT, text=True)
    return json.loads(out.strip())


def load_json(path: Path) -> dict | None:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline", default=str(BASELINE_PATH.relative_to(ROOT)))
    ap.add_argument("--snapshot", default=str(SNAPSHOT_PATH.relative_to(ROOT)))
    ap.add_argument("--report", default=str(REPORT_PATH.relative_to(ROOT)))
    ap.add_argument("--update-baseline", action="store_true")
    ap.add_argument("--evidence-ref", default="")
    args = ap.parse_args()

    # Always refresh snapshot first.
    run_snapshot()

    snapshot_path = ROOT / args.snapshot
    baseline_path = ROOT / args.baseline
    report_path = ROOT / args.report

    current = load_json(snapshot_path)
    if not current:
        print(json.dumps({"status": "error", "reason": "missing current snapshot"}))
        return 2

    baseline = load_json(baseline_path)
    now = datetime.now(timezone.utc).isoformat()

    if baseline is None:
        if args.update_baseline:
            baseline_path.parent.mkdir(parents=True, exist_ok=True)
            baseline_path.write_text(json.dumps(current, indent=2) + "\n", encoding="utf-8")
            print(json.dumps({"status": "ok", "message": "baseline created", "baseline": str(baseline_path.relative_to(ROOT))}))
            return 0
        print(json.dumps({"status": "error", "reason": "baseline_missing", "hint": "run with --update-baseline"}))
        return 2

    old_hash = baseline.get("root_hash")
    new_hash = current.get("root_hash")
    changed = old_hash != new_hash

    report = {
        "artifactType": "effective_direction_drift_report",
        "schemaVersion": "1.0.0",
        "checked_at": now,
        "baseline_path": str(baseline_path.relative_to(ROOT)),
        "snapshot_path": str(snapshot_path.relative_to(ROOT)),
        "baseline_root_hash": old_hash,
        "current_root_hash": new_hash,
        "changed": changed,
        "evidence_ref": args.evidence_ref or None,
        "status": "ok",
    }

    if changed and not args.evidence_ref:
        report["status"] = "fail"
        report["reason"] = "direction_drift_without_evidence_ref"

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    if args.update_baseline and (not changed or args.evidence_ref):
        baseline_path.write_text(json.dumps(current, indent=2) + "\n", encoding="utf-8")
        report["baseline_updated"] = True
        report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    print(json.dumps({
        "status": report["status"],
        "changed": changed,
        "baseline_root_hash": old_hash,
        "current_root_hash": new_hash,
        "report": str(report_path.relative_to(ROOT)),
    }))
    return 0 if report["status"] == "ok" else 1


if __name__ == "__main__":
    raise SystemExit(main())

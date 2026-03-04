#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "knowledge/evidence"

RULES = [
    ("tde-job-tick", "tde_job_tick", "1.0.0"),
    ("tde-canary-status", "tde_canary_status", "1.0.0"),
    ("tde-release-envelope", "tde_release_envelope", "1.0.0"),
]


def classify(path: Path, obj: dict) -> tuple[str, str] | None:
    name = path.name
    for needle, at, sv in RULES:
        if needle in name:
            return at, sv
    # fallback by shape
    if "tick_id" in obj and "job_id" in obj:
        return "tde_job_tick", "1.0.0"
    if "cycleTimestamp" in obj and "triggerSource" in obj:
        return "tde_canary_status", "1.0.0"
    if obj.get("artifactType") == "tde_release_envelope" or "releaseDecision" in obj:
        return "tde_release_envelope", "1.0.0"
    return None


def main() -> int:
    changed = 0
    scanned = 0
    for p in sorted(EVIDENCE.rglob("*.json")):
        scanned += 1
        try:
            obj = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        c = classify(p, obj)
        if not c:
            continue
        at, sv = c
        dirty = False
        if obj.get("artifactType") != at:
            obj["artifactType"] = at
            dirty = True
        if obj.get("schemaVersion") != sv:
            obj["schemaVersion"] = sv
            dirty = True
        if dirty:
            p.write_text(json.dumps(obj, indent=2) + "\n", encoding="utf-8")
            changed += 1
    print(json.dumps({"scanned": scanned, "updated": changed}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

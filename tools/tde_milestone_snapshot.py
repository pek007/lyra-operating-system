#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _extract_timestamp(payload: dict[str, Any]) -> str | None:
    for key in ("generatedAt", "cycleTimestamp", "sourceCycleTimestamp", "lastSummaryGeneratedAt"):
        value = payload.get(key)
        if isinstance(value, str) and value:
            return value
    return None


def _to_dt(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def _artifact_status(path: Path, stale_after_hours: int, now: datetime) -> dict[str, Any]:
    exists = path.exists()
    out: dict[str, Any] = {
        "path": str(path),
        "exists": exists,
        "stale": None,
        "ageHours": None,
        "timestampSource": None,
    }
    if not exists:
        out["status"] = "missing"
        return out

    mtime = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
    ts = mtime
    source = "mtime"

    if path.suffix.lower() == ".json":
        payload = _read_json(path)
        embedded = _to_dt(_extract_timestamp(payload))
        if embedded is not None:
            ts = embedded if embedded.tzinfo else embedded.replace(tzinfo=timezone.utc)
            source = "embedded"

    age_hours = (now - ts).total_seconds() / 3600.0
    stale = age_hours > stale_after_hours
    out.update(
        {
            "stale": stale,
            "ageHours": round(age_hours, 2),
            "timestamp": ts.isoformat(),
            "timestampSource": source,
            "status": "stale" if stale else "ok",
        }
    )
    return out


def build_snapshot(evidence_dir: Path, stale_after_hours: int) -> dict[str, Any]:
    now = datetime.now(timezone.utc)

    required = {
        "s4_status": evidence_dir / "tde-canary-status-latest.json",
        "s5_clean_cycles": evidence_dir / "tde-canary-simulation-3-clean-cycles.json",
        "s6_summary": evidence_dir / "tde-canary-operational-status-summary.json",
        "s6_note": evidence_dir / "tde-canary-operational-note.md",
        "s7_criteria": evidence_dir / "tde-broader-rollout-expansion-criteria.md",
        "s7_cycle": evidence_dir / "tde-broader-scope-simulated-cycle.json",
    }

    checks = {name: _artifact_status(path, stale_after_hours, now) for name, path in required.items()}
    missing = [name for name, result in checks.items() if result["status"] == "missing"]
    stale = [name for name, result in checks.items() if result["status"] == "stale"]

    s4 = _read_json(required["s4_status"]) if required["s4_status"].exists() else {}
    s6 = _read_json(required["s6_summary"]) if required["s6_summary"].exists() else {}
    s7 = _read_json(required["s7_cycle"]) if required["s7_cycle"].exists() else {}

    guardrail_signals: list[str] = []
    s4_violations = s4.get("guardrail", {}).get("violations", []) if isinstance(s4.get("guardrail", {}), dict) else []
    if any(str(v).startswith("approval_gate_bypass:") for v in s4_violations):
        guardrail_signals.append("s4_approval_gate_bypass_detected")

    if s6.get("guardrail", {}).get("status") not in (None, "ok"):
        guardrail_signals.append(f"s6_guardrail_status_{s6.get('guardrail', {}).get('status')}")

    if s7.get("guardrailEvaluation", {}).get("status") not in (None, "ok"):
        guardrail_signals.append(f"s7_guardrail_status_{s7.get('guardrailEvaluation', {}).get('status')}")

    consolidated = {
        "generatedAt": now.isoformat(),
        "staleAfterHours": stale_after_hours,
        "artifactChecks": checks,
        "integrity": {
            "missingArtifacts": missing,
            "staleArtifacts": stale,
            "guardrailSignals": guardrail_signals,
            "status": "ok" if not (missing or stale or guardrail_signals) else "attention_required",
        },
        "statusSnapshot": {
            "s4": {
                "counts": s4.get("counts"),
                "guardrailStatus": s4.get("guardrail", {}).get("status") if isinstance(s4.get("guardrail", {}), dict) else None,
                "consecutiveCleanCycles": s4.get("consecutiveCleanCycles"),
            },
            "s6": {
                "summary": s6.get("statusSummary"),
                "guardrailStatus": s6.get("guardrail", {}).get("status") if isinstance(s6.get("guardrail", {}), dict) else None,
            },
            "s7": {
                "decision": s7.get("broaderRolloutDecision"),
                "counts": s7.get("counts"),
                "stalledRatio": s7.get("stalledRatio"),
                "guardrailStatus": s7.get("guardrailEvaluation", {}).get("status") if isinstance(s7.get("guardrailEvaluation", {}), dict) else None,
            },
        },
    }

    return consolidated


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate consolidated TDE milestone snapshot from S4-S7 artifacts")
    parser.add_argument("--env", choices=["dev", "staging", "prod"], default=None)
    parser.add_argument("--evidence-dir", default=None)
    parser.add_argument("--stale-after-hours", type=int, default=24)
    parser.add_argument(
        "--output-path",
        default=None,
    )
    args = parser.parse_args()

    if args.env:
        period = datetime.now(timezone.utc).strftime('%Y-%m')
        evidence_dir = Path(args.evidence_dir) if args.evidence_dir else Path(f"knowledge/evidence/{args.env}/{period}")
        output_path = Path(args.output_path) if args.output_path else evidence_dir / "tde-milestone-s4-s7-snapshot.json"
    else:
        evidence_dir = Path(args.evidence_dir or "knowledge/evidence/2026-03")
        output_path = Path(args.output_path or "knowledge/evidence/2026-03/tde-milestone-s4-s7-snapshot.json")

    snapshot = build_snapshot(evidence_dir, stale_after_hours=args.stale_after_hours)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"snapshotPath": str(output_path), "integrity": snapshot["integrity"]}))


if __name__ == "__main__":
    main()

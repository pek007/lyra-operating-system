#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _read_json(path: Path, default: dict[str, Any] | None = None) -> dict[str, Any]:
    if not path.exists():
        return default or {}
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _trend(current: int, prior: int | None, better_when_lower: bool = False) -> str:
    if prior is None:
        return "baseline"
    if current == prior:
        return "flat"
    if better_when_lower:
        return "improving" if current < prior else "worsening"
    return "improving" if current > prior else "worsening"


def build_outputs(
    status_path: Path,
    summary_path: Path,
    checklist_path: Path,
    note_path: Path,
    state_path: Path,
) -> dict[str, Any]:
    status = _read_json(status_path)
    prior_state = _read_json(state_path)

    counts = status.get("counts", {})
    guardrail = status.get("guardrail", {})

    active = int(counts.get("active", 0))
    at_risk = int(counts.get("atRisk", 0))
    stalled = int(counts.get("stalled", 0))

    prior_counts = prior_state.get("counts", {}) if prior_state else {}
    summary = {
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "sourceCycleTimestamp": status.get("cycleTimestamp"),
        "sourceTrigger": status.get("triggerSource"),
        "statusSummary": {
            "activeBackground": {
                "count": active,
                "trend": _trend(active, prior_counts.get("active"), better_when_lower=False),
            },
            "atRisk": {
                "count": at_risk,
                "trend": _trend(at_risk, prior_counts.get("atRisk"), better_when_lower=True),
            },
            "stalled": {
                "count": stalled,
                "trend": _trend(stalled, prior_counts.get("stalled"), better_when_lower=True),
            },
        },
        "guardrail": {
            "status": guardrail.get("status", "unknown"),
            "violations": guardrail.get("violations", []),
            "thresholdBreached": bool(guardrail.get("thresholdBreached", False)),
        },
    }

    _write_json(summary_path, summary)

    # Rollout-readiness checklist
    checks: list[tuple[str, bool, str]] = [
        (
            "Cycle status artifact generated",
            bool(status.get("cycleTimestamp")),
            "Requires one complete runtime cycle output.",
        ),
        (
            "Operational summary generated",
            True,
            "Status summary includes active-background/at-risk/stalled with trend.",
        ),
        (
            "Guardrail is non-alert",
            summary["guardrail"]["status"] == "ok",
            "Fail-closed posture must remain intact; alerts block rollout.",
        ),
        (
            "No approval-gate bypass violation",
            not any(v.startswith("approval_gate_bypass:") for v in summary["guardrail"]["violations"]),
            "Any bypass is a hard blocker.",
        ),
        (
            "Consecutive clean cycles >= 3",
            int(status.get("consecutiveCleanCycles", 0)) >= 3,
            "Canary stabilization threshold from S5.",
        ),
    ]

    checklist_lines = [
        "# TDE Canary Rollout Readiness Checklist",
        "",
        f"Generated: {summary['generatedAt']}",
        f"Source cycle: {summary.get('sourceCycleTimestamp')}",
        "",
    ]
    for label, passed, note in checks:
        mark = "[x]" if passed else "[ ]"
        checklist_lines.append(f"- {mark} {label} — {note}")

    overall_ready = all(c[1] for c in checks)
    checklist_lines.extend(["", f"Overall readiness: {'READY' if overall_ready else 'NOT_READY'}", ""])
    _write_text(checklist_path, "\n".join(checklist_lines))

    # Single operational note surfacing guardrail alerts
    violations = summary["guardrail"]["violations"]
    note_lines = [
        "# TDE Canary Operational Note",
        "",
        f"Generated: {summary['generatedAt']}",
        f"Cycle: {summary.get('sourceCycleTimestamp')} ({summary.get('sourceTrigger')})",
        f"Guardrail status: {summary['guardrail']['status'].upper()}",
        "",
        "Status snapshot:",
        f"- active-background: {active} ({summary['statusSummary']['activeBackground']['trend']})",
        f"- at-risk: {at_risk} ({summary['statusSummary']['atRisk']['trend']})",
        f"- stalled: {stalled} ({summary['statusSummary']['stalled']['trend']})",
        "",
    ]

    if violations:
        note_lines.append("Guardrail alerts:")
        for violation in violations:
            note_lines.append(f"- {violation}")
    else:
        note_lines.append("Guardrail alerts:")
        note_lines.append("- none")

    note_lines.extend(["", f"Rollout gate decision: {'GO' if overall_ready else 'HOLD'}", ""])
    _write_text(note_path, "\n".join(note_lines))

    _write_json(
        state_path,
        {
            "lastSummaryGeneratedAt": summary["generatedAt"],
            "sourceCycleTimestamp": summary.get("sourceCycleTimestamp"),
            "counts": {"active": active, "atRisk": at_risk, "stalled": stalled},
            "guardrailStatus": summary["guardrail"]["status"],
        },
    )

    return {
        "summaryPath": str(summary_path),
        "checklistPath": str(checklist_path),
        "notePath": str(note_path),
        "statePath": str(state_path),
        "overallReadiness": "READY" if overall_ready else "NOT_READY",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Build TDE canary operational status/readiness artifacts")
    parser.add_argument("--status-path", default="knowledge/evidence/2026-03/tde-canary-status-latest.json")
    parser.add_argument("--summary-path", default="knowledge/evidence/2026-03/tde-canary-operational-status-summary.json")
    parser.add_argument("--checklist-path", default="knowledge/evidence/2026-03/tde-canary-rollout-readiness-checklist.md")
    parser.add_argument("--note-path", default="knowledge/evidence/2026-03/tde-canary-operational-note.md")
    parser.add_argument("--state-path", default="knowledge/evidence/2026-03/tde-canary-operational-summary-state.json")
    args = parser.parse_args()

    outputs = build_outputs(
        status_path=Path(args.status_path),
        summary_path=Path(args.summary_path),
        checklist_path=Path(args.checklist_path),
        note_path=Path(args.note_path),
        state_path=Path(args.state_path),
    )
    print(json.dumps(outputs))


if __name__ == "__main__":
    main()

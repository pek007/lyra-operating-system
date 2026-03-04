#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

from tde_kernel import TDEKernel, TriggerContract


def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    now = datetime.now(timezone.utc)

    # Bounded expansion criteria (fail-closed, no external dependencies)
    expansion_criteria = {
        "expansionWindow": {"fromMaxItems": 3, "toMaxItems": 8},
        "scopeRule": "expand high-priority local tasks only; no 3PP integrations",
        "requiredPreconditions": {
            "consecutiveCleanCyclesMin": 3,
            "guardrailStatus": "ok",
            "approvalGateBypass": "forbidden",
        },
        "cycleHealthThresholds": {
            "maxStalledCount": 1,
            "maxStalledRatio": 0.25,
        },
        "rollbackTriggers": [
            "guardrail.status == alert",
            "approval_gate_bypass detected",
            "stalled_count > 1 in broadened cycle",
        ],
    }

    criteria_path = Path("knowledge/evidence/2026-03/tde-broader-rollout-expansion-criteria.md")
    criteria_md = "\n".join(
        [
            "# TDE Canary→Broader Rollout Bounded Expansion Criteria",
            "",
            f"Generated: {now.isoformat()}",
            "",
            "- Expansion bound: max scope from 3 to 8 high-priority local tasks per cycle.",
            "- Scope restriction: local-only task set (no 3PP, no new repo, fail-closed policy preserved).",
            "- Preconditions: at least 3 consecutive clean canary cycles; guardrail status must be `ok`; no approval-gate bypass violations.",
            "- Health thresholds during broadened cycle: stalled count <= 1 and stalled ratio <= 25%.",
            "- Rollback triggers: any guardrail alert, any approval-gate bypass, or stalled count threshold breach.",
            "",
            "```json",
            json.dumps(expansion_criteria, indent=2),
            "```",
            "",
        ]
    )
    _write_text(criteria_path, criteria_md)

    # Guardrail-preserving checklist for broadened rollout
    checklist_path = Path("knowledge/evidence/2026-03/tde-broader-rollout-checklist.md")

    kernel = TDEKernel()
    items = [
        {
            "id": "TASK-BROAD-1",
            "priority": "high",
            "lastMeaningfulEventAt": (now - timedelta(minutes=25)).isoformat(),
            "nextExpectedCheckpointAt": (now + timedelta(minutes=40)).isoformat(),
        },
        {
            "id": "TASK-BROAD-2",
            "priority": "high",
            "lastMeaningfulEventAt": (now - timedelta(minutes=60)).isoformat(),
            "nextExpectedCheckpointAt": (now + timedelta(minutes=30)).isoformat(),
        },
        {
            "id": "TASK-BROAD-3",
            "priority": "high",
            "lastMeaningfulEventAt": (now - timedelta(minutes=170)).isoformat(),
            "nextExpectedCheckpointAt": (now + timedelta(minutes=5)).isoformat(),
        },
        {
            "id": "TASK-BROAD-4",
            "priority": "high",
            "lastMeaningfulEventAt": (now - timedelta(minutes=185)).isoformat(),
            "nextExpectedCheckpointAt": (now - timedelta(minutes=10)).isoformat(),
        },
        {
            "id": "TASK-BROAD-5",
            "priority": "high",
            "lastMeaningfulEventAt": (now - timedelta(hours=6)).isoformat(),
            "nextExpectedCheckpointAt": (now - timedelta(hours=1)).isoformat(),
            "stallReasonCode": "WAITING_APPROVAL",
        },
        {
            "id": "TASK-BROAD-6",
            "priority": "high",
            "lastMeaningfulEventAt": (now - timedelta(minutes=35)).isoformat(),
            "nextExpectedCheckpointAt": (now + timedelta(minutes=45)).isoformat(),
        },
    ]

    trigger = TriggerContract(
        trigger_source="cron",
        trigger_id=f"cron-tde-broader-scope-{now.strftime('%Y%m%d-%H%M%S')}",
        session_key="cron:tde-broader-rollout-v1",
        actor="lyra",
        job="JOB-ENG-001",
        triggered_at=now.isoformat(),
    )

    cycle = kernel.run_runtime_triggered_cycle(trigger, items, now=now)

    counts = {"active": 0, "atRisk": 0, "stalled": 0}
    approval_bypass = []
    for c in cycle["classifications"]:
        if c["state"] == "active-background":
            counts["active"] += 1
        elif c["state"] == "at-risk":
            counts["atRisk"] += 1
        elif c["state"] == "stalled":
            counts["stalled"] += 1

    for route in cycle["followups"]:
        if route["requiresApproval"] and route["status"] != "blocked_pending_approval":
            approval_bypass.append(route["targetId"])

    stalled_ratio = counts["stalled"] / len(cycle["classifications"]) if cycle["classifications"] else 0.0
    guardrail_ok = len(approval_bypass) == 0
    within_health_bounds = counts["stalled"] <= 1 and stalled_ratio <= 0.25

    cycle_artifact = {
        "generatedAt": now.isoformat(),
        "cycle": cycle,
        "counts": counts,
        "stalledRatio": round(stalled_ratio, 4),
        "expansionCriteria": expansion_criteria,
        "guardrailEvaluation": {
            "approvalGateBypassDetected": approval_bypass,
            "status": "ok" if guardrail_ok else "alert",
        },
        "healthEvaluation": {
            "withinBounds": within_health_bounds,
            "maxStalledCount": expansion_criteria["cycleHealthThresholds"]["maxStalledCount"],
            "maxStalledRatio": expansion_criteria["cycleHealthThresholds"]["maxStalledRatio"],
        },
        "broaderRolloutDecision": "GO" if guardrail_ok and within_health_bounds else "HOLD",
    }

    cycle_path = Path("knowledge/evidence/2026-03/tde-broader-scope-simulated-cycle.json")
    _write_json(cycle_path, cycle_artifact)

    checks = [
        ("Bounded expansion criteria defined", True, "Criteria file exists with explicit numeric bounds and rollback triggers."),
        ("Broader scope remains local-only", True, "Simulated item set only includes local high-priority tasks."),
        (
            "Approval-required routes stay blocked pending approval",
            guardrail_ok,
            "Any bypass of approval gate is a hard blocker.",
        ),
        (
            "Broadened-cycle stalled count and ratio within bounds",
            within_health_bounds,
            "Require stalled <= 1 and stalled ratio <= 25%.",
        ),
        (
            "Broader rollout decision is explicit",
            True,
            f"Decision from simulated cycle: {cycle_artifact['broaderRolloutDecision']}.",
        ),
    ]

    lines = [
        "# TDE Broader Rollout Checklist (Guardrail-Preserving)",
        "",
        f"Generated: {now.isoformat()}",
        f"Source cycle artifact: `{cycle_path}`",
        "",
    ]
    for label, passed, note in checks:
        lines.append(f"- {'[x]' if passed else '[ ]'} {label} — {note}")

    lines.extend([
        "",
        f"Overall decision: {cycle_artifact['broaderRolloutDecision']}",
        "",
    ])
    _write_text(checklist_path, "\n".join(lines))

    print(
        json.dumps(
            {
                "criteriaPath": str(criteria_path),
                "checklistPath": str(checklist_path),
                "cyclePath": str(cycle_path),
                "decision": cycle_artifact["broaderRolloutDecision"],
                "counts": counts,
                "stalledRatio": round(stalled_ratio, 4),
            }
        )
    )


if __name__ == "__main__":
    main()

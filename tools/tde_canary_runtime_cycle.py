#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from tde_kernel_slice_tests import TDEKernel, TriggerContract


def _default_items(now: datetime, simulate_clean: bool) -> list[dict[str, Any]]:
    if simulate_clean:
        return [
            {
                "id": "TASK-CANARY-ACTIVE-1",
                "priority": "high",
                "tde_canary": True,
                "lastMeaningfulEventAt": (now - timedelta(minutes=20)).isoformat(),
                "nextExpectedCheckpointAt": (now + timedelta(minutes=50)).isoformat(),
            },
            {
                "id": "TASK-CANARY-AT-RISK-1",
                "priority": "high",
                "tde_canary": True,
                "lastMeaningfulEventAt": (now - timedelta(minutes=150)).isoformat(),
                "nextExpectedCheckpointAt": (now + timedelta(minutes=10)).isoformat(),
            },
        ]

    return [
        {
            "id": "TASK-CANARY-STALE",
            "priority": "high",
            "tde_canary": True,
            "lastMeaningfulEventAt": (now - timedelta(hours=6)).isoformat(),
            "nextExpectedCheckpointAt": (now - timedelta(hours=1)).isoformat(),
            "stallReasonCode": "WAITING_APPROVAL",
        },
        {
            "id": "TASK-CANARY-ACTIVE",
            "priority": "high",
            "tde_canary": True,
            "lastMeaningfulEventAt": (now - timedelta(minutes=30)).isoformat(),
            "nextExpectedCheckpointAt": (now + timedelta(minutes=45)).isoformat(),
        },
    ]




TASK_LINE_RE = re.compile(r"^- \[ \] (?P<id>[A-Z0-9-]+) \| (?P<title>.+)$")


def _load_active_tasks_as_canary_items(tasks_path: Path, now: datetime) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    if not tasks_path.exists():
        return [], {"source": "tasks", "used": False, "reason": "tasks_path_missing", "tasksPath": str(tasks_path)}

    lines = tasks_path.read_text(encoding="utf-8").splitlines()
    in_active = False
    parsed = 0
    skipped = 0
    items: list[dict[str, Any]] = []

    for raw in lines:
        line = raw.strip()
        if raw.startswith("## "):
            in_active = raw.strip() == "## Active"
            continue
        if not in_active or not line:
            continue

        m = TASK_LINE_RE.match(line)
        if not m:
            skipped += 1
            continue

        task_id = m.group("id")
        title = m.group("title")
        parsed += 1

        items.append({
            "id": task_id,
            "title": title,
            "priority": "high",
            "tde_canary": True,
            # deterministic normalization defaults until richer metadata is wired
            "lastMeaningfulEventAt": (now - timedelta(minutes=30)).isoformat(),
            "nextExpectedCheckpointAt": (now + timedelta(minutes=45)).isoformat(),
        })

    return items, {
        "source": "tasks",
        "used": len(items) > 0,
        "tasksPath": str(tasks_path),
        "parsedActiveTasks": parsed,
        "skippedLines": skipped,
    }

def _load_state(state_path: Path) -> dict[str, Any]:
    if not state_path.exists():
        return {"consecutiveCleanCycles": 0, "lastCycleTimestamp": None}
    return json.loads(state_path.read_text(encoding="utf-8"))


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def run_cycle(
    trigger_source: str,
    stalled_alert_threshold: int,
    artifact_path: Path,
    state_path: Path,
    simulate_clean: bool = False,
    tasks_path: Path | None = None,
) -> dict[str, Any]:
    now = datetime.now(timezone.utc)
    kernel = TDEKernel()

    normalization = {"source": "synthetic-default", "used": True}
    if tasks_path is not None:
        loaded_items, normalization = _load_active_tasks_as_canary_items(tasks_path, now)
        items = loaded_items if loaded_items else _default_items(now, simulate_clean=simulate_clean)
        if not loaded_items:
            normalization = {**normalization, "fallback": "synthetic-default"}
    else:
        items = _default_items(now, simulate_clean=simulate_clean)

    canary_items = [i for i in items if i.get("tde_canary") is True and i.get("priority") == "high"]

    trigger = TriggerContract(
        trigger_source=trigger_source,
        trigger_id=f"{trigger_source}-tde-canary-{now.strftime('%Y%m%d-%H%M%S')}",
        session_key="main" if trigger_source == "heartbeat" else "cron:tde-canary-v1",
        actor="lyra",
        job="JOB-ENG-001",
        triggered_at=now.isoformat(),
    )

    cycle = kernel.run_runtime_triggered_cycle(trigger, canary_items, now=now)
    state_counts = {
        "active": 0,
        "atRisk": 0,
        "stalled": 0,
    }
    reason_summary: dict[str, int] = {}

    for c in cycle["classifications"]:
        if c["state"] == "active-background":
            state_counts["active"] += 1
        elif c["state"] == "at-risk":
            state_counts["atRisk"] += 1
        elif c["state"] == "stalled":
            state_counts["stalled"] += 1
            reason = c.get("stallReasonCode") or "UNKNOWN_NEEDS_TRIAGE"
            reason_summary[reason] = reason_summary.get(reason, 0) + 1

    guardrail_violations: list[str] = []
    for route in cycle["followups"]:
        if route["requiresApproval"] and route["status"] != "blocked_pending_approval":
            guardrail_violations.append(
                f"approval_gate_bypass:{route['targetId']}:{route['status']}"
            )

    threshold_breached = state_counts["stalled"] > stalled_alert_threshold
    if threshold_breached:
        guardrail_violations.append(
            f"stalled_threshold_breached:{state_counts['stalled']}>{stalled_alert_threshold}"
        )

    prior_state = _load_state(state_path)
    prior_streak = int(prior_state.get("consecutiveCleanCycles", 0))
    clean_cycle = len(guardrail_violations) == 0
    clean_streak = prior_streak + 1 if clean_cycle else 0

    artifact = {
        "artifactType": "tde_canary_status",
        "schemaVersion": "1.0.0",
        "cycleTimestamp": cycle["cycleTimestamp"],
        "triggerSource": cycle["trigger"]["triggerSource"],
        "triggerId": cycle["trigger"]["triggerId"],
        "evaluatedCount": len(cycle["classifications"]),
        "inputNormalization": normalization,
        "counts": state_counts,
        "stalledCount": state_counts["stalled"],
        "stallReasonSummary": reason_summary,
        "routes": cycle["followups"],
        "guardrail": {
            "stalledAlertThreshold": stalled_alert_threshold,
            "thresholdBreached": threshold_breached,
            "violations": guardrail_violations,
            "status": "alert" if guardrail_violations else "ok",
        },
        "cleanCycle": clean_cycle,
        "consecutiveCleanCycles": clean_streak,
    }

    _write_json(artifact_path, artifact)
    _write_json(
        state_path,
        {
            "consecutiveCleanCycles": clean_streak,
            "lastCycleTimestamp": cycle["cycleTimestamp"],
            "lastGuardrailStatus": artifact["guardrail"]["status"],
        },
    )

    return artifact


def main() -> None:
    parser = argparse.ArgumentParser(description="Run one TDE canary runtime cycle")
    parser.add_argument("--trigger-source", choices=["heartbeat", "cron"], default="cron")
    parser.add_argument("--stalled-alert-threshold", type=int, default=1)
    parser.add_argument(
        "--artifact-path",
        default="knowledge/evidence/2026-03/tde-canary-status-latest.json",
    )
    parser.add_argument(
        "--state-path",
        default="knowledge/evidence/2026-03/tde-canary-cycle-state.json",
    )
    parser.add_argument("--simulate-clean", action="store_true")
    parser.add_argument("--tasks-path", default="TASKS.md")
    args = parser.parse_args()

    artifact = run_cycle(
        trigger_source=args.trigger_source,
        stalled_alert_threshold=args.stalled_alert_threshold,
        artifact_path=Path(args.artifact_path),
        state_path=Path(args.state_path),
        simulate_clean=args.simulate_clean,
        tasks_path=Path(args.tasks_path) if args.tasks_path else None,
    )
    print(json.dumps(artifact))


if __name__ == "__main__":
    main()

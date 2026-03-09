#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

SUPPORTED_ACTIVATION_RULE = "all_predecessors_done"
TERMINAL_STATUSES = {"Done"}
NON_READY_ELIGIBLE = {"Inbox", "Triage", "Waiting"}


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def evaluate_ready_promotions(tasks: list[dict[str, Any]], *, tick_id: str, current_time: str | None = None) -> dict[str, Any]:
    by_id = {t["task_id"]: t for t in tasks}
    promoted: list[dict[str, Any]] = []
    skipped: list[dict[str, Any]] = []
    timestamp = current_time or now_iso()

    for task in tasks:
        metadata = task.get("metadata") or {}
        depends_on = metadata.get("depends_on")
        if not depends_on:
            continue

        status = task.get("status")
        if status == "Active":
            continue
        if status in TERMINAL_STATUSES:
            skipped.append({"task_id": task["task_id"], "reason": "terminal_status", "status": status})
            continue
        if status not in NON_READY_ELIGIBLE:
            skipped.append({"task_id": task["task_id"], "reason": "unsupported_source_status", "status": status})
            continue

        activation_rule = metadata.get("activation_rule", SUPPORTED_ACTIVATION_RULE)
        if activation_rule != SUPPORTED_ACTIVATION_RULE:
            skipped.append({"task_id": task["task_id"], "reason": "unsupported_activation_rule", "activation_rule": activation_rule})
            continue

        missing = [pred for pred in depends_on if pred not in by_id]
        if missing:
            skipped.append({"task_id": task["task_id"], "reason": "missing_predecessor", "missing": missing})
            continue

        incomplete = [pred for pred in depends_on if by_id[pred].get("status") != "Done"]
        if incomplete:
            skipped.append({"task_id": task["task_id"], "reason": "predecessors_not_done", "incomplete": incomplete})
            continue

        promoted.append(
            {
                "task_id": task["task_id"],
                "from_status": status,
                "to_status": "Active",
                "depends_on": depends_on,
                "activation_rule": activation_rule,
                "objective_id": metadata.get("objective_id"),
                "stage_id": metadata.get("stage_id"),
                "activated_by": f"tick:{tick_id}",
                "activated_at": timestamp,
            }
        )

    return {"promoted": promoted, "skipped": skipped, "tick_id": tick_id, "evaluated": len(tasks)}

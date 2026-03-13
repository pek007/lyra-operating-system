#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

REQUIRED_POLICY_FIELDS = {
    "artifactType",
    "schemaVersion",
    "policy_id",
    "workflow_family",
    "delegated_role",
    "escalation_role",
    "allowed_outcomes",
    "allowed_next_step_types",
    "confidence_threshold",
    "risk_threshold",
    "write_scope_boundary",
    "max_autonomous_hops",
    "retry_limit",
    "research_budget",
    "mandatory_escalation_triggers",
    "enabled",
}

ALLOWED_OUTCOMES = {"continue", "branch", "block", "retry", "defer", "research_further"}
RISK_LEVELS = {"low", "medium", "high", "critical"}
COST_LEVELS = {"low", "medium", "high", None}


def _read_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("policy_not_object")
    return payload


def validate_policy_envelope(payload: dict[str, Any]) -> tuple[bool, str | None]:
    missing = [key for key in REQUIRED_POLICY_FIELDS if key not in payload]
    if missing:
        return False, f"missing_required_fields:{','.join(sorted(missing))}"

    if payload.get("artifactType") != "tde_decision_policy_envelope":
        return False, "artifact_type_mismatch"
    if payload.get("schemaVersion") != "1.0.0":
        return False, "schema_version_mismatch"
    if payload.get("delegated_role") != "Product Owner":
        return False, "delegated_role_mismatch"
    if payload.get("escalation_role") != "Ultimate Decision-maker":
        return False, "escalation_role_mismatch"

    allowed = payload.get("allowed_outcomes")
    if not isinstance(allowed, list) or not allowed:
        return False, "invalid_allowed_outcomes"
    if any(item not in ALLOWED_OUTCOMES for item in allowed):
        return False, "invalid_allowed_outcome_value"

    if payload.get("risk_threshold") not in RISK_LEVELS:
        return False, "invalid_risk_threshold"
    if payload.get("cost_threshold") not in COST_LEVELS:
        return False, "invalid_cost_threshold"

    confidence = payload.get("confidence_threshold")
    if not isinstance(confidence, (int, float)) or not (0 <= confidence <= 1):
        return False, "invalid_confidence_threshold"

    for key in ("write_scope_boundary", "allowed_next_step_types", "mandatory_escalation_triggers"):
        value = payload.get(key)
        if not isinstance(value, list) or not value or any(not isinstance(x, str) or not x.strip() for x in value):
            return False, f"invalid_{key}"

    research_budget = payload.get("research_budget")
    if not isinstance(research_budget, dict):
        return False, "invalid_research_budget"
    max_rounds = research_budget.get("max_rounds")
    if not isinstance(max_rounds, int) or max_rounds < 0:
        return False, "invalid_research_budget_max_rounds"

    for key in ("max_autonomous_hops", "retry_limit"):
        value = payload.get(key)
        if not isinstance(value, int) or value < 0:
            return False, f"invalid_{key}"

    if not isinstance(payload.get("enabled"), bool):
        return False, "invalid_enabled"

    workflow_family = payload.get("workflow_family")
    if not isinstance(workflow_family, str) or not workflow_family.strip():
        return False, "invalid_workflow_family"

    return True, None


def resolve_policy_envelope(policy_ref: str, *, workspace_root: Path) -> tuple[dict[str, Any] | None, str | None, str | None]:
    if not isinstance(policy_ref, str) or not policy_ref.strip():
        return None, "decision_policy_ref_missing", None

    ref_path = Path(policy_ref)
    path = ref_path if ref_path.is_absolute() else (workspace_root / ref_path)
    if not path.exists() or not path.is_file():
        return None, "decision_policy_ref_unresolved", str(path)

    try:
        payload = _read_json(path)
    except Exception:
        return None, "decision_policy_envelope_invalid", str(path)

    ok, reason = validate_policy_envelope(payload)
    if not ok:
        return None, "decision_policy_envelope_invalid", str(path)

    return payload, None, str(path)


def validate_task_policy_binding(metadata: dict[str, Any], *, workspace_root: Path, expected_outcome: str = "continue") -> dict[str, Any]:
    if not isinstance(metadata, dict):
        return {"ok": False, "reason": "decision_policy_ref_missing"}

    workflow_family = metadata.get("workflow_family")
    policy_ref = metadata.get("decision_policy_ref")
    envelope, reason, resolved_path = resolve_policy_envelope(policy_ref, workspace_root=workspace_root)
    if reason:
        return {"ok": False, "reason": reason, "policy_ref": policy_ref, "resolved_path": resolved_path}

    assert envelope is not None
    if workflow_family and envelope.get("workflow_family") != workflow_family:
        return {
            "ok": False,
            "reason": "decision_policy_workflow_family_mismatch",
            "policy_ref": policy_ref,
            "resolved_path": resolved_path,
            "workflow_family": workflow_family,
            "envelope_workflow_family": envelope.get("workflow_family"),
        }

    allowed = envelope.get("allowed_outcomes") or []
    if expected_outcome not in allowed:
        return {
            "ok": False,
            "reason": "decision_outcome_not_authorized",
            "policy_ref": policy_ref,
            "resolved_path": resolved_path,
            "expected_outcome": expected_outcome,
        }

    return {
        "ok": True,
        "policy_ref": policy_ref,
        "resolved_path": resolved_path,
        "workflow_family": workflow_family or envelope.get("workflow_family"),
        "envelope": envelope,
    }

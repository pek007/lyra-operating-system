#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from tde_decision_policy import validate_task_policy_binding


def run_tests() -> None:
    workspace_root = Path(__file__).resolve().parents[1]

    ok = validate_task_policy_binding(
        {
            "workflow_family": "implementation_verification_readiness",
            "decision_policy_ref": "products/task-management/07-decisions/REFERENCE_TDE_POLICY_ENVELOPE_IMPLEMENTATION_VERIFICATION_V1.json",
        },
        workspace_root=workspace_root,
        expected_outcome="continue",
    )
    assert ok["ok"] is True

    missing = validate_task_policy_binding(
        {"workflow_family": "implementation_verification_readiness"},
        workspace_root=workspace_root,
        expected_outcome="continue",
    )
    assert missing["ok"] is False
    assert missing["reason"] == "decision_policy_ref_missing"

    mismatch = validate_task_policy_binding(
        {
            "workflow_family": "wrong_family",
            "decision_policy_ref": "products/task-management/07-decisions/REFERENCE_TDE_POLICY_ENVELOPE_IMPLEMENTATION_VERIFICATION_V1.json",
        },
        workspace_root=workspace_root,
        expected_outcome="continue",
    )
    assert mismatch["ok"] is False
    assert mismatch["reason"] == "decision_policy_workflow_family_mismatch"

    print("[PASS] TDE decision policy tests passed")


if __name__ == "__main__":
    run_tests()

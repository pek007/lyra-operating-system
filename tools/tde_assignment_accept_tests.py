#!/usr/bin/env python3
from __future__ import annotations

import tempfile
from pathlib import Path

from tde_assignment_accept import accept_assignment, ValidationError
from tde_state_store import connect


def _packet(**overrides):
    base = {
        "artifactType": "tde_assignment_packet",
        "schemaVersion": "1.0.0",
        "assignment_id": "TASK-20260314-TEST-ASSIGNMENT",
        "source_system": "control-panel-poc",
        "source_reference": "cp:test:1",
        "submitted_at": "2026-03-14T21:00:00Z",
        "submitted_by": "Control Panel",
        "title": "Test assignment",
        "summary": "Bounded test assignment for acceptance semantics.",
        "requested_action": "Drive the assignment through acceptance semantics.",
        "priority_hint": "high",
        "workspace_scope": "lyra-os-root",
        "product_scope": "A-007",
        "related_entities": [],
        "evidence_links": [],
        "assignment_owner_role": "Product Owner",
        "runner_binding_required": True,
        "objective_id": "OBJ-TEST-001",
        "decision_policy_ref": "products/task-management/policy.json",
        "workflow_family": "implementation_verification_readiness",
        "metadata": {},
    }
    base.update(overrides)
    return base


def run_tests() -> None:
    with tempfile.TemporaryDirectory() as td:
        db = Path(td) / "tde.sqlite"

        accepted = accept_assignment(packet=_packet(), db_path=db)
        assert accepted["acceptance_state"] == "accepted"
        assert accepted["task_id"] == "TASK-20260314-TEST-ASSIGNMENT"

        duplicate = accept_assignment(packet=_packet(), db_path=db)
        assert duplicate["status"] == "duplicate"

        no_runner = accept_assignment(packet=_packet(assignment_id="TASK-NO-RUNNER", objective_id=None, runner_binding_required=False), db_path=db)
        assert no_runner["acceptance_state"] == "accepted_no_runner"

        pending = accept_assignment(packet=_packet(assignment_id="TASK-PENDING", decision_policy_ref=None), db_path=db)
        assert pending["acceptance_state"] == "accepted_pending_binding"

        conn = connect(db)
        row = conn.execute("SELECT status, metadata_json FROM tasks WHERE task_id=?", ("TASK-PENDING",)).fetchone()
        assert row is not None
        assert row[0] == "Waiting"
        assert "accepted_pending_binding" in row[1]

        bad = _packet()
        del bad["title"]
        try:
            accept_assignment(packet=bad, db_path=db)
            raise AssertionError("expected ValidationError")
        except ValidationError:
            pass

    print("[PASS] TDE assignment accept tests passed")


if __name__ == "__main__":
    run_tests()

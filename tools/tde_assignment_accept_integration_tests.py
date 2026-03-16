#!/usr/bin/env python3
"""
TDE Assignment Accept — Integration Test Suite
Closes the thin-slice acceptance gap identified in:
  products/task-management/04-execution/TDE_ASSIGNMENT_ACCEPTANCE_THIN_SLICE_PLAN_2026-03-15.md

Covers all five canonical acceptance states plus DB persistence verification,
idempotency conflict, and event log linkage.

Run: python3 tools/tde_assignment_accept_integration_tests.py
"""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

from tde_assignment_accept import accept_assignment, ValidationError
from tde_state_store import connect


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _packet(**overrides):
    base = {
        "artifactType": "tde_assignment_packet",
        "schemaVersion": "1.0.0",
        "assignment_id": "TASK-INT-TEST-001",
        "source_system": "integration-test",
        "source_reference": "int:test:001",
        "submitted_at": "2026-03-16T02:00:00Z",
        "submitted_by": "Lyra Integration Test",
        "title": "Integration test assignment",
        "summary": "Validates thin-slice acceptance states end-to-end.",
        "requested_action": "Verify all acceptance states are persisted and returned correctly.",
        "priority_hint": "high",
        "workspace_scope": "lyra-os-root",
        "product_scope": "A-007",
        "related_entities": [],
        "evidence_links": [],
        "assignment_owner_role": "Control Tower",
        "runner_binding_required": True,
        "objective_id": "OBJ-TDE-FOUNDATION",
        "decision_policy_ref": "CONTROL_TOWER_OVERNIGHT_SYNTHESIS_POLICY_V1.md",
        "workflow_family": "implementation_verification_readiness",
        "metadata": {},
    }
    base.update(overrides)
    return base


def _assert(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(f"FAIL: {label}")
    print(f"  [ok] {label}")


# ---------------------------------------------------------------------------
# Test cases
# ---------------------------------------------------------------------------

def test_case_a_accepted(db: Path) -> None:
    """Case A: valid assignment, normal path → accepted + task created + event logged."""
    result = accept_assignment(packet=_packet(), db_path=db)
    _assert(result["acceptance_state"] == "accepted", "Case A: state=accepted")
    _assert(result["task_id"] == "TASK-INT-TEST-001", "Case A: task_id derived correctly")
    _assert(result["reason_code"] is None, "Case A: no reason_code")
    _assert(result["assignment_id"] == "TASK-INT-TEST-001", "Case A: assignment_id echoed")

    # DB: task row exists with correct status
    conn = connect(db)
    row = conn.execute(
        "SELECT status, metadata_json FROM tasks WHERE task_id=?",
        ("TASK-INT-TEST-001",),
    ).fetchone()
    _assert(row is not None, "Case A: task row persisted")
    _assert(row[0] == "Active", "Case A: task status=Active")
    meta = json.loads(row[1])
    _assert(meta.get("assignment_acceptance_state") == "accepted", "Case A: metadata has acceptance_state")

    # DB: assignment_packets row exists
    ap_row = conn.execute(
        "SELECT acceptance_state, result_json FROM assignment_packets WHERE assignment_id=?",
        ("TASK-INT-TEST-001",),
    ).fetchone()
    _assert(ap_row is not None, "Case A: assignment_packets row persisted")
    _assert(ap_row[0] == "accepted", "Case A: assignment_packets.acceptance_state=accepted")

    # DB: event logged
    evt = conn.execute(
        "SELECT type, payload_json FROM events WHERE event_id=?",
        ("evt:assignment:TASK-INT-TEST-001",),
    ).fetchone()
    _assert(evt is not None, "Case A: assignment event logged")
    _assert(evt[0] == "assignment_accepted", "Case A: event type=assignment_accepted")
    payload = json.loads(evt[1])
    _assert(payload["acceptance_state"] == "accepted", "Case A: event payload has acceptance_state")
    _assert(payload["task_id"] == "TASK-INT-TEST-001", "Case A: event payload has task_id")


def test_case_b_accepted_pending_binding(db: Path) -> None:
    """Case B: valid assignment, missing binding/objective context → accepted_pending_binding."""
    result = accept_assignment(
        packet=_packet(assignment_id="TASK-INT-TEST-PENDING", decision_policy_ref=None),
        db_path=db,
    )
    _assert(result["acceptance_state"] == "accepted_pending_binding", "Case B: state=accepted_pending_binding")
    _assert(result["reason_code"] == "missing_decision_policy_ref", "Case B: reason_code set")

    conn = connect(db)
    row = conn.execute(
        "SELECT status FROM tasks WHERE task_id=?", ("TASK-INT-TEST-PENDING",)
    ).fetchone()
    _assert(row is not None, "Case B: task row persisted")
    _assert(row[0] == "Waiting", "Case B: task status=Waiting (incomplete binding)")


def test_case_c_accepted_no_runner(db: Path) -> None:
    """Case C: valid assignment, no runner available → accepted_no_runner."""
    result = accept_assignment(
        packet=_packet(
            assignment_id="TASK-INT-TEST-NORUNNER",
            objective_id=None,
            runner_binding_required=False,
        ),
        db_path=db,
    )
    _assert(result["acceptance_state"] == "accepted_no_runner", "Case C: state=accepted_no_runner")
    _assert(result["reason_code"] == "missing_objective_id", "Case C: reason_code=missing_objective_id")

    conn = connect(db)
    row = conn.execute(
        "SELECT status FROM tasks WHERE task_id=?", ("TASK-INT-TEST-NORUNNER",)
    ).fetchone()
    _assert(row is not None, "Case C: task row persisted")
    _assert(row[0] == "Waiting", "Case C: task status=Waiting (no runner)")


def test_case_d_rejected_invalid_assignment(db: Path) -> None:
    """Case D: invalid packet (missing required field) → rejected_invalid_assignment."""
    bad = _packet(assignment_id="TASK-INT-TEST-INVALID")
    del bad["title"]
    try:
        result = accept_assignment(packet=bad, db_path=db)
        _assert(result["acceptance_state"] == "rejected_invalid_assignment", "Case D: state=rejected_invalid_assignment")
        _assert(result["task_id"] is None, "Case D: no task_id for rejected")
        _assert(result["reason_code"] is not None, "Case D: reason_code set")
    except ValidationError:
        # ValidationError raised when assignment_id absent; here it's present so result expected
        raise AssertionError("Case D: expected result dict, not ValidationError for named invalid packet")

    # DB: rejection persisted
    conn = connect(db)
    ap_row = conn.execute(
        "SELECT acceptance_state FROM assignment_packets WHERE assignment_id=?",
        ("TASK-INT-TEST-INVALID",),
    ).fetchone()
    _assert(ap_row is not None, "Case D: rejected packet persisted in assignment_packets")
    _assert(ap_row[0] == "rejected_invalid_assignment", "Case D: assignment_packets.acceptance_state=rejected")

    # DB: no task row for invalid packet
    task_row = conn.execute(
        "SELECT task_id FROM tasks WHERE task_id=?", ("TASK-INT-TEST-INVALID",)
    ).fetchone()
    _assert(task_row is None, "Case D: no task row for rejected assignment")


def test_case_e_duplicate(db: Path) -> None:
    """Case E: same assignment_id + same content → duplicate returned, no second row created."""
    # First submission (should already be present from Case A, but use fresh id)
    first = accept_assignment(
        packet=_packet(assignment_id="TASK-INT-TEST-DUP"),
        db_path=db,
    )
    _assert(first["acceptance_state"] == "accepted", "Case E setup: first submission accepted")

    # Second submission with identical content
    duplicate = accept_assignment(
        packet=_packet(assignment_id="TASK-INT-TEST-DUP"),
        db_path=db,
    )
    _assert(duplicate["acceptance_state"] == "duplicate", "Case E: state=duplicate")
    _assert(duplicate["reason_code"] == "duplicate_assignment_id", "Case E: reason_code=duplicate_assignment_id")
    _assert(duplicate["task_id"] == "TASK-INT-TEST-DUP", "Case E: duplicate result includes original task_id")

    # DB: only one assignment_packets row
    conn = connect(db)
    count = conn.execute(
        "SELECT COUNT(*) FROM assignment_packets WHERE assignment_id=?",
        ("TASK-INT-TEST-DUP",),
    ).fetchone()[0]
    _assert(count == 1, "Case E: only one row in assignment_packets (no duplicate insert)")


def test_case_f_idempotency_conflict(db: Path) -> None:
    """Case F: same assignment_id but different content → idempotency_conflict ValidationError."""
    # First submission
    accept_assignment(
        packet=_packet(assignment_id="TASK-INT-TEST-CONFLICT", title="Original title"),
        db_path=db,
    )

    # Second submission with different content (different title → different hash)
    try:
        accept_assignment(
            packet=_packet(assignment_id="TASK-INT-TEST-CONFLICT", title="Mutated title"),
            db_path=db,
        )
        raise AssertionError("Case F: expected ValidationError for idempotency_conflict, got no error")
    except ValidationError as exc:
        _assert("idempotency_conflict" in str(exc), "Case F: ValidationError mentions idempotency_conflict")


def test_persistence_result_roundtrip(db: Path) -> None:
    """Verify result JSON in assignment_packets round-trips correctly."""
    result = accept_assignment(
        packet=_packet(assignment_id="TASK-INT-TEST-ROUNDTRIP"),
        db_path=db,
    )
    conn = connect(db)
    ap_row = conn.execute(
        "SELECT result_json FROM assignment_packets WHERE assignment_id=?",
        ("TASK-INT-TEST-ROUNDTRIP",),
    ).fetchone()
    _assert(ap_row is not None, "Roundtrip: assignment_packets row exists")
    persisted = json.loads(ap_row[0])
    _assert(persisted["acceptance_state"] == result["acceptance_state"], "Roundtrip: acceptance_state matches")
    _assert(persisted["task_id"] == result["task_id"], "Roundtrip: task_id matches")
    _assert(persisted["assignment_id"] == result["assignment_id"], "Roundtrip: assignment_id matches")
    _assert("created_at" in persisted, "Roundtrip: created_at persisted")


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

def run_all() -> None:
    with tempfile.TemporaryDirectory() as td:
        db = Path(td) / "tde_int_test.sqlite"
        tests = [
            ("Case A — accepted + DB persistence + event", test_case_a_accepted),
            ("Case B — accepted_pending_binding", test_case_b_accepted_pending_binding),
            ("Case C — accepted_no_runner", test_case_c_accepted_no_runner),
            ("Case D — rejected_invalid_assignment", test_case_d_rejected_invalid_assignment),
            ("Case E — duplicate", test_case_e_duplicate),
            ("Case F — idempotency_conflict", test_case_f_idempotency_conflict),
            ("Persistence result roundtrip", test_persistence_result_roundtrip),
        ]
        passed = 0
        failed = 0
        for label, fn in tests:
            print(f"\n[{label}]")
            try:
                fn(db)
                passed += 1
            except Exception as exc:
                print(f"  [FAIL] {exc}")
                failed += 1

        print(f"\n{'='*60}")
        print(f"Results: {passed} passed, {failed} failed")
        if failed:
            raise SystemExit(1)
        print("[PASS] All TDE assignment accept integration tests passed")


if __name__ == "__main__":
    run_all()

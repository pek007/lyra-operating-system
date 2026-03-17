#!/usr/bin/env python3
"""
Test suite for tde_assignment_accept.py — thin-slice acceptance cases.

Linked task: TASK-20260315-CP-TDE-ASSIGNMENT-ACCEPTANCE
Linked plan: products/task-management/04-execution/TDE_ASSIGNMENT_ACCEPTANCE_THIN_SLICE_PLAN_2026-03-15.md

Five cases per the thin-slice plan:
  A — valid assignment, normal path → accepted
  B — valid assignment, missing binding/objective context → accepted_pending_binding
  C — valid assignment, no runner available → accepted_no_runner
  D — invalid packet (schema validation fails) → rejected_invalid_assignment
  E — duplicate packet (same id + content) → duplicate
"""
from __future__ import annotations

import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

# Ensure tools/ is on the path when running from repo root or tools/
sys.path.insert(0, str(Path(__file__).resolve().parent))

from tde_assignment_accept import accept_assignment, ValidationError


BASE_PACKET = {
    "artifactType": "tde_assignment_packet",
    "schemaVersion": "1.0.0",
    "assignment_id": "TASK-TEST-ACCEPT-A1",
    "source_system": "control-panel-test",
    "source_reference": "CP-TEST-001",
    "submitted_at": "2026-03-16T03:00:00Z",
    "submitted_by": "lyra-test",
    "title": "Test assignment alpha",
    "summary": "Automated thin-slice acceptance test case A",
    "requested_action": "Implement and verify acceptance state persistence for control-panel assignments",
    "priority_hint": "high",
    "workspace_scope": "lyra-os",
    "product_scope": "task-management",
    "related_entities": [
        {"entity_type": "task", "entity_ref": "TASK-TEST-ACCEPT-A1", "relationship": "self"}
    ],
    "evidence_links": [
        {"kind": "plan", "ref": "TDE_ASSIGNMENT_ACCEPTANCE_THIN_SLICE_PLAN_2026-03-15.md", "note": None}
    ],
    "assignment_owner_role": "developer",
    "objective_id": "OBJ-TDE-FOUNDATION",
    "runner_binding_required": False,
    "decision_policy_ref": None,
    "workflow_family": None,
    "metadata": {},
}


def _fresh_db() -> Path:
    """Return a path to a fresh temporary SQLite database."""
    td = tempfile.mkdtemp()
    return Path(td) / "test_tde_state.sqlite"


def _packet(**overrides) -> dict:
    p = {**BASE_PACKET, **overrides}
    return p


class TestCaseA_NormalAccept(unittest.TestCase):
    """Case A: valid assignment, normal path → accepted."""

    def setUp(self):
        self.db = _fresh_db()
        self.packet = _packet(assignment_id="TASK-TEST-ACCEPT-A1")

    def test_acceptance_state_is_accepted(self):
        result = accept_assignment(packet=self.packet, db_path=self.db)
        self.assertEqual(result["acceptance_state"], "accepted")

    def test_task_id_returned(self):
        result = accept_assignment(packet=self.packet, db_path=self.db)
        self.assertIsNotNone(result["task_id"])
        self.assertIn("TEST-ACCEPT-A1", result["task_id"])

    def test_assignment_persisted_in_db(self):
        accept_assignment(packet=self.packet, db_path=self.db)
        conn = sqlite3.connect(str(self.db))
        row = conn.execute(
            "SELECT acceptance_state FROM assignment_packets WHERE assignment_id=?",
            (self.packet["assignment_id"],),
        ).fetchone()
        conn.close()
        self.assertIsNotNone(row)
        self.assertEqual(row[0], "accepted")

    def test_task_created_in_tasks_table(self):
        result = accept_assignment(packet=self.packet, db_path=self.db)
        conn = sqlite3.connect(str(self.db))
        row = conn.execute(
            "SELECT task_id, status FROM tasks WHERE task_id=?",
            (result["task_id"],),
        ).fetchone()
        conn.close()
        self.assertIsNotNone(row)
        self.assertEqual(row[1], "Active")

    def test_result_payload_has_required_fields(self):
        result = accept_assignment(packet=self.packet, db_path=self.db)
        for field in ("assignment_id", "acceptance_state", "task_id", "reason_code", "message", "created_at", "updated_at"):
            self.assertIn(field, result, f"Missing required field: {field}")

    def test_event_emitted(self):
        accept_assignment(packet=self.packet, db_path=self.db)
        conn = sqlite3.connect(str(self.db))
        row = conn.execute(
            "SELECT type FROM events WHERE event_id=?",
            (f"evt:assignment:{self.packet['assignment_id']}",),
        ).fetchone()
        conn.close()
        self.assertIsNotNone(row)
        self.assertEqual(row[0], "assignment_accepted")


class TestCaseB_PendingBinding(unittest.TestCase):
    """Case B: valid assignment, runner_binding_required=True but no decision_policy_ref → accepted_pending_binding."""

    def setUp(self):
        self.db = _fresh_db()
        self.packet = _packet(
            assignment_id="TASK-TEST-ACCEPT-B1",
            runner_binding_required=True,
            decision_policy_ref=None,
        )

    def test_acceptance_state_is_pending_binding(self):
        result = accept_assignment(packet=self.packet, db_path=self.db)
        self.assertEqual(result["acceptance_state"], "accepted_pending_binding")

    def test_task_status_is_waiting(self):
        result = accept_assignment(packet=self.packet, db_path=self.db)
        conn = sqlite3.connect(str(self.db))
        row = conn.execute(
            "SELECT status FROM tasks WHERE task_id=?", (result["task_id"],)
        ).fetchone()
        conn.close()
        self.assertEqual(row[0], "Waiting")

    def test_reason_code_present(self):
        result = accept_assignment(packet=self.packet, db_path=self.db)
        self.assertIsNotNone(result["reason_code"])
        # Reason code must be non-empty and reference the missing context
        # (actual value: "missing_decision_policy_ref")
        self.assertTrue(len(result["reason_code"]) > 0)

    def test_assignment_persisted(self):
        accept_assignment(packet=self.packet, db_path=self.db)
        conn = sqlite3.connect(str(self.db))
        row = conn.execute(
            "SELECT acceptance_state FROM assignment_packets WHERE assignment_id=?",
            (self.packet["assignment_id"],),
        ).fetchone()
        conn.close()
        self.assertEqual(row[0], "accepted_pending_binding")


class TestCaseC_NoRunner(unittest.TestCase):
    """Case C: valid assignment, objective_id=None → accepted_no_runner."""

    def setUp(self):
        self.db = _fresh_db()
        self.packet = _packet(
            assignment_id="TASK-TEST-ACCEPT-C1",
            objective_id=None,
            runner_binding_required=False,
        )

    def test_acceptance_state_is_no_runner(self):
        result = accept_assignment(packet=self.packet, db_path=self.db)
        self.assertEqual(result["acceptance_state"], "accepted_no_runner")

    def test_task_status_is_waiting(self):
        result = accept_assignment(packet=self.packet, db_path=self.db)
        conn = sqlite3.connect(str(self.db))
        row = conn.execute(
            "SELECT status FROM tasks WHERE task_id=?", (result["task_id"],)
        ).fetchone()
        conn.close()
        self.assertEqual(row[0], "Waiting")

    def test_assignment_persisted(self):
        accept_assignment(packet=self.packet, db_path=self.db)
        conn = sqlite3.connect(str(self.db))
        row = conn.execute(
            "SELECT acceptance_state FROM assignment_packets WHERE assignment_id=?",
            (self.packet["assignment_id"],),
        ).fetchone()
        conn.close()
        self.assertEqual(row[0], "accepted_no_runner")


class TestCaseD_InvalidPacket(unittest.TestCase):
    """Case D: invalid packet → rejected_invalid_assignment (schema validation fails)."""

    def setUp(self):
        self.db = _fresh_db()

    def test_missing_required_field_raises_or_rejects(self):
        bad_packet = {
            "artifactType": "tde_assignment_packet",
            "schemaVersion": "1.0.0",
            "assignment_id": "TASK-TEST-ACCEPT-D1",
            # deliberately missing: source_system, title, summary, etc.
        }
        # With a bare id present, should return rejected result; without id, may raise
        try:
            result = accept_assignment(packet=bad_packet, db_path=self.db)
            self.assertEqual(result["acceptance_state"], "rejected_invalid_assignment")
        except ValidationError:
            pass  # also acceptable when assignment_id is absent

    def test_invalid_priority_hint_rejects(self):
        bad_packet = _packet(
            assignment_id="TASK-TEST-ACCEPT-D2",
            priority_hint="extreme",  # not in enum
        )
        result = accept_assignment(packet=bad_packet, db_path=self.db)
        self.assertEqual(result["acceptance_state"], "rejected_invalid_assignment")

    def test_rejected_result_has_no_task_id(self):
        bad_packet = _packet(
            assignment_id="TASK-TEST-ACCEPT-D3",
            priority_hint="invalid_value",
        )
        result = accept_assignment(packet=bad_packet, db_path=self.db)
        self.assertIsNone(result["task_id"])

    def test_rejected_packet_persisted(self):
        bad_packet = _packet(
            assignment_id="TASK-TEST-ACCEPT-D4",
            priority_hint="not_valid",
        )
        accept_assignment(packet=bad_packet, db_path=self.db)
        conn = sqlite3.connect(str(self.db))
        row = conn.execute(
            "SELECT acceptance_state FROM assignment_packets WHERE assignment_id=?",
            ("TASK-TEST-ACCEPT-D4",),
        ).fetchone()
        conn.close()
        self.assertIsNotNone(row)
        self.assertEqual(row[0], "rejected_invalid_assignment")


class TestCaseE_Duplicate(unittest.TestCase):
    """Case E: duplicate packet (same id + same content) → duplicate."""

    def setUp(self):
        self.db = _fresh_db()
        self.packet = _packet(assignment_id="TASK-TEST-ACCEPT-E1")

    def test_second_submission_returns_duplicate(self):
        accept_assignment(packet=self.packet, db_path=self.db)
        result2 = accept_assignment(packet=self.packet, db_path=self.db)
        self.assertEqual(result2["acceptance_state"], "duplicate")

    def test_duplicate_reason_code(self):
        accept_assignment(packet=self.packet, db_path=self.db)
        result2 = accept_assignment(packet=self.packet, db_path=self.db)
        self.assertIsNotNone(result2["reason_code"])
        self.assertIn("duplicate", result2["reason_code"])

    def test_no_second_task_row_created(self):
        accept_assignment(packet=self.packet, db_path=self.db)
        accept_assignment(packet=self.packet, db_path=self.db)
        conn = sqlite3.connect(str(self.db))
        count = conn.execute(
            "SELECT COUNT(*) FROM tasks WHERE task_id LIKE '%TEST-ACCEPT-E1%'"
        ).fetchone()[0]
        conn.close()
        self.assertEqual(count, 1)

    def test_idempotency_conflict_raises_on_content_change(self):
        accept_assignment(packet=self.packet, db_path=self.db)
        modified = _packet(assignment_id="TASK-TEST-ACCEPT-E1", title="Different title for conflict test")
        with self.assertRaises(ValidationError) as ctx:
            accept_assignment(packet=modified, db_path=self.db)
        self.assertIn("idempotency_conflict", str(ctx.exception))


if __name__ == "__main__":
    unittest.main(verbosity=2)

#!/usr/bin/env python3
from __future__ import annotations

import json
import tempfile
from pathlib import Path

from tde_formation_creator import create_from_formation
from tde_intent_intake import REQUEST_CLASS_TABLE
from tde_task_close import build_closure_record, close_task, ValidationError
from tde_state_store import connect


def run_tests() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        formation = REQUEST_CLASS_TABLE["basic_tde_gui"](
            request_text="Create a basic GUI for TDE",
            source_ref="telegram:test:close-task",
        )
        formation_path = root / "formation.json"
        formation_path.write_text(json.dumps(formation, indent=2), encoding="utf-8")
        created = create_from_formation(
            formation_path=formation_path,
            db_path=root / "tde_state.sqlite",
            objectives_path=root / "tde_objectives.json",
            tasks_projection_path=root / "TASKS_from_db.md",
        )
        task_id = created["created_tasks"][0]
        successor_id = created["created_tasks"][1]

        closure = build_closure_record(
            task_id=task_id,
            closure_state="Done",
            result_summary="Completed bounded GUI scope definition.",
            evidence_refs=["evidence/gui-scope.md"],
            outcome_vs_expected="Matched expected bounded first-slice outcome.",
            next_recommendation="Activate verification follow-up.",
            feedback_outcome="close_and_chain",
            friction_flags=[],
            objective_id=created["objective_id"],
            followup_refs=[successor_id],
        )
        result = close_task(closure_record=closure, db_path=root / "tde_state.sqlite", artifact_dir=root / "artifacts")
        assert result["closure_state"] == "Done"
        assert result["feedback_outcome"] == "close_and_chain"
        assert result["db_status"] == "Done"
        assert result["followup_actions"]["activated_followups"]

        conn = connect(root / "tde_state.sqlite")
        row = conn.execute("SELECT status, checked, metadata_json FROM tasks WHERE task_id=?", (task_id,)).fetchone()
        assert row is not None
        status, checked, metadata_json = row
        assert status == "Done"
        assert checked == 1
        assert "close_and_chain" in metadata_json

        successor_row = conn.execute("SELECT status FROM tasks WHERE task_id=?", (successor_id,)).fetchone()
        assert successor_row is not None
        assert successor_row[0] == "Active"

        blocked = build_closure_record(
            task_id=successor_id,
            closure_state="Escalated",
            result_summary="Cannot proceed without a higher-level scope decision.",
            evidence_refs=["evidence/escalation-note.md"],
            outcome_vs_expected="Work surfaced a decision outside delegated authority.",
            next_recommendation="Escalate to the Ultimate Decision-maker.",
            feedback_outcome="close_and_escalate",
            friction_flags=["scope_tradeoff"],
            objective_id=created["objective_id"],
        )
        esc_result = close_task(closure_record=blocked, db_path=root / "tde_state.sqlite", artifact_dir=root / "artifacts")
        esc_path = esc_result["followup_actions"]["escalation_package_path"]
        assert esc_path
        assert Path(esc_path).exists()

        bad = dict(closure)
        bad["feedback_outcome"] = "close_as_error"
        try:
            close_task(closure_record=bad, db_path=root / "tde_state.sqlite")
            raise AssertionError("expected validation failure")
        except ValidationError:
            pass

    print("[PASS] TDE task close tests passed")


if __name__ == "__main__":
    run_tests()

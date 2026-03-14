#!/usr/bin/env python3
from __future__ import annotations

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
        formation_path.write_text(__import__("json").dumps(formation, indent=2), encoding="utf-8")
        created = create_from_formation(
            formation_path=formation_path,
            db_path=root / "tde_state.sqlite",
            objectives_path=root / "tde_objectives.json",
            tasks_projection_path=root / "TASKS_from_db.md",
        )
        task_id = created["created_tasks"][0]

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
            followup_refs=[created["created_tasks"][1]],
        )
        result = close_task(closure_record=closure, db_path=root / "tde_state.sqlite")
        assert result["closure_state"] == "Done"
        assert result["feedback_outcome"] == "close_and_chain"
        assert result["db_status"] == "Done"

        conn = connect(root / "tde_state.sqlite")
        row = conn.execute("SELECT status, checked, metadata_json FROM tasks WHERE task_id=?", (task_id,)).fetchone()
        assert row is not None
        status, checked, metadata_json = row
        assert status == "Done"
        assert checked == 1
        assert "close_and_chain" in metadata_json

        blocked_task = created["created_tasks"][1]
        blocked = build_closure_record(
            task_id=blocked_task,
            closure_state="Blocked",
            result_summary="Could not proceed because an external dependency is missing.",
            evidence_refs=["evidence/blocker-note.md"],
            outcome_vs_expected="Work stopped before intended execution.",
            next_recommendation="Escalate or wait for dependency.",
            feedback_outcome="close_as_error",
            friction_flags=["dependency_missing"],
        )
        blocked_result = close_task(closure_record=blocked, db_path=root / "tde_state.sqlite")
        assert blocked_result["db_status"] == "Waiting"

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

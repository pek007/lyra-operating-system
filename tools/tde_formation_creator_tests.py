#!/usr/bin/env python3
from __future__ import annotations

import json
import tempfile
from pathlib import Path

from tde_formation_creator import create_from_formation
from tde_state_store import connect


def run_tests() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        formation = root / "formation.json"
        formation.write_text(json.dumps({
            "artifactType": "tde_intent_formation_record",
            "schemaVersion": "1.0.0",
            "formation_id": "FORM-001",
            "source_type": "chat_request",
            "source_ref": "telegram:msg:1",
            "interpreted_intent": "Build a basic internal TDE GUI.",
            "request_type": "implementation_request",
            "specificity_level": "medium",
            "ambiguity_types": ["missing_scope"],
            "actionability_status": "executable_with_assumptions",
            "assumptions": ["Start with a read-heavy operator GUI."],
            "known_unknowns": ["Exact operator actions in v1."],
            "proposed_objective": {
                "objective_title": "Create first basic TDE GUI",
                "objective_summary": "Create a bounded first GUI attempt for TDE."
            },
            "proposed_success_criteria": ["A first bounded GUI workflow exists."],
            "proposed_workflow_family": "implementation_verification_readiness",
            "proposed_first_stage_set": ["implementation", "verification", "readiness-review"],
            "proposed_first_task_set": [
                {
                    "task_title": "Design first GUI scope",
                    "task_summary": "Define a bounded read-heavy first GUI scope.",
                    "stage_id": "implementation"
                },
                {
                    "task_title": "Verify first GUI scope",
                    "task_summary": "Verify that the first GUI scope is coherent and safe.",
                    "stage_id": "verification"
                }
            ],
            "required_clarifications": [],
            "recommended_next_action": "proceed_with_assumptions",
            "formation_rationale": "A bounded first version can be created under assumptions.",
            "formed_at": "2026-03-13T20:55:00Z",
            "formed_by_role": "Product Owner"
        }, indent=2), encoding="utf-8")
        db = root / "tde_state.sqlite"
        objectives = root / "tde_objectives.json"
        projection = root / "TASKS_from_db.md"

        result = create_from_formation(
            formation_path=formation,
            db_path=db,
            objectives_path=objectives,
            tasks_projection_path=projection,
        )
        assert result["objective_id"] == "OBJ-FORM-FORM-001"
        assert len(result["created_tasks"]) == 2
        reg = json.loads(objectives.read_text(encoding="utf-8"))
        assert reg["objectives"][0]["formation_id"] == "FORM-001"
        conn = connect(db)
        rows = conn.execute("SELECT task_id, status, metadata_json FROM tasks ORDER BY task_id").fetchall()
        assert len(rows) == 2
        first_meta = json.loads(rows[0][2])
        assert first_meta["formation_id"] == "FORM-001"
        assert first_meta["decision_policy_ref"].endswith("REFERENCE_TDE_POLICY_ENVELOPE_IMPLEMENTATION_VERIFICATION_V1.json")
        assert projection.exists()

    print("[PASS] TDE formation creator tests passed")


if __name__ == "__main__":
    run_tests()

#!/usr/bin/env python3
from __future__ import annotations

import json
import tempfile
from pathlib import Path

from tde_job_tick_runner import run_job_tick
from tde_state_store import connect, import_tasks, init_schema, update_task_metadata

POLICY_REF = "products/task-management/07-decisions/REFERENCE_TDE_POLICY_ENVELOPE_IMPLEMENTATION_VERIFICATION_V1.json"


def _setup(root: Path, task_id: str) -> tuple[Path, Path, Path, Path]:
    tasks = root / "TASKS.md"
    tasks.write_text(
        f"""# TASKS.md\n\n## Inbox\n\n## Triage\n\n## Active\n- [ ] {task_id} | Pilot task\n\n## Waiting\n\n## Done\n""",
        encoding="utf-8",
    )
    bindings = root / "bindings.json"
    bindings.write_text(
        json.dumps({"bindings": [{"binding_id": "BIND-JOB-PROD-001-ACTIVE", "job_id": "JOB-PROD-001", "actor_id": "lyra", "session_key": "cron:tde-job-runner-v1", "status": "active", "binding_epoch": 1}]}),
        encoding="utf-8",
    )
    objectives = root / "objectives.json"
    objectives.write_text(json.dumps({"objectives": [{"objective_id": "OBJ-TDE-FOUNDATION", "allowed_checkpoints": ["S16"]}]}), encoding="utf-8")
    db = root / "tde_state.sqlite"
    conn = connect(db)
    init_schema(conn)
    import_tasks(conn, tasks)
    return tasks, bindings, objectives, db


def test_research_further() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        tasks, bindings, objectives, db = _setup(root, "TDE-RF-001")
        conn = connect(db)
        update_task_metadata(conn, "TDE-RF-001", {
            "workflow_family": "implementation_verification_readiness",
            "decision_policy_ref": POLICY_REF,
            "decision_outcome_hint": "research_further",
            "decision_next_task_id": "TDE-RESEARCH-001",
            "decision_branch_id": "verification_mixed_signals",
            "stage_id": "verification",
        })
        artifact = root / "artifact.json"
        result = run_job_tick(
            job_id="JOB-PROD-001", binding_id="BIND-JOB-PROD-001-ACTIVE", actor_id="lyra", session_key="cron:tde-job-runner-v1",
            trigger_source="cron", tick_id="rf-1", max_claim=1, objective_id="OBJ-TDE-FOUNDATION", objective_checkpoint="S16",
            rationale_trace="rf-test", tasks_path=tasks, artifact_path=artifact, writeback_tasks_path=root / "TASKS_from_db.md",
            binding_registry_path=bindings, objective_registry_path=objectives, canonical_store="db", canonical_db_path=db,
        )
        assert result["status"] == "ok"
        assert result["mutations"][0]["status"] == "research_further"
        assert result["mutations"][0]["decision_policy"]["decision_record_path"]


def test_escalate() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        tasks, bindings, objectives, db = _setup(root, "TDE-ESC-001")
        conn = connect(db)
        update_task_metadata(conn, "TDE-ESC-001", {
            "workflow_family": "implementation_verification_readiness",
            "decision_policy_ref": POLICY_REF,
            "decision_outcome_hint": "escalate",
            "decision_question": "Should this change proceed?",
            "decision_escalation_reason": "architectural_tradeoff_above_medium_risk",
            "stage_id": "readiness-review",
        })
        artifact = root / "artifact.json"
        result = run_job_tick(
            job_id="JOB-PROD-001", binding_id="BIND-JOB-PROD-001-ACTIVE", actor_id="lyra", session_key="cron:tde-job-runner-v1",
            trigger_source="cron", tick_id="esc-1", max_claim=1, objective_id="OBJ-TDE-FOUNDATION", objective_checkpoint="S16",
            rationale_trace="esc-test", tasks_path=tasks, artifact_path=artifact, writeback_tasks_path=root / "TASKS_from_db.md",
            binding_registry_path=bindings, objective_registry_path=objectives, canonical_store="db", canonical_db_path=db,
        )
        assert result["status"] == "ok"
        assert result["mutations"][0]["status"] == "escalate"
        esc_path = result["mutations"][0]["decision_policy"]["escalation_package_path"]
        assert esc_path
        payload = json.loads(Path(esc_path).read_text(encoding="utf-8"))
        assert payload["artifactType"] == "tde_decision_escalation_package"


if __name__ == "__main__":
    test_research_further()
    test_escalate()
    print("[PASS] TDE decision outcome tests passed")

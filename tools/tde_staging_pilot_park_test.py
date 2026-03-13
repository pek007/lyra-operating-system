#!/usr/bin/env python3
from __future__ import annotations

import json
import tempfile
from pathlib import Path

from tde_job_tick_runner import run_job_tick
from tde_state_store import connect, import_tasks, init_schema, update_task_metadata

POLICY_REF = "products/task-management/07-decisions/REFERENCE_TDE_POLICY_ENVELOPE_IMPLEMENTATION_VERIFICATION_V1.json"


def run_tests() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        tasks = root / "TASKS.md"
        tasks.write_text(
            """# TASKS.md

## Inbox

## Triage

## Active
- [ ] TDE-STAGE-ORIGIN-001 | Pilot origin task

## Waiting
- [ ] TDE-STAGE-RESEARCH-001 | Pilot research task
- [ ] TDE-STAGE-CONTINUE-001 | Pilot continue task

## Done
""",
            encoding="utf-8",
        )
        bindings = root / "bindings.json"
        bindings.write_text(json.dumps({"bindings": [{"binding_id": "BIND-JOB-PROD-001-ACTIVE", "job_id": "JOB-PROD-001", "actor_id": "lyra", "session_key": "cron:tde-job-runner-v1", "status": "active", "binding_epoch": 1}]}), encoding="utf-8")
        objectives = root / "objectives.json"
        objectives.write_text(json.dumps({"objectives": [{"objective_id": "OBJ-TDE-FOUNDATION", "allowed_checkpoints": ["S16"]}]}), encoding="utf-8")
        db = root / "tde_state.sqlite"
        conn = connect(db)
        init_schema(conn)
        import_tasks(conn, tasks)
        update_task_metadata(conn, "TDE-STAGE-ORIGIN-001", {
            "workflow_family": "implementation_verification_readiness",
            "decision_policy_ref": POLICY_REF,
            "decision_outcome_hint": "research_further",
            "decision_next_task_id": "TDE-STAGE-RESEARCH-001",
            "stage_id": "verification",
        })
        update_task_metadata(conn, "TDE-STAGE-RESEARCH-001", {
            "workflow_family": "implementation_verification_readiness",
            "decision_policy_ref": POLICY_REF,
            "decision_reentry_to_task_id": "TDE-STAGE-ORIGIN-001",
            "decision_reentry_default_outcome": "continue",
            "decision_reentry_next_task_id": "TDE-STAGE-CONTINUE-001",
            "stage_id": "verification-research",
        })

        run_job_tick(job_id="JOB-PROD-001", binding_id="BIND-JOB-PROD-001-ACTIVE", actor_id="lyra", session_key="cron:tde-job-runner-v1", trigger_source="cron", tick_id="pilot-1", max_claim=1, objective_id="OBJ-TDE-FOUNDATION", objective_checkpoint="S16", rationale_trace="pilot", tasks_path=tasks, artifact_path=root/"a1.json", writeback_tasks_path=root/"TASKS_from_db.md", binding_registry_path=bindings, objective_registry_path=objectives, canonical_store="db", canonical_db_path=db)
        result2 = run_job_tick(job_id="JOB-PROD-001", binding_id="BIND-JOB-PROD-001-ACTIVE", actor_id="lyra", session_key="cron:tde-job-runner-v1", trigger_source="cron", tick_id="pilot-2", max_claim=1, objective_id="OBJ-TDE-FOUNDATION", objective_checkpoint="S16", rationale_trace="pilot", tasks_path=tasks, artifact_path=root/"a2.json", writeback_tasks_path=root/"TASKS_from_db.md", binding_registry_path=bindings, objective_registry_path=objectives, canonical_store="db", canonical_db_path=db)
        assert result2["claimed"] == ["TDE-STAGE-RESEARCH-001"]
        assert result2["decisions"][0]["origin_task_id"] == "TDE-STAGE-ORIGIN-001"
        cont_row = conn.execute("SELECT status FROM tasks WHERE task_id='TDE-STAGE-CONTINUE-001'").fetchone()
        assert cont_row[0] == "Active"

    print("[PASS] TDE staging pilot park test passed")


if __name__ == "__main__":
    run_tests()

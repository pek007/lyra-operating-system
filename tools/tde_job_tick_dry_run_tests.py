#!/usr/bin/env python3
from __future__ import annotations

import json
import tempfile
from pathlib import Path

from tde_job_tick_runner import run_job_tick
from tde_state_store import connect, import_tasks, init_schema, update_task_metadata


def run_tests() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        tasks = root / "TASKS.md"
        tasks.write_text(
            """# TASKS.md\n\n## Inbox\n\n## Triage\n- [ ] TDE-CHAIN-B | Verify build\n\n## Active\n\n## Waiting\n\n## Done\n- [x] TDE-CHAIN-A | Implement build\n""",
            encoding="utf-8",
        )
        bindings = root / "bindings.json"
        bindings.write_text(
            json.dumps({"bindings": [{"binding_id": "BIND-JOB-PROD-001-ACTIVE", "job_id": "JOB-PROD-001", "actor_id": "lyra", "session_key": "cron:tde-job-runner-v1", "status": "active", "binding_epoch": 1}]}),
            encoding="utf-8",
        )
        objectives = root / "objectives.json"
        objectives.write_text(
            json.dumps({"objectives": [{"objective_id": "OBJ-TDE-FOUNDATION", "allowed_checkpoints": ["S16"]}]}),
            encoding="utf-8",
        )
        db = root / "tde_state.sqlite"
        conn = connect(db)
        init_schema(conn)
        import_tasks(conn, tasks)
        update_task_metadata(conn, "TDE-CHAIN-B", {"depends_on": ["TDE-CHAIN-A"], "activation_rule": "all_predecessors_done", "stage_id": "verify", "chain_policy": {"pilot_enabled": True, "family": "pilot-a"}})

        before = conn.execute("SELECT status, metadata_json FROM tasks WHERE task_id='TDE-CHAIN-B'").fetchone()
        artifact = root / "artifact.json"
        result = run_job_tick(
            job_id="JOB-PROD-001",
            binding_id="BIND-JOB-PROD-001-ACTIVE",
            actor_id="lyra",
            session_key="cron:tde-job-runner-v1",
            trigger_source="cron",
            tick_id="dryrun-1",
            max_claim=1,
            objective_id="OBJ-TDE-FOUNDATION",
            objective_checkpoint="S16",
            rationale_trace="dry-run-test",
            tasks_path=tasks,
            artifact_path=artifact,
            writeback_tasks_path=root / "TASKS_from_db.md",
            binding_registry_path=bindings,
            objective_registry_path=objectives,
            canonical_store="db",
            canonical_db_path=db,
            dry_run=True,
        )

        after = conn.execute("SELECT status, metadata_json FROM tasks WHERE task_id='TDE-CHAIN-B'").fetchone()
        assert result["status"] == "ok"
        assert result["dry_run"] is True
        assert result["chaining"]["applied"]["applied"] == 0
        assert result["chaining"]["applied"]["reason"] == "dry_run_no_mutation"
        assert result["claimed"] == []
        assert result["writeback"]["reason"] == "dry_run_no_mutation"
        assert before == after

    print("[PASS] TDE job tick dry-run tests passed")


if __name__ == "__main__":
    run_tests()

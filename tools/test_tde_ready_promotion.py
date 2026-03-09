#!/usr/bin/env python3
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tde_job_tick_runner import run_job_tick
from tde_state_store import connect, import_tasks, init_schema, update_task_metadata


class TDEReadyPromotionTest(unittest.TestCase):
    def test_done_predecessor_promotes_successor_and_tick_claims_it(self) -> None:
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

            artifact = root / "artifact.json"
            result = run_job_tick(
                job_id="JOB-PROD-001",
                binding_id="BIND-JOB-PROD-001-ACTIVE",
                actor_id="lyra",
                session_key="cron:tde-job-runner-v1",
                trigger_source="cron",
                tick_id="promotion-1",
                max_claim=1,
                objective_id="OBJ-TDE-FOUNDATION",
                objective_checkpoint="S16",
                rationale_trace="promotion-test",
                tasks_path=tasks,
                artifact_path=artifact,
                writeback_tasks_path=root / "TASKS_from_db.md",
                binding_registry_path=bindings,
                objective_registry_path=objectives,
                canonical_store="db",
                canonical_db_path=db,
            )

            self.assertEqual(result["status"], "ok")
            self.assertEqual(result["chaining"]["applied"]["applied"], 1)
            self.assertEqual(result["claimed"], ["TDE-CHAIN-B"])
            row = conn.execute("SELECT status, metadata_json FROM tasks WHERE task_id='TDE-CHAIN-B'").fetchone()
            self.assertEqual(row[0], "Waiting")
            self.assertIn("activated_by", row[1])


if __name__ == "__main__":
    unittest.main()

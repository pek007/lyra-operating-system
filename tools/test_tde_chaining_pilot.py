#!/usr/bin/env python3
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tde_job_tick_runner import run_job_tick
from tde_state_store import connect, export_tasks, import_tasks, init_schema, update_task_metadata


class TDEChainingPilotTest(unittest.TestCase):
    def test_successor_promotion_happy_path(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            tasks = root / "TASKS.md"
            tasks.write_text(
                """# TASKS.md\n\n## Inbox\n\n## Triage\n- [ ] TDE-CHAIN-002 | Verify chained work\n\n## Active\n\n## Waiting\n- [ ] TDE-CHAIN-003 | Deployment readiness review\n\n## Done\n- [x] TDE-CHAIN-001 | Implement chained work\n""",
                encoding="utf-8",
            )
            bindings = root / "bindings.json"
            bindings.write_text(json.dumps({"bindings": [{"binding_id": "BIND-JOB-PROD-001-ACTIVE", "job_id": "JOB-PROD-001", "actor_id": "lyra", "session_key": "cron:tde-job-runner-v1", "status": "active", "binding_epoch": 1}]}), encoding="utf-8")
            objectives = root / "objectives.json"
            objectives.write_text(json.dumps({"objectives": [{"objective_id": "OBJ-TDE-FOUNDATION", "allowed_checkpoints": ["S39"]}]}), encoding="utf-8")
            db = root / "tde_state.sqlite"
            conn = connect(db)
            init_schema(conn)
            import_tasks(conn, tasks)
            update_task_metadata(conn, "TDE-CHAIN-002", {
                "depends_on": ["TDE-CHAIN-001"],
                "activation_rule": "all_predecessors_done",
                "objective_id": "OBJ-TDE-FOUNDATION",
                "stage_id": "verification",
                "chain_policy": {"family": "pilot_family_a", "pilot_enabled": True, "promotion_cap_class": "bounded_single_successor"},
            })
            export_tasks(conn, tasks)

            artifact = root / "artifact.json"
            result = run_job_tick(
                job_id="JOB-PROD-001",
                binding_id="BIND-JOB-PROD-001-ACTIVE",
                actor_id="lyra",
                session_key="cron:tde-job-runner-v1",
                trigger_source="cron",
                tick_id="chain-happy-1",
                max_claim=1,
                objective_id="OBJ-TDE-FOUNDATION",
                objective_checkpoint="S39",
                rationale_trace="chain-happy",
                tasks_path=tasks,
                artifact_path=artifact,
                writeback_tasks_path=tasks,
                binding_registry_path=bindings,
                objective_registry_path=objectives,
                canonical_store="db",
                canonical_db_path=db,
            )
            self.assertEqual(result["status"], "ok")
            self.assertEqual(result["chaining"]["promoted"][0]["task_id"], "TDE-CHAIN-002")
            rows = conn.execute("SELECT status, metadata_json FROM tasks WHERE task_id='TDE-CHAIN-002'").fetchone()
            self.assertEqual(rows[0], "Waiting")
            self.assertIn("activated_at", rows[1])

    def test_missing_predecessor_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            tasks = root / "TASKS.md"
            tasks.write_text(
                """# TASKS.md\n\n## Inbox\n\n## Triage\n- [ ] TDE-CHAIN-002 | Verify chained work\n\n## Active\n\n## Waiting\n\n## Done\n""",
                encoding="utf-8",
            )
            db = root / "tde_state.sqlite"
            conn = connect(db)
            init_schema(conn)
            import_tasks(conn, tasks)
            update_task_metadata(conn, "TDE-CHAIN-002", {
                "depends_on": ["TDE-CHAIN-404"],
                "activation_rule": "all_predecessors_done",
                "objective_id": "OBJ-TDE-FOUNDATION",
            })
            from tde_state_store import evaluate_chaining_promotions
            result = evaluate_chaining_promotions(conn, "chain-missing-1")
            self.assertEqual(result["promoted"], [])
            self.assertEqual(result["skipped"][0]["reason"], "missing_predecessor")


if __name__ == "__main__":
    unittest.main()

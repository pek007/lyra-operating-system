#!/usr/bin/env python3
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tde_job_tick_runner import run_job_tick
from tde_state_store import connect, export_tasks, import_tasks, init_schema


class TDEDbCanonicalCutoverTest(unittest.TestCase):
    def test_db_canonical_writeback_updates_db_and_projection(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            tasks = root / "TASKS.md"
            tasks.write_text(
                """# TASKS.md\n\n## Inbox\n\n## Triage\n\n## Active\n- [ ] TDE-DB-001 | DB canonical task\n\n## Waiting\n\n## Done\n""",
                encoding="utf-8",
            )
            bindings = root / "bindings.json"
            bindings.write_text(
                json.dumps(
                    {
                        "bindings": [
                            {
                                "binding_id": "BIND-JOB-PROD-001-ACTIVE",
                                "job_id": "JOB-PROD-001",
                                "actor_id": "lyra",
                                "session_key": "cron:tde-job-runner-v1",
                                "status": "active",
                                "binding_epoch": 1,
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            objectives = root / "objectives.json"
            objectives.write_text(
                json.dumps({"objectives": [{"objective_id": "OBJ-TDE-FOUNDATION", "allowed_checkpoints": ["S16"]}] }),
                encoding="utf-8",
            )
            db = root / "tde_state.sqlite"
            conn = connect(db)
            init_schema(conn)
            import_tasks(conn, tasks)
            export_tasks(conn, tasks)

            artifact = root / "artifact.json"
            result = run_job_tick(
                job_id="JOB-PROD-001",
                binding_id="BIND-JOB-PROD-001-ACTIVE",
                actor_id="lyra",
                session_key="cron:tde-job-runner-v1",
                trigger_source="cron",
                tick_id="db-cutover-1",
                max_claim=1,
                objective_id="OBJ-TDE-FOUNDATION",
                objective_checkpoint="S16",
                rationale_trace="db-cutover-test",
                tasks_path=tasks,
                artifact_path=artifact,
                writeback_tasks_path=tasks,
                binding_registry_path=bindings,
                objective_registry_path=objectives,
                canonical_store="db",
                canonical_db_path=db,
            )

            self.assertEqual(result["status"], "ok")
            self.assertTrue(result["writeback"]["applied"])
            rows = conn.execute("SELECT task_id, status, metadata_json FROM tasks WHERE task_id='TDE-DB-001'").fetchall()
            self.assertEqual(rows[0][1], "Waiting")
            self.assertIn("db-cutover-1", rows[0][2])
            projection = tasks.read_text(encoding="utf-8")
            self.assertIn("## Waiting", projection)
            self.assertIn("TDE-DB-001 | DB canonical task", projection)
            self.assertNotIn("## Active\n- [ ] TDE-DB-001 | DB canonical task", projection)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tde_state_store import (
    connect,
    export_tasks,
    import_tasks,
    init_schema,
    read_tasks,
    update_task_metadata,
    validate_chain_metadata,
)


class TDEChainingMetadataTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.db = self.root / "tde.sqlite"
        self.tasks = self.root / "TASKS.md"
        self.tasks.write_text(
            """# TASKS\n\n## Inbox\n\n## Triage\n\n## Active\n- [ ] TDE-A | First task\n- [ ] TDE-B | Second task\n\n## Waiting\n\n## Done\n""",
            encoding="utf-8",
        )
        self.conn = connect(self.db)
        init_schema(self.conn)
        import_tasks(self.conn, self.tasks)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_validate_chain_metadata_accepts_v1_shape(self) -> None:
        ok, reason = validate_chain_metadata(
            {
                "depends_on": ["TDE-A"],
                "activation_rule": "all_predecessors_done",
                "objective_id": "OBJ-TDE-FOUNDATION",
                "stage_id": "verify",
                "chain_policy": {"family": "pilot-a", "pilot_enabled": True},
            }
        )
        self.assertTrue(ok)
        self.assertIsNone(reason)

    def test_validate_chain_metadata_rejects_invalid_rule(self) -> None:
        ok, reason = validate_chain_metadata({"activation_rule": "freeform_magic"})
        self.assertFalse(ok)
        self.assertEqual(reason, "unsupported_activation_rule")

    def test_update_metadata_persists_and_is_preserved_on_import(self) -> None:
        update_task_metadata(
            self.conn,
            "TDE-B",
            {
                "depends_on": ["TDE-A"],
                "activation_rule": "all_predecessors_done",
                "objective_id": "OBJ-TDE-FOUNDATION",
                "stage_id": "verify",
            },
        )
        rows = read_tasks(self.conn)
        row = next(x for x in rows if x["task_id"] == "TDE-B")
        self.assertEqual(row["metadata"]["depends_on"], ["TDE-A"])

        import_tasks(self.conn, self.tasks, preserve_metadata=True)
        rows = read_tasks(self.conn)
        row = next(x for x in rows if x["task_id"] == "TDE-B")
        self.assertEqual(row["metadata"]["activation_rule"], "all_predecessors_done")

    def test_export_projects_chaining_metadata_comment(self) -> None:
        update_task_metadata(
            self.conn,
            "TDE-B",
            {"depends_on": ["TDE-A"], "activation_rule": "all_predecessors_done", "stage_id": "verify"},
        )
        out = self.root / "TASKS_from_db.md"
        result = export_tasks(self.conn, out)
        text = out.read_text(encoding="utf-8")
        self.assertEqual(result["metadata_projected"], 1)
        self.assertIn("<!-- tde:metadata", text)
        self.assertIn('"depends_on": ["TDE-A"]', text)


if __name__ == "__main__":
    unittest.main()

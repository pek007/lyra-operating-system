#!/usr/bin/env python3
from __future__ import annotations

import json
import sqlite3
import tempfile
from pathlib import Path

from tde_job_tick_runner import run_job_tick


def seed_tasks(path: Path) -> None:
    path.write_text(
        """# TASKS.md\n\n## Inbox\n\n## Triage\n\n## Active\n- [ ] TDE-S35-001 | Ledger write test task\n\n## Waiting\n\n## Done\n""",
        encoding="utf-8",
    )


def seed_bindings(path: Path) -> None:
    payload = {
        "bindings": [
            {
                "binding_id": "BIND-JOB-PROD-001-ACTIVE",
                "job_id": "JOB-PROD-001",
                "actor_id": "lyra",
                "session_key": "cron:tde-job-runner-v1",
                "status": "active",
                "binding_epoch": 2,
                "expires_at": "2099-01-01T00:00:00+00:00",
            }
        ]
    }
    path.write_text(json.dumps(payload), encoding="utf-8")


def seed_objectives(path: Path) -> None:
    payload = {"objectives": [{"objective_id": "OBJ-TDE-FOUNDATION", "allowed_checkpoints": ["S35"]}]}
    path.write_text(json.dumps(payload), encoding="utf-8")


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        tasks = root / "TASKS.md"
        bindings = root / "bindings.json"
        objectives = root / "objectives.json"
        db = root / "state.sqlite"

        seed_tasks(tasks)
        seed_bindings(bindings)
        seed_objectives(objectives)

        result = run_job_tick(
            job_id="JOB-PROD-001",
            binding_id="BIND-JOB-PROD-001-ACTIVE",
            actor_id="lyra",
            session_key="cron:tde-job-runner-v1",
            trigger_source="cron",
            tick_id="s35-ledger",
            max_claim=1,
            objective_id="OBJ-TDE-FOUNDATION",
            objective_checkpoint="S35",
            rationale_trace="state-ledger",
            tasks_path=tasks,
            artifact_path=root / "artifact.json",
            writeback_tasks_path=tasks,
            binding_registry_path=bindings,
            objective_registry_path=objectives,
            shadow_state_enabled=True,
            shadow_state_db_path=db,
        )

        shadow = result.get("shadow_state", {})
        assert shadow.get("status") == "ok"
        assert "ledger" in shadow

        conn = sqlite3.connect(str(db))
        actions = conn.execute("SELECT COUNT(*) FROM actions").fetchone()[0]
        events = conn.execute("SELECT COUNT(*) FROM events").fetchone()[0]
        assert actions >= 1
        assert events >= 1

    print("[PASS] S35 state ledger write checks passed")


if __name__ == "__main__":
    main()

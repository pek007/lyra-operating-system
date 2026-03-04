#!/usr/bin/env python3
from __future__ import annotations

import json
import tempfile
from pathlib import Path

from tde_job_tick_runner import run_job_tick


def seed_tasks(path: Path) -> None:
    path.write_text(
        """# TASKS.md\n\n## Inbox\n\n## Triage\n\n## Active\n- [ ] TDE-S32-001 | Shadow state test task\n\n## Waiting\n\n## Done\n""",
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
    payload = {"objectives": [{"objective_id": "OBJ-TDE-FOUNDATION", "allowed_checkpoints": ["S32"]}]}
    path.write_text(json.dumps(payload), encoding="utf-8")


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        tasks = root / "TASKS.md"
        bindings = root / "bindings.json"
        objectives = root / "objectives.json"
        db = root / "state.sqlite"
        artifact = root / "artifact.json"

        seed_tasks(tasks)
        seed_bindings(bindings)
        seed_objectives(objectives)

        result = run_job_tick(
            job_id="JOB-PROD-001",
            binding_id="BIND-JOB-PROD-001-ACTIVE",
            actor_id="lyra",
            session_key="cron:tde-job-runner-v1",
            trigger_source="cron",
            tick_id="s32-shadow",
            max_claim=1,
            objective_id="OBJ-TDE-FOUNDATION",
            objective_checkpoint="S32",
            rationale_trace="shadow-state",
            tasks_path=tasks,
            artifact_path=artifact,
            writeback_tasks_path=tasks,
            binding_registry_path=bindings,
            objective_registry_path=objectives,
            shadow_state_enabled=True,
            shadow_state_db_path=db,
        )

        shadow = result.get("shadow_state", {})
        assert shadow.get("enabled") is True
        assert shadow.get("status") == "ok"
        assert shadow.get("parity", {}).get("match") is True

    print("[PASS] S32 shadow state write checks passed")


if __name__ == "__main__":
    main()

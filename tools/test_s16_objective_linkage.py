#!/usr/bin/env python3
from __future__ import annotations

import json
import tempfile
from pathlib import Path

from tde_job_tick_runner import run_job_tick


def _seed_tasks(path: Path) -> None:
    path.write_text(
        """# TASKS.md (Temporary Kanban)\n\n## Inbox\n\n## Triage\n\n## Active\n- [ ] TDE-S16-001 | Test task for objective linkage\n\n## Waiting\n\n## Done\n""",
        encoding="utf-8",
    )


def _seed_binding_registry(path: Path) -> None:
    payload = {
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
    path.write_text(json.dumps(payload), encoding="utf-8")


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tmpdir = Path(tmp)
        tasks = tmpdir / "TASKS.md"
        binding_registry = tmpdir / "bindings.json"
        pass_artifact = tmpdir / "s16-pass.json"
        fail_artifact = tmpdir / "s16-fail.json"

        _seed_tasks(tasks)
        _seed_binding_registry(binding_registry)

        ok = run_job_tick(
            job_id="JOB-PROD-001",
            binding_id="BIND-JOB-PROD-001-ACTIVE",
            actor_id="lyra",
            session_key="cron:tde-job-runner-v1",
            trigger_source="cron",
            tick_id="s16-pass",
            max_claim=1,
            objective_id="OBJ-TDE-FOUNDATION",
            objective_checkpoint="S16",
            rationale_trace="trace:objective-linkage",
            tasks_path=tasks,
            artifact_path=pass_artifact,
            writeback_tasks_path=tasks,
            binding_registry_path=binding_registry,
        )
        assert ok["outcomes"]["progressed"] == 1
        assert ok["objective_linkage"]["objective_id"] == "OBJ-TDE-FOUNDATION"

        _seed_tasks(tasks)
        bad = run_job_tick(
            job_id="JOB-PROD-001",
            binding_id="BIND-JOB-PROD-001-ACTIVE",
            actor_id="lyra",
            session_key="cron:tde-job-runner-v1",
            trigger_source="cron",
            tick_id="s16-fail",
            max_claim=1,
            objective_id="",
            objective_checkpoint="S16",
            rationale_trace="trace:objective-linkage",
            tasks_path=tasks,
            artifact_path=fail_artifact,
            writeback_tasks_path=tasks,
            binding_registry_path=binding_registry,
        )
        assert bad["status"] == "failed_validation"
        assert bad["fail_closed_reason"] == "missing_objective_linkage_field:objective_id"
        assert bad["outcomes"]["failed_validation"] == 1

    print("[PASS] S16 objective linkage checks passed")


if __name__ == "__main__":
    main()

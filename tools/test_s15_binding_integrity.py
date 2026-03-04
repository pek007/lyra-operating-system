#!/usr/bin/env python3
from __future__ import annotations

import json
import tempfile
from pathlib import Path

from tde_job_tick_runner import run_job_tick


def _seed_tasks(path: Path) -> None:
    path.write_text(
        """# TASKS.md (Temporary Kanban)\n\n## Inbox\n\n## Triage\n\n## Active\n- [ ] TDE-TEST-001 | Test task for S15 binding checks\n\n## Waiting\n\n## Done\n""",
        encoding="utf-8",
    )


def _seed_binding_registry(path: Path, binding_id: str) -> None:
    payload = {"bindings": [{"binding_id": binding_id, "job_id": "JOB-PROD-001", "actor_id": "lyra", "session_key": "cron:tde-job-runner-v1", "status": "active", "binding_epoch": 1}]}
    path.write_text(json.dumps(payload), encoding="utf-8")


def _seed_objectives(path: Path) -> None:
    payload = {"objectives": [{"objective_id": "OBJ-TDE-FOUNDATION", "allowed_checkpoints": ["S15"]}]}
    path.write_text(json.dumps(payload), encoding="utf-8")


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tmpdir = Path(tmp)
        tasks = tmpdir / "TASKS.md"
        artifact_pass = tmpdir / "pass.json"
        artifact_fail = tmpdir / "fail.json"
        binding_registry = tmpdir / "bindings.json"
        objective_registry = tmpdir / "objectives.json"

        _seed_tasks(tasks)
        _seed_binding_registry(binding_registry, "BIND-JOB-PROD-001-ACTIVE")
        _seed_objectives(objective_registry)

        pass_result = run_job_tick(job_id="JOB-PROD-001", binding_id="BIND-JOB-PROD-001-ACTIVE", actor_id="lyra", session_key="cron:tde-job-runner-v1", trigger_source="cron", tick_id="s15-pass", max_claim=1, objective_id="OBJ-TDE-FOUNDATION", objective_checkpoint="S15", rationale_trace="binding-integrity", tasks_path=tasks, artifact_path=artifact_pass, writeback_tasks_path=tasks, binding_registry_path=binding_registry, objective_registry_path=objective_registry)
        assert pass_result["outcomes"]["progressed"] == 1
        assert pass_result["outcomes"]["reauth_required"] == 0

        _seed_tasks(tasks)
        mismatch_result = run_job_tick(job_id="JOB-PROD-001", binding_id="BIND-STALE-OLD", actor_id="lyra", session_key="cron:tde-job-runner-v1", trigger_source="cron", tick_id="s15-mismatch", max_claim=1, objective_id="OBJ-TDE-FOUNDATION", objective_checkpoint="S15", rationale_trace="binding-integrity", tasks_path=tasks, artifact_path=artifact_fail, writeback_tasks_path=tasks, binding_registry_path=binding_registry, objective_registry_path=objective_registry)
        assert mismatch_result["outcomes"]["reauth_required"] == 1

    print("[PASS] S15 binding integrity checks passed")


if __name__ == "__main__":
    main()

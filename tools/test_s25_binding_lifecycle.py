#!/usr/bin/env python3
from __future__ import annotations

import json
import tempfile
from pathlib import Path

from tde_job_tick_runner import run_job_tick


def _seed_tasks(path: Path) -> None:
    path.write_text("""# TASKS.md (Temporary Kanban)\n\n## Inbox\n\n## Triage\n\n## Active\n- [ ] TDE-S25-001 | Binding lifecycle guard task\n\n## Waiting\n\n## Done\n""", encoding="utf-8")


def _seed_objectives(path: Path) -> None:
    payload = {"objectives": [{"objective_id": "OBJ-TDE-FOUNDATION", "allowed_checkpoints": ["S25"]}]}
    path.write_text(json.dumps(payload), encoding="utf-8")


def _seed_binding(path: Path, status: str, expires_at: str | None = None) -> None:
    rec = {
        "binding_id": "BIND-JOB-PROD-001-ACTIVE",
        "job_id": "JOB-PROD-001",
        "actor_id": "lyra",
        "session_key": "cron:tde-job-runner-v1",
        "status": status,
        "binding_epoch": 2,
    }
    if expires_at:
        rec["expires_at"] = expires_at
    path.write_text(json.dumps({"bindings": [rec]}), encoding="utf-8")


def _run(tasks: Path, bindings: Path, objectives: Path, tick: str) -> dict:
    return run_job_tick(
        job_id="JOB-PROD-001",
        binding_id="BIND-JOB-PROD-001-ACTIVE",
        actor_id="lyra",
        session_key="cron:tde-job-runner-v1",
        trigger_source="cron",
        tick_id=tick,
        max_claim=1,
        objective_id="OBJ-TDE-FOUNDATION",
        objective_checkpoint="S25",
        rationale_trace="binding-lifecycle",
        tasks_path=tasks,
        artifact_path=tasks.parent / f"{tick}.json",
        writeback_tasks_path=tasks,
        binding_registry_path=bindings,
        objective_registry_path=objectives,
    )


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        tasks = root / "TASKS.md"
        bindings = root / "bindings.json"
        objectives = root / "objectives.json"
        _seed_objectives(objectives)

        _seed_tasks(tasks)
        _seed_binding(bindings, "revoked")
        revoked = _run(tasks, bindings, objectives, "s25-revoked")
        assert revoked["status"] == "failed_validation"
        assert revoked["fail_closed_reason"] == "binding_unresolved_fail_closed"

        _seed_tasks(tasks)
        _seed_binding(bindings, "active", expires_at="2020-01-01T00:00:00+00:00")
        expired = _run(tasks, bindings, objectives, "s25-expired")
        assert expired["status"] == "failed_validation"
        assert expired["fail_closed_reason"] == "binding_unresolved_fail_closed"

    print("[PASS] S25 binding lifecycle checks passed")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from __future__ import annotations

import json
import tempfile
from pathlib import Path

from tde_job_tick_runner import run_job_tick


def _seed_tasks(path: Path) -> None:
    path.write_text("""# TASKS.md (Temporary Kanban)\n\n## Inbox\n\n## Triage\n\n## Active\n- [ ] TDE-S17-001 | Binding resolution fail-closed test task\n\n## Waiting\n\n## Done\n""", encoding="utf-8")


def _seed_objectives(path: Path) -> None:
    payload = {"objectives": [{"objective_id": "OBJ-TDE-FOUNDATION", "allowed_checkpoints": ["S17"]}]}
    path.write_text(json.dumps(payload), encoding="utf-8")


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        tasks = root / "TASKS.md"
        _seed_tasks(tasks)
        objectives = root / "objectives.json"
        _seed_objectives(objectives)

        result = run_job_tick(job_id="JOB-PROD-001", binding_id="BIND-JOB-PROD-001-ACTIVE", actor_id="lyra", session_key="cron:tde-job-runner-v1", trigger_source="cron", tick_id="s17-failclosed", max_claim=1, objective_id="OBJ-TDE-FOUNDATION", objective_checkpoint="S17", rationale_trace="binding-registry-proof", tasks_path=tasks, artifact_path=root/"s17.json", writeback_tasks_path=tasks, binding_registry_path=root/"missing-bindings.json", objective_registry_path=objectives)
        assert result["status"] == "failed_validation"
        assert result["fail_closed_reason"] == "binding_unresolved_fail_closed"

    print("[PASS] S17 binding resolution fail-closed checks passed")


if __name__ == "__main__":
    main()

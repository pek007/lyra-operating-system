#!/usr/bin/env python3
from __future__ import annotations

import json
import multiprocessing as mp
import tempfile
from pathlib import Path

from tde_job_tick_runner import run_job_tick


def _seed_tasks(path: Path) -> None:
    path.write_text("""# TASKS.md (Temporary Kanban)\n\n## Inbox\n\n## Triage\n\n## Active\n- [ ] TDE-S18-001 | Atomic writeback task A\n- [ ] TDE-S18-002 | Atomic writeback task B\n\n## Waiting\n\n## Done\n""", encoding="utf-8")


def _seed_bindings(path: Path) -> None:
    payload = {"bindings": [{"binding_id": "BIND-JOB-PROD-001-ACTIVE", "job_id": "JOB-PROD-001", "actor_id": "lyra", "session_key": "cron:tde-job-runner-v1", "status": "active", "binding_epoch": 1}]}
    path.write_text(json.dumps(payload), encoding="utf-8")


def _seed_objectives(path: Path) -> None:
    payload = {"objectives": [{"objective_id": "OBJ-TDE-FOUNDATION", "allowed_checkpoints": ["S18"]}]}
    path.write_text(json.dumps(payload), encoding="utf-8")


def _run_tick(tasks: Path, bindings: Path, objectives: Path, artifact: Path, tick_id: str) -> None:
    run_job_tick(job_id="JOB-PROD-001", binding_id="BIND-JOB-PROD-001-ACTIVE", actor_id="lyra", session_key="cron:tde-job-runner-v1", trigger_source="cron", tick_id=tick_id, max_claim=1, objective_id="OBJ-TDE-FOUNDATION", objective_checkpoint="S18", rationale_trace="atomic-writeback", tasks_path=tasks, artifact_path=artifact, writeback_tasks_path=tasks, binding_registry_path=bindings, objective_registry_path=objectives)


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        tasks, bindings, objectives = root / "TASKS.md", root / "bindings.json", root / "objectives.json"
        _seed_tasks(tasks); _seed_bindings(bindings); _seed_objectives(objectives)

        p1 = mp.Process(target=_run_tick, args=(tasks, bindings, objectives, root / "a1.json", "s18-a"))
        p2 = mp.Process(target=_run_tick, args=(tasks, bindings, objectives, root / "a2.json", "s18-b"))
        p1.start(); p2.start(); p1.join(); p2.join()
        assert p1.exitcode == 0 and p2.exitcode == 0

        final_text = tasks.read_text(encoding="utf-8")
        assert final_text.count("## Active") == 1 and final_text.count("## Waiting") == 1

    print("[PASS] S18 atomic writeback concurrency checks passed")


if __name__ == "__main__":
    main()

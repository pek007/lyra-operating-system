#!/usr/bin/env python3
from __future__ import annotations

import tempfile
from pathlib import Path

from tde_job_tick_runner import run_job_tick


def _seed_tasks(path: Path) -> None:
    path.write_text(
        """# TASKS.md (Temporary Kanban)\n\n## Inbox\n\n## Triage\n\n## Active\n- [ ] TDE-S17-001 | Binding resolution fail-closed test task\n\n## Waiting\n\n## Done\n""",
        encoding="utf-8",
    )


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tmpdir = Path(tmp)
        tasks = tmpdir / "TASKS.md"
        artifact = tmpdir / "s17-failclosed.json"
        missing_registry = tmpdir / "missing-bindings.json"  # intentionally absent

        _seed_tasks(tasks)

        result = run_job_tick(
            job_id="JOB-PROD-001",
            binding_id="BIND-JOB-PROD-001-ACTIVE",
            actor_id="lyra",
            session_key="cron:tde-job-runner-v1",
            trigger_source="cron",
            tick_id="s17-failclosed",
            max_claim=1,
            objective_id="OBJ-TDE-FOUNDATION",
            objective_checkpoint="S17",
            rationale_trace="binding-registry-proof",
            tasks_path=tasks,
            artifact_path=artifact,
            writeback_tasks_path=tasks,
            binding_registry_path=missing_registry,
        )

        assert result["status"] == "failed_validation"
        assert result["fail_closed"] is True
        assert result["fail_closed_reason"] == "binding_unresolved_fail_closed"
        assert result["writeback"]["applied"] is False
        assert result["outcomes"]["failed_validation"] == 1

    print("[PASS] S17 binding resolution fail-closed checks passed")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from __future__ import annotations

import json
import tempfile
from pathlib import Path

from tde_job_tick_runner import _write_decision_advancement_record


def run_tests() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        out_dir = Path(tmp)
        path = _write_decision_advancement_record(
            artifact_dir=out_dir,
            tick_id="tick-001",
            task_id="TASK-001",
            objective_id="OBJ-001",
            metadata={"stage_id": "verification", "workflow_family": "implementation_verification_readiness"},
            policy_binding={
                "policy_ref": "products/task-management/07-decisions/REFERENCE_TDE_POLICY_ENVELOPE_IMPLEMENTATION_VERIFICATION_V1.json",
                "workflow_family": "implementation_verification_readiness",
            },
        )
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
        assert payload["artifactType"] == "tde_decision_advancement_record"
        assert payload["selected_outcome"] == "continue"
        assert payload["policy_envelope_ref"].endswith("REFERENCE_TDE_POLICY_ENVELOPE_IMPLEMENTATION_VERIFICATION_V1.json")
        assert payload["workflow_family"] == "implementation_verification_readiness"

    print("[PASS] TDE job tick runner tests passed")


if __name__ == "__main__":
    run_tests()

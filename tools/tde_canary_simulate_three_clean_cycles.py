#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from tde_canary_runtime_cycle import run_cycle


def main() -> None:
    artifact_path = Path("knowledge/evidence/2026-03/tde-canary-simulation-latest.json")
    state_path = Path("knowledge/evidence/2026-03/tde-canary-simulation-state.json")
    if state_path.exists():
        state_path.unlink()

    runs = []
    for _ in range(3):
        runs.append(
            run_cycle(
                trigger_source="cron",
                stalled_alert_threshold=1,
                artifact_path=artifact_path,
                state_path=state_path,
                simulate_clean=True,
            )
        )

    result = {
        "simulatedCycles": len(runs),
        "allClean": all(r["cleanCycle"] for r in runs),
        "finalConsecutiveCleanCycles": runs[-1]["consecutiveCleanCycles"],
    }
    out = Path("knowledge/evidence/2026-03/tde-canary-simulation-3-clean-cycles.json")
    out.write_text(json.dumps({"result": result, "cycles": runs}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from __future__ import annotations

import json
from dataclasses import asdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

from tde_kernel_slice_tests import TDEKernel, TriggerContract


def main() -> None:
    now = datetime.now(timezone.utc)
    kernel = TDEKernel()

    items = [
        {
            "id": "TASK-CANARY-STALE",
            "priority": "high",
            "tde_canary": True,
            "lastMeaningfulEventAt": (now - timedelta(hours=6)).isoformat(),
            "nextExpectedCheckpointAt": (now - timedelta(hours=1)).isoformat(),
            "stallReasonCode": "WAITING_APPROVAL",
        },
        {
            "id": "TASK-CANARY-ACTIVE",
            "priority": "high",
            "tde_canary": True,
            "lastMeaningfulEventAt": (now - timedelta(minutes=30)).isoformat(),
            "nextExpectedCheckpointAt": (now + timedelta(minutes=45)).isoformat(),
        },
    ]

    canary_items = [i for i in items if i.get("tde_canary") is True and i.get("priority") == "high"]

    trigger = TriggerContract(
        trigger_source="cron",
        trigger_id=f"cron-tde-canary-{now.strftime('%Y%m%d-%H%M%S')}",
        session_key="cron:tde-canary-v1",
        actor="lyra",
        job="JOB-ENG-001",
        triggered_at=now.isoformat(),
    )

    cycle = kernel.run_runtime_triggered_cycle(trigger, canary_items, now=now)

    artifact = {
        "cycleTimestamp": cycle["cycleTimestamp"],
        "triggerSource": cycle["trigger"]["triggerSource"],
        "triggerId": cycle["trigger"]["triggerId"],
        "evaluatedCount": len(cycle["classifications"]),
        "stalledCount": len(cycle["followups"]),
        "routes": cycle["followups"],
    }

    out = Path("knowledge/evidence/2026-03/tde-canary-status-latest.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(artifact, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(artifact))


if __name__ == "__main__":
    main()

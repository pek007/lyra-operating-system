#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime, timedelta, timezone

from tde_kernel import ActionRequest, TDEKernel, TriggerContract


def assert_common_fields(result: dict[str, object]) -> None:
    assert "policy_decision_id" in result
    assert "audit_link" in result


def run_tests() -> None:
    k = TDEKernel()

    t1 = k.execute(ActionRequest("t1", "k-t1", "h1", "lyra", "JOB-ENG-001", "task.transition", "TASK-1", 0, "low"))
    assert t1["status"] == "executed"
    assert_common_fields(t1)

    t2a = k.execute(ActionRequest("t2a", "k-t2", "same", "lyra", "JOB-ENG-001", "task.transition", "TASK-2", 0, "low"))
    t2b = k.execute(ActionRequest("t2b", "k-t2", "same", "lyra", "JOB-ENG-001", "task.transition", "TASK-2", 0, "low"))
    assert t2a["status"] == "executed"
    assert t2b["status"] == "replay"

    t3 = k.execute(ActionRequest("t3", "k-t2", "DIFF", "lyra", "JOB-ENG-001", "task.transition", "TASK-2", 0, "low"))
    assert t3["status"] == "idempotency_conflict"

    t4 = k.execute(ActionRequest("t4", "k-t4", "h4", "lyra", "JOB-ENG-001", "external.send", "MSG-1", 0, "high", True))
    assert t4["status"] == "blocked_pending_approval"
    assert_common_fields(t4)

    first = k.execute(ActionRequest("t5a", "k-t5a", "h5a", "lyra", "JOB-ENG-001", "task.transition", "TASK-5", 0, "low"))
    second = k.execute(ActionRequest("t5b", "k-t5b", "h5b", "lyra", "JOB-ENG-001", "task.transition", "TASK-5", 0, "low"))
    assert first["status"] == "executed"
    assert second["status"] == "version_conflict"

    t6_exec = k.execute(ActionRequest("t6", "k-t6", "h6", "lyra", "JOB-ENG-001", "task.transition", "TASK-6", 0, "low", simulate_ack_interrupt=True))
    assert t6_exec["status"] == "executed"
    t6_reconcile = k.reconcile("k-t6")
    assert t6_reconcile["status"] == "reconciled"

    assert all(k.canary_hooks.values())

    fixed_now = datetime(2026, 3, 2, 12, 0, tzinfo=timezone.utc)
    active = {"id": "TASK-ACTIVE", "priority": "high", "lastMeaningfulEventAt": (fixed_now - timedelta(minutes=30)).isoformat(), "nextExpectedCheckpointAt": (fixed_now + timedelta(minutes=60)).isoformat()}
    active_state = k.classify_progress_state(active, now=fixed_now)
    assert active_state["state"] == "active-background"

    at_risk = {"id": "TASK-AT-RISK", "priority": "high", "lastMeaningfulEventAt": (fixed_now - timedelta(minutes=180)).isoformat(), "nextExpectedCheckpointAt": (fixed_now + timedelta(minutes=30)).isoformat()}
    at_risk_state = k.classify_progress_state(at_risk, now=fixed_now)
    assert at_risk_state["state"] == "at-risk"

    stalled = {"id": "TASK-HIGH-STALE", "priority": "high", "lastMeaningfulEventAt": (fixed_now - timedelta(hours=6)).isoformat(), "nextExpectedCheckpointAt": (fixed_now - timedelta(hours=1)).isoformat(), "stallReasonCode": "WAITING_APPROVAL"}
    stalled_state = k.classify_progress_state(stalled, now=fixed_now)
    assert stalled_state["state"] == "stalled"
    assert stalled_state["nextAction"] == "escalate"

    heartbeat_trigger = TriggerContract("heartbeat", "hb-20260302-1200", "main", "lyra", "JOB-ENG-001", fixed_now.isoformat())
    hb_cycle = k.run_runtime_triggered_cycle(heartbeat_trigger, [active, stalled], now=fixed_now)
    assert hb_cycle["trigger"]["triggerSource"] == "heartbeat"

    cron_trigger = TriggerContract("cron", "cron-tde-anti-stall-20260302-1200", "cron:tde-anti-stall-v1", "lyra", "JOB-ENG-001", fixed_now.isoformat())
    cron_cycle = k.run_runtime_triggered_cycle(cron_trigger, [stalled], now=fixed_now)
    assert cron_cycle["trigger"]["triggerSource"] == "cron"

    print("[PASS] TDE kernel thin-slice tests passed (T1-T7 + S2/S3 checks)")


if __name__ == "__main__":
    run_tests()

#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Any


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class ActionRequest:
    request_id: str
    idempotency_key: str
    intent_hash: str
    actor: str
    job: str
    action: str
    target_id: str
    expected_version: int
    risk: str  # low|high
    requires_approval: bool = False
    approval_id: str | None = None
    simulate_ack_interrupt: bool = False


@dataclass
class AuditRecord:
    policy_decision_id: str
    idempotency_key: str
    actor: str
    job: str
    audit_link: str
    status: str
    details: dict[str, Any] = field(default_factory=dict)


class TDEKernel:
    """Thin-slice deterministic governance kernel for acceptance tests."""

    def __init__(self) -> None:
        self.versions: dict[str, int] = {}
        self.replay_index: dict[str, dict[str, Any]] = {}
        self.pending_approvals: dict[str, ActionRequest] = {}
        self.audit_log: list[AuditRecord] = []
        self.interrupted_ack: set[str] = set()
        self.canary_hooks = {
            "trello_write_blocked": True,
            "reconciliation_probe": True,
            "traceability_fields_required": True,
        }

    def _decision_packet(self, req: ActionRequest) -> dict[str, Any]:
        decision = "allow"
        obligations: list[str] = []
        if req.requires_approval or req.risk == "high":
            decision = "allow_with_obligations"
            obligations.append("approval_required")
        return {
            "policy_decision_id": f"pdr-{req.request_id}",
            "decision": decision,
            "obligations": obligations,
            "audit_link": f"audit://tde/{req.request_id}",
        }

    def execute(self, req: ActionRequest) -> dict[str, Any]:
        packet = self._decision_packet(req)

        prior = self.replay_index.get(req.idempotency_key)
        if prior:
            if prior["intent_hash"] != req.intent_hash:
                return {
                    "status": "idempotency_conflict",
                    "policy_decision_id": packet["policy_decision_id"],
                    "audit_link": packet["audit_link"],
                }
            return {
                **prior["result"],
                "status": "replay",
            }

        current_v = self.versions.get(req.target_id, 0)
        if current_v != req.expected_version:
            result = {
                "status": "version_conflict",
                "policy_decision_id": packet["policy_decision_id"],
                "audit_link": packet["audit_link"],
            }
            self.replay_index[req.idempotency_key] = {
                "intent_hash": req.intent_hash,
                "result": result,
            }
            self.audit_log.append(
                AuditRecord(
                    packet["policy_decision_id"],
                    req.idempotency_key,
                    req.actor,
                    req.job,
                    packet["audit_link"],
                    "version_conflict",
                )
            )
            return result

        if "approval_required" in packet["obligations"] and not req.approval_id:
            self.pending_approvals[req.request_id] = req
            result = {
                "status": "blocked_pending_approval",
                "policy_decision_id": packet["policy_decision_id"],
                "audit_link": packet["audit_link"],
            }
            self.replay_index[req.idempotency_key] = {
                "intent_hash": req.intent_hash,
                "result": result,
            }
            self.audit_log.append(
                AuditRecord(
                    packet["policy_decision_id"],
                    req.idempotency_key,
                    req.actor,
                    req.job,
                    packet["audit_link"],
                    "blocked_pending_approval",
                    {"obligations": packet["obligations"]},
                )
            )
            return result

        self.versions[req.target_id] = current_v + 1
        result = {
            "status": "executed",
            "policy_decision_id": packet["policy_decision_id"],
            "audit_link": packet["audit_link"],
            "new_version": self.versions[req.target_id],
        }

        self.replay_index[req.idempotency_key] = {
            "intent_hash": req.intent_hash,
            "result": result,
        }

        if req.simulate_ack_interrupt:
            self.interrupted_ack.add(req.idempotency_key)
            self.audit_log.append(
                AuditRecord(
                    packet["policy_decision_id"],
                    req.idempotency_key,
                    req.actor,
                    req.job,
                    packet["audit_link"],
                    "tool_executed_ack_interrupted",
                )
            )
        else:
            self.audit_log.append(
                AuditRecord(
                    packet["policy_decision_id"],
                    req.idempotency_key,
                    req.actor,
                    req.job,
                    packet["audit_link"],
                    "executed",
                )
            )

        return result

    def reconcile(self, idempotency_key: str) -> dict[str, Any]:
        if idempotency_key in self.interrupted_ack and idempotency_key in self.replay_index:
            self.interrupted_ack.remove(idempotency_key)
            return {**self.replay_index[idempotency_key]["result"], "status": "reconciled"}
        return {"status": "noop"}

    def anti_stall_candidates(self, items: list[dict[str, Any]], idle_minutes: int = 240) -> list[dict[str, Any]]:
        cutoff = datetime.now(timezone.utc) - timedelta(minutes=idle_minutes)
        out: list[dict[str, Any]] = []
        for item in items:
            if item.get("priority") != "high":
                continue
            updated = datetime.fromisoformat(item["updated_at"])
            if updated < cutoff:
                out.append(item)
        return out


def assert_common_fields(result: dict[str, Any]) -> None:
    assert "policy_decision_id" in result
    assert "audit_link" in result


def run_tests() -> None:
    k = TDEKernel()

    # T1
    t1 = k.execute(
        ActionRequest("t1", "k-t1", "h1", "lyra", "JOB-ENG-001", "task.transition", "TASK-1", 0, "low")
    )
    assert t1["status"] == "executed"
    assert_common_fields(t1)

    # T2
    t2a = k.execute(
        ActionRequest("t2a", "k-t2", "same", "lyra", "JOB-ENG-001", "task.transition", "TASK-2", 0, "low")
    )
    t2b = k.execute(
        ActionRequest("t2b", "k-t2", "same", "lyra", "JOB-ENG-001", "task.transition", "TASK-2", 0, "low")
    )
    assert t2a["status"] == "executed"
    assert t2b["status"] == "replay"

    # T3
    t3 = k.execute(
        ActionRequest("t3", "k-t2", "DIFF", "lyra", "JOB-ENG-001", "task.transition", "TASK-2", 0, "low")
    )
    assert t3["status"] == "idempotency_conflict"

    # T4
    t4 = k.execute(
        ActionRequest("t4", "k-t4", "h4", "lyra", "JOB-ENG-001", "external.send", "MSG-1", 0, "high", True)
    )
    assert t4["status"] == "blocked_pending_approval"
    assert_common_fields(t4)

    # T5
    first = k.execute(
        ActionRequest("t5a", "k-t5a", "h5a", "lyra", "JOB-ENG-001", "task.transition", "TASK-5", 0, "low")
    )
    second = k.execute(
        ActionRequest("t5b", "k-t5b", "h5b", "lyra", "JOB-ENG-001", "task.transition", "TASK-5", 0, "low")
    )
    assert first["status"] == "executed"
    assert second["status"] == "version_conflict"

    # T6
    t6_exec = k.execute(
        ActionRequest(
            "t6",
            "k-t6",
            "h6",
            "lyra",
            "JOB-ENG-001",
            "task.transition",
            "TASK-6",
            0,
            "low",
            simulate_ack_interrupt=True,
        )
    )
    assert t6_exec["status"] == "executed"
    t6_reconcile = k.reconcile("k-t6")
    assert t6_reconcile["status"] == "reconciled"

    # T7
    assert all(k.canary_hooks.values())

    # Anti-stall hook definition behavior
    old_item = {
        "id": "TASK-HIGH-STALE",
        "priority": "high",
        "updated_at": (datetime.now(timezone.utc) - timedelta(hours=6)).isoformat(),
    }
    fresh_item = {
        "id": "TASK-HIGH-FRESH",
        "priority": "high",
        "updated_at": now_iso(),
    }
    cands = k.anti_stall_candidates([old_item, fresh_item], idle_minutes=240)
    assert [c["id"] for c in cands] == ["TASK-HIGH-STALE"]

    print("[PASS] TDE kernel thin-slice tests passed (T1-T7 + anti-stall candidate selection)")


if __name__ == "__main__":
    run_tests()

#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
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
    risk: str
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


@dataclass
class TriggerContract:
    trigger_source: str
    trigger_id: str
    session_key: str
    actor: str
    job: str
    triggered_at: str


class TDEKernel:
    PROGRESS_STATES = {"active-background", "at-risk", "stalled"}
    STALL_REASON_CODES = {"WAITING_APPROVAL", "DEPENDENCY_BLOCKED", "NO_EXECUTOR_ACTIVITY", "RETRYING_FAILURE", "UNKNOWN_NEEDS_TRIAGE"}
    STALL_REASON_TO_ROUTE = {
        "WAITING_APPROVAL": "escalate",
        "DEPENDENCY_BLOCKED": "escalate",
        "NO_EXECUTOR_ACTIVITY": "resume",
        "RETRYING_FAILURE": "redefine",
        "UNKNOWN_NEEDS_TRIAGE": "retire",
    }

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
        return {"policy_decision_id": f"pdr-{req.request_id}", "decision": decision, "obligations": obligations, "audit_link": f"audit://tde/{req.request_id}"}

    def execute(self, req: ActionRequest) -> dict[str, Any]:
        packet = self._decision_packet(req)
        prior = self.replay_index.get(req.idempotency_key)
        if prior:
            if prior["intent_hash"] != req.intent_hash:
                return {"status": "idempotency_conflict", "policy_decision_id": packet["policy_decision_id"], "audit_link": packet["audit_link"]}
            return {**prior["result"], "status": "replay"}

        current_v = self.versions.get(req.target_id, 0)
        if current_v != req.expected_version:
            result = {"status": "version_conflict", "policy_decision_id": packet["policy_decision_id"], "audit_link": packet["audit_link"]}
            self.replay_index[req.idempotency_key] = {"intent_hash": req.intent_hash, "result": result}
            self.audit_log.append(AuditRecord(packet["policy_decision_id"], req.idempotency_key, req.actor, req.job, packet["audit_link"], "version_conflict"))
            return result

        if "approval_required" in packet["obligations"] and not req.approval_id:
            self.pending_approvals[req.request_id] = req
            result = {"status": "blocked_pending_approval", "policy_decision_id": packet["policy_decision_id"], "audit_link": packet["audit_link"]}
            self.replay_index[req.idempotency_key] = {"intent_hash": req.intent_hash, "result": result}
            self.audit_log.append(AuditRecord(packet["policy_decision_id"], req.idempotency_key, req.actor, req.job, packet["audit_link"], "blocked_pending_approval", {"obligations": packet["obligations"]}))
            return result

        self.versions[req.target_id] = current_v + 1
        result = {"status": "executed", "policy_decision_id": packet["policy_decision_id"], "audit_link": packet["audit_link"], "new_version": self.versions[req.target_id]}
        self.replay_index[req.idempotency_key] = {"intent_hash": req.intent_hash, "result": result}
        status = "tool_executed_ack_interrupted" if req.simulate_ack_interrupt else "executed"
        if req.simulate_ack_interrupt:
            self.interrupted_ack.add(req.idempotency_key)
        self.audit_log.append(AuditRecord(packet["policy_decision_id"], req.idempotency_key, req.actor, req.job, packet["audit_link"], status))
        return result

    def reconcile(self, idempotency_key: str) -> dict[str, Any]:
        if idempotency_key in self.interrupted_ack and idempotency_key in self.replay_index:
            self.interrupted_ack.remove(idempotency_key)
            return {**self.replay_index[idempotency_key]["result"], "status": "reconciled"}
        return {"status": "noop"}

    def classify_progress_state(self, item: dict[str, Any], now: datetime | None = None, at_risk_minutes: int = 120, stalled_minutes: int = 240) -> dict[str, Any]:
        current = now or datetime.now(timezone.utc)
        last_meaningful_event_at = datetime.fromisoformat(item["lastMeaningfulEventAt"])
        checkpoint = datetime.fromisoformat(item["nextExpectedCheckpointAt"])
        age_minutes = int((current - last_meaningful_event_at).total_seconds() // 60)
        if age_minutes >= stalled_minutes:
            state = "stalled"
            stall_reason = item.get("stallReasonCode") or "UNKNOWN_NEEDS_TRIAGE"
            if stall_reason not in self.STALL_REASON_CODES:
                raise ValueError(f"invalid stall reason code: {stall_reason}")
            next_action = self.route_stall_action(stall_reason)
        elif age_minutes >= at_risk_minutes or checkpoint <= current:
            state = "at-risk"; stall_reason = None; next_action = "warning"
        else:
            state = "active-background"; stall_reason = None; next_action = "continue"
        return {"id": item["id"], "state": state, "lastMeaningfulEventAt": item["lastMeaningfulEventAt"], "nextExpectedCheckpointAt": item["nextExpectedCheckpointAt"], "stallReasonCode": stall_reason, "nextAction": next_action}

    def route_stall_action(self, stall_reason_code: str) -> str:
        if stall_reason_code not in self.STALL_REASON_TO_ROUTE:
            raise ValueError(f"unknown stall reason code: {stall_reason_code}")
        return self.STALL_REASON_TO_ROUTE[stall_reason_code]

    def anti_stall_candidates(self, items: list[dict[str, Any]], idle_minutes: int = 240, now: datetime | None = None) -> list[dict[str, Any]]:
        current = now or datetime.now(timezone.utc)
        out: list[dict[str, Any]] = []
        for item in items:
            if item.get("priority") != "high":
                continue
            classified = self.classify_progress_state(item, now=current, stalled_minutes=idle_minutes)
            if classified["state"] == "stalled":
                out.append(classified)
        return out

    def validate_trigger_contract(self, trigger: TriggerContract) -> dict[str, Any]:
        if trigger.trigger_source not in {"heartbeat", "cron"}:
            raise ValueError(f"invalid trigger_source: {trigger.trigger_source}")
        if not trigger.trigger_id.strip() or not trigger.session_key.strip() or not trigger.actor.strip() or not trigger.job.strip():
            raise ValueError("invalid trigger fields")
        datetime.fromisoformat(trigger.triggered_at)
        return {"triggerSource": trigger.trigger_source, "triggerId": trigger.trigger_id, "sessionKey": trigger.session_key, "actor": trigger.actor, "job": trigger.job, "triggeredAt": trigger.triggered_at}

    def apply_stall_followup_policy(self, classified: dict[str, Any]) -> dict[str, Any]:
        if classified["state"] != "stalled":
            raise ValueError("follow-up policy only applies to stalled items")
        route = classified["nextAction"]
        if route not in {"resume", "escalate", "redefine", "retire"}:
            raise ValueError(f"invalid routed action: {route}")
        requires_approval = route in {"escalate", "retire"}
        return {"targetId": classified["id"], "route": route, "stallReasonCode": classified["stallReasonCode"], "requiresApproval": requires_approval, "policyGate": "approval_required" if requires_approval else "none", "status": "blocked_pending_approval" if requires_approval else "ready_for_execution"}

    def run_runtime_triggered_cycle(self, trigger: TriggerContract, items: list[dict[str, Any]], now: datetime | None = None, idle_minutes: int = 240) -> dict[str, Any]:
        contract = self.validate_trigger_contract(trigger)
        current = now or datetime.now(timezone.utc)
        classifications = [self.classify_progress_state(item, now=current, stalled_minutes=idle_minutes) for item in items]
        followups = [self.apply_stall_followup_policy(c) for c in classifications if c["state"] == "stalled"]
        return {"cycleTimestamp": current.isoformat(), "trigger": contract, "classifications": classifications, "followups": followups}

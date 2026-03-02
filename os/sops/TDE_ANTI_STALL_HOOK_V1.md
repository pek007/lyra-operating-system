# TDE Anti-Stall Hook v1 (Heartbeat + Cron)

Status: Active  
Owner: JOB-OPS-001 (R), JOB-PROD-001 (A)

## Purpose
Prevent high-priority tasks from remaining idle indefinitely by running periodic stall detection and controlled follow-up actions.

## Triggering model
Use two complementary OpenClaw primitives:

1. **Heartbeat sweep (context-aware):**
   - prompt reads `HEARTBEAT.md` checklist
   - checks high-priority items with `last_update_age > 4h`
   - batches decisions with current conversation context

2. **Cron sweep (time-precise + isolated):**
   - schedule every 2h during active day window
   - executes same stale-item query in isolated run
   - emits report/evidence even when no main-session activity occurs

## Progress-state contract (S2)
Required machine-readable fields per tracked item:
- `lastMeaningfulEventAt`
- `nextExpectedCheckpointAt`
- `state` (`active-background|at-risk|stalled`)
- `stallReasonCode` (required when `state=stalled`)
- `nextAction`

Classification policy:
- `active-background`: recent meaningful activity and checkpoint still inside SLA
- `at-risk`: aging warning threshold breached or checkpoint overdue, but not yet stalled
- `stalled`: stale beyond SLA without meaningful progress

## Decision pathway per stalled high-priority item
Exactly one action must be selected and recorded.
Deterministic reason-code routing (v1):
- `WAITING_APPROVAL` -> **escalate**
- `DEPENDENCY_BLOCKED` -> **escalate**
- `NO_EXECUTOR_ACTIVITY` -> **resume**
- `RETRYING_FAILURE` -> **redefine**
- `UNKNOWN_NEEDS_TRIAGE` -> **retire**

## Guardrails
- No autonomous authority expansion.
- External-send or boundary-changing actions remain approval-gated.
- If route unresolved after two sweeps, escalate to `JOB-OWN-001`.

## Evidence contract
Each anti-stall sweep must emit:
- sweep timestamp
- stale-item list
- chosen action (`resume|escalate|redefine|retire`)
- actor/job
- audit link

## T7 readiness tie-in
Anti-stall is a canary-readiness hook: canary lane must prove no critical item can remain stale without a follow-up decision.

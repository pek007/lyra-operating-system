# TDE Kernel S2 Planning Packet v1

Date: 2026-03-02
Status: Active

## Scope
Implement the minimum autonomous flow-observability loop using OpenClaw-native primitives:
- progress-state classification
- anti-stall detection
- deterministic follow-up routing

## Deliverables
1. `WO-2026-TDE-KERNEL-S2.md`
2. Progress-state model update in kernel spec
3. Anti-stall heartbeat/cron contract update
4. Test runner extensions + verification evidence

## Progress-state model (v1)
- `active-background`: recent activity within SLA, next checkpoint defined
- `at-risk`: aging threshold warning, no terminal block yet
- `stalled`: SLA breach without meaningful progress event

Required fields per tracked item:
- `lastMeaningfulEventAt`
- `nextExpectedCheckpointAt`
- `state`
- `stallReasonCode`
- `nextAction`

## Stall reason codes (initial)
- `WAITING_APPROVAL`
- `DEPENDENCY_BLOCKED`
- `NO_EXECUTOR_ACTIVITY`
- `RETRYING_FAILURE`
- `UNKNOWN_NEEDS_TRIAGE`

## Routing policy
- `active-background` -> continue, report cadence only
- `at-risk` -> warning + checkpoint tighten
- `stalled` -> auto-route one of `resume|escalate|redefine|retire`

## Acceptance mapping
- T1–T7 remains baseline
- S2 adds: progress-state classification correctness + stalled routing determinism

## Risks
- False positives in stalled detection if signal quality is weak
- Over-escalation noise without reason-code hygiene

## Mitigations
- Start with conservative SLA defaults
- Require reason code in every stalled classification
- Keep escalation actions policy-gated and auditable

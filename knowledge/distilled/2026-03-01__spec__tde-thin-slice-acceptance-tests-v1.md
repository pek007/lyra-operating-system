# TDE Thin Slice Acceptance Tests v1

Status: Draft-for-approval  
Date: 2026-03-01

## Approval model
- Primary approver (product acceptance): **JOB-PROD-001 — Product Owner**
- Co-approver (technical/safety integrity): **JOB-ARC-001 — Chief Architect**
- Escalation/final arbiter only: **JOB-OWN-001 — System Owner & Final Decision Authority**

## Slice under test
Trigger -> evaluate state -> generate decision packet -> apply approval gate -> idempotent execution -> audit/evidence linkage.

## Test cases

### T1: Happy path (low risk)
- Given: valid low-risk task transition request
- Expect: transition allowed, executed once, audit recorded, evidence linked

### T2: Duplicate command replay
- Given: same idempotency key and identical intent submitted N times
- Expect: single logical side effect; deterministic replay response

### T3: Idempotency mismatch
- Given: same idempotency key with different intent hash
- Expect: conflict/error; no new side effect

### T4: Approval-required action
- Given: high-risk action (external send or boundary change)
- Expect: allow-with-obligations; execution blocked until approval

### T5: Concurrent mutation conflict
- Given: two actions on same target with same expected version
- Expect: one succeeds, one deterministic conflict

### T6: Partial failure recovery
- Given: action succeeds at tool layer but ack/state update interrupted
- Expect: safe reconciliation (idempotent replay or explicit escalation)

### T7: Trello canary slice readiness
- Given: canary domain in TDE
- Expect: no operational Trello writes, reconciliation stable, traceability complete

## Pass threshold
All tests pass without unresolved safety exceptions; any failure in T2–T6 is build-blocking.

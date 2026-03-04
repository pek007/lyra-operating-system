# TDE Kernel Slice S1 Spec

Status: Active (S1)  
Owner: JOB-ENG-001 (R), JOB-PROD-001 (A)

## Scope
Thin-slice governance kernel implementing:
Trigger -> evaluate -> decision packet -> approval gate -> idempotent execution -> audit link.

## Required records on mutate/execute
Every side-effecting request/result MUST include:
- `policy_decision_id`
- `idempotency_key`
- `actor`
- `job`
- `audit_link`

## Control flow
1. Intake action request with actor/job identity and expected target version.
2. Evaluate policy and emit decision packet (`allow` or `allow_with_obligations`).
3. If obligations include `approval_required`, block execution until approval token is attached.
4. Enforce idempotency contract:
   - same key + same intent hash => replay response, no new side effect
   - same key + different intent hash => deterministic conflict
5. Enforce optimistic concurrency via `expected_version`.
6. Write audit record linking request, policy decision, and outcome.
7. On partial-failure interruption, reconcile via idempotent replay and explicit `reconciled` event.

## Acceptance mapping (T1-T7)
- T1: Low-risk transition executes once with audit.
- T2: Duplicate replay is deterministic and side-effect free.
- T3: Idempotency mismatch fails closed.
- T4: High-risk action blocked pending approval.
- T5: Concurrent mutation conflict deterministic.
- T6: Partial failure recovery reconciles safely.
- T7: Canary readiness hooks present and enabled:
  - `trello_write_blocked`
  - `reconciliation_probe`
  - `traceability_fields_required`

## Notes
This is kernel scaffolding for governance correctness, not production runtime wiring.

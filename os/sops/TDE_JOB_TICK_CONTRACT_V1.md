# TDE Job Tick Contract v1

Status: Draft (S13)
Owner: JOB-PROD-001
Related WO: `WO-2026-TDE-KERNEL-S13`

## Purpose
Define deterministic runtime semantics for a job-scoped execution tick so jobs are operational (not only documented) in the TDE control plane.

## Trigger
- Allowed trigger sources: `cron` (default), `heartbeat` (control-plane exception)
- Default mode: isolated cron run
- Delivery default: internal/silent (no user-facing delivery unless escalation conditions are met)

## Required Inputs
- `job_id` (string, required)
- `binding_id` (string, required unless explicit `binding_status=unbound` path)
- `actor_id` (string, required)
- `session_key` (string, required)
- `tick_id` (string, unique per run)
- `max_claim` (int, bounded by WIP policy)

## Claim Rules
1. Pull only items routed to `job_id` and in ready state.
2. Enforce WIP bound before claiming (`max_claim`, policy cap).
3. Claim is atomic and idempotent by `tick_id` + item id.
4. If binding is missing/invalid for side-effecting transitions, fail closed and emit decision-required artifact.

## Execution Rules
- Every side-effecting mutation must carry:
  - `job_id`
  - `binding_id`
  - `policy_decision_id`
  - `idempotency_key`
  - `expected_version`
- Retry behavior must be idempotent (same key => same outcome class)
- Approval-required routes (`escalate`, `retire`, or policy-marked actions) must not execute without gate approval.

## Outputs
Per tick, emit deterministic artifact including:
- `tick_id`, `trigger_source`, `job_id`, `binding_id`, `actor_id`, timestamp
- Claimed item IDs + transition attempts
- Idempotency keys used
- Decision records created/updated
- Evidence artifacts produced
- Outcome counters: `progressed`, `blocked_pending_approval`, `failed_validation`, `no_work`

## Fail-Closed Conditions
Tick must end without mutation when any of the following are true:
- Missing/invalid `job_id` or `actor_id`
- Missing/expired `binding_id` for mutation path
- Policy decision unavailable for gated action
- Version conflict without safe retry path

## Escalation Conditions
Escalate to decision queue when:
- Repeated stalls exceed threshold
- Approval is required for route/action
- Binding/authority drift is detected
- Canonical source quality is insufficient for safe mutation

## Verification Hooks (S13)
- Add unit tests for input validation + fail-closed behavior
- Add run-cycle verification artifact in `knowledge/evidence/2026-03/`
- Demonstrate one isolated tick progressing at least one ready item without manual prompt

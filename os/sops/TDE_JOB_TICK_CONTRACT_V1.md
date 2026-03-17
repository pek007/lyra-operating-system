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
- `binding_registry` (active binding object source; required for strict runtime binding integrity)
- `objective_id` (string, required for side-effecting mutation path)
- `objective_checkpoint` (string, required checkpoint tag)
- `rationale_trace` (string, required concise rationale/trace reference)
- `objective_registry` (required objective authority source for validation of objective id/checkpoint)

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
- Runtime MUST validate objective linkage contract before side-effecting mutation:
  - `objective_id` present and non-empty
  - `objective_checkpoint` present and non-empty
  - `rationale_trace` present and non-empty
  - `objective_id` exists in objective registry
  - `objective_checkpoint` is allowed for the objective (when registry provides an allowlist)
- Runtime MUST resolve active binding object and validate envelope context.
- Binding lifecycle semantics are mandatory: only `status=active` and non-expired bindings are valid authority; `revoked`/`expired`/invalid-expiry records are treated as unresolved for mutation paths.
- For side-effecting mutation paths, unresolved binding registry lookup MUST fail closed (`binding_unresolved_fail_closed`); synthesized/fallback active bindings are not valid authority proof.
- Runtime MUST resolve active binding object and validate envelope context:
  - `envelope.job_id == active_binding.job_id`
  - `envelope.binding_id == active_binding.binding_id`
  - `actor_id == active_binding.actor_id`
  - `session_key == active_binding.session_key` (when set)
- On any binding mismatch/change, runtime must fail closed and return `REAUTH_REQUIRED_ON_BINDING_CHANGE` (or specific mismatch reason) with explicit retry obligations: fresh `policy_decision_id` + fresh `idempotency_key`.
- Retry behavior must be idempotent (same key => same outcome class)
- Approval-required routes (`escalate`, `retire`, or policy-marked actions) must not execute without gate approval.

## Outputs
Per tick, emit deterministic artifact including:
- `tick_id`, `trigger_source`, `job_id`, `binding_id`, `actor_id`, `session_key`, timestamp
- `objective_linkage` block with `objective_id`, `objective_checkpoint`, `rationale_trace`
- `binding_context` block with active binding object + source + status
- Claimed item IDs + transition attempts
- Idempotency keys used
- Decision records created/updated
- Evidence artifacts produced
- Outcome counters: `progressed`, `blocked_pending_approval`, `failed_validation`, `no_work`, `reauth_required`

## Fail-Closed Conditions
Tick must end without mutation when any of the following are true:
- Missing/invalid `job_id` or `actor_id`
- Missing objective linkage fields (`objective_id`, `objective_checkpoint`, `rationale_trace`) for mutation path
- Missing/expired `binding_id` for mutation path
- Binding mismatch/drift against active binding object (`actor/job/session_key/binding_id`)
- Policy decision unavailable for gated action
- Version conflict without safe retry path

## Escalation Conditions
Escalate to decision queue when:
- Repeated stalls exceed threshold
- Approval is required for route/action
- Binding/authority drift is detected
- Canonical source quality is insufficient for safe mutation
- Frontier/canonical-store status is unclear before a resumed implementation path

## Operating alignment note
This contract may rely on the improved Lyra OS memory/handoff substrate for continuity and coordination, but only under the following boundaries:
- durable job-shaped work should prefer job-bundle continuity over transcript continuity
- artifact-backed handoffs are preferred for same-runtime coordination
- coordination/handoff state is not canonical execution state
- canonical authority for mutation remains the current TDE runtime store and contract surface

## Verification Hooks (S13)
- Add unit tests for input validation + fail-closed behavior
- Add run-cycle verification artifact in `knowledge/evidence/2026-03/`
- Demonstrate one isolated tick progressing at least one ready item without manual prompt

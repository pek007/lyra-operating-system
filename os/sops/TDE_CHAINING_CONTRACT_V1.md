# TDE Chaining Contract v1

Status: Active
Owner: JOB-PROD-001
Date: 2026-03-09
Related plan: `governance/TDE_AUTONOMOUS_CHAINING_IMPLEMENTATION_PLAN_V1.md`

## Purpose
Define the first bounded runtime contract for autonomous chaining in TDE.

The goal is to let TDE continue moving toward a higher-level objective by promoting successor tasks to ready when predecessor tasks are completed, without requiring human intervention for each handoff.

This contract is intentionally limited to deterministic, dependency-aware **state-driven chaining**.

## Scope
### In scope
- predecessor/successor metadata on tasks
- deterministic readiness promotion
- scheduler-driven continuation via normal job tick execution
- bounded promotion under existing WIP and policy controls
- evidence of why a successor became ready

### Out of scope
- generic autonomous task generation
- direct-dispatch event bus
- free-text activation logic
- approval bypass for gated actions
- recursive or unbounded chain expansion

## Canonical model
Chaining in v1 is implemented as:

**predecessor completion -> successor eligibility evaluation -> successor promoted to ready -> normal tick claims next ready work**

This means TDE remains scheduler-governed.
Task completion does not directly dispatch uncontrolled follow-on execution.

## Canonical metadata fields
For v1, the following task metadata fields are authoritative when present in canonical DB state:

- `depends_on`: array of predecessor task IDs
- `activation_rule`: string enum; supported v1 value: `all_predecessors_done`
- `objective_id`: optional objective linkage for traceability
- `stage_id`: optional stage grouping identifier
- `chain_policy`: optional object for boundedness/promotion hints
- `activated_by`: runtime-written provenance field
- `activated_at`: runtime-written provenance field

## Metadata semantics
### `depends_on`
- Must be an array of task IDs.
- Empty or absent means the task does not rely on predecessor completion for readiness.
- Unknown task references are invalid for safe promotion.

### `activation_rule`
- If present, must be `all_predecessors_done` in v1.
- Any other value is unsupported and must fail closed for promotion.

### `objective_id`
- Optional for storage.
- Recommended whenever chaining is part of a larger high-level target.
- If runtime policy later requires objective linkage for certain chain families, that stricter rule may be layered on top.

### `stage_id`
- Optional grouping field for staged workflow readability.
- Does not itself control readiness.

### `chain_policy`
Optional object reserved for boundedness hints such as:
- `promotion_cap_class`
- `family`
- `pilot_enabled`

No free-form execution logic is permitted in `chain_policy`.

### `activated_by`
- Runtime-set provenance field naming the predecessor completion or system rule that caused activation.
- Must not be manually treated as authority.

### `activated_at`
- Runtime-set ISO-8601 timestamp for successor readiness promotion.

## Promotion rule
A task may be promoted to `ready` only when all of the following are true:
1. task exists in canonical state
2. task is not already `ready`, `done`, or otherwise terminal
3. `depends_on` is present and valid
4. every predecessor task exists
5. every predecessor task is complete
6. `activation_rule` is absent or equals `all_predecessors_done`
7. no chain-policy bound is breached
8. promotion does not bypass any approval gate that applies at execution time

## Approval semantics
Chaining promotion is **not** approval bypass.

Promotion to `ready` only means the successor is now eligible for normal execution handling.
Any later route/action that requires approval must still remain:
- `blocked_pending_approval`, or
- otherwise fail closed under the relevant runtime contract.

## Tick behavior
During an enabled chaining tick, runtime should:
1. load canonical task state
2. evaluate non-ready tasks with dependency metadata
3. promote newly eligible tasks to `ready`
4. record activation provenance
5. emit activation evidence
6. continue normal bounded claim-and-execute flow

The runtime may perform the claim step in the same tick if:
- promotion completed successfully,
- WIP bounds allow it,
- all ordinary mutation checks pass.

## Idempotency rule
Repeated evaluation on unchanged state must not create duplicate promotions.

If a task is already promoted/ready from a prior valid evaluation, re-running the tick must preserve the same state without duplication or drift.

## Fail-closed conditions
Successor promotion must not occur when any of the following are true:
- predecessor task reference missing
- predecessor completion state ambiguous
- unsupported activation rule
- malformed dependency metadata
- chain-policy guard violated
- runtime cannot produce deterministic activation evidence

In such cases, runtime should leave the successor non-ready and emit an explicit reason where possible.

## Evidence contract
Each chaining-enabled tick should emit either an activation block or separate activation artifact containing:
- tick identifier
- successor task ID
- predecessor task IDs
- activation rule used
- timestamp
- objective/stage context when present
- skipped promotions with reasons when relevant

## Boundedness rules
- Existing WIP / `max_claim` bounds remain authoritative.
- Chaining must never imply unlimited execution in a single tick.
- If multiple successors become ready at once, only bounded claim/execution may proceed.
- Broad or ambiguous fan-out patterns should be blocked or deferred until explicitly supported.

## Pilot workflow families approved for v1
The first approved pilot workflow families are:

### Pilot family A — implementation -> verification -> deployment-readiness review
Purpose: prove deterministic chaining in a familiar staged delivery flow.

Stages:
1. implementation complete
2. verification task promoted to ready
3. deployment-readiness review task promoted after verification completion

### Pilot family B — verification -> closeout / improvement capture
Purpose: prove that execution can feed the continuous-improvement loop.

Stages:
1. verification complete
2. closeout or improvement-capture task promoted to ready

## Product-owner modeling rule
Product Owners should model chaining only for:
- explicit staged work,
- bounded workflows,
- clearly named predecessor/successor relationships.

Do not use chaining metadata to represent vague aspirations, broad strategic intent, or open-ended exploration.

## Rollback rule
If chaining causes ambiguous promotion, unexpected fan-out, or governance uncertainty:
- disable chaining evaluation,
- preserve task metadata,
- return to ordinary scheduler-driven claim behavior,
- keep evidence for diagnosis and redesign.

## Change rule
Any expansion beyond:
- `all_predecessors_done`,
- bounded successor promotion,
- approved pilot families,

requires a new contract version or explicit amendment evidence.

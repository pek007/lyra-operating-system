# TDE Bounded Research/Re-entry Release Packet v1

Date: 2026-03-13
Status: Staging validation packet
Owner: Peter + Lyra
Purpose: Consolidated release-ready staging packet for the bounded TDE research/re-entry capability
Related:
- `TDE_RUNTIME_PROMOTION_CHECKLIST_V1.md`
- `TDE_RUNTIME_PROMOTE_ROLLBACK_SOP_V1.md`
- `products/task-management/07-decisions/TDE_DECISION_TO_ADVANCEMENT_POLICY_V1.md`
- `products/task-management/07-decisions/TDE_PILOT_WORKFLOW_FAMILY_IMPLEMENTATION_VERIFICATION_READINESS_V1.md`
- `products/task-management/07-decisions/TDE_DECISION_POLICY_RUNTIME_EMBODIMENT_V1.md`

## Candidate scope summary
This packet covers the bounded runtime D-layer slice that now supports:
- policy-bound `continue`
- bounded `research_further`
- formal `escalate`
- recursive re-entry after research completion
- re-entry outcomes:
  - `continue`
  - `retry`
  - `defer`
  - `block`
- research budget enforcement with forced escalation on exhaustion
- origin-task parking / non-claimable behavior while research is active
- evidence-aware re-entry decision records

## Why this packet exists
The implementation work is now spread across multiple commits and pilot notes.
This packet consolidates the validation story into one place so a future promotion decision can be made cleanly.

## Recommended promotion stance
**Not yet an automatic promotion recommendation.**

Recommended next promotion stance:
- eligible for a narrow production-adjacent promotion review after this packet is accepted
- but should still go through the formal checklist and approval gate

## Runtime scope validated in staging
### Core mechanics validated
- policy-bound decision outcomes
- decision advancement artifact generation
- escalation package generation
- bounded research successor activation
- recursive re-entry after research completion
- research budget enforcement
- origin-task parking / un-parking behavior
- dry-run no-mutate verification mode exists for safer promotion checks

### Outcome-family validation status
Validated in staging-style runs:
- `continue`
- `retry`
- `defer`
- `block`
- `escalate` (artifact path and budget-forced escalation behavior)

## Evidence index
### Continue path pilot
- `knowledge/evidence/staging/releases/2026-03-13__tde-decision-loop-staging-pilot__v2.md`

### Retry path pilot
- `knowledge/evidence/staging/releases/2026-03-13__tde-decision-loop-staging-pilot__retry-v1.md`

### Defer + block path pilots
- `knowledge/evidence/staging/releases/2026-03-13__tde-decision-loop-staging-pilot__defer-block-v1.md`

### Shared staging packet inputs
Representative supporting artifacts include:
- `knowledge/evidence/staging/2026-03/tde-stage-pilot-tick-1b.json`
- `knowledge/evidence/staging/2026-03/tde-stage-pilot-tick-2b.json`
- `knowledge/evidence/staging/2026-03/tde-stage-retry-pilot-iso-tick-1.json`
- `knowledge/evidence/staging/2026-03/tde-stage-retry-pilot-iso-tick-2.json`
- `knowledge/evidence/staging/2026-03/tde-stage-defer-pilot-iso-tick-1.json`
- `knowledge/evidence/staging/2026-03/tde-stage-defer-pilot-iso-tick-2.json`
- `knowledge/evidence/staging/2026-03/tde-stage-block-pilot-iso-tick-1.json`
- `knowledge/evidence/staging/2026-03/tde-stage-block-pilot-iso-tick-2.json`

## What is proven
### Proven strongly
1. A task can select `research_further` under policy.
2. A bounded research successor can activate automatically.
3. The origin task can be parked as non-claimable while research is active.
4. Research completion can re-enter the originating decision.
5. Re-entry can drive real operational outcomes (`continue`, `retry`, `defer`, `block`).
6. Research-loop budget exhaustion forces escalation.
7. Re-entry decision records can carry confidence/evidence/rationale from research output.

## What is only partially proven or not yet promoted
1. Shared staging runtime remains less deterministic than isolated fixtures for precise pilot validation.
2. `branch` and `complete_stop` remain design-level rather than runtime-embodied in this slice.
3. Production-adjacent promotion of this bounded research/re-entry capability has not yet been executed.
4. No real rollback execution has yet been rehearsed for this exact candidate slice.

## Important limitations
- Some pilots needed isolated temporary DB fixtures because the shared staging lane carried residual state.
- Research tasks currently return to `Waiting` after execution under existing writeback semantics.
- Origin tasks remain logically `Active`; parking is currently implemented as a claim-blocking metadata rule rather than a distinct parked state.

## Promotion-oriented reading of the evidence
The current evidence suggests:
- the bounded research/re-entry slice is materially more mature than a prototype
- the runtime behavior is now coherent enough for a narrow production-adjacent promotion review
- but promotion should still be limited to the bounded slice, not broader autonomy expansion

## Suggested promotion scope if approved later
A future narrow production-adjacent promotion could cover:
- bounded `research_further`
- bounded re-entry for `continue`, `retry`, `defer`, `block`, `escalate`
- parking/unparking behavior
- budget enforcement
- evidence-aware re-entry decision records

It should explicitly exclude for now:
- broader branch/generalized workflow expansion
- open-ended research loops
- any dynamic policy-authority broadening

## Recommended next operational step
Use this packet as the evidence bundle when preparing a real promotion candidate for the bounded research/re-entry slice.
That promotion should:
1. identify exact candidate commits,
2. identify rollback target,
3. run the formal checklist,
4. use dry-run verification on production-adjacent paths before/after apply.

## Bottom line
The bounded research/re-entry capability now has enough staging evidence to support a serious promotion review.
This packet is the clean summary that should anchor that decision.

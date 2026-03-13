# TDE Bounded Research/Re-entry Promotion Candidate v1

Date: 2026-03-13
Status: Candidate prepared for approval review
Owner: Peter + Lyra
Type: Narrow production-adjacent runtime promotion candidate
Related:
- `knowledge/evidence/staging/releases/2026-03-13__tde-bounded-research-reentry-release-packet__v1.md`
- `TDE_RUNTIME_PROMOTION_CHECKLIST_V1.md`
- `TDE_RUNTIME_PROMOTE_ROLLBACK_SOP_V1.md`

## Purpose
Define the exact candidate slice for a narrow production-adjacent promotion of the bounded research/re-entry capability.

This is a candidate packet only.
It is **not** an approved promotion and does not itself execute any runtime change.

## Candidate scope
Recommended commit slice:
- `91b349c` — `Add bounded research and escalation outcomes to TDE tick`
- `693ccee` — `Activate bounded research successors in TDE tick`
- `f56a03a` — `Add research re-entry loop to TDE tick`
- `291c388` — `Enforce research loop budget in TDE tick`
- `5c94252` — `Park origin tasks during TDE research loops`
- `cbdc196` — `Propagate research evidence into TDE re-entry decisions`
- `21690f8` — `Add retry defer and block re-entry outcomes to TDE tick`
- `d21224e` — `Sync TDE decision specs with runtime loop behavior`

Excluded from promotion scope (evidence/docs only, not required for runtime apply):
- `2e989a7`
- `846f104`
- `2ce7b9e`
- `7bdf445`

## Why this exact slice
This set captures the runtime mechanics needed for the bounded D-layer capability, while excluding evidence-packet commits that do not need to be part of runtime apply.

Included capability set:
- bounded `research_further`
- escalation package generation
- research successor activation
- recursive re-entry
- budget enforcement
- origin-task parking / un-parking
- evidence-aware re-entry decisions
- re-entry outcomes `continue|retry|defer|block|escalate`

## Risk class
**High**

Reason:
- touches `tde_job_tick_runner.py`
- changes canonical runtime decision behavior
- changes claimability semantics via parking rule
- affects production-adjacent task progression if promoted

## Rollback target
Recommended rollback target:
- `1def40f` — `Add no-mutate dry-run mode for TDE job tick`

Rationale:
- retains the important no-mutate verification safeguard
- predates the bounded research/re-entry runtime expansion
- is a cleaner fallback point than the older pathing-only promotion commit set

## Staging evidence refs
Primary consolidated packet:
- `knowledge/evidence/staging/releases/2026-03-13__tde-bounded-research-reentry-release-packet__v1.md`

Supporting pilot summaries:
- `knowledge/evidence/staging/releases/2026-03-13__tde-decision-loop-staging-pilot__v2.md`
- `knowledge/evidence/staging/releases/2026-03-13__tde-decision-loop-staging-pilot__retry-v1.md`
- `knowledge/evidence/staging/releases/2026-03-13__tde-decision-loop-staging-pilot__defer-block-v1.md`

## Checklist pre-read
### Candidate identification
- [x] Candidate commit slice is explicit
- [x] Scope is documented
- [x] Risk class is assigned
- [x] Related artifacts/specs are linked
- [x] Rollback target is identified

### Environment discipline
- [x] Capability exercised outside production-adjacent defaults
- [x] Staging paths / isolated staging-style fixtures used for evidence generation
- [x] No shared binding registry was required for isolated pilot proofs
- [x] Shared staging contamination was identified honestly and corrected with isolated fixtures

### Staging validation minimums
- [x] Focused tests passed during implementation cycles
- [x] Staging/isolated runtime executions completed successfully
- [x] Decision-policy behavior was verified
- [x] Evidence outputs landed in the staging evidence tree
- [x] No production-adjacent evidence path was required for validation
- [x] Fail-closed research-budget escalation behavior was exercised

### Not yet complete for real promotion
- [ ] Peter approval for this exact candidate slice is not yet recorded
- [ ] Production-adjacent pre-apply dry-run verification for this slice not yet executed
- [ ] Production-adjacent post-apply dry-run verification not yet executed
- [ ] Real rollback rehearsal for this exact slice not yet executed

## Expected production-adjacent impact if promoted
Expected positive effects:
- bounded research/re-entry capability becomes available in production-adjacent runtime
- origin tasks no longer get re-claimed while research children are active
- recursive decision handling becomes more complete and policy-governed
- escalation on exhausted research budget becomes available operationally

Expected risk areas:
- claim selection semantics change due to parking rule
- re-entry logic may surface edge cases in shared live task state
- existing task metadata may lack assumptions expected by the new paths

## Suggested promotion apply posture
If approved later, use a narrow production-adjacent promotion with:
1. pre-apply dry-run verification on current production-adjacent paths
2. apply only the approved candidate slice
3. immediate post-apply dry-run verification
4. only then a limited live tick exercise if needed

## Recommended approval question
If Peter is comfortable after reviewing this packet and the staging release packet, the approval question should be:

> Approve narrow production-adjacent promotion of the bounded TDE research/re-entry runtime slice defined in this packet?

## Bottom line
This candidate is ready for approval review.
The evidence is now strong enough for a serious narrow promotion decision, but the promotion should still be treated as high-risk and executed under the full checklist/SOP.

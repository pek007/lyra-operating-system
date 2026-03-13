# TDE Bounded Research/Re-entry Promotion v1

Date: 2026-03-13
Status: Approved and confirmed in production-adjacent workspace
Owner: Peter + Lyra
Approval: Peter explicit approval in chat
Related:
- `knowledge/evidence/staging/releases/2026-03-13__tde-bounded-research-reentry-promotion-candidate__v1.md`
- `knowledge/evidence/staging/releases/2026-03-13__tde-bounded-research-reentry-release-packet__v1.md`
- `TDE_RUNTIME_PROMOTION_CHECKLIST_V1.md`
- `TDE_RUNTIME_PROMOTE_ROLLBACK_SOP_V1.md`

## Promotion scope
Approved bounded runtime slice:
- `91b349c` — `Add bounded research and escalation outcomes to TDE tick`
- `693ccee` — `Activate bounded research successors in TDE tick`
- `f56a03a` — `Add research re-entry loop to TDE tick`
- `291c388` — `Enforce research loop budget in TDE tick`
- `5c94252` — `Park origin tasks during TDE research loops`
- `cbdc196` — `Propagate research evidence into TDE re-entry decisions`
- `21690f8` — `Add retry defer and block re-entry outcomes to TDE tick`
- `d21224e` — `Sync TDE decision specs with runtime loop behavior`

## Rollback target
- `1def40f` — `Add no-mutate dry-run mode for TDE job tick`

## Important apply note
At approval time, the approved candidate slice was already present in the current production-adjacent workspace history (`HEAD` at candidate-preparation time was beyond the approved slice and already included it).

Therefore this promotion was executed as a **promotion confirmation and acceptance event**, not as a fresh code-apply event.

This is acceptable for the current operating phase, but it should not be the preferred steady-state promotion shape.

## Pre-confirmation verification
Executed:
- `python3 tools/tde_state_store.py init`
- `python3 tools/tde_job_tick_runner.py --canonical-store db --shadow-state-enabled --dry-run`

Observed:
- runtime loaded cleanly
- default production-adjacent paths resolved correctly
- dry-run mode prevented mutation
- no claims executed
- no fail-open behavior observed

## Post-confirmation verification
Executed:
- `python3 tools/tde_job_tick_runner.py --canonical-store db --shadow-state-enabled --dry-run`

Observed:
- runtime loaded cleanly
- dry-run mode again prevented mutation
- no claims executed
- no fail-open behavior observed

## Checklist outcome summary
### Candidate identification
- [x] exact candidate identified
- [x] scope documented
- [x] risk class assigned (`High`)
- [x] related artifacts linked
- [x] rollback target identified

### Environment / staging evidence
- [x] staging validation packet exists
- [x] outcome-family pilots exist for continue/retry/defer/block
- [x] escalation / budget-forced escalation behavior exists in evidence
- [x] validation used staging or isolated staging-style paths

### Approval
- [x] Peter approval recorded

### Production-adjacent verification
- [x] pre-confirmation dry-run verification executed
- [x] post-confirmation dry-run verification executed
- [x] no unexpected mutation detected during verification
- [x] no fail-open behavior detected during verification

### Still not fully complete in the ideal model
- [ ] this was not a clean apply-after-approval event because the candidate was already present in the workspace
- [ ] real rollback execution for this exact slice has not yet been rehearsed

## Decision
**Promotion accepted for production-adjacent use.**

## Interpretation
The bounded research/re-entry runtime slice is now accepted for production-adjacent use under the current operating model.

The approval is supported by:
- consolidated staging evidence,
- isolated outcome-family pilots,
- and safe no-mutate verification against the production-adjacent lane.

## Follow-up recommendation
Before a later, more mature production model:
1. rehearse rollback execution for this exact slice
2. tighten the release process so approval happens before the candidate is present in the live workspace
3. decide whether `branch` and `complete_stop` should become runtime-supported in the same family or remain out of scope for now

## Bottom line
The bounded TDE research/re-entry capability is now approved for production-adjacent use, with verification completed and the current process caveat documented honestly.

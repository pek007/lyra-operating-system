# TDE Runtime Pathing Promotion v1

Date: 2026-03-13
Status: Promoted to production-adjacent use with warning noted
Owner: Peter + Lyra
Approval: Peter explicit approval in chat
Related:
- `TDE_RUNTIME_PROMOTION_CHECKLIST_V1.md`
- `TDE_RUNTIME_PROMOTE_ROLLBACK_SOP_V1.md`
- `knowledge/evidence/staging/releases/2026-03-13__tde-runtime-promotion-rehearsal__v1.md`

## Promotion scope
Approved narrow promotion scope:
- `11010be` — `Enable explicit staging TDE job tick path`
- `f82c9dd` — `Add native env support to TDE runtime scripts`
- `a4c454a` — `Add env-aware paths to TDE release evidence scripts`

## Why this slice
This is a narrow pathing/environment hardening slice.
It improves environment separation without broadening autonomy behavior.

## Risk class
**High**

Reason:
- touches runtime-path behavior
- affects DB/evidence/registry path resolution
- can cause wrong-environment writes if incorrect

## Rollback target
Last known-good rollback target:
- `11010be`

## Staging evidence used
- `knowledge/evidence/staging/2026-03/tde-job-tick-latest.json`
- `knowledge/evidence/staging/2026-03/tde-milestone-s4-s7-snapshot.json`
- `knowledge/evidence/staging/metrics/tde-shadow-state-alerts.jsonl`
- `knowledge/evidence/staging/releases/2026-03-13__tde-runtime-promotion-rehearsal__v1.md`

## Production-adjacent verification executed
Commands executed for post-promote verification:
- `python3 tools/tde_state_store.py init`
- `python3 tools/tde_job_tick_runner.py --canonical-store db --max-claim 0 --shadow-state-enabled`

## Verification results
### Pass
- runtime loaded cleanly
- default production-adjacent DB path resolved correctly: `os/runtime/tde_state.sqlite`
- default objective registry path resolved correctly: `os/runtime/tde_objectives.json`
- default binding registry path resolved correctly: `os/runtime/tde_active_bindings.json`
- default evidence output path resolved correctly: `knowledge/evidence/2026-03/tde-job-tick-latest.json`
- no fail-open policy behavior observed
- shadow-state parity remained OK

### Warning / important observation
The verification command was **not fully inert**.
Even with `--max-claim 0`, the tick still executed the chaining promotion pass and promoted:
- `TDE-CHAIN-PILOT-03` -> `Active`

This means a production-adjacent verification run can still mutate canonical task state through readiness promotion even when no claims are executed.

## Interpretation
The approved environment/pathing slice is still accepted as promoted for production-adjacent use.
However, the post-promote verification surfaced an operational safety gap:
- current tick verification is not a true no-op safety check
- a separate dry-run / no-mutate verification mode is needed

## Checklist outcome summary
### Candidate identification
- [x] explicit candidate identified
- [x] scope documented
- [x] risk assigned
- [x] rollback target identified

### Staging validation
- [x] staging evidence exists
- [x] staging runtime execution succeeded
- [x] environment isolation proved

### Approval
- [x] Peter approval received

### Post-promote verification
- [x] runtime loaded cleanly
- [x] intended production-adjacent paths resolved correctly
- [ ] no unexpected production-adjacent mutation detected

## Decision
**Promotion accepted with warning.**

Reason:
- the promoted slice itself behaved as intended for path resolution
- the observed mutation came from existing tick/chaining behavior during verification, not from incorrect environment routing
- this should be treated as a follow-up hardening item rather than immediate rollback material

## Required follow-up
1. Add a true dry-run / no-mutate verification mode for `tde_job_tick_runner.py`
2. Use that mode for future production-adjacent verification checks
3. Rehearse rollback execution on a narrow candidate when practical

## Bottom line
The first real narrow promotion is complete.
It succeeded on its primary objective: environment/path resolution is now promoted into production-adjacent use.

But the process also surfaced a real operational lesson:
verification tooling itself needs a no-mutation mode before broader runtime promotion work continues.

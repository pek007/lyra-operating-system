# TDE Bounded Research/Re-entry Rollback Rehearsal v1

Date: 2026-03-13
Status: Rehearsal completed successfully in isolated worktree
Owner: Peter + Lyra
Purpose: Rehearse rollback viability for the bounded TDE research/re-entry production-adjacent slice without altering the live workspace
Related:
- `knowledge/evidence/prod/releases/2026-03-13__tde-bounded-research-reentry-promotion__v1.md`
- `knowledge/evidence/staging/releases/2026-03-13__tde-bounded-research-reentry-promotion-candidate__v1.md`
- `TDE_RUNTIME_PROMOTE_ROLLBACK_SOP_V1.md`

## Rehearsal target
Rollback target commit:
- `1def40f` — `Add no-mutate dry-run mode for TDE job tick`

Why this target:
- it preserves the important no-mutate verification safeguard
- it predates the bounded research/re-entry runtime slice
- it is the documented rollback target for the approved promotion slice

## Rehearsal method
Used an isolated git worktree rather than touching the live production-adjacent workspace.

Worktree path used:
- `/tmp/openclaw-tde-rollback-rehearsal`

This approach was selected because it:
- proves the target revision still loads and runs,
- avoids mutating the current live workspace,
- and gives a credible rollback-readiness signal without executing a real rollback.

## Commands executed in the isolated worktree
- `python3 tools/tde_state_store.py init`
- `python3 tools/tde_job_tick_runner.py --canonical-store db --shadow-state-enabled --dry-run`

## Observed results
### Runtime load
- `tde_state_store.py init` returned OK
- default DB path resolved correctly

### No-mutate verification
Observed summary:
- status: `ok`
- dry_run: `true`
- claimed: `[]`
- writeback: `dry_run_no_mutation`
- fail_closed: `false`
- shadow_state: skipped due to dry-run, as expected

## Interpretation
This rehearsal demonstrates that the documented rollback target is operationally credible:
- the target revision still loads cleanly
- the target revision can execute safe verification checks
- and nothing in the rehearsal suggests rollback would fail trivially at startup/runtime-verification level

## Important limitation
This was a **rehearsal**, not an actual rollback of the live production-adjacent workspace.
So it does not prove:
- state migration reversibility under live mutated task metadata,
- semantic equivalence after actual live rollback,
- or that all production-adjacent runtime behavior would be identical after a real revert.

It does prove the rollback target is viable enough to trust as a credible rollback anchor.

## Delta awareness
Approximate scope difference between rollback target and approved candidate slice across key TDE files:
- 7 files changed
- ~623 insertions / 34 deletions

Key runtime files implicated:
- `tools/tde_job_tick_runner.py`
- `tools/tde_state_store.py`
- `tools/tde_decision_policy.py`
- `tools/tde_decision_escalation.py`
- `tools/tde_decision_rounds.py`

## Conclusion
Rollback readiness is now stronger than before this rehearsal.

The bounded research/re-entry slice still carries risk, but the documented rollback target is now supported by an isolated execution rehearsal rather than just assumption.

## Recommended next note for future promotions
For future promotions, prefer the same pattern:
1. identify rollback target
2. load it in an isolated worktree or equivalent clean runtime
3. run no-mutate verification there
4. record the result before or alongside promotion approval

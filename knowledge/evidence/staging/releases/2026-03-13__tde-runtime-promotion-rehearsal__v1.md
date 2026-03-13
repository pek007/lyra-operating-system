# TDE Runtime Promotion Rehearsal v1

Date: 2026-03-13
Type: Dry run / checklist rehearsal
Status: Rehearsal completed — no actual production promotion executed
Owner: Peter + Lyra
Related:
- `TDE_RUNTIME_PROMOTION_CHECKLIST_V1.md`
- `TDE_RUNTIME_PROMOTE_ROLLBACK_SOP_V1.md`
- `TDE_ENVIRONMENT_AND_PROMOTION_MODEL_V1.md`

## Rehearsal objective
Exercise the new TDE runtime promotion discipline against a recent real candidate without actually promoting it into production-adjacent or production use.

## Candidate chosen
Primary candidate commit:
- `f82c9dd` — `Add native env support to TDE runtime scripts`

Supporting adjacent commit:
- `a4c454a` — `Add env-aware paths to TDE release evidence scripts`

## Why this candidate
This candidate is a good rehearsal target because it affects real runtime-path behavior:
- `tde_job_tick_runner.py`
- `tde_state_store.py`
- downstream release/evidence path resolution

It is therefore clearly in the **high-risk TDE runtime change** category.

## Scope summary
The candidate introduced native `--env` support for core runtime scripts and extended environment-aware pathing into the next ring of release/evidence scripts.

Expected impact if later promoted for real:
- lower risk of cross-environment path leakage
- stronger staging/prod separation
- less dependence on wrapper-only discipline

## Risk class
**High**

Rationale:
- affects TDE runtime scripts directly
- changes path resolution for DB/evidence/registries
- could cause silent wrong-environment writes if incorrect

## Rollback target
Last known-good rollback target for rehearsal purposes:
- `11010be` — `Enable explicit staging TDE job tick path`

Why this rollback target:
- it predates native env support in the scripts
- it still contains the explicit staging-capable hook path
- it is recent enough to be credible for rollback reasoning

## Checklist rehearsal

### Candidate identification
- [x] Candidate commit / version is explicit
- [x] Change scope is documented
- [x] Risk class is assigned
- [x] Related artifacts/specs are linked
- [x] Rollback target identified

### Environment discipline
- [x] Candidate exercised outside production-adjacent defaults
- [x] Staging paths used for DB/objectives/bindings/evidence
- [x] No shared runtime DB or binding registry used across environments during proof runs
- [x] No ambiguous cron target/path remains in the exercised candidate path

### Staging validation minimums
- [x] Core tests passed
- [x] Relevant focused tests passed
- [x] At least one staging-only runtime execution completed successfully
- [x] Fail-closed behavior otherwise explicitly verified where relevant to the exercised path
- [x] Decision-policy behavior verified where applicable
- [x] Evidence outputs landed in the staging evidence tree
- [x] No production-adjacent evidence path written by the staging run

### Required evidence bundle
- [x] Staging run artifact path(s) recorded
- [x] Validation summary exists
- [x] Known limitations/non-tested paths stated explicitly
- [x] Cron/tick path change includes staging tick proof
- [ ] Decision artifact proof for promotion scenario not required in this rehearsal scope

### Promotion approval
- [x] Exact candidate identified
- [x] Expected production impact stated
- [ ] Peter approval for real promotion not requested in this rehearsal
- [x] Rollback method documented for rehearsal purposes

### Production / production-adjacent apply conditions
- [ ] Not executed — this was a dry run only

### Post-promote verification
- [ ] Not executed — this was a dry run only

## Evidence refs used in rehearsal
Primary staging evidence:
- `knowledge/evidence/staging/2026-03/tde-job-tick-latest.json`
- `knowledge/evidence/staging/2026-03/tde-milestone-s4-s7-snapshot.json`
- `knowledge/evidence/staging/metrics/tde-shadow-state-alerts.jsonl`

Supporting setup/spec refs:
- `TDE_STAGING_RUNTIME_SETUP_NOTE_V1.md`
- `TDE_ENVIRONMENT_PATH_CONVENTION_V1.md`

## Validation summary
What was actually proven in staging:
1. `tde_job_tick_runner.py` resolved staging paths natively via `--env staging`
2. `tde_state_store.py` resolved staging paths natively via `--env staging`
3. `tde_job_tick_cron_hook.sh` required explicit `TDE_ENV` and used staging paths correctly
4. `tde_milestone_snapshot.py` resolved staging evidence paths via `--env staging`
5. focused tests remained green after the runtime-path changes

## Known limitations / non-tested paths
This rehearsal did **not** prove all production-promotion conditions.
It did **not** include:
- a real production-adjacent promotion
- a real post-promote verification on production paths
- a real rollback execution
- full staging proofs for every downstream canary/reporting script
- a real decision-artifact promotion scenario across all D-layer branches

## Rehearsal decision
**Result: PASS as governance rehearsal, not as actual promotion approval.**

Interpretation:
- the checklist is workable
- the SOP is usable
- the evidence bundle shape is credible
- but a real promotion still requires explicit Peter approval and real post-promote verification

## What would be needed for a real promotion
Before a real promotion of this candidate class, we would still need:
1. explicit approval to promote the chosen candidate
2. a defined production/proto-prod target path set
3. a real pre-change backup/snapshot where applicable
4. immediate post-promote verification evidence
5. a documented rollback execution path tested or credibly rehearsed

## Recommendation after rehearsal
The new promotion discipline is usable enough to adopt.

Recommended next operational move:
- use this checklist/SOP for the **first real narrow production-adjacent runtime promotion**, probably on a pathing/environment change rather than a broader autonomy expansion.

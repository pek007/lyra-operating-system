# TDE Runtime Promotion Checklist v1

Status: Draft
Owner: Peter + Lyra
Date: 2026-03-13
Related:
- `TDE_ENVIRONMENT_AND_PROMOTION_MODEL_V1.md`
- `TDE_ENVIRONMENT_PATH_CONVENTION_V1.md`
- `TDE_STAGING_RUNTIME_SETUP_NOTE_V1.md`
- `OPENCLAW_CONFIG_CHANGE_SOP_V1.md`

## Purpose
Provide a concrete checklist for promoting TDE/OpenClaw runtime-path changes from development/staging into production-adjacent or production use.

Use this for changes affecting:
- `tde_job_tick_runner.py`
- `tde_state_store.py`
- chaining/promotion logic
- decision-policy enforcement
- cron/tick routing
- release/evidence runtime behavior

Default classification for these changes: **High risk**.

## Candidate identification
- [ ] Candidate commit / version is explicit
- [ ] Change scope is documented
- [ ] Risk class is assigned
- [ ] Related artifacts/specs are linked
- [ ] Rollback target (last known good commit/version) is identified

## Environment discipline
- [ ] Candidate has been exercised outside production-adjacent defaults
- [ ] Staging paths were used for DB/objectives/bindings/evidence
- [ ] No shared runtime DB or binding registry was used across environments
- [ ] No ambiguous cron target/path remains in the candidate path

## Staging validation minimums
- [ ] Core tests passed
- [ ] Relevant focused tests passed
- [ ] At least one staging-only runtime execution completed successfully
- [ ] Fail-closed behavior was exercised or otherwise explicitly verified
- [ ] Decision-policy behavior was verified where applicable
- [ ] Evidence outputs landed in the staging evidence tree
- [ ] No production-adjacent evidence path was written by the staging run

## Required evidence bundle
- [ ] Staging run artifact path(s) recorded
- [ ] Validation summary exists
- [ ] Any known limitations or non-tested paths are stated explicitly
- [ ] If decision-policy path changed: include decision artifact proof or fail-closed proof
- [ ] If cron/tick path changed: include staging tick proof

## Promotion approval
- [ ] Exact candidate to promote is identified
- [ ] Expected production impact is stated
- [ ] Peter approval is recorded for high-risk runtime change
- [ ] Rollback method is documented and credible

## Production / production-adjacent apply conditions
- [ ] Apply only the approved candidate
- [ ] No opportunistic unrelated edits are bundled
- [ ] Production path targets are explicit
- [ ] Backup / snapshot of relevant live files/config is available if applicable

## Post-promote verification
- [ ] Runtime starts/loads cleanly
- [ ] Expected environment paths are correct
- [ ] No fail-open behavior detected
- [ ] No unexpected production state mutation detected
- [ ] No unexpected external effect detected
- [ ] Evidence output landed in the intended production-adjacent / production path

## Rollback triggers
Rollback if any of the following occurs:
- [ ] runtime regression
- [ ] wrong environment path used
- [ ] fail-open decision/chaining behavior
- [ ] unexpected cron/scheduler behavior
- [ ] unexpected state mutation
- [ ] evidence artifact inconsistency

## Promotion decision summary
Record before or at promotion:
- Candidate:
- Risk class:
- Staging evidence refs:
- Approval:
- Rollback target:
- Expected impact:
- Post-promote verification result:

## Rehearsal note
First dry-run checklist rehearsal recorded at:
- `knowledge/evidence/staging/releases/2026-03-13__tde-runtime-promotion-rehearsal__v1.md`

## Current bounded research/re-entry packet
The first consolidated staging validation packet for the bounded research/re-entry slice is:
- `knowledge/evidence/staging/releases/2026-03-13__tde-bounded-research-reentry-release-packet__v1.md`

## Bottom line
No TDE runtime-path change should move into production-adjacent or production use without:
- explicit candidate identity,
- staging validation evidence,
- explicit approval,
- and a credible rollback target.

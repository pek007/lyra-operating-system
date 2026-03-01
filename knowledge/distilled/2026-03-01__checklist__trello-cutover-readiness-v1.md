# Trello Cutover Readiness Checklist v1

Use this checklist at each cutover gate.

## A) Data completeness
- [ ] In-scope boards/lists/cards fully enumerated
- [ ] Every in-scope Trello card mapped to exactly one TDE object
- [ ] No orphan TDE objects (missing provenance)
- [ ] Required fields complete for active/committed tasks
- [ ] Custom fields mapped deterministically (where used)

## B) Audit and traceability
- [ ] Audit import level (A/B/C) explicitly declared
- [ ] Historical import completed for in-scope slice
- [ ] Evidence links preserved and queryable
- [ ] Re-run import is idempotent (no duplicate logical events)

## C) Reliability and drift control
- [ ] Reconciliation job runs on cadence
- [ ] Drift rate is stable/declining
- [ ] Rate-limit handling (429) validated
- [ ] Backup/restore for TDE state validated

## D) Workflow adoption
- [ ] End-to-end thin slice runnable fully in TDE
- [ ] No operational Trello writes in canary domain
- [ ] Decision packet + approval flow works in TDE
- [ ] Day-to-day workflow can run without Trello open

## E) Security and dependency removal
- [ ] Trello write tokens removed from active automation path for cutover domain
- [ ] Agent/tool instructions updated with TDE as source of truth
- [ ] Access controls updated for read-only/archive Trello posture

## F) Rollback readiness
- [ ] Rollback trigger thresholds defined
- [ ] Rollback steps documented and tested
- [ ] Reconciliation-after-rollback procedure documented

## Gate outcome
- [ ] PASS -> proceed to next phase
- [ ] HOLD -> fix gaps and re-run checklist
- [ ] ROLLBACK -> execute rollback plan

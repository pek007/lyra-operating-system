# TDE Cutover Gap Assessment and S26 Recommendation v1

Date: 2026-03-10
Owner: Lyra
Status: Draft recommendation for execution

## Executive summary

The TDE kernel has progressed beyond thin-slice feasibility and into controlled runtime hardening. S21-S25 closed key governance/runtime gaps: kernel modularization, CI fail-closed guard enforcement, metrics baseline, objective-registry validation, and binding lifecycle fail-closed semantics.

The most useful next move is **not another generic kernel-hardening slice**. The remaining value bottleneck is cutover readiness for bounded live operational use.

Recommended next slice: **S26 — controlled cutover readiness and first bounded live rollout packet**.

## What appears complete already

The current evidence base indicates that the following are in place or materially advanced:

- Thin-slice governance kernel and acceptance path (S1-S8)
- Real task ingestion and safe writeback path (S12-S18)
- Runtime/test separation and CI fail-closed checks (S21-S22)
- DORA proxy baseline instrumentation (S23)
- Objective registry enforcement (S24)
- Binding lifecycle semantics with fail-closed rotation guard (S25)
- Activation guard / owner gate / release envelope artifacts for controlled handoff

## Remaining bottleneck

The unresolved question is no longer **"can the kernel enforce core governance semantics?"**
It is now **"what exact evidence is still required to permit bounded live TDE operation as the source of truth for a real operational slice?"**

This means the next slice should concentrate on operational cutover mechanics rather than another internal runtime invariant.

## Gap framing against existing cutover design

The repo already defines the target state and gate structure in:
- `knowledge/distilled/2026-03-01__design__trello-retirement-design-v1.md`
- `knowledge/distilled/2026-03-01__checklist__trello-cutover-readiness-v1.md`

Using that checklist as the governing frame, the most likely remaining gaps are:

### A. Data completeness gate still needs explicit bounded-slice proof
Likely missing or not yet consolidated into one owner-facing packet:
- exact in-scope canary domain enumerated
- every live object in that slice mapped 1:1 into TDE objects
- orphan/provenance checks published for the chosen cutover slice

### B. Reliability/drift control needs live-cutover evidence, not just kernel evidence
Current work shows strong runtime correctness, but cutover readiness still needs:
- reconciliation cadence for the specific live slice
- bounded drift thresholds with explicit pass/fail criteria
- backup/restore proof tied to the operational slice, not just generic process posture

### C. Workflow adoption gate needs an operator-ready runbook
The repo has design/checklist artifacts, but the next gating artifact should make it operationally obvious:
- what the operator does at cutover start
- what signals indicate hold vs proceed
- what gets checked each cycle during the bounded rollout window
- what constitutes successful steady state after the first live period

### D. Security/dependency removal needs explicit canary-domain cutover posture
Before any meaningful live cutover recommendation, the packet should explicitly state:
- whether Trello remains read-only, shadow, or still partially authoritative for the slice
- whether operational writes are disabled in the cutover domain
- what credentials/tokens remain in the path during the canary window

### E. Rollback readiness must be attached to the live slice itself
Rollback concepts exist in the repo, but the next decision packet should make rollback executable:
- rollback triggers with measurable thresholds
- exact rollback steps
- reconciliation-after-rollback procedure
- owner-visible decision boundary for GO / HOLD / ROLLBACK

## Recommended S26 objective

Produce a **single execution-ready cutover packet** for one bounded live TDE domain, with explicit gate criteria and rollback posture.

Selected canary domain for S26:
- `JOB-PROD-001` execution of open `TDE-2026-*` work items in `repos/lyra-operating-system/TASKS.md`
- repo-local authority only (`TASKS.md` canonical)
- no Trello/legacy operational authority in scope
- mutation surface constrained to the already-evidenced low-risk audited writeback path

## Proposed S26 acceptance criteria

1. A bounded live cutover scope is explicitly declared (domain, objects, authority source, success window).
2. A machine-checkable or checklist-backed readiness artifact exists covering data completeness, reliability/drift, workflow adoption, security/dependency removal, and rollback readiness for that scope.
3. An operator-facing runbook exists for GO / HOLD / ROLLBACK execution during the first bounded live rollout window.
4. An owner-facing decision packet exists that states current readiness, unresolved risks, and recommended next decision.

## Suggested execution sequence after S26

1. Complete S26 artifacts.
2. Review unresolved blockers (if any).
3. If acceptable, approve bounded live rollout for one canary domain.
4. Collect first live-cutover evidence.
5. Decide expand / hold / rollback.

## Recommendation

Open **WO-2026-TDE-KERNEL-S26** immediately and treat it as the bridge from kernel hardening to operational cutover governance.

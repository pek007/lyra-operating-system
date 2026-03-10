# TDE Bounded Live Rollout Runbook

Date: 2026-03-10
Status: Draft
Owner: Lyra
Linked WO: `WO-2026-TDE-KERNEL-S26`

## Purpose
Provide an operator-ready runbook for the first bounded live TDE rollout window.

## Preconditions
Do not start the bounded live rollout until all of the following are explicit:
- bounded domain named
- in-scope objects enumerated
- authority posture declared
- rollback owner and decision route declared
- reconciliation cadence defined
- rollback triggers defined

## 1. Preflight
Before GO:
1. Confirm bounded domain and object inventory are recorded.
2. Confirm current source-of-truth posture for the slice:
   - TDE canonical
   - legacy system shadow/reference only
   - no uncontrolled dual-write
3. Confirm latest kernel regression bundle passes.
4. Confirm latest readiness packet status is not missing critical items.
5. Confirm rollback operator, rollback command/process, and reconciliation-after-rollback path are documented.

## 2. Activation decision
Possible outcomes:
- **GO**: bounded live rollout may begin for the declared slice.
- **HOLD**: missing data, unclear authority, or incomplete rollback posture. Do not start.
- **ROLLBACK**: if already started and trigger breached, revert to prior authority posture and execute reconciliation.

## 3. During rollout window
Check at each cadence cycle:
1. Did the runtime claim only in-scope work?
2. Did any authority/binding/objective guard fail unexpectedly?
3. Did any drift/orphan/mapping exception occur?
4. Did any operator need Trello or another legacy system to complete normal work for the slice?
5. Did any rollback trigger fire?

Record each cycle as:
- PASS
- PASS WITH NOTE
- HOLD
- ROLLBACK

## 4. Hold triggers
Move to **HOLD** if any of the following occur:
- in-scope inventory becomes uncertain
- authority source is ambiguous
- evidence packet is incomplete for a required operational question
- operator cannot explain current state from TDE artifacts alone

## 5. Rollback triggers
Execute **ROLLBACK** if any of the following occur:
- wrong-object mutation or unexplained out-of-scope mutation
- reconciliation divergence above declared threshold
- rollback path itself is unclear or cannot be executed safely
- operator must re-enable uncontrolled dual-write behavior to continue
- approval/authority boundary is bypassed or weakened

## 6. Rollback procedure
1. Stop bounded live rollout and declare HOLD/ROLLBACK outcome.
2. Restore prior operational authority posture for the slice.
3. Preserve all evidence artifacts from the failed/held window.
4. Run reconciliation against the bounded object inventory.
5. Publish discrepancy summary and classify root cause:
   - mapping gap
   - authority gap
   - runtime bug
   - operator/runbook gap
   - dependency/removal gap
6. Decide next state:
   - retry after fix
   - remain on legacy source of truth
   - narrow scope and re-run

## 7. Exit criteria for successful bounded rollout
A bounded rollout may be considered successful only if:
- multiple cadence cycles complete without rollback trigger
- operator can run the slice without operational dependence on legacy tooling
- reconciliation remains within declared bounds
- evidence packet is complete enough to support expand / hold / rollback decision

## 8. Required follow-on artifact
At the end of the window, publish one owner-facing summary with recommendation:
- expand
- hold
- rollback

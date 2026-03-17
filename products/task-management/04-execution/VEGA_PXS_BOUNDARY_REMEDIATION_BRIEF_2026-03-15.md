# Vega/PXS Boundary Remediation Brief

Date: 2026-03-15
Owner: Control Tower / Task Management / Security
Linked TDE task: `TASK-20260314-VEGA-PXS-BOUNDARY-PASS`
Primary gate: `governance/VEGA_ACCEPTANCE_TEST_RUN_SHEET_V1.md`

## Why this is the portfolio bottleneck now
Both Security and Task Management nightly reports point to the same gating dependency: downstream `pxs` consumption cannot be treated as safe or repeatable until the Vega/PXS boundary is enforced as a real control and the acceptance sheet reruns to PASS with committed evidence.

## Current blocking failures
1. **B1 repo placement fail** — the acceptance sheet still records that `pxs` is not present inside the Vega workspace.
2. **C1/C2 pinned dependency fail** — the platform-core pinned dependency model is not yet implemented or evidenced.
3. **E2 boundary enforcement fail** — cross-domain reads are still allowed by default, which means the declared boundary is not an enforced control.

## Overnight execution order
1. Reconfirm the current intended Vega workspace/repo topology and whether B1 is still a live fail versus a stale acceptance artifact.
2. Make the minimum boundary-enforcement change that prevents default cross-domain reads or, if runtime enforcement is not yet available, document the exact control gap and required implementation surface.
3. Define the pinned dependency/pathing closure needed for Pattern A and attach evidence refs.
4. Rerun the acceptance sheet and record PASS/FAIL with committed evidence.

## Evidence already available
- `products/security/04-execution/reports/2026-03-15-po-nightly-report.json`
- `products/task-management/04-execution/nightly-reports/2026-03-15-po-nightly-report.json`
- `governance/VEGA_ACCEPTANCE_TEST_RUN_SHEET_V1.md`
- `products/security/06-architecture/BOUNDARY.md`
- `products/task-management/06-architecture/PXS_CONSUMPTION_INTERFACE.md`

## Control Tower note
Do not treat downstream interface polishing or product-local packaging wins as the overnight lead item until this boundary gate is either closed or narrowed to a smaller explicit blocker with fresh evidence.

# Work Order (WO) — TDE Kernel Slice S7

## Metadata
- WO-ID: WO-2026-TDE-KERNEL-S7
- Title: Canary-to-broader rollout controls with bounded expansion and simulated broadened cycle
- Owner: JOB-PROD-001
- Date opened: 2026-03-02
- Lane: Build
- Work type: Feature
- Risk class: Medium

## Intent
- Objective: Add explicit controls for expanding from canary scope to a broader local scope while preserving fail-closed guardrails.
- Why now: S6 made canary status operationally legible; S7 defines bounded expansion criteria and validates broadened-cycle behavior before real scope increase.
- Non-goals: 3PP integration, new repository split, bypassing approval gates.

## Acceptance Criteria
1. Define bounded expansion criteria for moving beyond canary scope (numerical bounds + rollback triggers).
2. Produce guardrail-preserving rollout checklist for broadened-scope operation.
3. Run at least one broadened-scope simulated cycle and capture evidence.
4. Keep fail-closed behavior intact (approval-required paths remain blocked pending approval).

## Verification Plan
- Automated: `python3 tools/tde_kernel_slice_tests.py`
- Simulation/artifacts: `python3 tools/tde_rollout_broader_scope_simulation.py`
- Manual review: validate generated criteria/checklist/cycle evidence files and rollout decision.

## Dependencies
- Existing TDE kernel runtime/cycle behavior from S1–S6.
- Local evidence path under `knowledge/evidence/2026-03/`.
- No 3PP dependency.

## Closure
- Outcome summary: Implementation-complete. Added bounded expansion criteria artifact, guardrail-preserving broader rollout checklist, and one broadened-scope simulated cycle artifact showing GO under bounded conditions (active=3, at-risk=2, stalled=1, stalled ratio=0.1667) with no approval-gate bypass.
- Accepted by: JOB-PROD-001 + JOB-ARC-001 (owner pre-authorization acknowledged 2026-03-02)
- Date closed: 2026-03-02

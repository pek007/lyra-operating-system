# Work Order (WO) — TDE Kernel Slice S2

## Metadata
- WO-ID: WO-2026-TDE-KERNEL-S2
- Title: Implement heartbeat-driven anti-stall loop + progress-state visibility contract
- Owner: JOB-PROD-001 (Product Owner)
- Date opened: 2026-03-02
- Lane: Build
- Work type: Feature
- Risk class: Medium

## Intent
- Objective: Deliver S2 control loop that distinguishes active-background work from true stalled work and auto-triggers next-state actions.
- Why now: S1 proved thin-slice kernel mechanics; S2 must solve transparency + stuck-flow risk.
- Non-goals: UI progress bars, 3PP orchestration, full production hardening.

## Acceptance Criteria (Required)
1. Progress-state contract defined (`active-background|at-risk|stalled`) with machine-readable fields and reason codes.
2. Heartbeat/cron anti-stall loop spec defines deterministic actions for stalled items (`resume|escalate|redefine|retire`).
3. Verification script includes progress-state classification and stale-item action routing checks.
4. Evidence artifact records one full simulated anti-stall cycle from detection to routed action.

## Verification Plan (Required)
- Automated tests: extend kernel runner with progress-state and anti-stall routing checks.
- Manual checks: run one sample classification snapshot and one stale-action routing scenario.
- Security/privacy checks (if applicable): ensure no high-risk action executes without policy/obligation gate.
- Definition of done reference: `STD-001_DEFINITION_OF_DONE.md`.

## Dependencies (Required)
- Models/providers involved: OpenClaw runtime primitives (heartbeat/cron concepts).
- Tools/services involved: workspace filesystem, git, python test script.
- 3PPs touched: None (escalate if needed).

## Constraints
- Time/budget constraints: keep WIP major item cap at 1.
- Policy/security constraints: maintain fail-closed behavior and audit linkage.

## Prompt/Execution Contract
- Prompt template + version: internal WO execution contract v1.
- Assigned executor agent/lane: JOB-ENG-001 under JOB-PROD-001 governance.
- Escalation trigger(s): major decisions, milestone gate, 3PP involvement, repo-structure change.

## Delivery Plan
- Planned file/components touched: kernel model/spec docs, anti-stall/progress contracts, test runner, evidence artifact.
- Rollback approach: revert S2 commits; preserve evidence logs.
- Expected output artifacts: updated specs/tests/evidence + S2 closure summary.

## Closure
- Outcome summary: Implementation-complete. S2 artifacts delivered: progress-state contract (`active-background|at-risk|stalled`) with stall reason codes, deterministic anti-stall routing map, kernel verification tests extended for classification + routing determinism, and S2 verification evidence captured.
- Accepted by: Pending formal acceptance (required: JOB-PROD-001 + JOB-ARC-001)
- Date closed: 2026-03-02 (implementation complete; acceptance pending)
- Linked Change Artifact(s): tools/tde_kernel_slice_tests.py; os/sops/TDE_ANTI_STALL_HOOK_V1.md; knowledge/evidence/2026-03/2026-03-02__verification__wo-2026-tde-kernel-s2.md

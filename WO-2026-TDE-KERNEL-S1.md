# Work Order (WO) — TDE Kernel Slice S1

## Metadata
- WO-ID: WO-2026-TDE-KERNEL-S1
- Title: Build TDE kernel thin slice (policy-checked transition + approval gate + idempotent execution + audit link)
- Owner: JOB-PROD-001 (Product Owner)
- Date opened: 2026-03-02
- Lane: Build
- Work type: Feature
- Risk class: Medium

## Intent
- Objective: Implement the minimum end-to-end TDE governance flow required by thin-slice tests (T1–T7 baseline path).
- Why now: Build gate is ready; this is the smallest deployable kernel proving governance mechanics.
- Non-goals: UI productization, broad workflow expansion, non-kernel integrations.

## Acceptance Criteria (Required)
1. End-to-end path works: trigger -> evaluate -> decision packet -> approval gate -> idempotent execution -> audit/evidence linkage.
2. Thin-slice tests T1–T6 pass; T7 readiness hooks are implemented for canary transition.
3. All mutate/execute actions emit policy decision record id, idempotency key, actor+job identity, and audit link.
4. Anti-stall control hook defined for heartbeat/cron follow-up of idle high-priority items (resume/escalate/redefine/retire pathway).

## Verification Plan (Required)
- Automated tests: thin-slice suite mapped to `knowledge/distilled/2026-03-01__spec__tde-thin-slice-acceptance-tests-v1.md`.
- Manual checks: one real low-risk transition and one approval-required action dry run with auditable output.
- Security/privacy checks (if applicable): verify no bypass of obligation gates; verify denied actions fail closed.
- Definition of done reference: `STD-001_DEFINITION_OF_DONE.md`.

## Dependencies (Required)
- Models/providers involved: OpenClaw main runtime; local policy evaluation path.
- Tools/services involved: workspace filesystem, git, test runner.
- 3PPs touched: None by default (escalate if Claude Code / Deep Research required).

## Constraints
- Time/budget constraints: keep slice implementation bounded to first milestone; avoid scope expansion.
- Policy/security constraints: enforce job-bound authority model and anti-self-escalation controls.

## Prompt/Execution Contract
- Prompt template + version: internal WO execution contract v1.
- Assigned executor agent/lane: JOB-ENG-001 (Developer) under JOB-PROD-001 coordination.
- Escalation trigger(s): reserved owner boundaries (major decision, milestone gate, 3PP involvement, repo structure decision).

## Delivery Plan
- Planned file/components touched: TDE kernel code paths, policy enforcement wrapper, thin-slice tests, audit linkage artifacts.
- Rollback approach: feature-flag or revert to prior branch state; preserve audit logs.
- Expected output artifacts: implementation diff, test evidence, gate-ready closure summary.

## Closure
- Outcome summary: Kernel-slice scaffolding implemented with T1-T7 acceptance runner and anti-stall hook contract; verification evidence recorded.
- Accepted by: Pending formal acceptance (JOB-PROD-001 + JOB-ARC-001)
- Date closed: 2026-03-02 (implementation complete; awaiting acceptance sign-off)
- Linked Change Artifact(s): `knowledge/evidence/2026-03/2026-03-02__verification__wo-2026-tde-kernel-s1.md`

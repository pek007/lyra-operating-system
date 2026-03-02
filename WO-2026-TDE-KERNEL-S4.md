# Work Order (WO) — TDE Kernel Slice S4

## Metadata
- WO-ID: WO-2026-TDE-KERNEL-S4
- Title: Canary live wiring for runtime-triggered anti-stall checks
- Owner: JOB-PROD-001
- Date opened: 2026-03-02
- Lane: Build
- Work type: Feature
- Risk class: Medium

## Intent
- Objective: Wire a canary runtime path that executes anti-stall checks from heartbeat/cron trigger events against a bounded task subset.
- Why now: S1–S3 validated logic and simulation; S4 introduces controlled live execution behavior.
- Non-goals: Full fleet rollout, UI dashboarding, 3PP orchestration.

## Acceptance Criteria
1. Canary scope definition is explicit and bounded (task subset + trigger schedule + guardrails).
2. Runtime-triggered check emits auditable status artifact per cycle.
3. Approval-required routes remain blocked pending obligations (fail-closed).
4. Evidence captures at least one canary run artifact and one blocked approval-required route.

## Verification Plan
- Automated: existing kernel tests remain pass.
- Manual: execute one canary cycle and capture status artifact.
- Security: verify blocked approval-required path in canary output.

## Dependencies
- OpenClaw heartbeat/cron path and local workspace artifacts.
- No 3PP dependency.

## Closure
- Outcome summary: Implementation-complete. Added canary runtime cycle runner (`tools/tde_canary_runtime_cycle.py`) that emits auditable cycle status artifact (`knowledge/evidence/2026-03/tde-canary-status-latest.json`) with fail-closed approval-required routing behavior demonstrated.
- Accepted by: JOB-PROD-001 + JOB-ARC-001 (owner pre-authorization acknowledged 2026-03-02)
- Date closed: 2026-03-02

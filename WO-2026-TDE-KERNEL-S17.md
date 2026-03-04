# Work Order (WO) — TDE Kernel Slice S17

## Metadata
- WO-ID: WO-2026-TDE-KERNEL-S17
- Title: Fail-closed binding resolution proof for mutation paths
- Owner: JOB-PROD-001
- Date opened: 2026-03-04
- Lane: Build
- Work type: Hardening
- Risk class: High

## Intent
- Objective: Remove authority ambiguity by requiring proven active-binding registry resolution before any side-effecting mutation.
- Why now: S15 introduced binding integrity checks but unresolved registry lookups could still use synthesized fallback bindings, weakening fail-closed guarantees.
- Non-goals: Multi-job orchestration redesign, full storage migration away from TASKS.md.

## Scope
1. Enforce fail-closed behavior when binding source is unresolved/fallback for claimed mutation paths.
2. Emit deterministic reason code (`binding_unresolved_fail_closed`) with retry obligations.
3. Keep non-mutation/no-claim operational checks runnable.
4. Add dedicated regression test + verification artifacts.

## Acceptance Criteria
1. Claimed mutation path with unresolved registry binding is blocked with deterministic fail-closed reason.
2. No writeback side effects occur in unresolved binding path.
3. Proven binding path remains functional.
4. Verification bundle includes pass + fail-closed artifacts.

## Planned Change Artifacts
- `tools/tde_job_tick_runner.py`
- `tools/test_s17_binding_resolution_failclosed.py`
- `os/sops/TDE_JOB_TICK_CONTRACT_V1.md`
- `knowledge/evidence/2026-03/tde-job-tick-s17-pass.json`
- `knowledge/evidence/2026-03/tde-job-tick-s17-failclosed-binding-unresolved.json`
- `knowledge/evidence/2026-03/2026-03-04__verification__wo-2026-tde-kernel-s17.md`

## Closure
- Outcome summary: Implemented fail-closed enforcement for unresolved binding registry sources on side-effecting mutation paths. Claimed work now blocks with `binding_unresolved_fail_closed` and explicit retry obligations; no writeback is applied in this path.
- Accepted by: JOB-PROD-001 (execution baseline); JOB-ARC-001 formal sign-off pending
- Date closed: 2026-03-04
- Linked Change Artifact(s): `tools/tde_job_tick_runner.py`; `tools/test_s17_binding_resolution_failclosed.py`; `os/sops/TDE_JOB_TICK_CONTRACT_V1.md`; `knowledge/evidence/2026-03/tde-job-tick-s17-pass.json`; `knowledge/evidence/2026-03/tde-job-tick-s17-failclosed-binding-unresolved.json`; `knowledge/evidence/2026-03/2026-03-04__verification__wo-2026-tde-kernel-s17.md`

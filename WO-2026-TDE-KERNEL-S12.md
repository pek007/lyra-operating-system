# Work Order (WO) — TDE Kernel Slice S12

## Metadata
- WO-ID: WO-2026-TDE-KERNEL-S12
- Title: Real workload canary integration (ingestion/normalization + first audited write-back)
- Owner: JOB-PROD-001
- Date opened: 2026-03-03
- Lane: Build
- Work type: Feature
- Risk class: Medium

## Intent
- Objective: Pivot the TDE canary from synthetic tasks to real canonical task-state input and prove one safe, idempotent, audited write-back action end-to-end.
- Why now: S1–S11 established deterministic governance and rollout artifacts; the next risk is adoption gap (artifact-complete simulation without real-workflow execution).
- Non-goals: Trello full cutover, broad write-back surface, UI redesign, approval-gate relaxation, repo split.

## Scope
1. Add a real-task ingestion + normalization adapter for canary runtime input.
2. Replace default synthetic-only input path with canonical task-source read path (with deterministic validation and fail-closed fallback).
3. Run canary classification/routing on real workload state.
4. Execute one low-risk mutation path as idempotent audited write-back.

## Acceptance Criteria
1. Canary runtime can ingest canonical task state (not only in-script synthetic seed data) through a deterministic adapter contract.
2. Normalization/validation contract is explicit and test-covered for missing/ambiguous metadata cases.
3. End-to-end S12 evidence cycle demonstrates progress-state/routing output on real workload input.
4. At least one low-risk write-back action is executed idempotently with audit linkage (actor/job/policy decision reference + idempotency key).
5. Fail-closed behavior remains intact when canonical input is invalid/unavailable.

## Planned Change Artifacts
- `tools/tde_canary_runtime_cycle.py`
- `tools/tde_kernel_slice_tests.py`
- `os/sops/TDE_CANARY_SCHEDULING_CONTRACT_V1.md` (if contract updates are needed)
- `knowledge/evidence/2026-03/2026-03-03__verification__wo-2026-tde-kernel-s12.md`

## Closure
- Outcome summary: Implemented real-task ingestion/normalization adapter in canary runtime (`tools/tde_canary_runtime_cycle.py`) with deterministic TASKS Active-lane parsing + fallback metadata; executed first real-workload end-to-end job-tick slice with low-risk idempotent audited write-back to canonical task state via `tools/tde_job_tick_runner.py`.
- Accepted by: JOB-PROD-001 (execution baseline); JOB-ARC-001 formal sign-off pending
- Date closed: 2026-03-03
- Linked Change Artifact(s): `tools/tde_canary_runtime_cycle.py`; `tools/tde_job_tick_runner.py`; `knowledge/evidence/2026-03/tde-canary-realworkload-latest.json`; `knowledge/evidence/2026-03/tde-job-tick-s12-writeback.json`; `knowledge/evidence/2026-03/2026-03-03__verification__tde-2026-024-real-task-ingestion-baseline.md`; `knowledge/evidence/2026-03/2026-03-03__verification__tde-2026-025-real-workload-writeback-slice.md`

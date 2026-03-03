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
- Outcome summary: _Pending_
- Accepted by: _Pending_
- Date closed: _Pending_
- Linked Change Artifact(s): _Pending_

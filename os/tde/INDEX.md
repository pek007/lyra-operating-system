# TDE Canonical Entrypoint Index

Status: Active
Owner: JOB-PROD-001

## Purpose
Single entrypoint for Task & Decision Engine contracts, runtime tools, tests, and evidence surfaces.

## Contracts
- `os/sops/TDE_JOB_TICK_CONTRACT_V1.md` — job tick mutation/authority/objective rules.
- `os/sops/TDE_CANARY_SCHEDULING_CONTRACT_V1.md` — canary trigger and status cycle semantics.
- `os/sops/TDE_DB_CANONICAL_CUTOVER_GATE_V1.md` — DB cutover GO/NO-GO gate criteria.

## Runtime tools
- `tools/tde_kernel.py` — shared deterministic governance kernel module (runtime import surface).
- `tools/tde_job_tick_runner.py` — deterministic claim/validate/mutate/writeback loop.
- `tools/tde_canary_runtime_cycle.py` — canary classification + guardrail cycle.
- `tools/tde_release_envelope.py` — release gate packet helper.
- `tools/tde_state_store.py` — durable state shadow store bootstrap (SQLite init/import/export/parity primitives).
- `tools/tde_cutover_readiness_report.py` — cutover readiness verdict emitter (GO/NO-GO baseline).
- `tools/tde_state_parity_check.py` — shadow parity verifier between canonical TASKS parse and DB projection.

## Verification tests
- `tools/tde_kernel_slice_tests.py`
- `tools/test_s15_binding_integrity.py`
- `tools/test_s16_objective_linkage.py`
- `tools/test_s17_binding_resolution_failclosed.py`
- `tools/test_s18_atomic_writeback.py`
- `tools/test_s25_binding_lifecycle.py`
- `tools/test_s32_shadow_state_write.py`
- `tools/test_s33_shadow_thresholds.py`
- `tools/test_s35_state_ledger_write.py`

## Authority and runtime state
- `os/runtime/tde_active_bindings.json` — active binding registry.
- `os/runtime/tde_objectives.json` — objective registry (objective IDs/checkpoint allowlists).
- `TASKS.md` — current canonical task board (temporary kanban SoR).

## Evidence surfaces
- `knowledge/evidence/2026-03/` — sprint verification bundles + machine-readable artifacts.
- `knowledge/reports/` — external deep research ingests and analyses.

## Real vs simulated status
- **Real:** job tick writeback on canonical TASKS board, binding checks, objective linkage checks, fail-closed mutation guards.
- **Simulated/limited:** full multi-job concurrency orchestration, non-local durable execution ledger, production deployment boundary metrics.

## Change rule
Any contract or runtime change must update this index when paths/status change.

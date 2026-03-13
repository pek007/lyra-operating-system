# TDE Staging Runtime Setup Note v1

Status: Draft
Owner: Peter + Lyra
Date: 2026-03-13
Related:
- `TDE_ENVIRONMENT_AND_PROMOTION_MODEL_V1.md`
- `TDE_ENVIRONMENT_PATH_CONVENTION_V1.md`
- `OPENCLAW_CONFIG_CHANGE_SOP_V1.md`

## Purpose
Define the first practical setup for a staging TDE/OpenClaw runtime under the new environment model.

This note is intentionally narrow.
It does not attempt to redesign the whole runtime stack.
It defines the minimum staging embodiment needed to stop testing new TDE runtime behavior directly against production-adjacent paths.

## Immediate objective
Stand up a **staging** runtime path set that is isolated from current production-adjacent paths for:
- canonical TDE DB
- objectives
- bindings
- projected task board
- evidence outputs
- cron/tick targets

## Current baseline
Current default/proto-prod paths are still:
- `os/runtime/tde_state.sqlite`
- `os/runtime/tde_objectives.json`
- `os/runtime/tde_active_bindings.json`
- `os/runtime/TASKS_from_db.md`
- `knowledge/evidence/2026-03/...`

These should now be treated as **legacy production-adjacent defaults**, not as the desired future structure.

## Staging target paths
The first staging runtime should use:
- DB: `os/runtime/staging/tde_state.sqlite`
- projected tasks: `os/runtime/staging/TASKS_from_db.md`
- objectives: `os/runtime/staging/tde_objectives.json`
- bindings: `os/runtime/staging/tde_active_bindings.json`
- evidence root: `knowledge/evidence/staging/`
- cron/config root: `os/config/staging/cron/`

## Directory skeleton status
Environment skeleton directories now exist for:
- `os/runtime/dev/`
- `os/runtime/staging/`
- `os/runtime/prod/`
- `os/config/dev/cron/`
- `os/config/staging/cron/`
- `os/config/prod/cron/`
- `knowledge/evidence/dev/`
- `knowledge/evidence/staging/`
- `knowledge/evidence/prod/`

## First scripts to parameterize
The first priority is not every tool.
It is the scripts on or near the active TDE runtime path.

### Priority 1 — core runtime path
1. `tools/tde_job_tick_runner.py`
   - currently defaults to legacy paths for DB, bindings, objectives, and evidence output
   - should become environment-aware first

2. `tools/tde_job_tick_cron_hook.sh`
   - already has some path env vars
   - should become the first environment-aware wrapper and default to explicit staging/prod path sets instead of ambiguous defaults

3. `tools/tde_state_store.py`
   - currently defaults to legacy DB and projection paths
   - should accept environment-scoped defaults or wrappers

### Priority 2 — adjacent TDE release/evidence path
4. `tools/tde_cutover_readiness_report.py`
5. `tools/tde_milestone_snapshot.py`
6. `tools/tde_owner_gate_packet.py`
7. `tools/tde_release_envelope.py`
8. `tools/tde_activation_execution_receipt.py`

These still default to legacy `knowledge/evidence/2026-03/...` paths and should eventually be environment-scoped.

### Priority 3 — canary/simulation/reporting path
9. `tools/tde_canary_runtime_cycle.py`
10. `tools/tde_canary_operational_summary.py`
11. `tools/tde_canary_simulate_three_clean_cycles.py`
12. `tools/tde_rollout_broader_scope_simulation.py`

## Recommended implementation approach
### Step 1 — wrapper-first
Do **not** refactor every script immediately.
Start with wrapper/config discipline.

Preferred near-term method:
- keep script-level explicit flags where possible
- use environment-specific wrapper invocations from `os/config/staging/cron/`
- pass staging paths explicitly

This reduces risk versus changing every tool default at once.

### Step 2 — make the core scripts environment-aware
After wrapper-based staging is proven, add first-class environment flags/default resolution to:
- `tde_job_tick_runner.py`
- `tde_state_store.py`
- `tde_job_tick_cron_hook.sh`

Status update:
- `tde_job_tick_runner.py` now supports `--env dev|staging|prod`
- `tde_state_store.py` now supports `--env dev|staging|prod`
- `tde_job_tick_cron_hook.sh` now requires explicit `TDE_ENV=dev|staging|prod`

### Step 3 — migrate surrounding evidence emitters
Move adjacent TDE evidence-producing scripts to environment-scoped outputs.

## Minimum staging setup procedure
### A. Seed staging runtime files
Create or copy initial staging artifacts for:
- `os/runtime/staging/tde_objectives.json`
- `os/runtime/staging/tde_active_bindings.json`
- `os/runtime/staging/tde_state.sqlite` (initialized or imported from a safe test fixture, not production live state unless explicitly intended)

### B. Use a staging-specific tick invocation
A staging tick command should explicitly pass staging paths for:
- canonical DB
- bindings registry
- objective registry
- projection output
- artifact output
- shadow DB/output if used

### C. Write all staging evidence to `knowledge/evidence/staging/...`
No staging validation artifact should land in the production-adjacent evidence tree by accident.

### D. Keep production cron unchanged until staging proves stable
Do not repoint production cron hooks yet.

## Staging safety rules
1. No production cron should target staging paths accidentally.
2. No staging cron should target production-adjacent DB/objective/binding paths.
3. Staging decision-policy tests may use synthetic objectives/tasks.
4. Staging evidence must be clearly separated from production-adjacent evidence.
5. If a wrapper or script path is ambiguous, fail closed and require explicit path arguments.

## Suggested first concrete command shape
Illustrative shape only; finalize after wrapper design:

```bash
python3 tools/tde_job_tick_runner.py \
  --canonical-db-path os/runtime/staging/tde_state.sqlite \
  --binding-registry-path os/runtime/staging/tde_active_bindings.json \
  --objective-registry-path os/runtime/staging/tde_objectives.json \
  --writeback-tasks-path os/runtime/staging/TASKS_from_db.md \
  --artifact-path knowledge/evidence/staging/2026-03/tde-job-tick-latest.json \
  --shadow-state-db-path os/runtime/staging/tde_state.sqlite
```

## Immediate next implementation tasks
1. Add environment-aware path flags/default helpers to `tde_job_tick_runner.py` and `tde_state_store.py`.
2. Migrate the next ring of TDE evidence emitters away from legacy `knowledge/evidence/2026-03/...` defaults.
3. Define the first staging promotion checklist.
4. Decide whether staging should use seeded synthetic objectives/tasks or a curated production mirror for future validation cycles.

## Initial staging proof
A first staging-only end-to-end tick has now been run with:
- isolated staging DB
- isolated staging objectives/bindings
- staging artifact output under `knowledge/evidence/staging/2026-03/`

Observed result:
- run completed successfully
- no work was claimed (`no_work = 1`)
- no production-adjacent DB/objective/binding/evidence path was targeted by the hook

Key evidence path:
- `knowledge/evidence/staging/2026-03/tde-job-tick-latest.json`

## Native environment-resolution proof
The core runtime scripts have also now been exercised directly in staging mode without relying only on the cron hook wrapper:
- `python3 tools/tde_state_store.py init --env staging`
- `python3 tools/tde_job_tick_runner.py --env staging --canonical-store db --shadow-state-enabled`

Result:
- native environment path resolution worked as intended
- staging DB/evidence/registry paths were used automatically

## Bottom line
The first professionalizing move is not a giant refactor.
It is to stand up a real staging path set and route the core TDE runtime loop through it explicitly.

That creates a safe place to validate further D-layer and chaining changes before they touch production-adjacent paths.
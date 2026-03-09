# TDE DB canonical cutover executed

- Date: 2026-03-09
- Decision: GO / executed
- Owner authorization: Peter Eklind granted explicit authorization in Lyra Operations group thread on 2026-03-09.
- Observation window: satisfied (>3 days of shadow observation with healthy parity evidence)

## What was executed
- Refreshed DB state from current `TASKS.md` baseline:
  - `python3 tools/tde_state_store.py import-tasks --db os/runtime/tde_state.sqlite --tasks TASKS.md`
- Reconfirmed parity:
  - `python3 tools/tde_state_store.py parity --db os/runtime/tde_state.sqlite --tasks TASKS.md`
  - Result: `match=true`, `file_count=110`, `db_count=110`
- Generated runtime projection from DB canonical state:
  - `os/runtime/TASKS_from_db.md`
- Switched scheduled TDE job tick hook default canonical store from markdown to DB:
  - `tools/tde_job_tick_cron_hook.sh`
  - Default canonical store now: `db`
  - Default projection path now: `os/runtime/TASKS_from_db.md`
- Executed no-op cutover verification tick in DB canonical mode:
  - Artifact: `knowledge/evidence/2026-03/tde-db-cutover-execution-check.json`
  - Result: `status=ok`, `shadow_state.status=ok`, `threshold_exceeded=false`

## Safety / rollback posture
- `TASKS.md` was intentionally preserved as a legacy markdown artifact and not overwritten during cutover.
- Runtime-visible projection from DB is written to `os/runtime/TASKS_from_db.md` to avoid destructive loss of rich notes/history in `TASKS.md`.
- Rollback path: set `TDE_CANONICAL_STATE_STORE=markdown` (or restore previous hook default) and continue using `TASKS.md` as canonical source.

## Operational status after execution
- Canonical TDE runtime store: **DB (`os/runtime/tde_state.sqlite`)**
- Legacy markdown board: retained
- Runtime projection: `os/runtime/TASKS_from_db.md`
- Cutover status: **executed**

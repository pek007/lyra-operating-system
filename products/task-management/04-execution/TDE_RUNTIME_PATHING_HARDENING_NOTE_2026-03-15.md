# TDE Runtime Pathing Hardening Note — 2026-03-15

Owner: Lyra  
Linked task: `TASK-20260315-CP-TDE-ASSIGNMENT-ACCEPTANCE`

## Problem
The TDE runtime surface was split by default pathing:
- assignment acceptance defaulted to canonical `os/runtime/tde_state.sqlite`
- several intake / formation / closure tools still defaulted to staging paths under `os/runtime/staging/`

That meant producer acceptance, intake, formation, and closure could silently target different DBs unless an operator explicitly overrode paths.

## Hardening change applied
The following tools now default to canonical runtime paths:
- `tools/tde_request_entry.py`
- `tools/tde_intake_ingest.py`
- `tools/tde_intent_intake.py`
- `tools/tde_formation_creator.py`
- `tools/tde_task_close.py`

Canonical defaults now point to:
- DB: `os/runtime/tde_state.sqlite`
- objective registry: `os/runtime/tde_objectives.json`
- task projection: `os/runtime/TASKS_from_db.md`

## Why this matters
This removes the accidental active-vs-staging split from the default operator path.
Staging remains available through explicit path override, but no longer acts as the hidden default for core TDE intake/formation/closure flows.

## Current stance
- Canonical runtime default = `os/runtime/*`
- Staging usage must now be explicit
- Silent path divergence risk is reduced materially

## Remaining follow-up
This change hardens defaults, but a fuller follow-up may still be warranted later:
- explicit `--env` handling or shared runtime-path resolver
- fail-loud warnings when mixing canonical and staging artifacts in one flow
- stronger path/authority documentation in TDE runbooks/contracts

## Bottom line
The immediate pathing defect was real and is now materially reduced:
core TDE tools no longer split across canonical vs staging by default.

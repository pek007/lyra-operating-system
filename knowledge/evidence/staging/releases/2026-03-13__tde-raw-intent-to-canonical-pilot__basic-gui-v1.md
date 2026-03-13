# TDE Raw Intent-to-Canonical Pilot — Basic GUI v1

Date: 2026-03-13
Status: Pilot executed successfully in staging
Owner: Peter + Lyra
Scope: First end-to-end pilot from raw request text -> formation record -> canonical objective/task creation

## Purpose
Prove the first true end-to-end intent pipeline for a real request class.

## Raw request used
- `Create a basic GUI for TDE`

## Command executed
- `python3 tools/tde_intent_intake.py --request-text "Create a basic GUI for TDE" --source-ref "telegram:lyra-operations:basic-gui-live-request" --formation-out knowledge/evidence/staging/2026-03/tde-intent-formation-basic-gui-live.json --create-canonical --db-path os/runtime/staging/tde_state.sqlite --objectives-path os/runtime/staging/tde_objectives.json --tasks-projection-path os/runtime/staging/TASKS_from_db.md`

## What happened
### 1. Request classification
The intake layer classified the request as:
- request class: `basic_tde_gui`

### 2. Formation artifact created
Formation artifact path:
- `knowledge/evidence/staging/2026-03/tde-intent-formation-basic-gui-live.json`

Key formation attributes:
- recommended next action: `proceed_with_assumptions`
- workflow family: `implementation_verification_readiness`

### 3. Canonical objective created
- `OBJ-FORM-FORM-TELEGRAM-LYRA-OPERATIONS-BASIC-GUI-LIVE-`

### 4. Canonical tasks created
- `TDE-FORM-FORM-TELEGRAM-LYRA-OPERATIONS-BASIC-GUI-LIVE--001`
  - `Define first bounded TDE GUI scope`
  - status: `Active`
- `TDE-FORM-FORM-TELEGRAM-LYRA-OPERATIONS-BASIC-GUI-LIVE--002`
  - `Verify first TDE GUI scope and constraints`
  - status: `Waiting`

## Why this matters
This is the first successful proof of the full thin v1 path:
- raw human request
- request-class-specific intake
- formation artifact generation
- canonical objective creation
- canonical task creation
- projection into staging task view

## Important limitation
This is still a thin, request-class-specific intake path, not a general formation engine.

What is proven:
- TDE can now do the full path for at least one bounded real request class.

What is not yet proven:
- broad/general request interpretation across arbitrary request classes
- rich clarification dialogue before formation
- cross-family formation output beyond the first approved family

## Bottom line
The end-to-end path is now real for a first request class.

That means the remaining gap is no longer whether TDE can go from intent to work at all.
The remaining gap is expanding and generalizing that capability beyond the first thin pilot path.

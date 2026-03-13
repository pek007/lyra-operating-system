# TDE Environment Path Convention v1

Status: Draft
Owner: Peter + Lyra
Date: 2026-03-13
Related:
- `TDE_ENVIRONMENT_AND_PROMOTION_MODEL_V1.md`
- `OPENCLAW_CONFIG_CHANGE_SOP_V1.md`
- `CRON_SPEC_AUTONOMOUS_GOVERNANCE_SWEEPS.md`

## Purpose
Turn the environment/promotion model into a concrete naming and path convention that can be implemented.

This document defines where environment-specific TDE/OpenClaw runtime artifacts should live for:
- development
- staging
- production

## Core decision
Adopt a single-repo, environment-scoped runtime-root model as the near-term standard.

That means:
- code can remain in one repo/workspace for now,
- but runtime state, environment config, evidence outputs, and scheduler surfaces must become environment-scoped.

## Canonical environment names
Use these exact names:
- `dev`
- `staging`
- `prod`

Do not mix synonyms like:
- `development`
- `test`
- `production`
- `live`

Human prose may use those words, but artifact paths and machine-readable fields should use:
- `dev`
- `staging`
- `prod`

## Environment runtime root pattern
Preferred pattern:
- `os/runtime/<env>/...`
- `knowledge/evidence/<env>/...`
- `os/config/<env>/...`

This keeps environment scoping visible and local to the workspace.

## Canonical path map

## 1) Canonical TDE DB
### Current production-adjacent path
- `os/runtime/tde_state.sqlite`

### New convention
- `os/runtime/dev/tde_state.sqlite`
- `os/runtime/staging/tde_state.sqlite`
- `os/runtime/prod/tde_state.sqlite`

### Rule
No environment may share the same DB file.

## 2) Projected task board
### Current production-adjacent path
- `os/runtime/TASKS_from_db.md`

### New convention
- `os/runtime/dev/TASKS_from_db.md`
- `os/runtime/staging/TASKS_from_db.md`
- `os/runtime/prod/TASKS_from_db.md`

### Rule
Projected task views must reflect their own environment DB only.

## 3) Objective registry
### Current production-adjacent path
- `os/runtime/tde_objectives.json`

### New convention
- `os/runtime/dev/tde_objectives.json`
- `os/runtime/staging/tde_objectives.json`
- `os/runtime/prod/tde_objectives.json`

### Rule
Production objectives must not be reused directly in development or staging when those environments are exercising experimental automation.

## 4) Active binding registry
### Current production-adjacent path
- `os/runtime/tde_active_bindings.json`

### New convention
- `os/runtime/dev/tde_active_bindings.json`
- `os/runtime/staging/tde_active_bindings.json`
- `os/runtime/prod/tde_active_bindings.json`

### Rule
Bindings are environment-specific authority artifacts and must never be shared across environments.

## 5) Tick / runtime artifacts
### Current production-adjacent pattern
- typically under `knowledge/evidence/YYYY-MM/...`

### New convention
- `knowledge/evidence/dev/YYYY-MM/...`
- `knowledge/evidence/staging/YYYY-MM/...`
- `knowledge/evidence/prod/YYYY-MM/...`

### Rule
Any runtime artifact that may influence operational decisions should be written to the environment-specific evidence tree.

Examples:
- job tick artifacts
- decision advancement records
- escalation packages
- cutover/readiness reports
- release/promotion validation evidence

## 6) Environment config roots
### New convention
- `os/config/dev/`
- `os/config/staging/`
- `os/config/prod/`

### Intended contents
- environment-specific runtime path values
- cron enablement flags
- environment identity markers
- optional wrappers or helper configs

This does not replace OpenClaw's actual live config location by itself.
It creates a workspace-side source-of-truth structure for environment-scoped runtime operation.

## 7) Cron / scheduler specs
### New convention
Base specs may remain global, but environment activation must be explicit.

Recommended structure:
- global design spec remains in current top-level docs
- environment-specific activation notes or wrappers live under:
  - `os/config/dev/cron/`
  - `os/config/staging/cron/`
  - `os/config/prod/cron/`

### Rule
The same scheduler hook or cron command must not point different environments at the same runtime DB/evidence path.

## 8) Runtime release / promotion artifacts
### New convention
- `knowledge/evidence/staging/releases/...`
- `knowledge/evidence/prod/releases/...`

Examples:
- candidate validation packet
- promotion approval packet
- rollback execution note
- post-promote verification note

## 9) Scratch / simulation artifacts
### New convention
- `knowledge/evidence/dev/simulations/...`
- `knowledge/evidence/staging/simulations/...`

### Rule
Synthetic or simulated results should never be stored in production evidence folders.

## Recommended environment markers
Where machine-readable markers are needed, use:

```json
{
  "environment": "dev"
}
```

or

```json
{
  "environment": "staging"
}
```

or

```json
{
  "environment": "prod"
}
```

Do not invent alternate values.

## Path examples by environment

### Development example
- DB: `os/runtime/dev/tde_state.sqlite`
- objectives: `os/runtime/dev/tde_objectives.json`
- bindings: `os/runtime/dev/tde_active_bindings.json`
- evidence: `knowledge/evidence/dev/2026-03/...`
- config root: `os/config/dev/`

### Staging example
- DB: `os/runtime/staging/tde_state.sqlite`
- objectives: `os/runtime/staging/tde_objectives.json`
- bindings: `os/runtime/staging/tde_active_bindings.json`
- evidence: `knowledge/evidence/staging/2026-03/...`
- config root: `os/config/staging/`

### Production example
- DB: `os/runtime/prod/tde_state.sqlite`
- objectives: `os/runtime/prod/tde_objectives.json`
- bindings: `os/runtime/prod/tde_active_bindings.json`
- evidence: `knowledge/evidence/prod/2026-03/...`
- config root: `os/config/prod/`

## Transition from current state
Current production-adjacent paths should be treated as legacy/default paths pending cutover.

### Temporary interpretation rule
Until path cutover is complete:
- `os/runtime/tde_state.sqlite` should be treated as production-adjacent / proto-prod
- `os/runtime/tde_objectives.json` should be treated as production-adjacent
- `os/runtime/tde_active_bindings.json` should be treated as production-adjacent
- `knowledge/evidence/2026-03/...` remains mixed legacy evidence and should not be treated as cleanly environment-scoped

### Migration sequence
1. Create environment directories
2. Define environment-specific runtime flags/CLI defaults
3. Stand up staging paths first
4. Validate staging runtime behavior
5. Repoint production runtime explicitly
6. Decommission ambiguous legacy/default paths when safe

## Non-negotiable rules
1. No shared DB across environments.
2. No shared binding registry across environments.
3. No shared production/staging evidence output path for runtime decision artifacts.
4. Any cron-enabled environment must point explicitly at its own runtime root.
5. Legacy unscoped paths are transitional only and must not be treated as the long-term standard.

## Immediate next implementation targets
1. Add environment-aware path flags to TDE runtime scripts.
2. Stand up `staging` first.
3. Keep `prod` on legacy paths until staging proves stable.
4. Create the first staging-only end-to-end validation run.

## Initial embodiment status
The first directory skeleton now exists for:
- `os/runtime/dev/`
- `os/runtime/staging/`
- `os/runtime/prod/`
- `os/config/dev/cron/`
- `os/config/staging/cron/`
- `os/config/prod/cron/`
- `knowledge/evidence/dev/`
- `knowledge/evidence/staging/`
- `knowledge/evidence/prod/`

The first staging setup note is defined in:
- `TDE_STAGING_RUNTIME_SETUP_NOTE_V1.md`

## Bottom line
This convention gives us a concrete near-term separation model without requiring a full multi-repo or multi-host setup immediately.

The key professional move is simple:
keep one codebase for now if needed, but stop sharing runtime state, authority artifacts, cron targets, and evidence paths across environments.
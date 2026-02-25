# SERVICE_BOUNDARY_ARCHITECTURE.md

## Purpose
Define how reusable services are shared across Operating System and PX Strategy **without data/usage overlap**.

## Core Rule
Shared codebase, separated instances.

- Reuse the same service architecture/modules.
- Run separate instances per domain:
  - `os` instance (Lyra Operating System)
  - `px` instance (PX Strategy delivery)

## Isolation Requirements
Each instance must have its own:
- workspace root/data directory
- task database/files
- evidence/log storage
- API keys/secrets namespace
- routing/model policy config
- dashboards and access controls

## Namespace Standard
Use explicit domain keys everywhere:
- `domain=os` or `domain=px`
- IDs prefixed accordingly when needed (e.g., `OS-TASK-*`, `PX-TASK-*`)

## Shared Services Pattern
Build services as reusable modules with domain-aware configuration:
- Task service
- Evidence service
- Risk/controls service
- Model-routing service
- Notification service

Each module reads a domain-specific config object and never assumes global singleton state.

## Deployment Pattern (recommended)
- Single repository, multi-instance runtime.
- Environment files per domain:
  - `.env.os`
  - `.env.px`
- Separate cron schedules per domain.

## Data Safety Guardrails
- No cross-domain reads by default.
- Cross-domain access requires explicit allow rule and audit log entry.
- Export/import only through explicit handoff artifacts.

## Immediate Application
- Control Panel build should include domain selector support from start (`os` first, `px` later).
- Task manager should support multi-instance initialization, not a single hardcoded workspace.

## Version
- v1.0
- Date: 2026-02-25

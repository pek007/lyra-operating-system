# TDE Request Entry Result Artifact v1

Status: Draft
Owner: Peter + Lyra
Product: Task Management (`A-007`)
Date: 2026-03-13
Related:
- `products/task-management/07-decisions/TDE_REQUEST_ENTRY_WORKFLOW_V1.md`
- `tools/tde_request_entry.py`

## Purpose
Define the first durable result artifact emitted by the integrated TDE request-entry workflow.

## Why this matters
Without a dedicated result artifact, the workflow is still too ephemeral.
A first-class result artifact makes the request-entry path auditable and reviewable.

## Current artifact shape
Current result artifacts include at least:
- `artifactType = tde_request_entry_result`
- `schemaVersion = 1.0.0`
- `recorded_at`
- `request_text`
- `source_ref`
- `request_class`
- `formation_id`
- `formation_path`
- `recommended_next_action`
- `required_clarifications`
- `canonical_creation` when applicable

## Current behavior
The integrated request-entry workflow can now emit this artifact for both:
- proceed flows
- ask/clarification flows

## Next likely follow-on work
1. define a formal schema for `tde_request_entry_result`
2. decide standard artifact paths by environment
3. include richer trace refs or audit linkage where useful

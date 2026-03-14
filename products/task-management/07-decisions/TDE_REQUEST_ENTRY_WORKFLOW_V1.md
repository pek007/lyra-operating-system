# TDE Request Entry Workflow v1

Status: Draft
Owner: Peter + Lyra
Product: Task Management (`A-007`)
Date: 2026-03-13
Related:
- `products/task-management/07-decisions/TDE_INTENT_INTAKE_AND_FORMATION_POLICY_V1.md`
- `products/task-management/07-decisions/TDE_FORMATION_TO_CANONICAL_CREATION_MAPPING_V1.md`
- `tools/tde_request_entry.py`

## Purpose
Describe the first integrated user-facing TDE request-entry flow.

This workflow packages three previously separate steps into one higher-level capability:
1. intake and request classification
2. formation artifact generation
3. canonical work creation when execution-ready

## Workflow shape
### Input
A raw request, such as:
- `Create a basic GUI for TDE`
- `Build an internal tool`

### Step 1 — Intake
TDE classifies the request into a bounded request class and forms a canonical `tde_intake_packet`.

### Step 2 — Validation
TDE validates the intake packet against the registered schema before continuing.

### Step 3 — Formation
TDE creates a `tde_intent_formation_record` and validates it against the registered schema.

### Step 4 — Branch
If formation says:
- `proceed_directly` or `proceed_with_assumptions`
  - create canonical objective/task artifacts
- `ask_clarifying_questions`
  - stop after formation and surface questions
- `escalate_for_strategic_framing`
  - stop after formation and route framing escalation

## Current implementation surface
The first integrated workflow entry now exists at:
- `tools/tde_request_entry.py`

The first durable result artifact for this workflow is defined at:
- `products/task-management/07-decisions/TDE_REQUEST_ENTRY_RESULT_ARTIFACT_V1.md`

## Current bounded behavior
The current v1 workflow supports both major first-branch behaviors:
- proceed into canonical creation
- ask clarifying questions and stop

## Why this matters
This is the first time TDE has a single higher-level request-entry path rather than only separate low-level formation and creation utilities.

## Next likely follow-on work
1. add a dedicated result artifact for the request-entry run itself
2. integrate the workflow into a more native TDE runtime surface
3. expand the request-class table and clarification logic
4. decide when strategic-framing escalation should become active in the same workflow

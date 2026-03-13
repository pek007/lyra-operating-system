# TDE Formation-to-Canonical-Creation Mapping v1

Status: Draft
Owner: Peter + Lyra
Product: Task Management (`A-007`)
Date: 2026-03-13
Related:
- `products/task-management/07-decisions/TDE_INTENT_INTAKE_AND_FORMATION_POLICY_V1.md`
- `schemas/tde_intent_formation_record/v1.0.0.schema.json`
- `products/task-management/07-decisions/TDE_PILOT_WORKFLOW_FAMILY_IMPLEMENTATION_VERIFICATION_READINESS_V1.md`
- `products/task-management/07-decisions/TDE_DECISION_POLICY_RUNTIME_EMBODIMENT_V1.md`
- `PRODUCT_PORTFOLIO_REGISTRY.md`

## Purpose
Define the first bridge from a valid TDE intent-formation record into canonical TDE objective/task creation.

This is the missing transition from:
- "TDE has interpreted the request"
to:
- "TDE has created governable work in canonical state"

## Scope of v1
This mapping is intentionally narrow.

It applies only when:
- a valid `tde_intent_formation_record` exists,
- the recommended next action is execution-oriented,
- and the proposed workflow family maps to an approved creation family.

For v1, the approved creation family is:
- `implementation_verification_readiness`

## Core decision
A formation record does **not** immediately imply execution.

Instead, v1 mapping should do two things:
1. create canonical objective/task artifacts when the formation result is execution-ready,
2. stop at the formation artifact when the result still requires clarification or strategic framing.

## Mapping gate
A formation record may map into canonical objective/task creation only if all of the following are true:
- `recommended_next_action` is either:
  - `proceed_directly`, or
  - `proceed_with_assumptions`
- `proposed_workflow_family` is recognized and approved for creation
- the formation output includes at least one first-stage and one first-task entry
- no required clarification is marked blocking for v1 creation

If these conditions are not met, TDE should persist the formation artifact but stop short of canonical work creation.

## v1 creation family
### Approved family
- `implementation_verification_readiness`

### Why this family first
It already has:
- a pilot workflow definition,
- a policy envelope,
- decision/runtime embodiment,
- and staging validation evidence.

That makes it the safest first target for automatic formation-to-work creation.

## Canonical creation outputs
When mapping is allowed, TDE should create or assign:

### A. Objective layer
A canonical objective record or objective candidate containing:
- objective title
- objective summary
- originating formation ID
- owning product = `A-007` (Task Management) unless a different product lane is explicitly selected later
- workflow family
- success criteria
- creation mode (`direct` or `assumption_based`)

### B. Task layer
A first canonical task set containing:
- task title
- task summary
- stage ID
- workflow family
- `decision_policy_ref`
- `objective_id`
- any initial chain metadata required by the selected family
- traceability back to the formation record

### C. Traceability layer
Each created objective/task artifact should retain:
- `formation_id`
- `source_ref`
- `creation_mapping_version`
- assumption flag if created under assumptions

## v1 stage mapping
For `implementation_verification_readiness`, the mapping should interpret:

### `proposed_first_stage_set`
Allowed v1 stage values include:
- `implementation`
- `verification`
- `readiness-review`
- `closeout`
- `verification-research`

### `proposed_first_task_set`
Each task should map into a canonical DB task with:
- `title`
- `summary`
- `stage_id`
- `workflow_family`
- `decision_policy_ref`
- `formation_id`
- `objective_id`

## v1 objective ownership default
Unless explicitly overridden by a later lane-selection rule, v1 formation-created work should default to:
- Product: `A-007` Task Management

Rationale:
- this work is still inside the TDE formation/runtime pilot surface,
- and should not prematurely spill into other product lanes without a clearer ownership rule.

## v1 assumption handling
If the formation record's `recommended_next_action` is `proceed_with_assumptions`, canonical creation is allowed, but the created artifacts must carry:
- `created_with_assumptions = true`
- assumption list refs or copied assumption summary

This ensures the work is professional and honest, not falsely certain.

## v1 non-creation outcomes
### If `recommended_next_action = ask_clarifying_questions`
TDE should:
- persist the formation record,
- surface the required clarifications,
- and create no canonical tasks yet.

### If `recommended_next_action = escalate_for_strategic_framing`
TDE should:
- persist the formation record,
- create no canonical tasks yet,
- and route the result as a framing/escalation artifact rather than an execution artifact.

## Suggested canonical metadata fields for created tasks
At minimum, tasks created from a formation record should include:
- `formation_id`
- `source_ref`
- `workflow_family`
- `decision_policy_ref`
- `stage_id`
- `created_with_assumptions`
- `creation_mapping_version` = `v1`

## Suggested canonical fields for created objective records
At minimum:
- `objective_title`
- `objective_summary`
- `workflow_family`
- `success_criteria`
- `formation_id`
- `created_with_assumptions`
- `creation_mapping_version` = `v1`

## v1 recommended runtime behavior
The first embodiment should likely be:
1. validate the formation record against schema,
2. decide whether creation is allowed,
3. if allowed, create objective/task artifacts in canonical DB-backed state,
4. export projection/update evidence,
5. retain full traceability to the originating formation record.

## Non-goals for v1
- generalized multi-family formation mapping
- cross-product lane routing from formation
- autonomous strategic portfolio reprioritization
- automatic creation for aspiration-only requests
- replacement of Product Owner shaping judgment with fully generic generation

## Recommended next follow-on work
1. Define the first schema for canonical objective creation from a formation record.
2. Decide whether objective creation should be DB-backed first or file-backed first.
3. Pilot the mapping on one real request class, likely the first basic TDE GUI attempt.
4. Decide whether creation should also emit a dedicated creation artifact beyond DB/objective-registry mutation.

## First thin creator added
The first thin creator for this mapping now exists at:
- `tools/tde_formation_creator.py`

Reference formation example:
- `products/task-management/07-decisions/examples/TDE_INTENT_FORMATION_RECORD_BASIC_GUI_V1.json`

## Bottom line
This mapping defines the first safe bridge from:
- interpreted human intent,
to:
- real canonical TDE work.

For v1, the bridge should stay narrow:
- only execution-ready formation outputs,
- only approved workflow families,
- full traceability,
- and assumption-aware creation into canonical state.

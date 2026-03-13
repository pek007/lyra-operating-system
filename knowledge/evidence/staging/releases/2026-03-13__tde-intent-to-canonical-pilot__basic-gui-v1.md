# TDE Intent-to-Canonical Pilot — Basic GUI v1

Date: 2026-03-13
Status: Pilot executed successfully in staging
Owner: Peter + Lyra
Scope: First end-to-end pilot of intent formation -> canonical objective/task creation using the basic TDE GUI example

## Purpose
Prove that TDE can move from a formation artifact to real canonical work creation for a bounded request class.

## Input formation artifact
- `products/task-management/07-decisions/examples/TDE_INTENT_FORMATION_RECORD_BASIC_GUI_V1.json`

## Command executed
- `python3 tools/tde_formation_creator.py --formation-path products/task-management/07-decisions/examples/TDE_INTENT_FORMATION_RECORD_BASIC_GUI_V1.json --db-path os/runtime/staging/tde_state.sqlite --objectives-path os/runtime/staging/tde_objectives.json --tasks-projection-path os/runtime/staging/TASKS_from_db.md`

## Result summary
### Objective created
- `OBJ-FORM-FORM-TDE-GUI-001`
- owner: `A-007`
- workflow family: `implementation_verification_readiness`
- created with assumptions: `true`

### Canonical tasks created
1. `TDE-FORM-FORM-TDE-GUI-001-001`
   - title: `Define first bounded TDE GUI scope`
   - status: `Active`
   - stage: `implementation`

2. `TDE-FORM-FORM-TDE-GUI-001-002`
   - title: `Verify first TDE GUI scope and constraints`
   - status: `Waiting`
   - stage: `verification`

### Metadata/traceability present
Created tasks include:
- `formation_id`
- `source_ref`
- `workflow_family`
- `decision_policy_ref`
- `stage_id`
- `objective_id`
- `created_with_assumptions`
- `creation_mapping_version`

### Projection updated
The generated tasks are now visible in:
- `os/runtime/staging/TASKS_from_db.md`

## Interpretation
This is the first real proof that the new intake/formation layer can produce real canonical TDE work from a bounded intent/formation artifact.

In practical terms, TDE can now do this path for the first pilot family:
- intent (represented here as a formation artifact)
- objective creation
- canonical task creation
- policy-bearing task metadata generation
- projection into the readable staging task view

## Important limitation
This pilot starts from a manually authored formation record.
So it does **not** yet prove the full path from raw user request -> automatic formation record -> canonical work creation.

It proves the next bridge only:
- formation artifact -> canonical TDE work

## Conclusion
The intent-to-canonical bridge now exists in a first thin form for the approved pilot family.

That means the remaining major missing step is now much narrower:
- automatic/runtime generation of the formation artifact itself from real user input.

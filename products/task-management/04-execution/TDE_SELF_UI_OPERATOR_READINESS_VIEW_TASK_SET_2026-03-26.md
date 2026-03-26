# TDE Self-UI Operator Readiness View — Initial Live Task Set

Status: Draft active
Date: 2026-03-26
Owner: Task Management Product / Lyra
Related experiment brief: `products/task-management/04-execution/TDE_SELF_UI_PROVING_EXPERIMENT_BRIEF_2026-03-26.md`
Related gate assessment: `products/task-management/04-execution/TDE_SELF_UI_RUNTIME_CLOSURE_GATE_ASSESSMENT_2026-03-26.md`
Related intake: `control/tde-intake/tde-self-ui-proving-experiment-2026-03-26.json`

## Purpose
Define the first live task set for the bounded proving slice:
- **TDE Operator Readiness View**

This artifact intentionally defines the live task set before canonical runtime formation is executed, so the work can be reviewed as a governed experiment package rather than being half-formed inside runtime state first.

## Experiment constraint carried forward
Per the gate assessment, this experiment proceeds under a declared limitation:
- the assignment-acceptance substrate is strongly proven
- the broader producer/adapter -> runtime -> operated-proof chain is only partially proven
- any manual rescue or closure ambiguity during execution must be logged and counted against a full PASS

## Objective for this task set
Create and operate one bounded operator-facing UI slice that makes the TDE self-UI proving experiment inspectable through real execution state rather than descriptive documents alone.

## Proposed objective record
Suggested objective id:
- `OBJ-TDE-SELF-UI-OPERATOR-READINESS-2026-03-26`

Suggested title:
- `Implement and operate the TDE Operator Readiness View proving slice`

Suggested workflow family:
- `implementation_verification_readiness`

Suggested success criteria:
- a bounded objective is entered through the canonical experiment intake
- canonical tasks are formed for the slice
- a working operator-facing view exists
- the view reflects real runtime/task state or post-build event updates
- the experiment leaves behind an inspectable evidence package

## Initial live task set
### Task 1 — Formation / execution framing
Suggested task id:
- `TDE-SELF-UI-READINESS-20260326-001`

Title:
- Define and approve bounded slice scope, runtime assumptions, and evidence expectations

Purpose:
- lock the slice scope to the TDE Operator Readiness View
- bind the proving brief, gate assessment, and declared limitation into execution
- prevent scope expansion before runtime evidence exists

Expected output:
- `products/task-management/04-execution/TDE_SELF_UI_READINESS_20260326_001_EXECUTION_FRAMING.md`

### Task 2 — Runtime/data binding definition
Suggested task id:
- `TDE-SELF-UI-READINESS-20260326-002`

Title:
- Define the canonical data/state bindings for the Operator Readiness View

Purpose:
- specify which runtime/task surfaces the UI reads
- specify how state transitions and evidence links are surfaced
- avoid manually populated presentation-only UI behavior

Expected output:
- `products/task-management/04-execution/TDE_SELF_UI_READINESS_20260326_002_BINDING_CONTRACT.md`

### Task 3 — Thin implementation slice
Suggested task id:
- `TDE-SELF-UI-READINESS-20260326-003`

Title:
- Implement the bounded Operator Readiness View thin slice

Purpose:
- create the smallest working operator-facing UI that exposes the proving slice clearly
- show experiment identity, task state, transitions/events, and evidence links

Expected output:
- implementation artifact(s)
- accessible local UI or equivalent rendered proof

### Task 4 — Verification and operated proof
Suggested task id:
- `TDE-SELF-UI-READINESS-20260326-004`

Title:
- Verify the slice against real state change and capture operated proof

Purpose:
- confirm the slice is not only implemented but operated
- show at least one real update/event after implementation
- capture whether manual rescue was required

Expected output:
- verification/evidence artifact
- pass/partial/fail judgment against the proving rubric

## Proposed stage mapping
- Task 1 -> implementation framing
- Task 2 -> implementation/data binding
- Task 3 -> implementation
- Task 4 -> verification / readiness review

## Minimum evidence package for this task set
- objective/intake linkage
- task formation evidence
- implementation artifact(s)
- UI proof (screenshot/access path)
- at least one post-build runtime/update/event proof
- explicit note of any manual rescue
- final pass/partial/fail assessment

## Recommended formation rule
Do not treat this task-set artifact itself as canonical runtime formation.

Instead:
1. create or register the objective record
2. form canonical runtime tasks from that objective
3. execute the slice under the declared experiment limitation
4. assess the result against the proving brief rubric

## Recommended next action
Create the linked objective/intake formation artifact for `OBJ-TDE-SELF-UI-OPERATOR-READINESS-2026-03-26`, then route this task set into canonical runtime formation.
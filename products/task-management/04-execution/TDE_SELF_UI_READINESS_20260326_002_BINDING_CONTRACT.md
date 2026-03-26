# TDE Self-UI Readiness 20260326-002 — Binding Contract

Date: 2026-03-26
Owner: Lyra
Linked objective: `OBJ-TDE-SELF-UI-OPERATOR-READINESS-2026-03-26`
Linked proposed task id: `TDE-SELF-UI-READINESS-20260326-002`
Related execution framing: `products/task-management/04-execution/TDE_SELF_UI_READINESS_20260326_001_EXECUTION_FRAMING.md`
Related experiment brief: `products/task-management/04-execution/TDE_SELF_UI_PROVING_EXPERIMENT_BRIEF_2026-03-26.md`
Related gate assessment: `products/task-management/04-execution/TDE_SELF_UI_RUNTIME_CLOSURE_GATE_ASSESSMENT_2026-03-26.md`
Related interfaces:
- `products/task-management/06-architecture/INTERFACES.md`
- `products/task-management/06-architecture/TDE_INTAKE_INTERFACE_CONTRACT_V1.md`
- `products/task-management/06-architecture/TDE_ASSIGNMENT_ACCEPTANCE_CONTRACT_V1.md`

## Purpose
Define the canonical data/state bindings for the **TDE Operator Readiness View** so the thin slice reads from real Task Management/TDE surfaces rather than a presentation-only mock state.

## Binding rule
The Operator Readiness View must bind to named canonical or governed-readable surfaces.

It must not rely on:
- chat transcript reconstruction
- manually maintained duplicate UI-only state
- hidden local assumptions not declared in this contract

## View sections and bindings

### 1. Experiment identity and governing artifacts
The view should show:
- experiment title
- objective id
- proving brief link
- gate result
- declared limitation

Canonical binding sources:
- `control/tde-intake/tde-self-ui-proving-experiment-2026-03-26.json`
- `control/tde-intake/tde-self-ui-operator-readiness-objective-2026-03-26.json`
- `products/task-management/04-execution/TDE_SELF_UI_PROVING_EXPERIMENT_BRIEF_2026-03-26.md`
- `products/task-management/04-execution/TDE_SELF_UI_RUNTIME_CLOSURE_GATE_ASSESSMENT_2026-03-26.md`

### 2. Objective and formation status
The view should show:
- objective id
- formation id
- workflow family
- recommended next action
- proposed/formed task ids

Canonical binding sources:
- `os/runtime/tde-self-ui-operator-readiness-formation.json`
- `os/runtime/tde-self-ui-operator-readiness-result.json`
- `os/runtime/tde_objectives.json`

### 3. Canonical task/runtime visibility
The view should show:
- whether the experiment tasks are present in canonical runtime state
- current task state/status where available
- readable projection of relevant task entries

Primary canonical source:
- `os/runtime/tde_state.sqlite`

Governed readable projection for the thin slice:
- `os/runtime/TASKS_from_db.md`

Current thin-slice rule:
- until the experiment tasks are actually formed into DB-backed runtime state, the view may show them as **registered but not yet runtime-formed** using the formation/result artifacts above
- once runtime formation occurs, the canonical source of task state becomes the DB-backed runtime path and its readable projection

### 4. Assignment / acceptance visibility
The view should show, where relevant:
- whether assignment acceptance is part of the active flow
- the governing acceptance-state vocabulary
- any visible acceptance/result evidence associated with the slice

Canonical binding sources for semantics:
- `products/task-management/06-architecture/TDE_ASSIGNMENT_ACCEPTANCE_CONTRACT_V1.md`
- `products/task-management/04-execution/TDE_ASSIGNMENT_ACCEPTANCE_TEST_EVIDENCE_2026-03-16.md`

Thin-slice rule:
- in the first version, the view may bind to acceptance semantics and evidence artifacts even if the experiment does not yet produce a fresh assignment packet/result of its own
- if a fresh assignment/result path is later exercised, that evidence should be added as a live bound surface

### 5. Runtime/update/event evidence
The view should show:
- current stage of the experiment
- latest execution artifact(s)
- the next expected move
- any post-build runtime/update/event proof once implementation exists

Canonical binding sources for current execution stage:
- `products/task-management/04-execution/TDE_SELF_UI_READINESS_20260326_001_EXECUTION_FRAMING.md`
- this artifact
- later execution artifacts for `...003` and `...004`

Thin-slice rule:
- execution artifacts are acceptable as governed evidence surfaces for the proving slice as long as they remain explicitly linked to canonical objective/task formation
- they are not a substitute for runtime state, but they are part of the evidence chain the UI should expose

### 6. Readiness / cutover posture
The view should show:
- current gate judgment
- current readiness posture
- whether the slice is running in bounded pilot mode

Canonical binding sources:
- `products/task-management/04-execution/TDE_SELF_UI_RUNTIME_CLOSURE_GATE_ASSESSMENT_2026-03-26.md`
- `products/task-management/05-performance/READINESS_SCORECARD.md`
- `products/task-management/04-execution/PLAN.md`
- `products/task-management/04-execution/RISKS.md`

### 7. Manual rescue disclosure
The view should show:
- whether manual rescue was required
- where that rescue is recorded
- whether it affects pass/partial/fail judgment

Binding rule:
- any manual rescue must be recorded in the experiment execution/verification artifacts
- the UI should surface the presence/absence of manual rescue as an explicit field, not leave it implicit

## Data-state interpretation rules
1. **Canonical beats descriptive**
   - if DB-backed runtime state conflicts with narrative documents, treat DB-backed runtime state as authoritative for task status
2. **Formation beats assumption**
   - if the objective/formation artifacts show the slice is registered but runtime tasks are not yet present, show that honestly rather than implying active execution
3. **Evidence beats appearance**
   - the UI should privilege evidence links and latest verified artifacts over optimistic presentation state
4. **Declared limitation stays visible**
   - the gate-assessment limitation must remain visible in the view until the broader closure chain is proven stronger

## Minimum data contract for the first thin implementation
At minimum, the first working view should be able to render:
- experiment title
- objective id
- gate result
- declared limitation
- formation id
- proposed task ids
- runtime formation status (`registered_not_yet_runtime_formed` | `runtime_formed`)
- latest execution artifact links
- manual rescue status (`none_recorded` | `recorded` | `unknown`)

## Outcome
This artifact defines the canonical binding contract for `TDE-SELF-UI-READINESS-20260326-002` and authorizes movement into the next step: implementing the bounded Operator Readiness View thin slice.

## Recommended next action
Proceed to:
- `TDE-SELF-UI-READINESS-20260326-003` — implement the bounded Operator Readiness View thin slice using the bindings defined here.
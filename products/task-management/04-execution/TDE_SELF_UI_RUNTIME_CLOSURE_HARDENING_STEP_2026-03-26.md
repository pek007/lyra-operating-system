# TDE Self-UI Runtime-Closure Hardening Step

Status: Draft active
Date: 2026-03-26
Owner: Task Management Product / Lyra
Related experiment brief: `products/task-management/04-execution/TDE_SELF_UI_PROVING_EXPERIMENT_BRIEF_2026-03-26.md`
Related intake: `control/tde-intake/tde-self-ui-proving-experiment-2026-03-26.json`

## Purpose
Define the one bounded hardening step that should be completed before launching the TDE self-UI proving experiment.

The goal is not broad redesign. The goal is to remove the main source of ambiguity that would otherwise weaken the experiment: incomplete or insufficiently inspectable runtime closure from experiment intake to canonical task/runtime state to operated evidence.

## Hardening objective
Make the producer/adapter -> runtime -> evidence chain explicit enough that the proving experiment can be judged on actual system behavior rather than manual reconstruction.

## Scope of this hardening step
In scope:
- identify and document the canonical entry path for the experiment objective
- identify the canonical runtime/task truth surface for the experiment slice
- identify the producer/adapter path that converts the experiment objective into executable work
- identify the minimum evidence chain required to prove runtime closure
- declare the bounded operating mode and DB/readiness posture for the experiment

Out of scope:
- full runtime redesign
- broad interface expansion
- full TDE UI design or implementation
- generalized observability overhaul

## Required outputs
This hardening step should produce a compact, inspectable closure package containing at least:
1. **Entry-path statement**
   - where the experiment enters
   - which artifact is authoritative
   - which owner/product scope governs it
2. **Canonical-state statement**
   - where task/runtime truth lives for the experiment
   - which projection is used for inspection
   - which surfaces are explicitly non-authoritative
3. **Producer/adapter statement**
   - what transforms intake into executable work
   - what writes or updates canonical state
   - what evidence markers show those transitions occurred
4. **Operating-mode statement**
   - bounded pilot-operational mode
   - what manual intervention is allowed
   - what must be logged if manual rescue occurs
5. **DB/readiness posture statement**
   - explicit GO/NO-GO-or-bounded-pilot posture for this experiment
   - evidence basis for that posture

## Pass/fail gate for this hardening step
### PASS
This hardening step passes only if a reviewer can answer all of the following without relying on tribal knowledge:
- Where does the TDE self-UI experiment objective enter?
- What is the canonical runtime/task truth for the experiment?
- What producer/adapter path converts intake into executable work?
- What evidence would prove that execution actually happened?
- Under what bounded readiness posture is the experiment allowed to run?

### PARTIAL PASS
- Most of the chain is explicit
- but one material step still depends on operator interpretation or undocumented glue
- and that dependency is honestly declared as an experiment limitation

### FAIL
- canonical state remains ambiguous
- producer/adapter closure is still mostly narrative
- readiness posture is still implicit
- or runtime evidence requirements remain too vague to test honestly

## Why this is the right next move
Current Task Management evidence suggests the dominant remaining bottleneck is not lack of product framing or substrate design, but incomplete closure of the producer/adapter runtime path and the DB-cutover decision chain. This hardening step directly addresses that bottleneck while staying narrow enough to avoid slipping into another broad design phase.

## Evidence anchors
- `products/task-management/04-execution/TOP_PRIORITIES.md`
- `products/task-management/04-execution/PLAN.md`
- `products/task-management/04-execution/RISKS.md`
- `products/task-management/05-performance/READINESS_SCORECARD.md`
- `products/task-management/06-architecture/PXS_CONSUMPTION_INTERFACE.md`
- `products/task-management/04-execution/TDE_ASSIGNMENT_ACCEPTANCE_TEST_EVIDENCE_2026-03-16.md`
- `os/runtime/TASKS_from_db.md`

## Current assessment linkage
Current gate assessment:
- `products/task-management/04-execution/TDE_SELF_UI_RUNTIME_CLOSURE_GATE_ASSESSMENT_2026-03-26.md`

## Recommended immediate next action after PASS
If this hardening step passes:
- instantiate the first live experiment task set
- keep the scope to the TDE Operator Readiness View
- require the experiment evidence package defined in the proving brief

## Recommended immediate next action after FAIL or PARTIAL PASS
If this hardening step does not fully pass:
- do not claim full end-to-end closure
- either convert the missing closure point into the next explicit Task Management runtime-path work item or proceed only in bounded pilot mode with the limitation explicitly declared
- rerun the gate after the closure point is materially improved

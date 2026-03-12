# Intent-to-Task Maturity Model v1

Status: Draft active
Owner: Peter / Lyra
Date: 2026-03-12
Related artifacts:
- `INTENT_TDE_DELIVERY_OPERATIONS_MODEL_V1.md`
- `OBJECTIVE_START_GATE_V1.md`
- `knowledge/reports/2026-03-12__deepresearch__best-practices-for-an-intent-to-execution-service-feeding-lyra-openclaw-tde__v1.md`

## Purpose
Define a progressive maturity path for building an Intent-to-Task capability.

The goal is to avoid two opposite mistakes:
1. building a naive linear breakdown flow that later has to be replaced, or
2. overengineering a highly advanced recursive planning system before the fundamentals are working.

This model provides a way to start simple while still aligning with stronger best practices from the beginning.

## Core principle
Start with the **right primitives**, even if the first implementation is simple.

Simple is acceptable.
Simplistic is not.

## End-state direction
The end-state is an Intent-to-Task capability that:
- supports iterative shaping upstream,
- keeps artifact types distinct,
- preserves traceability,
- compiles bounded execution bundles for runtime,
- and learns from execution outcomes.

## Maturity Level 1 — Structurally correct linear baseline
### Objective
Create a minimal but disciplined artifact chain from intent to task bundle.

### Required artifact types
At this level, the system should distinguish at least:
- Vision
- Goal
- Design
- Plan
- Task Bundle

### Minimum required content
#### Vision
- purpose / why
- target outcome
- non-goals
- value proposition

#### Goal
- measurable target
- time horizon
- owner
- success criteria

#### Design
- problem statement
- scope and non-goals
- functional design
- data / information architecture
- use cases / user flows
- constraints / assumptions
- risks
- verification idea

#### Plan
- work breakdown
- dependencies
- sequencing
- decision points
- evidence expectations

#### Task Bundle
- bounded tasks
- dependencies
- assignees
- approvals if relevant
- evidence requirements
- done conditions

### Minimum quality rules
- every downstream artifact links upstream,
- every design has scope and non-goals,
- every plan has dependencies,
- every task has evidence requirements and done condition,
- no task bundle enters TDE without explicit boundedness.

### Why this level matters
This level prevents sloppy breakdown and gives the system a stable spine.
It is still relatively linear, but it is structurally correct enough to evolve.

## Maturity Level 2 — Disciplined decomposition
### Objective
Improve how goals and designs are decomposed without yet requiring advanced recursive planning.

### New capabilities
- decomposition rules beyond “break it down however you want”,
- first-slice thinking,
- use-case-driven breakdown,
- goal-to-plan decomposition discipline,
- explicit decision-point identification,
- split/merge rules for plans that become too large or unclear.

### Typical methods introduced
- simple goal trees,
- OKR-like goal structure,
- user journey / user story map thinking,
- explicit decomposition heuristics.

### Additional quality rules
- plans should be decomposable without ambiguity,
- tasks should align to use cases or verification needs,
- verification tasks should be derived explicitly from goal/design claims.

### Why this level matters
This is where the system becomes meaningfully better than a plain waterfall checklist.
It adds discipline without requiring heavy recursion or advanced orchestration.

## Maturity Level 3 — Iterative convergence loops
### Objective
Make intent shaping explicitly iterative rather than implicitly linear.

### New capabilities
- review design back against goal,
- review goal back against vision,
- review plan back against design,
- trigger reframing when misalignment appears,
- create discovery/prototype tasks when uncertainty is high,
- allow multiple intent/design iterations before execution handoff.

### Example loop types
- clarify loop,
- decompose loop,
- validate loop,
- reframe loop.

### Key operating rule
The output of shaping is not “final truth.”
It is the **current best converged packet** that is good enough to enter bounded execution.

### Why this level matters
This is the first level where the system clearly outgrows waterfall behavior and starts to reflect real planning/design work.

## Maturity Level 4 — Bounded compile / submit / observe integration
### Objective
Separate upstream iterative shaping from downstream bounded execution.

### New capabilities
- compile shaped intent into bounded execution bundles,
- submit those bundles into TDE runtime,
- observe execution outputs back into the shaping system,
- preserve traceability across compile -> submit -> observe.

### New interface expectations
#### Compile
Convert vision/goal/design/plan into:
- execution-ready task bundle,
- explicit metadata,
- bounded chain family,
- evidence requirements,
- provenance links.

#### Submit
Push bounded bundle into TDE under runtime contracts.

#### Observe
Capture back:
- tick/status outputs,
- evidence,
- failures,
- approvals,
- execution metrics,
- rework signals.

### Quality rules
- no runtime fan-out unless explicitly allowed,
- compiled bundles must pass validation,
- runtime receives bounded execution packages rather than open-ended planning prompts.

### Why this level matters
This is the key maturity boundary where the system becomes architecturally robust:
recursive planning is upstream; deterministic execution is downstream.

## Maturity Level 5 — Advanced planning intelligence and governance
### Objective
Add more sophisticated planning intelligence, safety controls, and measurement once the core flow is already working.

### New capabilities
- hybrid HTN / goal-graph / use-case decomposition,
- guarded agentic proposal generation,
- deterministic validation gates,
- stronger provenance/canonicalization,
- risk-based planning and policy controls,
- planning-quality metrics,
- richer feedback-driven replanning.

### Typical advanced controls
- boundedness validators,
- safety/policy validators,
- traceability completeness checks,
- deeper provenance models,
- execution-to-planning feedback metrics,
- advanced evaluation of decomposition quality.

### Why this level matters
This is where the system becomes “best-practice aware” in a more advanced sense.
But it only works well if the earlier levels are already stable.

## Recommended build order
### Build now
- Level 1 fully
- selective parts of Level 2

### Add next
- Level 3 convergence loops
- the first parts of Level 4 compile/submit/observe

### Add later
- Level 5 advanced planning intelligence and governance controls

## Best-practice reminders to adopt from day one
Even at Level 1, carry these lessons from the research:

1. **Keep artifact types distinct**
   - vision != goal != design != plan != task

2. **Do not skip design**
   - and do not allow design to omit scope, non-goals, functional shape, data/information shape, use cases, risks, and verification thinking.

3. **Make evidence explicit early**
   - not as a release-stage afterthought.

4. **Preserve traceability**
   - every task should be explainable upstream.

5. **Preserve boundedness**
   - execution packages should not be open-ended.

6. **Allow refinement upstream**
   - even if the first implementation still looks fairly linear.

## Anti-patterns to avoid
- flat direct jump from vision to tasks,
- treating every statement as actionable work,
- writing designs that are mostly narrative and omit architecture/use-case substance,
- allowing tasks without evidence or done conditions,
- mixing runtime execution with open-ended planning logic,
- introducing recursive complexity before basic artifact hygiene exists.

## What this means for current Lyra OS work
This maturity model suggests:
- the first implementation should not try to do everything,
- but it should already be shaped so that iterative convergence, bounded compilation, and stronger validation can be added later without replacing the whole model.

## Current recommendation
Use this model as the guide for sequencing design and build choices.

Short rule:
**Start simple, but start with the right primitives so sophistication can be added without redesigning the whole system.**

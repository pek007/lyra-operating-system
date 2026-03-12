# Intent-to-Task Level 1 Artifact Pack v1

Status: Draft active
Owner: Peter / Lyra
Date: 2026-03-12
Related artifacts:
- `INTENT_TO_TASK_MATURITY_MODEL_V1.md`
- `INTENT_TO_TASK_MATURITY_ASSESSMENT_2026-03-12.md`
- `OBJECTIVE_START_GATE_V1.md`
- `knowledge/reports/2026-03-12__deepresearch__best-practices-for-an-intent-to-execution-service-feeding-lyra-openclaw-tde__v1.md`

## Purpose
Define the canonical Level 1 artifact pack for the Intent-to-Task capability.

This artifact is meant to close the biggest current Level 1 gap:
we have a promising architecture frame, but not yet a fully defined canonical artifact family for upstream shaping into execution-ready work.

## Level 1 design goal
Provide a simple but structurally correct artifact chain that can:
- represent upstream intent clearly,
- prevent category confusion,
- preserve traceability,
- and produce bounded execution-ready task bundles.

This Level 1 pack is intentionally simple.
It is not yet the full recursive/compiler-style system.
But it must be strong enough that later maturity can extend it without replacing it.

## Canonical Level 1 artifact family
The Level 1 artifact pack contains five canonical artifact types:
1. Vision
2. Goal
3. Design
4. Plan
5. Task Bundle

## Artifact 1 — Vision
### Purpose
Capture the durable “why” and the intended value/outcome direction.

### Vision is for
- long-lived purpose,
- value proposition,
- target outcome direction,
- explicit non-goals,
- constraints that should remain stable across many goals/plans.

### Vision must contain
- Vision ID
- Title
- Purpose / why
- Target outcome
- Value proposition
- Target user/operator/customer
- Explicit non-goals
- Durable constraints
- Qualitative success definition
- Owner
- Last review date

### Vision must not be
- directly executable,
- a task list,
- a detailed implementation plan.

## Artifact 2 — Goal
### Purpose
Translate vision or intent into a bounded measurable target.

### Goal is for
- a clear outcome target,
- measurable success,
- a time horizon,
- a named owner,
- a bounded scope of ambition.

### Goal must contain
- Goal ID
- Linked Vision ID (or explicit source intent if no formal Vision exists)
- Title
- Objective statement
- Time horizon
- Owner
- Success criteria / measurable target(s)
- Scope statement
- Key assumptions
- Main risks
- Status

### Goal must not be
- a design,
- a plan,
- a direct task list.

## Artifact 3 — Design
### Purpose
Describe the intended solution shape and constraints before execution planning.

### Design is for
- problem framing,
- solution structure,
- architecture choices,
- assumptions/constraints,
- use cases,
- verification thinking.

### Minimum Design standard
Every Design must contain at least:
- Design ID
- Linked Goal ID
- Title
- Problem statement
- Scope and non-goals
- Functional design
- Data / information architecture
- Interfaces / integration considerations
- Use cases / user flows
- Constraints and assumptions
- Risks and trade-offs
- Verification approach
- Owner
- Status

### Design must not be
- only a narrative idea note,
- only a UI concept,
- only a list of tasks.

### Critical rule
A Design that omits functional design, data/information architecture, or use cases is incomplete for Level 1.

## Artifact 4 — Plan
### Purpose
Translate a Design into a bounded route to execution.

### Plan is for
- work breakdown,
- sequencing,
- dependencies,
- decision points,
- evidence expectations,
- execution boundaries.

### Plan must contain
- Plan ID
- Linked Goal ID
- Linked Design ID
- Title
- Work breakdown
- Dependencies
- Sequencing / stage order
- Major decision points
- Evidence expectations
- Boundedness statement
- Owner
- Status

### Plan must not be
- a loose brainstorm,
- a direct execution log,
- a substitute for design.

## Artifact 5 — Task Bundle
### Purpose
Provide the bounded set of execution-ready tasks that can enter TDE/runtime.

### Task Bundle is for
- executable work units,
- dependencies,
- assignees,
- evidence requirements,
- approval boundaries,
- done conditions.

### Task Bundle must contain
- Task Bundle ID
- Linked Goal ID
- Linked Design ID
- Linked Plan ID
- Boundedness declaration
- Task list

Each Task in the bundle must contain at least:
- Task ID
- Title
- Purpose
- Assignee / owner
- Dependency list
- Activation condition if relevant
- Evidence required
- Done condition
- Approval requirement if relevant
- Risk level if relevant

### Task Bundle must not be
- open-ended,
- missing evidence expectations,
- detached from upstream Goal/Design/Plan artifacts.

## Upstream-to-downstream traceability rule
At Level 1, every artifact must trace upstream:
- Goal -> Vision
- Design -> Goal
- Plan -> Goal + Design
- Task Bundle -> Goal + Design + Plan
- Task -> Task Bundle + upstream chain by inheritance/reference

If an artifact cannot be explained by its upstream link, it should not be treated as canonical.

## Minimum status model
A simple Level 1 status approach is sufficient.

### Vision
- active
- retired

### Goal
- proposed
- active
- achieved
- retired

### Design
- draft
- active
- superseded
- retired

### Plan
- draft
- active
- superseded
- retired

### Task Bundle
- draft
- ready-for-execution
- in-execution
- completed
- retired

## Minimum Level 1 quality checks
Before a Task Bundle is considered ready-for-execution, confirm:
1. A linked Goal exists.
2. A linked Design exists.
3. A linked Plan exists.
4. The Design includes scope/non-goals, functional design, data/information architecture, use cases, risks, and verification approach.
5. The Plan includes dependencies, sequencing, decision points, evidence expectations, and boundedness.
6. Every task has assignee, dependencies (or explicit none), evidence required, and done condition.
7. The bundle is bounded enough to enter execution safely.

## Relationship to the Objective Packet
The existing Objective Packet remains useful as an intake/gating artifact.

Current recommendation:
- treat the Objective Packet as an intake/start-gate artifact,
- not as a replacement for the full Level 1 artifact family.

In practice, the Objective Packet can help bridge from loose intent into:
- Goal,
- Design,
- Plan,
- and eventually Task Bundle.

## Anti-patterns this pack is designed to prevent
- jumping from loose objective directly into tasks,
- writing design artifacts that are mostly prose and omit architecture/use-case substance,
- treating plans as design substitutes,
- allowing execution-ready tasks without evidence expectations,
- losing traceability from execution back to upstream purpose.

## Current recommendation
Adopt this artifact pack as the Level 1 baseline for the Intent-to-Task capability.

Short rule:
**Vision explains why. Goal states what. Design explains how in principle. Plan explains how in sequence. Task Bundle defines what can actually enter execution.**

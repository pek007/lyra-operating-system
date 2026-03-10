# MEMORY_IMPLEMENTATION_ROADMAP_V1.md

Status: Active draft v1  
Owner: Lyra via Control Panel  
Date: 2026-03-10

## Purpose
Turn `MEMORY_PROCESS_V1.md` into an executable implementation sequence with clear phases, deliverables, and success signals.

## Strategic intent
Build memory as a managed operating capability for Lyra OS.

This roadmap covers five layers:
- agent memory
- session memory
- job memory
- knowledge memory
- coordination memory

## Operating principle
Prioritize reliability and activation over theoretical sophistication.

The goal is not to store more. The goal is to ensure that the right context:
- is captured,
- lives in the right canonical store,
- is activated at the right time,
- is retrievable when needed,
- remains scoped and auditable.

## Phase 1 — Stabilize the current memory baseline

### Objective
Make the current memory stack actually reliable before expanding scope.

### Focus
- confirm live retrieval behavior
- clarify active memory surfaces
- align major artifacts with the new scope model
- remove ambiguity around terminology and ownership

### Work items
1. Validate live `memory_search` behavior and identify why current recall is weak/non-functional in this runtime.
2. Confirm which memory/index plugin path is actually active in live runtime.
3. Define the first activation-class map for priority memory-bearing artifacts.
4. Classify current major memory-bearing artifacts by scope:
   - agent
   - session
   - job
   - knowledge
   - coordination
5. Clean up live `Control Tower` terminology where the new product model requires `Control Panel`.

### Deliverables
- retrieval status diagnosis
- initial activation map
- terminology cleanup plan
- updated process/task references

### Success signals
- known answer to “is retrieval working, and on what corpus?”
- no ambiguity about who owns memory capability governance
- first activation map published and usable

## Phase 2 — Make job memory first-class and portable

### Objective
Ensure responsibilities can move without relying on session carry-over.

### Focus
- job bundles
- explicit write-back at job boundaries
- deterministic job activation

### Work items
1. Enforce the job memory bundle standard for active durable jobs:
   - `JOB.md`
   - `STATE.md`
   - `MEMORY.md`
   - `HANDOVER.md`
2. Define minimum required update points:
   - reassignment
   - pause
   - completion
   - major decision/blocker
3. Define job activation behavior:
   - explicit-load of `STATE.md`
   - optional retrieval over job memory bundle
4. Add lightweight checks for missing/incomplete job memory bundles.

### Deliverables
- job-memory operating standard
- activation rule for job start/switch
- first compliance check or review cadence

### Success signals
- jobs can be picked up by another context with materially lower continuity loss
- session history is no longer implicitly carrying job state

## Phase 3 — Extend retrieval from memory files to knowledge assets

### Objective
Make the knowledge library operational at runtime rather than archival-only.

### Focus
- high-signal retrieval corpora
- scope boundaries
- selective activation

### Work items
1. Define the first retrieval-indexed knowledge set:
   - curated memory
   - job bundles
   - `knowledge/distilled/`
   - `knowledge/decisions/`
   - selected approved runbooks/processes
2. Keep lower-signal corpora lower priority or excluded by default:
   - raw reports
   - inboxes
   - noisy evidence feeds
3. Define bridge rules for any shared/cross-namespace retrieval.
4. Add provenance expectations for memory-backed answers.

### Deliverables
- retrieval-scope policy v1
- initial indexed-corpus decision
- bridge-rule shortlist

### Success signals
- library research can materially help runtime answers
- retrieval recall improves without broad context pollution

## Phase 4 — Establish coordination memory

### Objective
Provide cross-context awareness without collapsing isolated contexts into one shared prompt space.

### Focus
- current activity awareness
- blockers and dependencies
- shared operational visibility

### Work items
1. Define the canonical coordination source:
   - structured event log and/or projected status state
2. Avoid using a free-form shared markdown file as source of truth.
3. Generate a human-readable coordination view from canonical state.
4. Define read/write rules:
   - what gets posted
   - when it expires
   - who consumes it
5. Connect coordination memory to situational awareness and job state where appropriate.

### Deliverables
- coordination-memory design note
- canonical-source decision
- first generated coordination view

### Success signals
- lower duplicate work risk
- clearer visibility into current activity across isolated sessions/jobs
- no uncontrolled shared-state sprawl

## Phase 5 — Evaluate and tune memory quality

### Objective
Treat memory as an engineering system with measurable quality, not folklore.

### Focus
- evaluation
- failure analysis
- quality metrics
- cost discipline

### Work items
1. Define a memory-critical prompt set covering:
   - preference recall
   - prior decision recall
   - policy recall
   - job continuity recall
   - scope isolation
2. Track quality dimensions:
   - retrieval usefulness
   - grounding/faithfulness
   - leakage incidents
   - continuity failures
   - write-back reliability
   - context cost
3. Review misses and false recalls as first-class operating defects.
4. Tune activation/retrieval policy based on evidence.

### Deliverables
- memory quality review checklist
- first baseline memory-quality report
- prioritized improvement backlog

### Success signals
- memory changes are testable and comparable
- regressions become visible early

## Phase sequencing recommendation
Recommended order:
1. Phase 1
2. Phase 2
3. Phase 3
4. Phase 4
5. Phase 5

Rationale:
- fix the current seam before broadening scope
- make job continuity real before scaling retrieval breadth
- create shared coordination only after scope and activation discipline exist
- add deeper evaluation once there is a stable baseline to evaluate

## Immediate next actions
1. Execute `OPS-2026-070` as the formal implementation entrypoint.
2. Produce the first activation map for current priority artifacts.
3. Diagnose live retrieval/index behavior.
4. Define the first active-job bundle coverage review.
5. Decide the canonical coordination-memory source pattern.

## Out of scope for this roadmap version
- replacing markdown as canonical memory
- indexing everything in the workspace
- broad automatic memory capture without scope controls
- third-party black-box memory adoption as the primary strategy

## Version
- v1.0
- Date: 2026-03-10

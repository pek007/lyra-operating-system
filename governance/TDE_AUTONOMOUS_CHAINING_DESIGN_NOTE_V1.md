# TDE Autonomous Chaining Design Note v1

Status: Draft
Owner: Lyra
Date: 2026-03-09

## Purpose
Clarify:
1. what TDE already does for continuous unattended work,
2. what is still missing to support sustained movement toward a high-level target,
3. the recommended implementation path from the current design to a stronger autonomous chaining model.

## Executive summary
TDE already supports continuous unattended work, but mainly through a **scheduled pull loop**:
- cron or heartbeat triggers a runtime tick,
- the tick looks for ready work,
- the runtime claims and executes bounded work,
- state is written back,
- later ticks continue from the updated state.

This is enough for ongoing execution when the next work item already exists and is claimable.

TDE does **not yet** appear to implement a general native mechanism where completion of one task directly and deterministically activates or creates the next task toward a higher-level objective.

Recommendation:
- Near term: strengthen **state-driven chaining** on top of the existing scheduler/tick model.
- Later: add **event-driven successor activation/creation** as a controlled higher-order capability.

## Current-state architecture

### What exists today
The current TDE runtime already provides the following core behaviors:

1. **Job tick execution loop**
   - Triggered primarily by cron
   - Heartbeat allowed as a control-plane exception
   - Claims ready work under bounded WIP
   - Executes through deterministic mutation rules
   - Writes back canonical task state

2. **Canonical runtime state**
   - DB-backed canonical state store
   - Human-readable runtime projection available separately
   - Deterministic writeback and parity checks already in place

3. **Anti-stall runtime path**
   - Heartbeat and cron sweeps inspect stale/high-priority work
   - Routed follow-up actions include `resume`, `escalate`, `redefine`, `retire`
   - Approval-gated actions remain fail-closed

4. **Fail-closed governance controls**
   - Binding validation
   - Objective linkage validation
   - Policy gating for approval-requiring routes
   - Idempotent tick execution

## Current continuity mechanism
The current mechanism for continuous work is primarily:

**scheduled tick -> inspect ready work -> claim -> execute -> write back -> next tick continues**

This is a valid autonomous work loop, but it is **pull-based** rather than **completion-event push-based**.

## What this already enables
TDE can already support continuous progress toward a larger target when:
- the work has been decomposed into multiple tasks or stages,
- those tasks already exist in TDE,
- state transitions make later work ready,
- scheduled ticks keep pulling the next ready item.

This means TDE is already able to sustain unattended execution across a chain of work **if the chain is pre-structured or otherwise made ready over time**.

## Current gap
The missing capability is a native, general mechanism for:

**task completion -> successor activation or successor creation -> immediate or next-tick continuation**

That gap matters because high-level autonomous execution becomes much stronger when the system can do more than merely re-scan for existing ready work.

Without that mechanism, TDE relies on one of two weaker patterns:
1. all downstream tasks were created ahead of time, or
2. some separate process manually or semi-manually creates follow-up tasks.

## Mechanism options

### Option A — State-driven chaining
Model the workflow so that downstream tasks already exist but are initially inactive / non-ready.
Completion of one task changes the state of the next task or stage to ready.
The next scheduled tick then picks it up.

#### Advantages
- Fits today’s TDE design naturally
- Preserves determinism and auditability
- Lower implementation risk
- Easier rollback and debugging
- Works well with bounded WIP and fail-closed policy checks

#### Drawbacks
- Requires more up-front task graph definition
- Less flexible when the next step depends on fresh runtime interpretation
- Still depends on polling cadence rather than immediate event reaction

### Option B — Successor creation on completion
When a task completes, TDE applies a rule/template/objective mapping to generate one or more follow-up tasks automatically.
Those tasks are inserted into canonical state and become claimable.

#### Advantages
- More expressive
- Better fit for adaptive, high-level objective pursuit
- Reduces need to predefine every downstream task

#### Drawbacks
- Higher governance and quality risk
- More complexity around duplication, loops, and task explosion
- Harder to validate deterministically
- Requires stronger safeguards for authority, scope, and quality of generated successors

### Option C — Direct dispatch trigger
When a task completes, TDE immediately dispatches the next successor execution path rather than waiting for the next scheduler tick.

#### Advantages
- Lowest latency
- Strongest “flow” behavior

#### Drawbacks
- Highest operational complexity
- Increased risk of runaway chains
- Harder to preserve bounded execution and clean audit boundaries
- Less aligned with current scheduler-governed architecture

## Recommended implementation path

### Phase 1 — Standardize state-driven chaining (recommended now)
This should be the default next step.

#### Design intent
Use the current scheduler/job-tick model, but make chained work first-class by introducing explicit successor-readiness semantics.

#### Proposed additions
1. **Task dependency / predecessor metadata**
   - Add optional metadata fields such as:
     - `depends_on`
     - `unblocks`
     - `activation_rule`
     - `objective_id`
     - `stage_id`

2. **Ready-state evaluation rule**
   - A task becomes ready only when:
     - all required predecessors are complete,
     - required approvals are satisfied,
     - objective linkage is valid,
     - activation guard passes.

3. **Tick-time activation check**
   - At the start or end of a job tick, evaluate blocked/inactive tasks whose predecessors changed.
   - Promote newly-eligible tasks to ready state deterministically.

4. **Bounded chain progression**
   - Keep `max_claim` / WIP bounds in force.
   - Even if several tasks become ready, only claim up to policy cap.

5. **Evidence artifact for chain activation**
   - Emit activation evidence showing:
     - predecessor completed
     - successor now eligible
     - activation reason
     - any approval gate still pending

#### Why Phase 1 first
This would deliver most of the practical value Peter wants while staying compatible with the current TDE architecture.
It gives continuous progress toward higher-level goals without needing a fragile always-on event bus.

### Phase 2 — Controlled successor generation
After Phase 1 is stable, add limited automatic successor creation for approved workflow families.

#### Constraints
- Only for explicitly approved workflow templates
- Hard cap on generated successors per completion event
- Mandatory idempotency and duplication checks
- Objective linkage required
- Fail closed on ambiguous generation

#### Good initial use cases
- verification follow-up after implementation completion
- deployment-readiness follow-up after verification completion
- review/closeout task creation after rollout completion
- recurring improvement loop tasks based on evidence thresholds

### Phase 3 — Optional direct dispatch for narrow cases
Only consider direct dispatch after the above two phases are proven reliable.
This should be limited to narrow, low-risk, well-instrumented workflow classes.

## What mechanisms we are using today
At present, the mechanisms actually in use are:

1. **Scheduled cron-driven job tick execution** — primary mechanism
2. **Heartbeat-triggered control-plane exception path** — secondary mechanism
3. **Anti-stall sweep** — continuity/recovery mechanism
4. **Canonical state writeback** — persistence mechanism

What we are **not yet** using as a general mechanism:
- completion-event-driven successor activation across a dependency graph
- generic automatic successor creation
- immediate direct dispatch on completion

## Recommended product/operating stance right now
Until stronger chaining is added, Product Owners should operate TDE as follows:
- define higher-level goals explicitly,
- decompose work into staged tasks ahead of time where possible,
- ensure likely successor tasks already exist or can be deterministically promoted,
- rely on scheduled job ticks to continue pulling next ready work,
- use anti-stall to catch chains that lose momentum,
- avoid relying on chat or memory to decide what should happen next.

## Decision recommendation
Recommend the following decision sequence:

1. **Adopt Phase 1 as the next TDE capability target**
   - Explicit state-driven chaining
   - Dependency-aware readiness promotion
   - No generic autonomous task generation yet

2. **Treat heartbeat as support, not the primary chaining mechanism**
   - Heartbeat is useful for awareness and anti-stall
   - Cron/job-tick should remain the main continuous execution engine

3. **Delay direct-trigger dispatch until bounded state-driven chaining is proven**
   - safer
   - easier to audit
   - closer to current architecture

## Bottom line
TDE already has the foundations for continuous unattended work.
The current model is strong enough for pull-based chained execution when downstream tasks already exist or can be made ready deterministically.

The next meaningful step is not a general event bus.
The next meaningful step is to make **dependency-aware state-driven chaining** an explicit first-class runtime behavior.

That would move TDE much closer to the intended outcome: sustained autonomous progress from high-level targets with minimal human intervention, while preserving boundedness, traceability, and fail-closed governance.

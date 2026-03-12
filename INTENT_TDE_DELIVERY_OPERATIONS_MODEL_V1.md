# Intent + TDE + Delivery + Operations Model v1

Status: Draft active
Owner: Peter / Lyra
Date: 2026-03-12
Related artifacts:
- `OBJECTIVE_TO_PRODUCTION_GAP_MAP_V1.md`
- `OBJECTIVE_START_GATE_V1.md`
- `TDE_ASSIGNED_WORK_WAKEUP_MODEL_V1.md`
- `products/delivery/06-architecture/DELIVERY_AS_CODE_DESIGN_V1.md`

## Purpose
Define the broader end-to-end operating model for Lyra OS beyond the narrow label of “Delivery.”

The aim is to describe how the system should work from:
- idea / intent,
through
- shaping / design / planning,
into
- execution / release,
and onward into
- in-use operations / learning / adaptation.

This artifact also clarifies a key architectural judgment:
**vision-to-task breakdown should be treated as a separable capability, not only as an internal TDE subroutine.**

## Core thesis
Lyra OS should not be modeled as one monolithic flow engine.
It should be modeled as a set of connected but separable capabilities with explicit interfaces.

The most useful current separation is:
1. **Intent Shaping**
2. **TDE / Task-Decision Execution**
3. **Delivery / Release Governance**
4. **Operations / In-Use Learning**

## Why this separation matters
This separation preserves flexibility and avoids over-coupling.

It allows:
- intent shaping to be used without full TDE execution,
- TDE to manage already-shaped work without requiring full strategy decomposition every time,
- Delivery to govern bounded work once it is execution-ready,
- operations/learning to close the loop after release rather than being treated as an afterthought.

## Capability 1 — Intent Shaping
### Purpose
Convert high-level idea, vision, or strategic intent into a clearer and more actionable shape.

### Typical inputs
- idea
- vision
- strategic concern
- opportunity/problem
- constraints
- desired outcome

### Typical outputs
- goal
- target design
- possible implementation paths
- first-slice candidates
- key decisions
- objective packet or equivalent intake shape

### What it should answer
- Why does this matter?
- What outcome are we actually aiming for?
- What target design appears most sensible?
- What is the first meaningful slice?
- What should be explicitly decided before execution starts?

### Why it is separable
This capability is useful even without entering TDE execution.
It can be used as a standalone shaping service for strategy, design, planning, or concept work.

## Capability 2 — TDE / Task-Decision Execution
### Purpose
Manage the canonical operational state of work, decisions, assignments, dependencies, and collaboration.

### Typical inputs
- objective packet
- target design
- implementation intent
- assigned work items
- dependencies
- decision requests

### Typical outputs
- canonical work state
- assignment/wakeup events
- blockers/dependencies
- decision status
- coordination state
- execution progress

### What it should answer
- What work exists now?
- Who owns or is assigned to what?
- What is blocked?
- What decisions are open?
- What collaboration is active?
- What is the current execution reality?

### Why it is distinct
TDE is the execution coordination substrate.
It should not need to own all upstream shaping logic in order to be useful.
It should also not need to own all downstream release governance in order to coordinate work properly.

## Capability 3 — Delivery / Release Governance
### Purpose
Govern the movement from execution-ready work to accepted, released, and verified outcome.

### Typical inputs
- execution-ready objective/plan
- Delivery Unit or equivalent governed work package
- implementation outputs
- evidence
- approvals and exceptions

### Typical outputs
- qualification result
- delivery plan / DU state
- verification packet
- release recommendation
- approval decision
- in-use verification outcome
- post-delivery review

### What it should answer
- Is this clear enough to enter governed delivery?
- Has the required evidence been produced?
- Is release recommended?
- Is release approved?
- Has the change worked in use?
- What do we retain or improve next?

### Why it is distinct
Delivery is not just task progression.
It is the control layer for gates, evidence, release judgment, and auditability.

## Capability 4 — Operations / In-Use Learning
### Purpose
Track what happens after release/activation and convert live use into learning, follow-up work, and system improvement.

### Typical inputs
- released change
- runtime behavior
- operator experience
- issues/incidents
- post-release verification
- review findings

### Typical outputs
- in-use verification
- improvement opportunities
- incidents/misses
- lessons learned
- new objectives, decisions, or work items

### What it should answer
- Did the change actually work in use?
- What went wrong or better than expected?
- What should be improved or retained?
- What new work should enter the system?

### Why it matters
Without this layer, the system risks ending at “released” rather than running a true closed-loop operating model.

## End-to-end chain
A practical end-to-end chain looks like this:

1. **Idea / intent**
2. **Goal formation**
3. **Target design**
4. **Objective packet / intake shape**
5. **Implementation plan / execution-ready package**
6. **Activities / assigned work**
7. **Execution**
8. **Verification**
9. **Release / handoff / activation**
10. **In-use operation**
11. **Learning / adaptation**

## Ownership by layer
### Primarily Intent Shaping
- idea framing
- vision -> goal conversion
- target design shaping
- first-slice thinking

### Primarily TDE
- canonical work state
- assignment and wakeup
- dependency management
- decision visibility
- cross-product coordination

### Primarily Delivery
- qualification
- planning gate
- verification gate
- release/readiness judgment
- evidence requirements
- rendered delivery outputs

### Primarily Operations / Learning
- in-use validation
- post-release review
- issue capture
- adaptation/improvement loop

## Key interfaces
### Interface A — Intent Shaping -> TDE
This interface should pass:
- objective packet,
- target design,
- first-slice scope,
- initial decision needs,
- participating products/functions.

### Interface B — TDE -> Delivery
This interface should pass:
- execution-ready scope,
- work package / DU candidate,
- dependencies,
- evidence expectations,
- owner/assignee state,
- risk/approval context.

### Interface C — Delivery -> Operations / Learning
This interface should pass:
- release/activation result,
- verification status,
- known risks/exceptions,
- in-use validation expectations,
- review triggers.

### Interface D — Operations / Learning -> Intent Shaping / TDE
This interface should pass:
- new problems/opportunities,
- misses/incidents,
- lessons learned,
- follow-up work,
- improvement objectives.

## Standalone vs integrated use
### Intent Shaping standalone
Valid when:
- the goal is to clarify a concept,
- compare solution directions,
- produce an objective packet,
- or define a target design before entering execution.

### TDE standalone
Valid when:
- work arrives already shaped enough,
- the task is operationally concrete,
- or the system only needs execution coordination.

### Delivery standalone-ish
Valid when:
- a bounded work package is already well formed,
- and the need is governed execution/release rather than upstream shaping.

### Integrated mode
Best when:
- the system must handle the full chain from intent to in-use result with strong traceability and auditability.

## Architectural recommendation
Treat these capabilities as **separable but tightly interfaced services/capabilities**, not as one fused monolith.

A service-oriented analogy is reasonable at the conceptual level, even if the implementation remains lighter-weight for now.

The key is explicit contracts and clean boundaries, not heavy infrastructure.

## What this means for current design work
### For TDE
TDE should not absorb all upstream strategy logic.
It should focus on:
- canonical assigned work,
- decisions,
- collaboration state,
- wakeup/notification,
- execution truth.

### For Intent Shaping
We should likely define a dedicated shaping/intake capability that can output objective packets and target designs without requiring full TDE engagement every time.

### For Delivery
Delivery should define the governed path that begins once work is shaped enough to enter controlled execution and release.

### For operations
We should explicitly plan for in-use verification and follow-up learning rather than treating release as the end.

## Implication for the current pilot
The TDE UI pilot should be treated as a test of the interfaces between these capabilities, not only as a build effort.

It should help us test:
- intent shaping quality,
- TDE execution coordination,
- Delivery governance,
- and post-release learning capture.

## Current recommendation
Use this model as the broader architectural frame for the next phase of design.

Do not force all shaping into TDE.
Do not reduce the whole system to “Delivery.”
Do not end the system boundary at release.

Short rule:
**Intent shapes work. TDE coordinates work. Delivery governs change. Operations validates and teaches the system.**

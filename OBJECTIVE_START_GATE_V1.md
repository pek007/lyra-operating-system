# Objective Start Gate v1

Status: Draft active
Owner: Peter / Lyra
Date: 2026-03-12
Related artifacts:
- `OBJECTIVE_TO_PRODUCTION_GAP_MAP_V1.md`
- `ONE_ITERATION_TDE_UI_PILOT_V1.md`
- `TDE_UI_PILOT_SMALLEST_SLICE_V1.md`
- `products/delivery/04-execution/TDE_UI_PILOT_DELIVERY_CONTRACT_V1.md`

## Purpose
Define the standard conversion step from a high-level objective to an execution-ready objective packet.

This is the first priority control artifact from the Objective-to-Production Gap Map.
Its job is to prevent ambiguity from entering the system too early and to ensure that Delivery does not receive an underspecified objective.

## Core rule
No high-level objective should enter governed execution as an application/product delivery effort until it has passed this start gate.

The output of this gate is an **Objective Packet**.

## Objective Packet — required fields
Every execution-ready objective packet must contain the following fields.

### 1. Objective statement
A concise statement of the high-level outcome to be achieved.

Question:
- What are we trying to accomplish?

### 2. Why now
The reason this objective matters now.

Question:
- Why is this worth doing at this moment?

### 3. Success criteria
Observable conditions that would make the effort count as successful.

Question:
- What would have to be true for us to say this objective was achieved?

### 4. Operator/user problem
The practical user or operator problem the objective is meant to solve first.

Question:
- What real problem is being removed or reduced?

### 5. Smallest acceptable slice
The bounded first slice that should be delivered first.

Question:
- What is the smallest real thing we can ship that still tests the objective meaningfully?

### 6. Explicit non-goals
What the first effort will deliberately not attempt.

Question:
- What are we explicitly refusing to include in the first slice?

### 7. Risks and failure modes
The most important ways the effort could fail or misfire.

Question:
- What are the main ways this could go wrong?

### 8. Decision needs
The decisions that must be made explicitly before or during execution.

Question:
- What cannot be left implicit if we want professional delivery and auditability?

### 9. Evidence expectations
The minimum evidence that should exist before the result can be judged acceptable.

Question:
- What evidence must be present before we can say this is ready?

### 10. Production/release intent
A first pass at what “production” or “in use” means for this effort.

Question:
- What counts as a real deployed outcome rather than a mockup or local experiment?

### 11. Kill criteria / fail conditions
Conditions under which the effort should be stopped, reframed, or declared not yet ready.

Question:
- What would tell us to stop or narrow rather than continue?

### 12. Participating products/functions
Which products or functions need to be involved.

Question:
- Who must participate for this objective to be delivered professionally?

## Start-gate quality checks
An objective packet should not pass the gate unless all of the following are true:

### Check A — boundedness
The first slice is small enough to be imaginable as one governed iteration or similarly bounded run.

### Check B — operator reality
The objective is linked to a real user/operator problem, not just a technology idea.

### Check C — non-goal clarity
There is a visible scope boundary, not just an aspiration.

### Check D — decision visibility
The major decisions that matter early are named.

### Check E — evidence readiness
The packet says what evidence would make the work judgeable.

### Check F — release realism
There is an explicit idea of what counts as “real use” or “production.”

### Check G — ownership clarity
The participating products/functions are named clearly enough to allow handoff and acceptance.

## Gate result states
Use one of these states:
- `not-started`
- `needs-clarification`
- `ready-for-governed-execution`
- `reframe-required`

## Role split

### Task Management / TDE responsibility
- drive the conversion from high-level objective to objective packet,
- surface missing fields and ambiguities,
- ensure decisions and scope boundaries become explicit.

### Delivery responsibility
- confirm whether the packet is strong enough to enter governed delivery,
- refuse packets that are too vague to support professional execution,
- clarify evidence and release expectations.

### Shared responsibility
- agree when the packet is good enough to enter the next execution stage,
- keep the packet linked to downstream plans, decisions, and evidence.

## Recommended next artifact
After this gate passes, the next artifact should usually be one of:
- scoped pilot/initiative record,
- delivery-unit definition,
- explicit decision packet,
- product-to-product request/acceptance if cross-product work is required.

## Current recommendation for the TDE UI pilot
For the current pilot, this start gate should be treated as the main missing control layer between:
- the original high-level ambition, and
- the bounded smallest-slice / Delivery-contract artifacts already created.

That means the next practical step is to instantiate this gate for the TDE UI pilot in one concrete objective packet.

## Short rule
**High-level objective first. Objective packet second. Governed execution only after that.**
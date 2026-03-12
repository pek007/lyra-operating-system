# Objective-to-Production Gap Map v1

Status: Draft active
Owner: Peter / Lyra
Date: 2026-03-12
Related artifacts:
- `ONE_ITERATION_TDE_UI_PILOT_V1.md`
- `TDE_UI_PILOT_SMALLEST_SLICE_V1.md`
- `products/delivery/04-execution/TDE_UI_PILOT_DELIVERY_CONTRACT_V1.md`
- `PRODUCT_INBOX_COORDINATION_MODEL_V1.md`

## Purpose
Define the current gap between:
- the capability we want, and
- the capability Lyra OS currently has.

The target capability is:

**Given a high-level objective, Lyra OS should be able to produce a bounded production application through a professional, auditable, end-to-end delivery process.**

This artifact exists to make the missing pieces explicit and to separate:
- what belongs primarily to TDE / Task Management,
- what belongs primarily to Delivery,
- what belongs to the shared operating layer between them.

## Desired end-state
The desired end-state is an **Objective-to-Production Control Loop** that can:
1. accept a high-level objective,
2. convert it into a delivery-ready objective packet,
3. surface and resolve the required decisions,
4. coordinate the involved products/functions,
5. execute through a governed Delivery flow,
6. release with explicit evidence and judgment,
7. preserve the full audit trail from objective to production outcome.

## Current overall read
Lyra OS now has:
- stronger product models,
- a clearer Delivery direction,
- a stronger TDE governance spine,
- a functioning interim cross-product coordination bridge,
- a bounded pilot target.

But Lyra OS does **not yet** have a fully reliable default path from high-level objective to production application without meaningful manual stitching and judgment improvisation.

## Gap map by layer

### Gap 1 — Objective shaping gap
#### Problem
A high-level objective can be stated, but it does not yet consistently become an execution-ready objective packet with all the fields Delivery and TDE need.

#### Missing capability
A standard objective-start gate that produces:
- objective,
- success criteria,
- non-goals,
- operator/user problem,
- bounded first slice,
- key risks,
- explicit decision needs,
- evidence expectations,
- kill criteria or fail conditions where relevant.

#### Why it matters
Without this, ambiguity enters the system too early and gets redistributed into planning, delivery, and implementation.

#### Primary owner
Shared, but led by **Task Management / TDE**.

#### Solve in
- TDE / Task Management: define and own the objective packet conversion step.
- Delivery: define which minimum fields must be present before governed delivery can proceed.

## Gap 2 — Decision operating gap
### Problem
Decision principles exist, but decisions are not yet fully embedded as active operating objects within the execution loop.

### Missing capability
A consistent mechanism to:
- identify when something becomes a decision,
- assign owner,
- capture options/trade-offs,
- require evidence proportionate to risk,
- keep open decisions visible,
- resolve them explicitly,
- link them to execution and release state.

### Why it matters
Without this, important choices are still too easy to make informally in chat or hide inside plans/tasks.

### Primary owner
Shared, but structurally led by **TDE / Task Management**.

### Solve in
- TDE / Task Management: decision object or equivalent explicit decision-tracking layer.
- Delivery: standard decision points for scope, readiness, release, and major blockers.

## Gap 3 — Delivery default-path gap
### Problem
Delivery has a good design direction, but not yet a fully productized default path that can take a fresh objective packet and run it to production with minimal improvisation.

### Missing capability
A reusable Delivery default path for software/application work that includes:
- intake contract,
- bounded delivery unit formation,
- gate model,
- evidence expectations per stage,
- explicit release/readiness decision,
- post-delivery review pattern.

### Why it matters
Without this, each new initiative still risks becoming a custom process run instead of a reliable professional delivery flow.

### Primary owner
**Delivery**.

### Solve in
- Delivery: canonical delivery-unit path and default gate set.
- Shared layer: clean handoff from objective packet into Delivery intake.

## Gap 4 — Cross-product coordination gap
### Problem
Cross-product coordination only recently became operational through the interim inbox bridge. It is now usable, but not yet native, canonical, or strong enough for the long term.

### Missing capability
A TDE-native coordination object or equivalent canonical coordination state that supports:
- requester,
- receiver,
- linked objective,
- requested outcome,
- decision-needed flag,
- status,
- owner,
- refs/evidence,
- acceptance/closure trail.

### Why it matters
Without this, product collaboration depends too much on bridge mechanisms and manual continuity.

### Primary owner
Shared, but structurally led by **TDE / Task Management**.

### Solve in
- TDE / Task Management: canonical coordination object.
- Interim bridge (already in place): inbox intake model.

## Gap 5 — Canonical traceability gap
### Problem
The chain from objective -> scope -> decision -> implementation -> evidence -> release is improving, but still not complete enough to act as a full trusted operating substrate.

### Missing capability
A stronger canonical traceability model that makes it easy to answer:
- what are we trying to achieve?
- what exact scope was accepted?
- what decisions remain open?
- what implementation work is underway?
- what evidence exists?
- why was release accepted?

### Why it matters
Without this, the system remains partially auditable but not fully controllable.

### Primary owner
Shared.

### Solve in
- TDE / Task Management: objective/task/decision visibility.
- Delivery: implementation/evidence/release visibility.
- Shared layer: explicit reference discipline across artifacts.

## Gap 6 — Release judgment gap
### Problem
We are shaping the notion of readiness/release decision, but not yet consistently applying an explicit release judgment standard to bounded product/application slices.

### Missing capability
A lightweight but explicit release judgment pattern that answers:
- ready or not ready,
- why,
- based on what evidence,
- with what residual risk,
- with what rollback/containment posture.

### Why it matters
Without this, “production” can still become informal or elastic.

### Primary owner
**Delivery**.

### Solve in
- Delivery: release/readiness decision artifact and gate standard.
- Shared layer: ensure decision trace links back to objective and scope.

## Priority order
Recommended current priority order:

### Priority 1 — Objective-to-scope gate
Build a standard high-level-objective -> execution-ready packet conversion step.

### Priority 2 — Decision operating layer
Make decisions active, visible, owned, and linked to execution.

### Priority 3 — Delivery default path
Turn Delivery’s approach into a reusable default flow for application/software work.

### Priority 4 — Thin TDE-native coordination
Replace bridge-only coordination with canonical accepted coordination state.

### Priority 5 — Stronger canonical traceability
Tighten end-to-end link integrity across objective, decision, work, evidence, and release.

### Priority 6 — Explicit release judgment standard
Make “production accepted” a real explicit artifact, not a vibe.

## What this means for the current pilot
The TDE UI pilot should not be treated mainly as a UI experiment.
It should be treated as a proving run for the Objective-to-Production Control Loop.

That means the real evaluation questions are:
- Could we turn a high-level objective into a bounded first slice?
- Did we make the important decisions explicit?
- Did Task Management and Delivery coordinate coherently?
- Did Delivery provide a professional execution path?
- Did we produce evidence strong enough for a real release judgment?
- Can an auditor reconstruct the chain afterward?

## TDE vs Delivery vs shared-layer summary

### Primarily TDE / Task Management
- objective packet formation,
- decision visibility,
- coordination object evolution,
- canonical work/decision state.

### Primarily Delivery
- default delivery path,
- evidence expectations by stage,
- release/readiness gate model,
- post-delivery review pattern.

### Shared layer
- objective -> delivery handoff contract,
- cross-product request/acceptance semantics,
- cross-artifact traceability,
- common audit trail expectations.

## Current recommendation
Use this gap map as the control document for deciding what to improve next.

Do not optimize primarily for building the GUI faster.
Optimize for closing the gaps that prevent Lyra OS from reliably converting high-level objectives into production outcomes through a professional, auditable process.

# Current Plan

## Planning horizon
Rolling near-term plan for the next 2-6 weeks.

## Current objectives
1. Close the Vega/PXS boundary readiness gap and rerun it to PASS.
2. Deliver a minimal executable `pxs` consumption contract with schemas and worked examples.
3. Stabilize and prove the canonical substrate that `pxs` will consume.
4. Keep Task Management product boundaries explicit while the downstream consumption path hardens.

## Current workstreams
### Workstream 1: Product model foundation
- create canonical Task Management product model artifacts
- define what is durable versus operationally volatile
- use the Task Management product as the pilot for a reusable product standard

### Workstream 2: Interface clarity
- document interfaces into `pxs`
- make dependencies and responsibilities explicit
- reduce hidden coupling and implicit assumptions

### Workstream 3: Operational readiness
- align TDE deployment requirements, evidence, and product health view
- make it easier to answer whether the product is ready for broader operational use

## Immediate next steps
- define and refine the formal Task Management → `pxs` consumption interface
- create a compact readiness/health scorecard for Task Management / TDE
- connect the product model more explicitly to readiness evidence and downstream usage
- the interim inbox experiment has been completed and superseded as a primary coordination direction
- integrate Delivery’s accepted pilot contract into the shared pilot flow by defining the smallest acceptable GUI slice, explicit non-goals, and the initial decision/evidence structure ✅
- shift coordination design work toward TDE-native assigned work with assignee wake/notification
- obtain a Delivery-defined execution process contract through the eventual assigned-work / handoff model rather than extending mailbox-style coordination
- define how the shared As-Code Contract Pack maps into TDE intake classes, evidence expectations, and execution state transitions
- design the smallest auditable execution-bridge MVP between PXS exports and Lyra OS intake/triage

## Added as-code rollout focus
- Task Management owns the execution-side mapping from cross-repo contracts into signal/work/decision handling
- the first bridge should be minimal: decisions, active tasks, and evidence bundle ingest with explicit approval points for high-risk transformations
- avoid creating a separate planning layer; use product artifacts for intended structure and TDE for executable follow-through

## Out of scope for now
- full commercialization packaging
- generalized multi-product schema enforcement
- heavy process expansion without evidence of need

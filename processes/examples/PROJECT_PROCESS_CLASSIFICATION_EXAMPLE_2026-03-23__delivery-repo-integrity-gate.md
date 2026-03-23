# Project Process Classification Example — Delivery repo-integrity fail-fast gate

Status: Active example
Date: 2026-03-23
Owner: Lyra

## Purpose
Demonstrate one live project classification using the root process discovery layer and the machine-usable process-route registry.

## Candidate work item
Source: `products/delivery/04-execution/TOP_PRIORITIES.md`

Selected live item:
- **Priority 1:** Add repo-integrity fail-fast gates for merge markers and other delivery hygiene failures.

## Discovery path used
1. `PROCESS_DISCOVERY_INDEX.md`
2. Delivery / release / implementation workflow family
3. `PROJECT_PROCESS_ROUTING_V1.md`
4. `processes/PROCESS_ROUTE_REGISTRY_V1.yaml`

## Classification
### Selected project type
`software_delivery`

### Selected route id
`ROUTE_SOFTWARE_DELIVERY_V1`

## Why this classification fits
This work is best treated as a software / digital capability delivery project because:
- it changes a real software-delivery control surface
- it requires implementation, verification, and evidence capture
- it directly affects release trustworthiness and in-use delivery quality
- the canonical next step is to define and wire an enforceable gate, then capture evidence from a real run

## Rejected alternative classifications
### `governance_change`
Rejected as primary classification because this is not mainly a policy/authority rewrite. Governance is involved, but the dominant work is implementing and verifying a delivery control.

### `os_process_improvement`
Rejected as primary classification because the improvement dimension is real but secondary. The dominant execution path is still Delivery-owned implementation and verification.

## Default process bundle selected
### 1. Intent shaping
- `INTENT_TDE_DELIVERY_OPERATIONS_MODEL_V1.md`
- `products/delivery/01-identity/`
- `products/delivery/02-strategy/`

### 2. Execution coordination
- `JOBS_PROCESS_V1.md`
- `products/task-management/`

### 3. Delivery governance
- `SOFTWARE_DELIVERY_PROCESS_3PP_OS.md`
- `products/delivery/03-operating-model/OPERATING_MODEL.md`
- `products/delivery/03-operating-model/GOVERNANCE.md`
- `products/delivery/06-architecture/DELIVERY_AS_CODE_DESIGN_V1.md`

### 4. Learning loop
- `CONTINUOUS_IMPROVEMENT_PROCESS_V1.md`

## Required add-ons judgment
### Security/governance add-on
**Decision:** not required as a primary add-on for the initial step.

Reason:
- the current work item appears to be a medium-governance delivery-control improvement inside the Delivery product boundary
- no direct credential, authority, permission, or high-downside security boundary change is yet evident from the priority description alone

### Add-on trigger to watch
If the implementation path touches:
- repository permissions,
- merge authority,
- CI/CD approval boundaries,
- release authority,
- or security-sensitive enforcement paths,
then add:
- `SECURITY_PROCESS_V1.md`
- `governance/`
- `products/security/`

## Owning product / dominant process owner
- Owning product: `Delivery` (`A-006`)
- Dominant process owner: Delivery product
- Supporting coordination: Task Management for execution routing; Improvement for any repeated miss or control-gap follow-through

## Practical next-step interpretation
Using the selected route, the work should now be treated as:
1. a Delivery-owned governed implementation item,
2. routed through canonical execution state,
3. implemented with explicit verification evidence,
4. assessed for whether any security/governance add-on becomes necessary,
5. reviewed for whether the result should generate follow-on improvement work.

## What this test tells us about the routing system
### What worked
- the root discovery layer gave a clear starting point
- the route registry offered an unambiguous primary match
- the bundle was easy to explain in operational terms

### What still feels weak
- add-on triggers are still prose-heavy rather than strongly machine-testable
- there is not yet a compact canonical project-classification record format for repeated use
- route selection still depends on judgment rather than deterministic validation

## Recommended follow-up
If repeated use is expected, create a small project-classification record schema so each live project can store:
- project type
- selected route id
- owning product/workspace
- chosen bundle
- explicit add-ons
- rationale
- reviewer/approver when material

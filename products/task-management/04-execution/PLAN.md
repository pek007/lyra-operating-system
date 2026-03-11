# Current Plan

## Planning horizon
Rolling near-term plan for the next 2-6 weeks.

## Current objectives
1. Establish the first working Product-as-Code model for Task Management.
2. Clarify the product boundary between Task Management, governance, and downstream workspaces.
3. Make TDE deployment/readiness status easier to assess and act on.
4. Improve the path for `pxs` to consume Task Management capability.

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

## Out of scope for now
- full commercialization packaging
- generalized multi-product schema enforcement
- heavy process expansion without evidence of need

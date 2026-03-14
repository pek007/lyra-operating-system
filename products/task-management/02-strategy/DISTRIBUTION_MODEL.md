# Distribution Model

For Task Management, distribution means adoption and operational use rather than classic marketing/sales.

## Primary distribution path
Enable consuming environments such as `pxs` to use the product through explicit interfaces, documented operating patterns, and evidence-backed deployment.

## Adoption model
1. Prove the capability in Lyra OS itself.
2. Stabilize the interfaces and operating expectations.
3. Enable `pxs` as the first downstream consumer.
4. Expand only after usage is reliable and boundaries are clear.

## Distribution mechanisms
- workspace artifacts
- operating documents and policies
- runtime bindings and jobs
- readiness gates and evidence packs
- workspace operating package artifacts in downstream consumers where needed
- future capability-pack and/or service interfaces if needed

## Workspace consumption requirements
For a downstream workspace such as `pxs`, successful consumption is not just a matter of receiving guidance artifacts.
The workspace must also have a usable local operating package so the capability has clear local routes and authority.

At minimum, downstream consumption should make explicit:
- local workspace purpose and authority boundary
- local source-of-truth map
- local process discovery front door
- local task system of record
- local decision/escalation path
- local error/incident handling path

These do not all need to originate inside the product itself, but the product distribution model must account for them as part of coherent adoption.

## Activation model
The product is activated by:
- explicit use of TDE operating patterns
- approved deployment into downstream environments
- clear intake/output contracts
- visible ownership and review cadence

## Friction points to remove
- unclear onboarding into the product
- ambiguous task/decision handoff points
- undocumented dependencies on workspace internals
- difficulty seeing product health and current state

## Success signal
A downstream consumer can start using the product with minimal custom explanation because the interfaces, artifacts, and operating expectations are already clear.

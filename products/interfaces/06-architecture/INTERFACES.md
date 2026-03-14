# Interfaces

## Upstream interfaces
- product models
- delivery capabilities
- governance rules

## Downstream interfaces
- capability consumers such as `pxs`
- cross-product contract and packaging consumers

## Ownership stance
Interfaces owns:
- cross-cutting interface contract templates and standards
- packaging/versioning/change-governance discipline for exported interface artifacts
- verification expectations for interface-contract changes

Interfaces does not own:
- every provider product's concrete service/API/interface surface
- the full internal behavior of the products it connects

Provider-specific interfaces should remain owned by the provider product and may consume Interfaces standards rather than being absorbed by Interfaces.

## Workspace package implication
When Interfaces contributes packaging or contract discipline into a downstream workspace, the consumer should have enough local operating-package structure to make those interfaces discoverable and usable in local context.
That typically means explicit local front doors for:
- source-of-truth
- process discovery
- any local routes needed to consume adopted interface/packaging artifacts coherently

## Key boundary rule
Interfaces owns the explicit contract/packaging/connector discipline for crossing boundaries; it does not own the full internal behavior of the products it connects.

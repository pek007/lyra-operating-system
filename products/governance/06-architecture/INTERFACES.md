# Interfaces

## Upstream interfaces
- governance records and portfolio artifacts

## Downstream interfaces
- shared rules, decision-rights logic, and boundary constraints applied across products
- adopted governance artifacts consumed by downstream workspaces such as `pxs`
- governance assembly consumers and reviewers

## Product vs assembly relationship
Governance must answer two related but different questions clearly:
- product state: what Governance is trying to achieve now as a product
- assembly state: what Governance v0.1 exports for downstream adoption

These should remain linked but not conflated.

## Workspace package implication
When Governance is consumed in a downstream workspace, the consumer should have enough local operating-package structure to make governance authority usable locally.
That typically means explicit local front doors for:
- source-of-truth
- process discovery
- decision/escalation

Governance should shape those routes, not replace the workspace's local operating package.

## Key boundary rule
Governance owns system-level rules and coordination constraints, not the internal day-to-day operating processes of each product.

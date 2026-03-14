# Interfaces

## Upstream interfaces
- governance records and portfolio artifacts

## Downstream interfaces
- shared rules, decision-rights logic, and boundary constraints applied across products
- adopted governance artifacts consumed by downstream workspaces such as `pxs`

## Workspace package implication
When Governance is consumed in a downstream workspace, the consumer should have enough local operating-package structure to make governance authority usable locally.
That typically means explicit local front doors for:
- source-of-truth
- process discovery
- decision/escalation

Governance should shape those routes, not replace the workspace's local operating package.

## Key boundary rule
Governance owns system-level rules and coordination constraints, not the internal day-to-day operating processes of each product.

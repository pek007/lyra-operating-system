# Interfaces

## Upstream interfaces
- governance and product management artifacts

## Downstream interfaces
- improvement process and deployment outputs to products and consuming environments
- adopted improvement artifacts consumed by downstream workspaces such as `pxs`

## Workspace package implication
When Improvement is consumed in a downstream workspace, the consumer should have enough local operating-package structure to make findings, follow-up work, and learning paths locally usable.
That typically means explicit local front doors for:
- task system of record
- error/incident handling
- decision/escalation

Improvement should strengthen those routes, not silently depend on them remaining implicit.

## Key boundary rule
Improvement should enable other products to improve without taking over their day-to-day ownership or the canonical execution-state role owned by Task Management.

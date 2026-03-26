# Interfaces

## Upstream interfaces
- governance and product management artifacts
- external AI-agent and OpenClaw information sources, research feeds, release notes, demos, and observed use-case examples

## Downstream interfaces
- improvement process and deployment outputs to products and consuming environments
- adopted improvement artifacts consumed by downstream workspaces such as `pxs`
- minimum product-side improvement interface for active products

## Minimum improvement interface
Each active product with a canonical `TOP_PRIORITIES.md` surface must expose at least:
- a named improvement-relevant signal class
- an explicit conversion rule from material incidents, repeated misses, or review findings into canonical TDE-linked improvement work
- the six-field intake linkage requirement (`source_system`, `source_reference`, `product_scope`, `evidence_links`, `improvement_type`, `expected_closure_evidence`)
- a closure-evidence rule with explicit source-to-closure trace
- a recurring review-visibility expectation for open product-origin improvement items

For Phase 1 canonical Improvement work, the intake/log mechanism must route through a canonical TDE task plus a linked intake artifact that satisfies `products/improvement/04-execution/intake/CANONICAL_IMPROVEMENT_INTAKE_CONTRACT_V1.md`.

That intake artifact must include:
- `source_system`
- `source_reference`
- `product_scope`
- `evidence_links`
- `improvement_type`
- `expected_closure_evidence`

Any lighter product-local note, nightly report, or discussion surface may still exist as a signal source, but it is non-canonical until this TDE-linked intake contract is met.

This is the minimum surface that lets Improvement turn product-local signals into compounding portfolio learning without drifting back into ambiguous entry paths.

The standard reusable rollout/reference package for this interface is:
- `products/improvement/04-execution/MINIMUM_IMPROVEMENT_INTERFACE_STANDARD_REFERENCE_SET_2026-03-22.md`

## Workspace package implication
When Improvement is consumed in a downstream workspace, the consumer should have enough local operating-package structure to make findings, follow-up work, and learning paths locally usable.
That typically means explicit local front doors for:
- task system of record
- error/incident handling
- decision/escalation

Improvement should strengthen those routes, not silently depend on them remaining implicit.

## Key boundary rule
Improvement should enable other products to improve without taking over their day-to-day ownership or the canonical execution-state role owned by Task Management.

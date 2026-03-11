# Control Panel Product

- Product ID: `CP-001`
- Product name: `Control Panel`
- Owner: `Peter / Lyra`
- Domain: `OS`
- Type: `Internal (SaaS-candidate potential)`
- Status: `Active`

## Purpose
Control Panel exists to provide the operator-experience plane of Lyra OS: a trusted control surface that makes the system observable, steerable, and easier to operate without tribal knowledge.

## Why this product matters
As the operating system grows, operators need a clear place to inspect state, understand risk, and act safely. Control Panel is the strongest current candidate for that operator-experience role.

## Scope
This product includes:
- control-panel runtime and service surfaces
- operator visibility and control mechanisms
- related policy/runbook guidance
- future boundary/interface work for broader product usage

This product does not own the underlying work state, policy decisions, or delivery mechanisms; it owns the operator-facing surface over those layers.

## Product model
Thin v1 product model artifacts:
- `MODEL.yaml`
- `01-identity/VISION.md`
- `02-strategy/STRATEGY.md`
- `03-operating-model/OPERATING_MODEL.md`
- `04-execution/PLAN.md`
- `05-performance/METRICS.md`
- `06-architecture/INTERFACES.md`
- `07-decisions/DECISIONS.md`

## Current mandate
- maintain a coherent control-surface concept for Lyra OS
- support safe operational visibility and control
- avoid premature monolith formation

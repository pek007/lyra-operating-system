# Shared Corrective Action System v1

Status: Draft active rule
Owner: Peter / Lyra
Date: 2026-03-11

## Purpose
Define the canonical action system for shared/system corrective actions.

This artifact exists because product-local corrective actions can live inside product-owned systems, but cross-product/system corrective actions also need a canonical placement that does not fall back to ambiguous or legacy artifacts such as `TASKS.md`.

## Scope
This rule applies only to:
- cross-product corrective actions
- system-level corrective actions
- follow-up actions from shared/system error reports
- shared coordination fixes that do not belong inside a single product’s local action system

It does **not** replace product-local action systems.

## Core rule
For shared/system issues, the canonical action system is:
1. the owning shared/system error report as the authoritative corrective-action container
2. linked shared coordination or standards artifacts as the structural update layer
3. explicit review/closure criteria inside the error report as the verification layer

In other words:
- the error report is the canonical action anchor
- not `TASKS.md`
- not an ad hoc inbox
- not a product-local board unless ownership is explicitly transferred

## Why this design
Right now the system has:
- product-local action systems
- shared/system standards and coordination artifacts
- structured error reports

What it does **not** yet have is a separate clearly defined shared/system task board.

Until such a board is deliberately created, the cleanest canonical system for shared/system corrective actions is the shared/system error report itself.

## Practical rule
When a shared/system issue occurs:
1. create or update the shared/system error report
2. list corrective actions there
3. update the relevant shared/system artifacts (rules, maps, standards, protocols)
4. define closure criteria there
5. only create product-local tasks if ownership is explicitly delegated into a product boundary

## Product-transfer rule
If a shared/system corrective action becomes clearly product-owned:
- transfer it into the owning product’s action system
- update the shared/system error report to reference that transfer
- keep the error report as the cross-boundary incident record, not the day-to-day product execution board

## Anti-patterns
Avoid:
- adding new shared/system corrective actions to legacy/reference boards by habit
- placing cross-product corrective actions in a product-local system without explicit ownership transfer
- creating untracked shared actions in chat only
- duplicating the same corrective action across multiple systems without clear source of truth

## Current implication
Until a dedicated shared/system corrective-action board is deliberately designed, the canonical home for shared/system corrective actions is:
- the relevant shared/system error report
- plus any linked shared standards/rules/maps that were updated as part of correction

## Relationship to existing artifacts
- `ERROR_REPORTING_STANDARD_V1.md` defines the structure of the report
- `CLOSED_LOOP_IMPROVEMENT_MODEL_V1.md` defines the improvement loop
- `PROCESS_OWNERSHIP_AND_COORDINATION_RULE_V1.md` defines ownership boundaries

This artifact answers the narrower question:
- where shared/system corrective actions should actually live right now

## Short rule
**For shared/system issues, the error report is the canonical corrective-action system until ownership is transferred or a dedicated shared board is deliberately created.**

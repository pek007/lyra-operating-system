# TDE Product Owner Nightly Report Spec v1

Status: Draft spec
Owner: Task Management / Control Tower
Date: 2026-03-14

## Purpose
Define the canonical nightly report artifact for product-owner reporting in the TDE operating model.

This spec exists to bridge:
- refreshed product priorities in code
- executive nightly reporting
- canonical TDE signal intake

It ensures that nightly product-owner reporting is not merely a chat prompt pattern, but a structured operating artifact that can be validated, transformed, and consumed by Task Management.

## Core principle
A nightly product-owner report should be:
1. grounded in the full product stack
2. based on the current `TOP_PRIORITIES.md`
3. produced as a canonical structured report artifact
4. rendered into a human-readable summary as a projection
5. treated operationally as `signal`, not automatically as `work`

## Relationship to other artifacts
This spec should be read together with:
- `PRODUCT_OWNER_DAILY_PRIORITY_REFRESH_PROTOCOL_V1.md`
- `PRODUCT_TOP_PRIORITIES_STANDARD_V1.md`
- `PRODUCT_PRIORITY_SETTING_PROTOCOL_V1.md`
- `CONTROL_TOWER_OVERNIGHT_SYNTHESIS_POLICY_V1.md`
- `products/task-management/06-architecture/TDE_PO_NIGHTLY_REPORT_ADAPTER_CONTRACT_V1.md`
- `products/task-management/06-architecture/TDE_INTAKE_INTERFACE_CONTRACT_V1.md`

## Canonical workflow
The intended nightly product-owner chain is:
1. Product Owner reviews the full product stack
2. Product Owner refreshes `TOP_PRIORITIES.md` if needed
3. Product Owner emits a canonical nightly report artifact
4. Human-readable executive summary is rendered from that artifact
5. Adapter translates the report into a canonical `tde_intake_packet`
6. TDE triages the packet under `intake_class = signal`
7. Control Tower decides whether any signal should become work/decision/action

## Canonical source precedence
The nightly report should use this source precedence:
1. `TOP_PRIORITIES.md` as the canonical source of current top priorities
2. full product model as supporting context
3. current TDE/execution state as current-state evidence

If `TOP_PRIORITIES.md` is missing or stale, the report must say so explicitly.
It must not silently replace the codified source of truth unless the run is explicitly performing a priority-refresh update first.

## Required input basis
A nightly product-owner report should review at minimum:
- `PRODUCT.md`
- `MODEL.yaml`
- `01-identity/VISION.md`
- `02-strategy/STRATEGY.md`
- relevant `03-operating-model/*` artifacts
- `04-execution/PLAN.md`
- `04-execution/RISKS.md` / `ROADMAP.md` where present
- `05-performance/METRICS.md` and any readiness/health artifacts where present
- `07-decisions/DECISIONS.md`
- current `04-execution/TOP_PRIORITIES.md`
- current TDE/execution reality

## Canonical report content
A valid nightly product-owner report should contain:
- report id
- product id / product name
- product owner
- report date
- overall health
- short executive summary
- current top priorities (from code)
- key blockers
- key risks
- proposed next actions
- evidence links / supporting references where relevant
- indication of whether priorities were refreshed in this run

## Recommended semantic fields
Recommended fields for the canonical report object:
- `artifactType`
- `schemaVersion`
- `reportId`
- `productId`
- `productName`
- `productOwner`
- `reportDate`
- `overallHealth`
- `summary`
- `topPriorities`
- `blockers`
- `risks`
- `proposedTdeActions`
- `priorityRefreshStatus`
- `evidenceLinks`
- `sourceReferences`

## Health scale
Recommended health values:
- `green`
- `yellow`
- `red`

Interpretation:
- `green` = healthy enough, no major execution concern
- `yellow` = meaningful weakness/blocker/risk present
- `red` = materially blocked, degraded, or requiring rapid attention

## Priority refresh field
The nightly report should explicitly state one of:
- `unchanged`
- `updated`
- `missing`
- `stale_detected_not_updated`

This makes it visible whether the code-based priority surface is actually current.

## Human-readable summary projection
The executive Telegram summary should be derived from the canonical report object.

Recommended concise structure:
- product name + overall health
- one-line summary
- top 3 priorities
- main blocker/risk
- recommended overnight next action

This summary is a projection, not the canonical source.

## Relationship to TDE
Per Task Management intake design, the nightly report should normally enter TDE as:
- `signal`

not as:
- direct `work`

Promotion into work, decision items, or no-action recording should happen only after triage and/or Control Tower synthesis.

## Storage guidance
Canonical nightly report artifacts should live in a stable machine-usable location.

Recommended pattern:
- product-local execution artifact path, or
- dedicated runtime/report path linked from the product

The exact storage path may evolve, but the report should be durable, inspectable, and replayable.

## Validation rule
The report should be schema-valid before adapter transformation into a `tde_intake_packet`.
Invalid report objects must fail closed rather than silently entering TDE.

## Anti-patterns
Avoid:
- making Telegram output the only source of the nightly report
- treating nightly reporting as a hidden priority-setting mechanism
- silently inferring priorities when codified priorities exist
- converting every nightly report into work automatically
- losing blocker/risk meaning during transformation

## Minimum implementation expectation
A compliant nightly runtime should:
1. run product-owner daily priority refresh logic
2. produce a canonical nightly report object
3. render a concise executive summary from it
4. make the canonical object available for adapter/triage

## Version
- v1.0
- Date: 2026-03-14
- Owner: Task Management / Control Tower

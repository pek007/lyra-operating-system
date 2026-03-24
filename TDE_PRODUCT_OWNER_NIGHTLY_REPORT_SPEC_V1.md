# TDE Product Owner Nightly Report Spec v1

Status: Draft spec
Owner: Task Management / Control Tower
Date: 2026-03-14

## Purpose
Define the canonical nightly synthesis delta artifact for product-owner reporting in the TDE operating model.

This spec exists to bridge:
- product-local artifact updates in code
- compact executive overnight synthesis
- canonical TDE signal intake

It ensures that overnight product-owner reporting is not merely a chat prompt pattern, but a structured operating artifact derived from the product's own canonical model and research system.

## Core principle
A nightly product-owner synthesis should be:
1. grounded in the full product stack
2. derived from current canonical product artifacts, not freeform narration
3. able to reflect product-local research deltas where relevant
4. produced as a canonical structured synthesis artifact
5. rendered into a human-readable summary only as a projection
6. treated operationally as `signal`, not automatically as `work`

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
1. Product Owner reviews the full product stack and relevant research artifacts
2. Product Owner updates product-local canonical artifacts if understanding or direction changed
3. Product Owner refreshes `TOP_PRIORITIES.md` if needed
4. Product Owner emits a canonical nightly synthesis artifact capturing only material deltas
5. Human-readable executive summary is rendered from that artifact
6. Adapter translates the synthesis into a canonical `tde_intake_packet`
7. TDE triages the packet under `intake_class = signal`
8. Control Tower decides whether any signal should become work/decision/action

## Canonical source precedence
The nightly synthesis should use this source precedence:
1. canonical product artifacts updated in this run
2. `TOP_PRIORITIES.md` as the canonical source of current top priorities
3. full product model as supporting context
4. current TDE/execution state as current-state evidence
5. product-local research artifacts where relevant

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

## Canonical synthesis content
A valid nightly product-owner synthesis should contain:
- synthesis id
- product id / product name
- product owner
- synthesis date
- short executive summary
- material changes since last run
- current top priorities (from code)
- key blockers or constraints
- key risks or opportunities
- product-local research delta, if any
- proposed next actions
- evidence links / supporting references where relevant
- indication of whether priorities were refreshed in this run

## Recommended semantic fields
Recommended fields for the canonical synthesis object:
- `artifactType`
- `schemaVersion`
- `synthesisId`
- `productId`
- `productName`
- `productOwner`
- `synthesisDate`
- `summary`
- `materialChanges`
- `topPriorities`
- `constraints`
- `risksOrOpportunities`
- `researchDelta`
- `proposedTdeActions`
- `priorityRefreshStatus`
- `evidenceLinks`
- `sourceReferences`

## State expression rule
Avoid human-style color coding.

Use short explicit language instead, for example:
- `on_track`
- `needs_decision`
- `blocked_externally`
- `under_investigation`
- `plan_changed`
- `execution_in_progress`
- `evidence_weak`
- `risk_rising`
- `ready_for_review`

The purpose is to communicate the actual state in words rather than compressing it into color symbolism.

## Priority refresh field
The nightly report should explicitly state one of:
- `unchanged`
- `updated`
- `missing`
- `stale_detected_not_updated`

This makes it visible whether the code-based priority surface is actually current.

## Human-readable summary projection
The executive summary should be derived from the canonical synthesis object.

Recommended concise structure:
- product name
- one-line summary
- material change or no-material-change marker
- top 1-3 priorities only if materially relevant
- main blocker/risk/opportunity in words
- recommended overnight next action

This summary is a projection, not the canonical source.

## Relationship to TDE
Per Task Management intake design, the nightly report should normally enter TDE as:
- `signal`

not as:
- direct `work`

Promotion into work, decision items, or no-action recording should happen only after triage and/or Control Tower synthesis.

## Canonical storage path and filename
Canonical nightly report artifacts should live in one stable product-local machine-usable location.

Required pattern:
- `products/<slug>/04-execution/nightly-reports/YYYY-MM-DD-po-nightly-report.json`

Rules:
- do not alternate between `reports/` and `nightly-reports/`
- do not vary the filename shape (`PO_NIGHTLY`, `_product-owner-nightly-report`, etc.)
- one product should use one canonical path pattern consistently across nights
- if legacy report locations exist, treat them as historical artifacts, not the forward standard

The purpose is to make report discovery, verification, replay, and downstream automation trivial.

## Canonical minimum schema
A compliant nightly report object should use one canonical field shape.

Required top-level keys:
- `artifactType`
- `schemaVersion`
- `synthesisId`
- `productId`
- `productName`
- `productOwner`
- `synthesisDate`
- `overallHealth`
- `summary`
- `materialChanges`
- `topPriorities`
- `blockers`
- `risksOrOpportunities`
- `proposedNextActions`
- `priorityRefreshStatus`
- `evidenceLinks`

Field normalization rules:
- use `synthesisId`, not `reportId`
- use `synthesisDate`, not `reportDate`
- use `risksOrOpportunities`, not parallel ad hoc `risks` unless also normalized into the canonical field
- keep `priorityRefreshStatus` constrained to: `unchanged`, `updated`, `missing`, or `stale_detected_not_updated`
- additional fields are allowed when useful, but they must not replace or rename the canonical minimum keys

## Validation rule
The report should be schema-valid before adapter transformation into a `tde_intake_packet`.
Invalid report objects must fail closed rather than silently entering TDE.

If a runtime cannot satisfy the canonical path or canonical minimum schema in a given run, it should:
- record that fact explicitly in the run output
- prefer a visible partial/failed control outcome over silently improvising a variant artifact
- avoid claiming a fully conforming success when path/schema drift occurred

## Anti-patterns
Avoid:
- making chat output the only source of the nightly synthesis
- treating overnight reporting as a hidden priority-setting mechanism
- silently inferring priorities when codified priorities exist
- converting every nightly synthesis into work automatically
- losing blocker/risk meaning during transformation
- pushing product-local research reasoning into the main Control Tower context by default

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

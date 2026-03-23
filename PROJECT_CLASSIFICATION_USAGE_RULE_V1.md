# Project Classification Usage Rule v1

Status: Active (v1)
Owner: Lyra OS Platform
Date: 2026-03-23

## Purpose
Define when a project-classification record is mandatory, where it fits in the operating flow, and what minimum behavior is required before non-trivial work proceeds.

This rule exists to make project routing a real operating step rather than an optional planning aid.

## Core rule
A project-classification record is required before non-trivial work proceeds when the work:
- starts a new project, initiative, or bounded workstream,
- materially changes an existing project’s operating path,
- crosses product, workspace, delivery, governance, or authority boundaries,
- or needs explicit delivery, security, governance, or improvement add-ons.

If a classification is materially ambiguous, that ambiguity must be recorded and treated as a process-routing issue rather than silently improvised away.

## Minimum use threshold
Classification is mandatory for work that is any of the following:
- expected to require more than one process bundle,
- expected to enter canonical execution state in TDE,
- expected to be released, handed off, deployed, or activated,
- expected to affect governance, security, authority, or auditability,
- expected to change a workspace operating package or local source-of-truth/discovery layer,
- or expected to generate follow-on work across multiple sessions, products, or operators.

Classification is optional for:
- trivial one-step local work,
- low-risk hygiene edits that clearly stay inside an already-classified operating path,
- or work already governed by an active classification record with no material routing change.

## Required operating sequence
For work requiring classification, use this order:
1. consult `PROCESS_DISCOVERY_INDEX.md` or the applicable workspace-local discovery index
2. select the closest route using `PROJECT_PROCESS_ROUTING_V1.md` and `processes/PROCESS_ROUTE_REGISTRY_V1.yaml`
3. create or update a record using `processes/standards/PROJECT_CLASSIFICATION_RECORD_SCHEMA_V1.yaml`
4. register the record in `processes/PROJECT_CLASSIFICATION_REGISTRY_V1.yaml`
5. only then treat the project as minimally process-routed for execution, delivery, or further planning

## Minimum record content
A valid project-classification record must state:
- owning scope
- selected project type
- selected route id
- chosen primary bundle
- add-ons included, deferred, or watch-triggered
- rationale for the classification

## Reuse rule
If an existing active classification already governs the work:
- reuse it when the route and add-ons still fit,
- update it if the operating path materially changes,
- supersede it if the project has changed enough that the prior classification would now mislead execution.

## Review / escalation rule
Human review should be required when:
- the classification changes approval, authority, or delivery posture materially,
- governance and delivery are both primary and the dominant route is not obvious,
- a workspace-local process conflicts with a shared/product route,
- or route ambiguity remains after reasonable discovery.

Default reviewer:
- the relevant product owner for product-owned work,
- the workspace owner for workspace-local work,
- Peter when classification materially affects governance, release, or real-world downside.

## Process-miss linkage
The following are process misses and must feed the improvement loop:
- non-trivial work started without a required classification record,
- a stale classification continued to govern materially changed work,
- a wrong route was selected and caused operational confusion or control weakness,
- the route/add-on logic was too ambiguous to apply consistently.

## Source artifacts
- `PROCESS_DISCOVERY_INDEX.md`
- `PROJECT_PROCESS_ROUTING_V1.md`
- `processes/PROCESS_ROUTE_REGISTRY_V1.yaml`
- `processes/PROJECT_CLASSIFICATION_REGISTRY_V1.yaml`
- `processes/standards/PROJECT_CLASSIFICATION_RECORD_SCHEMA_V1.yaml`
- `CONTINUOUS_IMPROVEMENT_PROCESS_V1.md`

## Short form
For any new non-trivial project: discover -> route -> classify -> register -> execute.

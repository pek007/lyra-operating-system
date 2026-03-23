# Project Process Routing v1

Status: Draft active
Owner: Lyra OS Platform
Date: 2026-03-23

## Purpose
Provide a compact default router from project type to the process bundle that should govern the work.

This artifact exists because professional execution usually requires a stack of processes, not a single document. It helps operators and agents choose a sensible default operating bundle before execution begins.

## Use rule
When a new project, initiative, or bounded workstream starts:
1. classify the work into the closest project type below
2. use the listed bundle as the default process stack
3. refine only if the owning product/workspace has a more specific approved operating path
4. if no project type fits cleanly, escalate the ambiguity instead of improvising

## Global routing rules
- Always prefer the most specific approved local or product-owned process over a broader shared fallback.
- If security, authority, or real-world downside is material, include the security/governance bundle even if not listed as primary.
- If the work will create or change canonical state, ensure the task/decision execution bundle is included.
- If the work will be released, handed off, or activated in use, ensure the delivery bundle is included.
- If the work reveals a repeated miss, ambiguity, or friction pattern, include the improvement bundle.

## Project types and default bundles

### 1. Software / digital capability delivery project
Use when:
- building or materially changing a software capability
- shaping a feature, application, service, integration, or internal tool
- architecture, testing, release, or in-use verification matter

Default bundle:
- Intent shaping:
  - `INTENT_TDE_DELIVERY_OPERATIONS_MODEL_V1.md`
  - relevant product `01-identity/` + `02-strategy/` artifacts
- Execution coordination:
  - `JOBS_PROCESS_V1.md`
  - task-management product artifacts under `products/task-management/`
- Delivery governance:
  - `SOFTWARE_DELIVERY_PROCESS_3PP_OS.md`
  - `products/delivery/03-operating-model/OPERATING_MODEL.md`
  - `products/delivery/03-operating-model/GOVERNANCE.md`
  - `products/delivery/06-architecture/DELIVERY_AS_CODE_DESIGN_V1.md`
- Security/control layer:
  - `SECURITY_PROCESS_V1.md`
  - relevant governance + security product artifacts
- Learning loop:
  - `CONTINUOUS_IMPROVEMENT_PROCESS_V1.md`
  - relevant product review / post-delivery review artifacts

### 2. Business development / strategic initiative
Use when:
- shaping a business offer, operating move, commercial initiative, or strategic change
- work is outcome-heavy and may or may not require software delivery later

Default bundle:
- Intent shaping:
  - `INTENT_TDE_DELIVERY_OPERATIONS_MODEL_V1.md`
  - relevant product strategy/vision artifacts
- Decision / execution routing:
  - `JOBS_PROCESS_V1.md`
  - task-management product artifacts under `products/task-management/`
- Product / initiative governance:
  - `PRODUCT_WAY_OF_WORKING_PROCESS_V1.md`
  - relevant product `04-execution/*` and `07-decisions/DECISIONS.md`
- Improvement loop:
  - `CONTINUOUS_IMPROVEMENT_PROCESS_V1.md`

Optional add-on:
- include Delivery if the initiative crosses into governed implementation, release, handoff, or deployment

### 3. Governance / policy / control change
Use when:
- changing rules, policy, authority, compliance posture, approvals, or control logic
- auditability and escalation boundaries matter more than delivery speed alone

Default bundle:
- Intent / decision framing:
  - `INTENT_TDE_DELIVERY_OPERATIONS_MODEL_V1.md`
  - relevant governance decision artifacts
- Governance / control process:
  - `governance/`
  - `SECURITY_PROCESS_V1.md` when security or authority is implicated
- Execution routing:
  - `JOBS_PROCESS_V1.md`
- Delivery bundle:
  - only if the policy/control change must be packaged, released, or activated as a governed change
- Improvement / verification:
  - `CONTINUOUS_IMPROVEMENT_PROCESS_V1.md`
  - error/corrective-action artifacts if this was triggered by a miss or incident

### 4. Workspace bootstrap / retrofit / operating-package change
Use when:
- creating or upgrading a downstream workspace
- clarifying source of truth, process discovery, authority, or local operating paths
- moving a workspace from ad hoc to operable

Default bundle:
- Workspace package layer:
  - `WORKSPACE_OPERATING_PACKAGE_STANDARD_V1.md`
  - `PROCESS_DISCOVERY_INDEX_STANDARD_V1.md`
  - `WORKSPACE_BOOTSTRAP_AND_RETROFIT_PROTOCOL_V1.md`
- Local authority and discovery:
  - workspace-local `SOURCE_OF_TRUTH.md`
  - workspace-local `PROCESS_DISCOVERY_INDEX.md`
  - workspace-local `AGENTS.md`
- Execution routing:
  - `JOBS_PROCESS_V1.md`
- Improvement loop:
  - `CONTINUOUS_IMPROVEMENT_PROCESS_V1.md`

### 5. Internal operating-system/process improvement project
Use when:
- improving Lyra OS operating behavior itself
- tightening process discovery, routing, validation, cadence, or control surfaces
- converting repeated friction into better operating architecture

Default bundle:
- Improvement layer:
  - `CONTINUOUS_IMPROVEMENT_PROCESS_V1.md`
  - `CLOSED_LOOP_IMPROVEMENT_MODEL_V1.md`
- Error/corrective-action layer:
  - `ERROR_REPORTING_STANDARD_V1.md`
  - relevant error artifacts when applicable
- Process/discovery layer:
  - `PROCESS_DISCOVERY_INDEX.md`
  - `PROCESS_DISCOVERY_INDEX_STANDARD_V1.md`
  - `PROCESS_OWNERSHIP_AND_COORDINATION_RULE_V1.md`
- Execution routing:
  - `JOBS_PROCESS_V1.md`

## Ambiguity handling
If a project appears to span multiple types:
- choose the dominant project type
- add the missing bundles explicitly rather than inventing a hybrid process from scratch
- record the judgment in the relevant project or decision artifact if the classification materially affects governance or execution behavior

If no route is clear:
- classify this as a process-routing ambiguity
- route it into the improvement/error loop for clarification
- do not treat ambiguity as permission to skip process selection

## Machine-usable companion
The human-readable routing defined here is paired with:
- `processes/PROCESS_ROUTE_REGISTRY_V1.yaml`
- `processes/standards/PROCESS_ROUTE_SCHEMA_V1.yaml`
- `processes/PROJECT_CLASSIFICATION_REGISTRY_V1.yaml`
- `processes/standards/PROJECT_CLASSIFICATION_RECORD_SCHEMA_V1.yaml`

These artifacts exist so route selection can become easier to validate, automate, inspect, and store without relying only on prose interpretation.

## Output expectation
A project is considered minimally process-routed when the operator or agent can state:
- project type
- chosen default process bundle
- owning product/workspace
- any explicit add-on bundles required for security, delivery, or improvement

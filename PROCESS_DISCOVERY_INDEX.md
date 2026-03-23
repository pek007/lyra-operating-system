# PROCESS_DISCOVERY_INDEX

Status: Active (v1)
Workspace: Lyra OS root workspace
Date: 2026-03-23
Owner: Lyra OS Platform

## Scope
This index applies to the Lyra OS root workspace at `/Users/lyra/.openclaw/workspace`.

Its purpose is to give operators and agents one front door for locating the official process, SOP, runbook, and standards that apply in this root operating scope.

## Use rule
Before performing a non-trivial operational activity, check whether an official process, SOP, runbook, or standard applies here.

Use this artifact as a routing layer, not as a substitute for the owning process.

## Official artifacts in this scope
Official process artifacts in the root workspace are:
- approved root-level process docs, SOPs, runbooks, and standards in owning locations
- approved product-owned operating artifacts inside `products/<slug>/`
- approved governance artifacts inside `governance/` when they define control or authority
- approved workspace-operating-package standards when the task is about workspace setup, retrofit, or local operability

Official status is determined by ownership and governance, not by filename alone.

## Precedence
When multiple candidate artifacts exist, use this order:
1. most specific approved local artifact for the current scope
2. approved product-owned operating artifact for the owning product/domain
3. approved shared/platform coordination artifact when the matter is genuinely cross-product
4. broader fallback artifact only when no more specific approved artifact exists

## Process families

### 1. Intent shaping / project formation
Start with:
- `INTENT_TDE_DELIVERY_OPERATIONS_MODEL_V1.md`
- relevant product `01-identity/` and `02-strategy/` artifacts
- `PROJECT_PROCESS_ROUTING_V1.md`

Use when:
- shaping a new initiative
- converting goals into execution-ready work
- deciding whether the work is primarily strategic, operational, software, governance, or workspace-facing

### 2. Task / decision execution
Start with:
- `JOBS_PROCESS_V1.md`
- task-management product artifacts under `products/task-management/`
- `PROJECT_PROCESS_ROUTING_V1.md`

Use when:
- routing work into canonical execution state
- clarifying assignments, dependencies, or decision visibility
- determining how ongoing work should be coordinated

### 3. Delivery / release / implementation workflow
Start with:
- `SOFTWARE_DELIVERY_PROCESS_3PP_OS.md`
- `products/delivery/PRODUCT.md`
- `products/delivery/03-operating-model/OPERATING_MODEL.md`
- `products/delivery/03-operating-model/GOVERNANCE.md`
- `products/delivery/04-execution/PLAN.md`
- `products/delivery/06-architecture/DELIVERY_AS_CODE_DESIGN_V1.md`
- `PROJECT_PROCESS_ROUTING_V1.md`

Use when:
- moving work from execution-ready state to implementation, verification, release/handoff, and in-use verification
- deciding delivery mode or delivery governance shape
- selecting professional delivery controls for software or other governed change work

### 4. Security / authority / control changes
Start with:
- `SECURITY_PROCESS_V1.md`
- `governance/`
- `products/security/`
- `PROJECT_PROCESS_ROUTING_V1.md`

Use when:
- a change affects security boundaries, authority, credentials, permissions, or recovery posture
- approval or escalation rules may be triggered

### 5. Product management / product operating loop
Start with:
- `PRODUCT_WAY_OF_WORKING_PROCESS_V1.md`
- relevant product artifacts under `products/<slug>/`
- `PROJECT_PROCESS_ROUTING_V1.md`

Use when:
- updating product vision, goals, plan, risks, interfaces, or decisions
- running product reviews or changing product priorities

### 6. Error / incident / corrective action
Start with:
- `ERROR_REPORTING_STANDARD_V1.md`
- `CLOSED_LOOP_IMPROVEMENT_MODEL_V1.md`
- `CONTINUOUS_IMPROVEMENT_PROCESS_V1.md`
- relevant owning product or governance artifacts

Use when:
- a meaningful error, miss, control failure, near-miss, or incident occurred
- corrective or preventive action needs canonical routing and verification

### 7. Continuous improvement / process refinement
Start with:
- `CONTINUOUS_IMPROVEMENT_PROCESS_V1.md`
- `products/improvement/`
- `PROJECT_PROCESS_ROUTING_V1.md`

Use when:
- recurring friction or repeated misses indicate a system improvement need
- process routing, discovery, or operability needs tightening

### 8. Workspace setup / retrofit / local operability
Start with:
- `WORKSPACE_OPERATING_PACKAGE_STANDARD_V1.md`
- `PROCESS_DISCOVERY_INDEX_STANDARD_V1.md`
- `WORKSPACE_BOOTSTRAP_AND_RETROFIT_PROTOCOL_V1.md`
- any workspace-local `PROCESS_DISCOVERY_INDEX.md` and `SOURCE_OF_TRUTH.md`

Use when:
- bootstrapping or retrofitting a workspace
- deciding what must be locally authoritative versus consumed from shared/product outputs
- assessing whether a workspace is truly operable

## Related authority artifacts
- `AGENTS.md`
- `PROCESS_REGISTRY.md`
- `PROCESS_OWNERSHIP_MODEL_V1.md`
- `PROCESS_OWNERSHIP_AND_COORDINATION_RULE_V1.md`
- `PROJECT_PROCESS_ROUTING_V1.md`
- `PROJECT_CLASSIFICATION_USAGE_RULE_V1.md`
- `processes/PROCESS_ROUTE_REGISTRY_V1.yaml`
- `processes/standards/PROCESS_ROUTE_SCHEMA_V1.yaml`
- `processes/PROJECT_CLASSIFICATION_REGISTRY_V1.yaml`
- `processes/standards/PROJECT_CLASSIFICATION_RECORD_SCHEMA_V1.yaml`
- `WORKSPACE_OPERATING_PACKAGE_STANDARD_V1.md`
- `PROCESS_DISCOVERY_INDEX_STANDARD_V1.md`

## Notes
- This artifact is a root routing layer, not a parallel process manual.
- Product-owned recurring processes should remain with the owning product.
- Shared artifacts should define only genuine cross-product coordination, common routing, or platform-level constraints.

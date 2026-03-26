# Interfaces

## Purpose
Define how Task Management interacts with upstream governance/runtime elements and downstream consumers.

## Upstream interfaces
### Governance
Provides:
- policy and boundary conditions
- readiness and evidence expectations
- escalation rules for material changes

### Lyra runtime
Provides:
- agent execution environment
- jobs, sessions, memory, and operating context
- automation pathways for product execution

### TDE contract artifacts
Provide:
- intake/output expectations
- task/decision operating semantics
- readiness and evidence patterns

## Downstream interfaces
### `pxs` workspace
Consumes:
- task/decision management capability
- operating patterns and delivery mechanisms
- future explicit interfaces for invoking or embedding product functionality

## Current interface problems
- some boundaries are still documented indirectly across multiple artifacts
- some product behavior still depends on workspace context rather than explicit contracts
- downstream consumption path is clear strategically but not yet fully formalized operationally

## Interface design rules
1. No hidden cross-workspace coupling.
2. Product responsibilities must be explicit.
3. Consumer adoption should rely on documented interfaces, not tribal knowledge.
4. Where possible, prefer stable contracts over chat-history assumptions.

## Named downstream interface
### `pxs` consumption interface
Canonical artifact:
- `06-architecture/PXS_CONSUMPTION_INTERFACE.md`

This interface defines:
- what `pxs` consumes from Task Management
- what remains internal to the product
- consumer obligations
- provider obligations
- what evidence makes the interface operationally usable

## Named intake interface
### TDE intake interface contract
Canonical artifact:
- `06-architecture/TDE_INTAKE_INTERFACE_CONTRACT_V1.md`

This interface defines:
- the canonical intake surface for TDE
- the intake classes accepted by Task Management
- producer adapter expectations
- validation and persistence expectations
- how local process discovery should point to product-owned intake behavior without duplicating it

### TDE PO nightly report adapter contract
Canonical artifact:
- `06-architecture/TDE_PO_NIGHTLY_REPORT_ADAPTER_CONTRACT_V1.md`

This interface defines:
- the first real upstream producer adapter for nightly product-owner reporting
- how Control Panel / nightly report signals become canonical TDE `signal` intake packets
- validation expectations for both source report and canonical intake packet
- provenance and enrichment rules for the producer chain

### TDE error-to-corrective-action policy
Canonical artifact:
- `06-architecture/TDE_ERROR_TO_CORRECTIVE_ACTION_POLICY_V1.md`

This interface/policy bridge defines:
- how structured error/control reports connect to canonical TDE corrective action
- why error reporting and TDE action tracking are distinct but linked layers
- the first adapter path from error reports into canonical TDE intake packets

### TDE assignment acceptance contract
Canonical artifact:
- `06-architecture/TDE_ASSIGNMENT_ACCEPTANCE_CONTRACT_V1.md`

This contract defines:
- why direct task insertion is not assignment success
- the first explicit acceptance states returned to a producer
- the thin runtime path by which a producer can know whether TDE actually accepted operational responsibility

## Minimum improvement interface
### Task Management -> Improvement interface
- compact-surface drift, stale steering surfaces, and recurring product-control gaps must not remain prose-only observations
- when those gaps are material or repeated, Task Management should route them into canonical TDE-linked improvement work rather than a parallel tracker
- the linked improvement intake should carry `source_system`, `source_reference`, `product_scope`, `evidence_links`, `improvement_type`, and `expected_closure_evidence`
- closure requires linked evidence plus explicit source-to-closure trace
- open Task-Management-origin improvement items should remain visible in recurring product review until dispositioned or closed

### First bounded deployment rule
- initial deployment scope for the minimum product-side improvement interface is compact-surface drift and stale steering/control surfaces
- seed reference: `products/task-management/04-execution/nightly-reports/2026-03-21-po-nightly-report.json`
- canonical path: Task Management surfaces detect the drift/control gap; TDE holds the task state; Improvement governs the source-to-closure discipline

## Next interface work
- map current TDE artifacts to the product interface surface
- make the TDE machine-execution boundary explicit relative to prompt-level work and executive/control-plane objects
- define a clearer invocation rule for when downstream work should enter TDE versus remain outside the execution plane
- strengthen the external-object linking model so TDE executes against domain objects without absorbing them into one blended pool
- extend intake ingest beyond the first `signal` path
- add clearer operational examples for `pxs` usage
- decide whether a capability-pack or service boundary is the better long-term distribution shape

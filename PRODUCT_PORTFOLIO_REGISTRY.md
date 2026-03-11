# Product Portfolio Registry v1

## Purpose
Maintain explicit product boundaries across OS and PX initiatives, reduce accidental coupling, and preserve optionality for future SaaS/commercialization.

## Portfolio Rules
1. Treat each initiative as a product with explicit ownership and boundaries.
2. ID convention: external/customer-facing product lines use `A-xxx`; internal control-plane products use `CP-xxx`.
3. Products may depend on **Platform/Shared** capabilities, not directly on other products, unless approved by ADR.
4. Cross-product reuse requires a published interface contract and versioning policy.
5. Customer-facing/SaaS-candidate products must isolate data, identity, and deployment paths.
6. Product transfer unit is a **Product Assembly** (one product may include multiple artifact types).
7. Every product record must declare distribution and activation lanes for each artifact type.

## Product Record Schema
- Product ID
- Product Name
- Domain (OS / PX)
- Type (Internal / Client-facing / SaaS candidate)
- Owner
- Status (Discovery / Active / Maintenance / Retired)
- Revenue Potential (Low / Medium / High)
- Data Classification (Internal / Sensitive / Customer)
- Tenant Model (N/A / Single-tenant / Multi-tenant-ready)
- Canonical Repo
- Deployment Boundary
- Allowed Dependencies (Platform only by default)
- Prohibited Dependencies
- Public Interfaces (API/events/contracts)
- Artifacts (`service`, `skill-pack`, `policy-pack`, `schema-pack`, `ops-pack`)
- Distribution (per artifact: `cron|daemon`, `managed-skills|workspace-skills|extraDirs|plugin`, `submodule|subtree|release`)
- Activation (how each artifact is enabled at runtime)
- Enforcement (required checks/gates/evidence)
- Audit/Compliance Notes

## Products

### CP-001
- Product ID: `CP-001`
- Product Name: Control Panel
- Domain: OS
- Type: Internal (SaaS-candidate potential)
- Owner: Peter/Lyra
- Status: Active
- Revenue Potential: Medium (future)
- Data Classification: Internal → potentially Customer (future)
- Tenant Model: N/A currently; Multi-tenant-ready target if externalized
- Canonical Repo: `repos/control-panel`
- Canonical Product Model Path: `products/control-panel/`
- Legacy Management Path: `products/CP-001-control-panel/management/`
- Deployment Boundary: Separate service/runtime from other products
- Allowed Dependencies: Platform/shared libraries with stable interfaces
- Prohibited Dependencies: Direct runtime dependency on PX product codebases
- Public Interfaces: To be defined in boundary doc
- Artifacts: `service` (control-panel runtime), `skill-pack` (operator/runbook guidance), `policy-pack` (change-control + safety policy)
- Distribution: service=`daemon`; skill-pack=`workspace-skills`; policy-pack=`submodule` (version-pinned)
- Activation: service via domain-scoped runtime config; skill-pack via workspace load precedence; policy-pack via referenced governance docs/checks
- Enforcement: evidence pack required for production-bound changes; approval gate for authority/security-impacting changes
- Audit/Compliance Notes: Must retain WO/CA traceability for all production-bound changes

### A-001 to A-003 (Placeholders)
- Product IDs: `A-001`, `A-002`, `A-003`
- Status: Discovery (metadata pending)
- Owner: TBD
- Legacy management path pattern: `products/<product-id>/management/`
- Canonical Product Model Paths: `products/A-001-thin/`, `products/A-002-thin/`, `products/A-003-thin/`
- Notes: These remain discovery placeholders. Thin Product-as-Code folders now reserve the canonical future structure without inventing product detail.

### A-004
- Product ID: `A-004`
- Product Name: Security
- Domain: OS
- Type: Internal
- Owner: Lyra
- Status: Active
- Revenue Potential: Medium (indirect; trust and deployment enabling)
- Data Classification: Sensitive
- Tenant Model: Single-customer operational context currently; stronger isolation required before multi-customer packaging
- Canonical Repo: `.` (workspace-level product spanning security policy, posture, evidence, research conversion, and deployment requirements)
- Canonical Product Model Path: `products/security/`
- Legacy Management Path: `products/A-004/management/`
- Deployment Boundary: Workspace/process boundary with customer impact through PXS deployment posture and security requirements
- Allowed Dependencies: Platform/shared capabilities, governance records, approved product interfaces, security evidence sources, and security research in the library
- Prohibited Dependencies: Hidden cross-product coupling, silent trust-boundary/access expansion, unreviewed high-privilege external tooling
- Public Interfaces: Security requirements, posture summaries, residual-risk decisions, evidence/review outputs, control/policy guidance
- Artifacts: `policy-pack`, `ops-pack`, `management artifacts`, `evidence artifacts` (current); future `schema-pack` / tooling support possible
- Distribution: policy-pack=`workspace|submodule|subtree|release`; ops-pack=`workspace|workspace-docs`; management artifacts=`workspace`; evidence artifacts=`cron|workspace-docs`
- Activation: via product operating cadence, security reviews, evidence generation, and deployment requirements applied to PXS
- Enforcement: escalation for trust-boundary/credential/access/exposure changes; routine audit evidence; explicit decision records for material risk acceptance
- Audit/Compliance Notes: Security is an enabling constraint across products; current operating mode assumes internal/single-customer trust posture and requires explicit review before broader externalization

### A-007
- Product ID: `A-007`
- Product Name: Task Management
- Domain: OS
- Type: Internal
- Owner: Lyra
- Status: Active
- Revenue Potential: High (capability-enabling; future productization potential)
- Data Classification: Internal, with future customer-operational implications through consuming workspaces
- Tenant Model: N/A currently; should evolve toward multi-tenant-ready interface discipline if externalized
- Canonical Repo: `.` (workspace-level product spanning TDE, task/decision automation contracts, and delivery mechanisms into consuming workspaces)
- Canonical Product Model Path: `products/task-management/`
- Legacy Management Path: `products/A-007/management/`
- Deployment Boundary: Workspace/process boundary now; future capability-pack and/or deterministic service boundary for consumer delivery
- Allowed Dependencies: Platform/shared capabilities; approved governance/process artifacts; explicit downstream integration artifacts for consuming workspaces
- Prohibited Dependencies: Hidden cross-workspace coupling; undocumented authority escalation; direct consumer-state ownership beyond approved interfaces
- Public Interfaces: TDE intake/output contracts, job/binding primitives, task/decision evidence artifacts, future capability/service interfaces for consuming workspaces such as `pxs`
- Artifacts: `ops-pack`, `schema-pack`, `policy-pack`, `management artifacts`, with future `service` and `skill-pack` potential
- Distribution: ops-pack=`workspace|cron`; schema-pack=`workspace|release`; policy-pack=`workspace|submodule|subtree|release`; management artifacts=`workspace`; future service=`daemon|plugin`
- Activation: via workspace task/decision operating docs, TDE runtime/job bindings, evidence-backed deployment decisions, and future capability distribution into consuming workspaces
- Enforcement: TDE production readiness gate, explicit GO decision, evidence-backed cutover, interface/boundary controls, and escalation for material real-world-impact changes
- Audit/Compliance Notes: Task Management may proceed to full TDE deployment once technical requirements are fulfilled and evidence is recorded; larger deployment decisions and real-world-impacting changes remain visible to Peter

### A-005
- Product ID: `A-005`
- Product Name: Improvement
- Domain: OS
- Type: Internal
- Owner: Lyra
- Status: Active
- Revenue Potential: Medium (indirect; capability-enabling)
- Data Classification: Internal
- Tenant Model: N/A currently
- Canonical Repo: `.` (workspace-level product spanning portfolio improvement process, assemblies, and deployment controls)
- Canonical Product Model Path: `products/improvement/`
- Legacy Management Path: `products/A-005/management/`
- Deployment Boundary: Workspace/process boundary with deployment into PXS via managed assembly consumption
- Allowed Dependencies: Platform/shared capabilities; approved product management artifacts; PXS assembly lock and deployment docs for consumption state
- Prohibited Dependencies: Hidden cross-domain reads/writes; undocumented product-specific runtime coupling; authority/security-impacting changes without escalation
- Public Interfaces: Continuous improvement process, cadence checklist, improvement log conventions, deployment/verification mechanism for improvement assembly
- Artifacts: `policy-pack`, `ops-pack`, `skill-pack`, `management artifacts`
- Distribution: policy-pack=`submodule|subtree|release`; ops-pack=`workspace-skills|workspace-docs|assembly`; skill-pack=`workspace-skills|managed-skills`; management artifacts=`workspace`
- Activation: via product operating cadence, assembly activation in PXS, and linked improvement logs / execution artifacts
- Enforcement: every accepted improvement requires owner + success signal + review date; authority/security-impacting changes require approval gate; deployment changes require lockfile + evidence updates
- Audit/Compliance Notes: Improvement owns portfolio-wide process design but does not self-authorize high-risk boundary changes; larger strategic or real-world-consequence changes are surfaced to Peter

### A-006
- Product ID: `A-006`
- Product Name: Delivery
- Domain: OS
- Type: Internal
- Owner: Lyra
- Status: Active
- Revenue Potential: Medium (indirect; capability-enabling)
- Data Classification: Internal
- Tenant Model: N/A currently
- Canonical Repo: `.` (workspace-level product spanning workspace delivery assets and related repos)
- Canonical Product Model Path: `products/delivery/`
- Legacy Management Path: `products/A-006/management/`
- Deployment Boundary: Workspace/process boundary for software creation, verification, release readiness, and delivery-system improvement
- Allowed Dependencies: Platform/shared capabilities; approved product-specific repos and workspace assemblies required for delivery work
- Prohibited Dependencies: Unapproved cross-product runtime coupling; undocumented external delivery dependencies
- Public Interfaces: Delivery process, gate/checklist artifacts, definition-of-done standards, future delivery-management tooling/interfaces
- Artifacts: `ops-pack`, `policy-pack`, `tooling/process assets` (current), with future `service` potential for delivery-management surfaces
- Distribution: ops-pack=`workspace-skills|workspace-docs`; policy-pack=`submodule|subtree|release`; tooling/process assets=`workspace|repo`
- Activation: via workspace operating docs, product management artifacts, delivery gates/checklists, and future automation or services
- Enforcement: explicit acceptance criteria, evidence-backed completion, risk-aware review, and escalation for strategic/real-world-consequence changes
- Audit/Compliance Notes: Delivery owns DevSecOps discipline for capability development; strategic shifts, launches, and real-world consequence actions require Peter involvement

## Shared Components Registry (initial)
Use this list for components intended for reuse across products.

| Component | Owner | Stability | Consumers | Versioning | Notes |
|---|---|---|---|---|---|
| (none yet) | - | - | - | - | Add only after ADR approval |

## Review Cadence
- Monthly portfolio boundary review
- Quarterly commercialization readiness review for SaaS-candidate products

## Version
- v1.0
- Date: 2026-02-27
- Owner: Peter/Lyra

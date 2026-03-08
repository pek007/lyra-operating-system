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
- Deployment Boundary: Separate service/runtime from other products
- Allowed Dependencies: Platform/shared libraries with stable interfaces
- Prohibited Dependencies: Direct runtime dependency on PX product codebases
- Public Interfaces: To be defined in boundary doc
- Artifacts: `service` (control-panel runtime), `skill-pack` (operator/runbook guidance), `policy-pack` (change-control + safety policy)
- Distribution: service=`daemon`; skill-pack=`workspace-skills`; policy-pack=`submodule` (version-pinned)
- Activation: service via domain-scoped runtime config; skill-pack via workspace load precedence; policy-pack via referenced governance docs/checks
- Enforcement: evidence pack required for production-bound changes; approval gate for authority/security-impacting changes
- Audit/Compliance Notes: Must retain WO/CA traceability for all production-bound changes

### A-001 to A-005, A-007 (Placeholders)
- Product IDs: `A-001`, `A-002`, `A-003`, `A-004`, `A-005`, `A-007`
- Status: Discovery (metadata pending)
- Owner: TBD
- Canonical management path: `products/<product-id>/management/`
- Notes: Baseline management artifact sets have been instantiated; Product Owners should fill product-specific content.

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

# Product Portfolio Registry v1

## Purpose
Maintain explicit product boundaries across OS and PX initiatives, reduce accidental coupling, and preserve optionality for future SaaS/commercialization.

## Portfolio Rules
1. Treat each initiative as a product with explicit ownership and boundaries.
2. Products may depend on **Platform/Shared** capabilities, not directly on other products, unless approved by ADR.
3. Cross-product reuse requires a published interface contract and versioning policy.
4. Customer-facing/SaaS-candidate products must isolate data, identity, and deployment paths.

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
- Audit/Compliance Notes

## Products

### P-001
- Product ID: `P-001`
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
- Audit/Compliance Notes: Must retain WO/CA traceability for all production-bound changes

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

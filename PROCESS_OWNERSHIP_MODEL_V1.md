# Process Ownership Model v1

## Decision
Adopt **product-owned process governance**.

- Every process must have an **owning product**.
- The platform is treated as an internal product: **P-PLATFORM (Lyra OS Platform)**.
- Interface processes (cross-product) are owned by the **dominant product** with required co-approver(s).

## Why
- Single accountability path per process.
- Cleaner governance than parallel process-owner structures.
- Aligns with Product Assembly model and product-owner operating rhythm.

## Ownership Types

### 1) Product-Internal Process
- Scope: one product only.
- Owner: that product owner.
- Example: PXS task/decision workflow internals.

### 2) Platform Process
- Scope: cross-cutting standards/governance provided by platform.
- Owner: P-PLATFORM owner.
- Example: authority-change rules, config-change controls.

### 3) Interface Process
- Scope: handoff between products.
- Owner: dominant product.
- Required approver: impacted counterparty product owner.
- ADR trigger: boundary, authority, or dependency exceptions.

## Required Metadata for New/Updated Processes
- `owning_product`
- `ownership_type` (`product-internal` | `platform` | `interface`)
- `dominant_product` (required for `interface`)
- `required_approvers` (required for `interface`)
- `assemblies_using_process` (optional but recommended)

## Governance Rules
1. No process without an owning product.
2. Interface process changes cannot be self-approved if they increase authority/risk.
3. If dominant ownership is disputed, default owner is P-PLATFORM until ADR resolves.
4. Process docs should be packaged through Product Assemblies where reusable.

## Initial Product Mapping
- **P-PLATFORM (Lyra OS Platform)** — internal product for governance/runtime/process backbone.
- **PXS** — execution/product implementation environment.

## Review Cadence
- Monthly review of interface processes and approver mappings.
- Quarterly review of platform-process scope to avoid over-centralization.

## Version
- v1.0
- Date: 2026-03-07
- Owner: Peter/Lyra

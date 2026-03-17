# Interfaces Capabilities

Status: Draft active capability record
Product: A-009 Interfaces
Owner: Lyra
Standard: `CAPABILITY_MODEL_STANDARD_V1.md`
Date: 2026-03-17

## A-009.C1 — Interface contract discipline
- Owning product: Interfaces
- Purpose: Make cross-product and cross-workspace interfaces explicit, reviewable, and stable enough to reduce hidden coupling.
- Scope / boundary: Owns cross-cutting interface discipline and templates; does not absorb every provider product’s concrete interface surface
- Primary consumers: all products, `pxs`
- Delivery mode(s): interface docs + standards + product architecture artifacts
- Entrypoint / interface: product `06-architecture/INTERFACES.md` artifacts and shared interface standards
- Canonical artifacts: `PRODUCT.md`, `06-architecture/INTERFACES.md`, relevant decisions
- Dependencies: provider products, governance rules, delivery-mode decisions
- Constraints / guardrails: provider-specific interfaces remain provider-owned
- Readiness: usable
- Lifecycle state: active
- Evidence: explicit interface product established and referenced by downstream work
- Known gaps / risks: still under-executed relative to importance; contracts not yet uniformly formalized
- Upgrade / retirement trigger: upgrade when product-local capability records adopt shared interface conventions consistently

## A-009.C2 — OS -> PXS export/import boundary model
- Owning product: Interfaces
- Purpose: Define how capabilities cross from Lyra OS into `pxs` without hidden coupling.
- Scope / boundary: Owns connector/packaging discipline for crossing the boundary; does not own all provider-side behavior
- Primary consumers: `pxs`, Vega
- Delivery mode(s): interface docs + packaging rules + workspace package conventions
- Entrypoint / interface: boundary/interface docs, consumption interfaces, workspace package implications
- Canonical artifacts: `06-architecture/INTERFACES.md`, provider-side `PXS_CONSUMPTION_INTERFACE.md`, boundary/acceptance artifacts
- Dependencies: Task Management, Governance, Security, workspace operating package model
- Constraints / guardrails: no implicit cross-workspace assumptions; import/export logic must be reviewable
- Readiness: usable
- Lifecycle state: active
- Evidence: Phase 1 Vega/PXS acceptance pass and workspace retrofit path
- Known gaps / risks: still relies on process discipline and interim copies more than strong packaged boundaries
- Upgrade / retirement trigger: upgrade when repeatable packaging and versioned import/export discipline exists

## A-009.C3 — Capability packaging and versioning model
- Owning product: Interfaces
- Purpose: Define how capabilities become portable, versioned, and consumable units rather than loose local artifacts.
- Scope / boundary: Owns packaging/versioning/connector discipline; does not force every capability into a heavy service boundary
- Primary consumers: future downstream workspaces, provider products
- Delivery mode(s): interface docs + packaging/versioning standards + eventual schema/assembly support
- Entrypoint / interface: packaging and connector decisions, future capability-pack conventions
- Canonical artifacts: `PRODUCT.md`, `06-architecture/INTERFACES.md`, delivery-mode framework, capability standards
- Dependencies: product-local capability records, delivery-mode decisions, governance
- Constraints / guardrails: choose the lightest packaging mode that preserves clarity and governance fitness
- Readiness: draft
- Lifecycle state: building
- Evidence: capability inventory + new capability standards now make the need explicit
- Known gaps / risks: one of the major current bottlenecks; “skills” vs ops-pack vs schema-pack vs assembly remains under-specified
- Upgrade / retirement trigger: upgrade when first repeatable multi-consumer packaging pattern is proven

# Task Management Capabilities

Status: Draft active capability record
Product: A-007 Task Management
Owner: Lyra
Standard: `CAPABILITY_MODEL_STANDARD_V1.md`
Date: 2026-03-17

## Purpose
Make the current Task Management capability layer explicit as the managed unit between product purpose and downstream delivery.

---

## A-007.C1 — Canonical task state management
- Owning product: Task Management
- Purpose: Provide canonical, queryable, governable task state for Lyra OS execution.
- Scope / boundary: Owns task-state canon and readable projection; does not own all downstream local planning systems.
- Primary consumers: `main`, operators
- Delivery mode(s): runtime tooling + DB-backed canonical state + generated projection
- Entrypoint / interface: `os/runtime/tde_state.sqlite`, `os/runtime/TASKS_from_db.md`, TDE runtime tools
- Canonical artifacts: `PRODUCT.md`, `03-operating-model/*`, `06-architecture/INTERFACES.md`
- Dependencies: Lyra runtime, TDE state store, product governance rules
- Constraints / guardrails: canonical state must not regress to legacy markdown board authority
- Readiness: proven
- Lifecycle state: active
- Evidence: DB cutover readiness artifacts, projection generation, live runtime usage
- Known gaps / risks: downstream `pxs` local task-state consumption not yet proven end-to-end
- Upgrade / retirement trigger: upgrade when multi-consumer downstream use stabilizes

## A-007.C2 — Decision and evidence linkage in execution flow
- Owning product: Task Management
- Purpose: Link tasks, decisions, and evidence so execution is traceable and governable.
- Scope / boundary: Owns execution-plane linkage semantics; does not replace governance product’s decision-rights ownership
- Primary consumers: `main`, operators
- Delivery mode(s): runtime tooling + operating rules + schema-adjacent contracts
- Entrypoint / interface: task metadata, intake packets, TDE decision/evidence artifacts
- Canonical artifacts: `07-decisions/*`, `06-architecture/TDE_*_CONTRACT_V1.md`
- Dependencies: Governance, runtime tooling, evidence generation
- Constraints / guardrails: must preserve auditability and fail-closed behavior on invalid transitions
- Readiness: usable
- Lifecycle state: active
- Evidence: assignment acceptance tests, decision advancement/runtime embodiment work
- Known gaps / risks: capability exists in practice but is not yet uniformly expressed across all TDE flows
- Upgrade / retirement trigger: upgrade when all major TDE flows share explicit contracts and verification

## A-007.C3 — Assignment acceptance / intake-to-task conversion
- Owning product: Task Management
- Purpose: Accept structured work into TDE with explicit validation, persistence, and acceptance semantics.
- Scope / boundary: Owns canonical intake and acceptance behavior; producers remain outside the product boundary
- Primary consumers: `main`, future product adapters, downstream workspaces
- Delivery mode(s): runtime tooling + schema contract
- Entrypoint / interface: `06-architecture/TDE_INTAKE_INTERFACE_CONTRACT_V1.md`, `06-architecture/TDE_ASSIGNMENT_ACCEPTANCE_CONTRACT_V1.md`
- Canonical artifacts: intake/acceptance contracts, TDE tooling
- Dependencies: TDE state store, schema validation, producer adapters
- Constraints / guardrails: direct task insertion is not equivalent to accepted operational responsibility
- Readiness: proven
- Lifecycle state: active
- Evidence: assignment acceptance integration tests and live probe
- Known gaps / risks: downstream producer packaging and examples still maturing
- Upgrade / retirement trigger: upgrade when multiple producers consume the interface routinely

## A-007.C4 — Autonomous chaining / readiness promotion
- Owning product: Task Management
- Purpose: Progress bounded successor work automatically when predecessor state justifies it.
- Scope / boundary: Owns deterministic readiness promotion only; not unrestricted autonomous scope expansion
- Primary consumers: `main`
- Delivery mode(s): runtime tooling + policy rules + evidence-backed rollout control
- Entrypoint / interface: `tools/tde_chaining.py`, job tick runner, chaining metadata
- Canonical artifacts: chaining design/implementation artifacts, runtime tools
- Dependencies: canonical task state, policy rules, job tick runtime
- Constraints / guardrails: bounded progression, approval-gate respect, idempotence, rollback path
- Readiness: usable
- Lifecycle state: active
- Evidence: chaining tests, pilot rollout, broader rollout review
- Known gaps / risks: broader downstream consumption model not yet defined; boundedness policy still evolving
- Upgrade / retirement trigger: upgrade when downstream consumers need the same pattern under explicit contracts

## A-007.C5 — PXS task-management consumption interface
- Owning product: Task Management
- Purpose: Let `pxs` consume task/decision management capability without relying on hidden thread memory.
- Scope / boundary: Owns provider-side interface and obligations; does not own `pxs` local operating package itself
- Primary consumers: `pxs`, Vega
- Delivery mode(s): workspace artifacts + ops-pack style assets + provider interface docs
- Entrypoint / interface: `06-architecture/PXS_CONSUMPTION_INTERFACE.md`
- Canonical artifacts: `PXS_CONSUMPTION_INTERFACE.md`, delivery mode decision, workspace package standards
- Dependencies: Interfaces, Governance, `pxs` local operating package
- Constraints / guardrails: no hidden cross-workspace coupling; consumer obligations must be explicit
- Readiness: usable
- Lifecycle state: active
- Evidence: Vega/PXS acceptance pass (Phase 1), `pxs` workspace retrofit
- Known gaps / risks: domain-local TDE execution inside `pxs` is not yet proven; current delivery remains artifact-based rather than packaged
- Upgrade / retirement trigger: upgrade when `pxs` consumption becomes repeatable enough for stronger packaging

## A-007.C6 — Human-readable task projection
- Owning product: Task Management
- Purpose: Provide a readable task projection for operators and integrations without restoring markdown as canonical authority.
- Scope / boundary: Projection only; not system of record
- Primary consumers: operators, audits, Trello sync, reviews
- Delivery mode(s): generated projection
- Entrypoint / interface: `os/runtime/TASKS_from_db.md`, `tools/generate_tasks_view.py`
- Canonical artifacts: projection generator and runtime projection file
- Dependencies: canonical DB state
- Constraints / guardrails: must remain clearly non-authoritative
- Readiness: proven
- Lifecycle state: active
- Evidence: live projection-backed tooling migration, hygiene checks
- Known gaps / risks: historical references to retired root `TASKS.md` still need gradual cleanup
- Upgrade / retirement trigger: upgrade when projection format or downstream integrations need stronger contracts

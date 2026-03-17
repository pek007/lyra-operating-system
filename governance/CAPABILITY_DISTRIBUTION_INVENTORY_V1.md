# Capability Distribution Inventory v1

Status: Draft active inventory
Date: 2026-03-17
Owner: Lyra
Purpose: Make the current Lyra OS capability layer explicit by mapping each product to the capabilities it currently provides, how those capabilities are distributed, who can consume them, and where the main gaps remain.

---

## Why this exists

Lyra OS already has substantial product strategy, plan, governance, and implementation artifacts in code.
What is still missing is a clear **capabilities-as-code layer** answering:

1. What capabilities do we actually have now?
2. Which product owns each capability?
3. How is each capability distributed?
4. Who can consume it today?
5. What is real vs aspirational?

This inventory is the first cross-product answer.

---

## Terms

- **Capability** = what the system can actually do for a consumer.
- **Distribution mode** = how that capability is delivered/consumed.
- **Consumers** = who can use it now (`main`, `pxs`, Vega, operators, future workspaces).
- **Readiness**
  - `draft` = concept/artifacts exist but capability is not yet proven in use
  - `usable` = capability can be used now in bounded form
  - `proven` = capability has been exercised with evidence and is dependable enough for normal use
  - `scaled` = capability is reusable across multiple consumers with explicit interface discipline

---

## Distribution modes used in this inventory

- **governance artifacts** — policy/process/decision docs
- **workspace artifacts** — consumer-local operating package/front-door docs
- **ops-pack style assets** — explicit operating rules, runbooks, local package layers
- **schema contract** — machine-checkable input/output or interface contract
- **runtime tooling** — scripts/tools/DB-backed runtime behavior
- **projection** — human-readable generated view over canonical state
- **cron loop** — scheduled operational execution
- **service/UI** — operator-facing runtime surface
- **interim copy** — tracked temporary artifact copy pending cleaner packaging/distribution

---

## Product capability inventory

## A-007 — Task Management
Primary product focus: TDE / task and decision execution plane.

- **A-007.C1 — Canonical task state management**
  - Distributed via: runtime tooling + DB-backed canonical state (`os/runtime/tde_state.sqlite`) + projection (`os/runtime/TASKS_from_db.md`)
  - Consumers: `main`
  - Readiness: **proven**
  - Main gaps: downstream `pxs` local execution not yet proven; some historical doc residue remains

- **A-007.C2 — Decision and evidence linkage in execution flow**
  - Distributed via: runtime tooling + schema-adjacent conventions + operating rules
  - Consumers: `main`
  - Readiness: **usable**
  - Main gaps: capability exists in practice but is not yet normalized into an explicit capability contract

- **A-007.C3 — Assignment acceptance / intake-to-task conversion**
  - Distributed via: runtime tooling + intake contracts + DB-backed persistence
  - Consumers: `main`, future downstream workspaces
  - Readiness: **proven**
  - Main gaps: downstream consumer packaging/interface still maturing

- **A-007.C4 — Autonomous chaining / successor readiness promotion**
  - Distributed via: runtime tooling + policy rules + evidence-backed rollout controls
  - Consumers: `main`
  - Readiness: **usable**
  - Main gaps: broader downstream consumer model not yet defined; governance of fallback/limits still maturing

- **A-007.C5 — PXS task-management consumption interface**
  - Distributed via: workspace artifacts + ops-pack style assets + supporting interface docs
  - Consumers: `pxs`, Vega
  - Readiness: **usable**
  - Main gaps: domain-local TDE execution inside `pxs` is not yet proven; current delivery remains artifact-based rather than packaged

- **A-007.C6 — Human-readable task projection**
  - Distributed via: generated projection (`os/runtime/TASKS_from_db.md`)
  - Consumers: operators, Trello sync, audits, reviews
  - Readiness: **proven**
  - Main gaps: historical confusion from retired root `TASKS.md` still needs gradual cleanup in archives/docs

---

## A-008 — Governance
Primary product focus: explicit system rules, decision rights, and control discipline.

- **A-008.C1 — System governance / change-control rules**
  - Distributed via: governance artifacts
  - Consumers: all products, `main`, future workspaces
  - Readiness: **usable**
  - Main gaps: still fragmented across multiple artifacts; no single capability map until this inventory

- **A-008.C2 — Decision-record discipline**
  - Distributed via: governance artifacts + decision templates/records
  - Consumers: all products, operators
  - Readiness: **usable**
  - Main gaps: uneven adoption; some decisions still land in memory or synthesis before canonically closing

- **A-008.C3 — Error reporting standard / control-failure loop**
  - Distributed via: governance artifacts + error report templates
  - Consumers: all products, `main`
  - Readiness: **usable**
  - Main gaps: pipeline from report -> corrective task is improving but not yet fully productized everywhere

- **A-008.C4 — Workspace operating package standard**
  - Distributed via: governance artifacts + workspace artifacts + retrofit/validation protocol
  - Consumers: `pxs`, future workspaces
  - Readiness: **usable**
  - Main gaps: current downstream packages are still Level 1 / minimal

---

## A-004 — Security
Primary product focus: practical controls, usable guardrails, and evidence-backed risk reduction.

- **A-004.C1 — Security baseline / posture guidance**
  - Distributed via: governance artifacts + product-local security docs + review checklists
  - Consumers: `main`, operators, future deployments, `pxs`
  - Readiness: **usable**
  - Main gaps: some controls remain guidance-heavy rather than enforced automatically

- **A-004.C2 — Boundary review and acceptance discipline**
  - Distributed via: product-local boundary docs + acceptance test artifacts + decisions
  - Consumers: `main`, Vega, `pxs`
  - Readiness: **usable**
  - Main gaps: Phase 1 posture intentionally leaves exec open; long-term hard compartmentalization not yet implemented

- **A-004.C3 — Security review / audit loop**
  - Distributed via: cron loops + review artifacts + evidence snapshots
  - Consumers: operators, `main`
  - Readiness: **usable**
  - Main gaps: some sweeps still convert findings through legacy wording/surfaces rather than fully capability-native interfaces

---

## A-006 — Delivery
Primary product focus: build/change/verify/package/release safely and with evidence.

- **A-006.C1 — Verification and release-readiness discipline**
  - Distributed via: runbooks + tests + evidence artifacts + operator practice
  - Consumers: `main`, operators
  - Readiness: **usable**
  - Main gaps: delivery capability exists but is still spread across tools, SOPs, and product-local evidence rather than a normalized packaged interface

- **A-006.C2 — Safe shipping workflow for Lyra OS changes**
  - Distributed via: runtime tooling + tests + git workflow + evidence publication
  - Consumers: `main`
  - Readiness: **proven**
  - Main gaps: some git/sync controls still depend on operator discipline; nested repo topology remains a recurring complexity source

- **A-006.C3 — Downstream capability packaging support**
  - Distributed via: product-local artifacts + interfaces work + delivery-mode decisions
  - Consumers: `pxs`, future workspaces
  - Readiness: **draft**
  - Main gaps: not yet a clean packaging/service layer; still dependent on artifact-based delivery

---

## A-005 — Improvement
Primary product focus: closed-loop learning and prevention.

- **A-005.C1 — Incident-to-improvement conversion**
  - Distributed via: governance artifacts + task-management linkage + operating rules
  - Consumers: all products, `main`
  - Readiness: **usable**
  - Main gaps: canonical intake substrate is still being matured; first full conversion template only recently proven

- **A-005.C2 — Continuous improvement sweep / backlog creation**
  - Distributed via: cron loop + docs hygiene bundle + evidence + TDE intake flow
  - Consumers: `main`, operators
  - Readiness: **usable**
  - Main gaps: still some historical references and process wording from pre-DB-canonical era

- **A-005.C3 — Closed-loop prevention model**
  - Distributed via: governance/process artifacts + improvement product docs
  - Consumers: all products
  - Readiness: **draft**
  - Main gaps: product concept is clear, but reusable downstream deployment pattern is not yet mature

---

## A-009 — Interfaces
Primary product focus: explicit contracts, packaging rules, and cross-boundary capability movement.

- **A-009.C1 — Interface contract discipline**
  - Distributed via: interface docs + product-local architecture artifacts
  - Consumers: all products, `pxs`
  - Readiness: **usable**
  - Main gaps: still under-executed relative to importance; packaging logic not yet fully consolidated

- **A-009.C2 — OS -> PXS export/import boundary model**
  - Distributed via: interface docs + boundary decisions + workspace package conventions
  - Consumers: `pxs`, Vega
  - Readiness: **usable**
  - Main gaps: still relies on process discipline and interim copies more than strong packaged boundaries

- **A-009.C3 — Capability packaging/versioning model**
  - Distributed via: interface docs + assembly/interim-copy discipline
  - Consumers: future downstream workspaces
  - Readiness: **draft**
  - Main gaps: one of the major current bottlenecks; this is where skills/ops-packs/schema-packs need sharper definition

---

## CP-001 — Control Panel
Primary product focus: operator visibility and control surface.

- **CP-001.C1 — Operator visibility into system state**
  - Distributed via: service/UI concepts + control-panel artifacts + status/reporting routines
  - Consumers: Peter, operators
  - Readiness: **draft**
  - Main gaps: strongest as a concept and artifact set, but not yet a mature daily operator surface

- **CP-001.C2 — Safe steering/control surface**
  - Distributed via: control-panel product docs + runtime/service direction
  - Consumers: Peter, operators
  - Readiness: **draft**
  - Main gaps: still largely conceptual; not yet a stable production control plane

---

## Cross-product / current-state observations

### 1. We do have real capabilities already
The issue is not absence of capability.
The issue is that the capability layer is not yet cleanly normalized.

### 2. The strongest currently real capabilities are:
- canonical TDE task state and execution flow
- intake/assignment acceptance
- governance / decision / error-report discipline
- workspace operating package retrofit model
- boundary review / acceptance discipline
- recurring review/sweep loops

### 3. The weakest area is distribution packaging
We are much stronger at:
- strategy
- plans
- operating rules
- internal implementation

than at:
- explicit reusable capability packaging for downstream consumers like `pxs`

### 4. `pxs` can consume more than it can consume cleanly
Today `pxs` can access capability through:
- local workspace package
- explicit artifact delivery
- pinned/shared artifacts
- open exec posture in Phase 1

But `pxs` still lacks a mature, low-ambiguity, packaged consumption interface.

---

## Current top gaps

1. **No formal capability model per product**
   - This inventory is cross-product and first-pass only.
   - Product-local capability records still need to be created.

2. **Packaging/distribution model still weak**
   - Especially for `pxs` consumption.
   - “Skills” is promising, but not yet mapped cleanly to which capabilities should use it.

3. **Domain-local TDE in `pxs` not yet proven**
   - This is the biggest near-term execution gap for downstream capability use.

4. **Interim-copy dependency still present**
   - Controlled, but not an end-state.

---

## Recommended next steps

### Next step 1 — make this product-local
For each active product, add a local capability section/file with:
- capability ID
- purpose
- consumer(s)
- delivery mode
- entrypoint
- readiness
- evidence
- known gaps

### Next step 2 — create a capability-to-delivery map for `pxs`
For each capability relevant to `pxs`, answer:
- can `pxs` consume it now?
- through what surface?
- with what constraints?
- what is the next packaging step?

### Next step 3 — prove domain-local task capability in `pxs`
This is the most important downstream proof point still missing.

---

## Initial conclusion

Yes: Lyra OS already has meaningful capabilities in code.

No: those capabilities are not yet represented through a clean, explicit capabilities-as-code layer.

This inventory is the first step in making that layer visible.

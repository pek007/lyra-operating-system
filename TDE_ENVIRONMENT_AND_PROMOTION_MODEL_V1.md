# TDE Environment and Promotion Model v1

Status: Draft
Owner: Peter + Lyra
Date: 2026-03-13
Related:
- `ASSEMBLY_INSTALL_PROMOTE_ROLLBACK_SOP_V1.md`
- `OPENCLAW_CONFIG_CHANGE_SOP_V1.md`
- `OPENCLAW_CONFIG_CHANGE_CHECKLIST_V1.md`
- `products/task-management/07-decisions/TDE_DECISION_POLICY_RUNTIME_EMBODIMENT_V1.md`
- `products/task-management/07-decisions/TDE_PILOT_WORKFLOW_FAMILY_IMPLEMENTATION_VERIFICATION_READINESS_V1.md`

## Purpose
Define a professional operating model for separating TDE/OpenClaw work across environments so that:
- experimentation does not directly become production behavior,
- runtime policy changes are validated before promotion,
- and rollback is practical when automation or decision logic regresses.

This is especially important now that TDE is moving from design artifacts into real runtime enforcement.

## Core decision
Adopt a minimum three-environment model:
- **Development**
- **Staging / Test**
- **Production**

This applies not only to code, but also to:
- schemas
- policy artifacts
- runtime state
- task metadata conventions
- cron/tick behavior
- decision-routing behavior
- evidence and release artifacts

## Why this matters now
Until recently, most TDE work was still design-heavy and artifact-heavy.
That made live-workspace iteration tolerable.

Now we are introducing:
- decision-policy enforcement in runtime,
- automatic decision-record emission,
- stronger continuity/autonomy behavior,
- and eventually richer `research_further` / escalation logic.

At that point, the cost of mixing experiment and production rises sharply.

## Environment definitions

## 1) Development
Purpose:
- design, prototype, and iterate quickly
- try new schemas, metadata keys, and runtime enforcement ideas
- run synthetic/local simulations

Allowed characteristics:
- breakage acceptable
- incomplete artifacts acceptable
- simulated or synthetic tasks/objectives acceptable
- direct code edits allowed
- frequent changes expected

Not allowed:
- production authority assumptions
- unreviewed promotion into live production runtime
- using development evidence as production evidence

Typical contents:
- experimental tool changes
- draft schemas
- draft policy envelopes
- synthetic chain examples
- local tests and simulations

## 2) Staging / Test
Purpose:
- validate production-like behavior before promotion
- test runtime interactions under realistic structure
- prove fail-closed behavior and rollback readiness

Allowed characteristics:
- production-like workspace structure
- production-like schemas and policy artifacts
- realistic task/state shapes
- canary cron/job tick runs
- isolated DB and evidence outputs

Not allowed:
- real external effects by default
- production authority mutation
- live production objective/task ownership

Typical contents:
- mirror of candidate production artifacts
- staging TDE DB
- test objective registry
- test bindings
- validation evidence bundle
- release candidate artifacts

## 3) Production
Purpose:
- run approved, stable TDE/OpenClaw behavior for real operations

Required characteristics:
- only promoted code/policy/schema/config changes
- explicit rollback path
- evidence-backed release state
- strong audit trail
- minimal opportunistic edits

Not allowed:
- ad hoc experimental runtime changes
- unreviewed schema mutations
- mixed test and production state
- relying on transcript memory as deployment control

## Separation dimensions
The environment model must separate at least these dimensions.

### A. Code / tooling
Examples:
- `tools/tde_*`
- runtime helpers
- validation utilities

### B. Canonical state
Examples:
- `os/runtime/tde_state.sqlite`
- objective/binding registries
- task metadata in canonical DB state

### C. Policy + schema artifacts
Examples:
- decision policy envelopes
- schemas
- runtime embodiment specs
- chaining/decision contracts

### D. Scheduler behavior
Examples:
- cron jobs
- heartbeat hooks
- tick cadence
- automation enablement flags

### E. Evidence outputs
Examples:
- decision advancement records
- escalation packages
- tick artifacts
- readiness reports

A professional separation model fails if only code is separated while DB, cron, or policy state remains shared.

## Recommended practical model for Lyra/OpenClaw/TDE

## Option A — Separate workspaces/runtimes (preferred steady state)
Use distinct environment roots and/or gateway/runtime instances for:
- dev
- staging
- prod

Advantages:
- strongest separation
- easiest reasoning about authority/state
- safer cron and DB isolation

Disadvantages:
- more setup overhead
- more operational discipline required

## Option B — Single repo, environment-scoped runtime roots (acceptable intermediate state)
Keep one codebase/repo, but separate:
- runtime DB paths
- config files
- cron enablement
- evidence directories
- objective/binding registries

This is likely the best near-term move if full environment duplication is too heavy immediately.

### Minimum acceptable isolation in Option B
Development, staging, and production must not share:
- the same canonical TDE DB
- the same active cron/tick schedule
- the same binding registry
- the same objective registry for authoritative flows
- the same output paths for release/evidence artifacts when those artifacts drive operational decisions

## Environment-specific expectations

### Development expectations
- decision-policy and chaining changes may be tested against synthetic chains
- release/promotion not required for every change
- commits should still be clean and reversible

### Staging expectations
A change must prove at least:
- schema validity
- metadata compatibility
- fail-closed behavior for missing or invalid policy refs
- no approval bypass
- correct decision-record emission where applicable
- rollback feasibility

### Production expectations
A change may be promoted only when:
- development work is committed and scoped
- staging validation passes
- release note or promotion packet exists
- rollback path is documented
- impact/risk is understood

## Promotion flow

## Step 1 — Develop
In development:
- change code / schema / policy artifact
- run focused tests
- produce candidate artifacts

## Step 2 — Validate in staging
In staging:
- load candidate artifacts
- run simulated or isolated tick paths
- verify decision-policy enforcement
- verify evidence outputs
- test fail-closed cases
- produce validation evidence

## Step 3 — Approve for production
Promotion decision should include:
- exact candidate version/commit
- scope of change
- risk class
- validation evidence refs
- rollback method

## Step 4 — Promote
Promote only the approved candidate.
Do not bundle opportunistic unrelated changes.

## Step 5 — Verify production
Immediately verify:
- runtime starts/loads cleanly
- expected tick behavior remains correct
- no unexpected fail-open behavior
- no unexpected external effects
- production evidence path is healthy

## Step 6 — Roll back if needed
Rollback triggers include:
- runtime regression
- fail-open policy behavior
- unexpected production state mutation
- cron/scheduler misbehavior
- artifact/evidence inconsistency

## Change classes for TDE runtime changes

### Low risk
- documentation only
- non-operative examples
- comments/formatting
- isolated tests that do not affect live runtime paths

### Medium risk
- schema additions without active enforcement
- new artifact emitters not yet on live critical path
- staging-only runtime flags

### High risk
- changes to `tde_job_tick_runner.py`
- changes to `tde_state_store.py` affecting canonical metadata/state semantics
- changes to chaining/promotion logic
- changes to policy enforcement behavior
- changes to cron/tick enablement for production runtime

Default for D-layer runtime work: **High risk** unless clearly proven otherwise.

## Immediate practical rules
Until a fuller environment setup exists, use these temporary rules:

1. Treat the current workspace as **production-adjacent**, not true development-only.
2. Any runtime-path code change to TDE decision/chaining logic is **high risk**.
3. No broadened autonomous behavior should go live without at least a staging-like validation pass.
4. Do not introduce new scheduler-enabled autonomous paths in production without explicit promotion evidence.
5. Keep production auto-advance narrow until environment separation is in place.

## Recommended near-term implementation path

### Phase 1 — Naming and path discipline
Define explicit environment naming and directory/path conventions for:
- runtime DB
- objective registry
- binding registry
- evidence outputs
- configs

### Phase 2 — Staging runtime
Stand up a staging TDE/OpenClaw runtime with:
- isolated DB
- isolated config
- isolated cron/tick hooks
- isolated evidence directory

Status update:
- staging runtime root exists
- staging-only tick path has been proven
- core TDE runtime scripts support `--env`
- next-ring release/evidence scripts support `--env`

### Phase 3 — Promotion contract
Create a TDE-specific promote/rollback checklist and release packet.

### Phase 4 — Production hardening
Restrict live production changes to promoted candidates only.

## Minimum artifacts to add next
1. TDE runtime promotion checklist
2. TDE runtime rollback checklist
3. Optional release-envelope template for runtime changes

## Naming/path convention added
The first concrete environment naming/path convention is now defined in:
- `TDE_ENVIRONMENT_PATH_CONVENTION_V1.md`

## Staging setup note added
The first staging runtime setup note is now defined in:
- `TDE_STAGING_RUNTIME_SETUP_NOTE_V1.md`

## Bottom line
Yes, we are currently working in a live production-adjacent environment.
That was acceptable for early system formation.
It is not the right long-term operating model.

The professional path forward is to separate development, staging, and production across code, state, policy, cron behavior, and evidence outputs — and to require promotion/rollback discipline for TDE runtime changes.
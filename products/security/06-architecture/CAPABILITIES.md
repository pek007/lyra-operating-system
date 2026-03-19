# Security Capabilities

Status: Draft active capability record
Product: A-004 Security
Owner: Lyra
Standard: `CAPABILITY_MODEL_STANDARD_V1.md`
Date: 2026-03-19

## Role of this artifact
This is the compact active capability record for the Security product.
Use `06-architecture/CAPABILITY_MAP.md` for the broader capability-planning view and current maturity/gap interpretation.

## A-004.C1 — Security baseline / posture guidance
- Owning product: Security
- Purpose: Provide practical security baseline, posture expectations, and usable guardrails for Lyra OS and consuming environments.
- Scope / boundary: Owns security posture guidance and baseline expectations; does not silently take ownership of other products’ domain decisions
- Primary consumers: `main`, operators, future deployments, `pxs`
- Delivery mode(s): governance artifacts + product-local security docs + review checklists
- Entrypoint / interface: Security product artifacts, baseline docs, review outputs
- Canonical artifacts: `PRODUCT.md`, `03-operating-model/*`, `05-performance/PXS_DEPLOYMENT_BASELINE.md`, `06-architecture/BOUNDARY.md`, `06-architecture/ESTATE_MAP.md`
- Dependencies: governance, deployment contexts, evidence/review loops, current estate clarity
- Constraints / guardrails: security guidance must reduce real risk without freezing delivery
- Readiness: usable
- Lifecycle state: active
- Evidence: current baseline/posture docs and active security review routines
- Known gaps / risks: some controls remain guidance-heavy rather than automatically enforced; estate growth can outpace baseline translation
- Upgrade / retirement trigger: upgrade when stronger automated controls or downstream packaging become justified

## A-004.C2 — Boundary review and acceptance discipline
- Owning product: Security
- Purpose: Define and review boundary/security expectations for cross-domain and high-risk interactions.
- Scope / boundary: Governs required security expectations and review evidence; implementation may live elsewhere
- Primary consumers: `main`, Vega, `pxs`
- Delivery mode(s): boundary docs + acceptance tests + decision records
- Entrypoint / interface: `06-architecture/BOUNDARY.md`, boundary review artifacts, acceptance sheets
- Canonical artifacts: boundary docs, acceptance artifacts, security decisions
- Dependencies: Governance, Interfaces, provider products, runtime configuration
- Constraints / guardrails: boundary-affecting changes require explicit review and evidence
- Readiness: usable
- Lifecycle state: active
- Evidence: Vega/PXS boundary pass in Phase 1
- Known gaps / risks: current phase intentionally leaves exec open; long-term hard compartmentalization is not yet implemented
- Upgrade / retirement trigger: upgrade when confidential compartmentalization becomes an active requirement

## A-004.C3 — Security review / audit loop
- Owning product: Security
- Purpose: Detect posture drift, risk signals, and remediation needs through recurring review and evidence generation.
- Scope / boundary: Owns security review pattern and outputs; does not own every remediation action itself
- Primary consumers: operators, `main`
- Delivery mode(s): cron loops + review artifacts + evidence snapshots
- Entrypoint / interface: scheduled reviews, audit outputs, evidence artifacts
- Canonical artifacts: product review docs, evidence artifacts, security tasks/findings, `04-execution/SURFACE_CHANGE_LOG.md`
- Dependencies: runtime visibility, delivery and governance hooks, task-management follow-through
- Constraints / guardrails: findings must route into explicit remediation or disposition paths
- Readiness: usable
- Lifecycle state: active
- Evidence: active security cron/review behavior and recent audit artifacts
- Known gaps / risks: some sweep wording and conversions still reflect transitional/legacy paths
- Upgrade / retirement trigger: upgrade when review-to-remediation conversion is fully normalized and lower-noise

## A-004.C4 — Upstream release and vulnerability impact assessment
- Owning product: Security
- Purpose: Monitor OpenClaw and other key upstream changes and classify their local impact on Lyra OS and `pxs`.
- Scope / boundary: Owns the triage and disposition logic; implementation of upgrades or local hardening may live elsewhere
- Primary consumers: operators, `main`, downstream environments depending on Lyra OS posture
- Delivery mode(s): monitoring model + review outputs + explicit watch/update/defer decisions
- Entrypoint / interface: `08-research/UPSTREAM_MONITORING_MODEL.md`
- Canonical artifacts: `08-research/UPSTREAM_MONITORING_MODEL.md`, `04-execution/SURFACE_CHANGE_LOG.md`, `08-research/IMPLICATIONS.md`
- Dependencies: OpenClaw docs and release visibility, current local version/posture awareness
- Constraints / guardrails: frequent releases are not a reason for blind auto-updating or blind drift acceptance
- Readiness: emerging
- Lifecycle state: active
- Evidence: explicit recognition of the release-stream risk and monitoring model now in place
- Known gaps / risks: cadence, first dispositions, and deferred-risk handling still need embedding in routine operations
- Upgrade / retirement trigger: upgrade when the loop is stable enough to support lower-friction repeated assessment

## A-004.C5 — Integration and platform onboarding review
- Owning product: Security
- Purpose: Assess new platforms and services for security implications when they become material parts of the operating environment.
- Scope / boundary: Owns the security review and posture translation; platform ownership and implementation may live in the consuming environment
- Primary consumers: `pxs`, operators, future downstream environments
- Delivery mode(s): estate updates + surface-change entries + posture and capability implications
- Entrypoint / interface: `06-architecture/ESTATE_MAP.md`, `04-execution/SURFACE_CHANGE_LOG.md`
- Canonical artifacts: `06-architecture/ESTATE_MAP.md`, `04-execution/SURFACE_CHANGE_LOG.md`, `06-architecture/CAPABILITY_MAP.md`
- Dependencies: visibility into new services, identity models, sharing/integration behavior, and local operating intent
- Constraints / guardrails: new services should not become normalized before their material security implications are at least minimally assessed
- Readiness: early
- Lifecycle state: active
- Evidence: Google Workspace introduction in `pxs` as the first explicit current test case
- Known gaps / risks: platform introductions can outpace explicit posture translation and control design
- Upgrade / retirement trigger: upgrade when the onboarding review pattern is stable enough to standardize more tightly

## A-004.C6 — Auditability, logging, and traceability governance
- Owning product: Security
- Purpose: Ensure that material actions, failures, and control-relevant events can be reconstructed and investigated.
- Scope / boundary: Owns the expectation and minimum standard logic; logging implementation may be distributed across provider surfaces
- Primary consumers: operators, `main`, review/evidence loops
- Delivery mode(s): posture guidance + review expectations + targeted standards for high-risk surfaces
- Entrypoint / interface: Security review outputs, capability planning, future logging standards
- Canonical artifacts: `06-architecture/CAPABILITY_MAP.md`, `08-research/ECOSYSTEM_PATTERN_LOG.md`, future baseline/evidence artifacts
- Dependencies: runtime visibility, evidence discipline, provider-surface cooperation
- Constraints / guardrails: prefer selective high-value traceability over indiscriminate logging volume
- Readiness: early
- Lifecycle state: active
- Evidence: explicit recognition of traceability/logging as a recurring need and capability gap
- Known gaps / risks: minimum standards are not yet defined for the highest-risk actions and surfaces
- Upgrade / retirement trigger: upgrade when the first compact traceability/logging standard is defined and in use

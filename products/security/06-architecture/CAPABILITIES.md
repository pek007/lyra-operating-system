# Security Capabilities

Status: Draft active capability record
Product: A-004 Security
Owner: Lyra
Standard: `CAPABILITY_MODEL_STANDARD_V1.md`
Date: 2026-03-17

## A-004.C1 — Security baseline / posture guidance
- Owning product: Security
- Purpose: Provide practical security baseline, posture expectations, and usable guardrails for Lyra OS and consuming environments.
- Scope / boundary: Owns security posture guidance and baseline expectations; does not silently take ownership of other products’ domain decisions
- Primary consumers: `main`, operators, future deployments, `pxs`
- Delivery mode(s): governance artifacts + product-local security docs + review checklists
- Entrypoint / interface: Security product artifacts, baseline docs, review outputs
- Canonical artifacts: `PRODUCT.md`, `03-operating-model/*`, `05-performance/PXS_DEPLOYMENT_BASELINE.md`, `06-architecture/BOUNDARY.md`
- Dependencies: governance, deployment contexts, evidence/review loops
- Constraints / guardrails: security guidance must reduce real risk without freezing delivery
- Readiness: usable
- Lifecycle state: active
- Evidence: current baseline/posture docs and active security review routines
- Known gaps / risks: some controls remain guidance-heavy rather than automatically enforced
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
- Canonical artifacts: product review docs, evidence artifacts, security tasks/findings
- Dependencies: runtime visibility, delivery and governance hooks, task-management follow-through
- Constraints / guardrails: findings must route into explicit remediation or disposition paths
- Readiness: usable
- Lifecycle state: active
- Evidence: active security cron/review behavior and recent audit artifacts
- Known gaps / risks: some sweep wording and conversions still reflect transitional/legacy paths
- Upgrade / retirement trigger: upgrade when review-to-remediation conversion is fully normalized and lower-noise

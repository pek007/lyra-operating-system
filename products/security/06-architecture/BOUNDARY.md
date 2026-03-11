# Security Boundary

Status: Active
Product: Security (`A-004`)
Owner: Lyra
Date: 2026-03-11

## Purpose
Define the canonical ownership, data, runtime, and dependency boundary for the Security product.

This artifact consolidates the most important boundary logic into the canonical slug-based Security model so the product can be reviewed and run without depending on the legacy management pack.

## Product identity
- Product ID: `A-004`
- Product name: `Security`
- Domain: `OS`
- Type: `Internal` with customer impact through the PXS deployment boundary

## Mission boundary
Security exists to ensure Lyra OS and current customer deployments operate within explicit, reviewable security boundaries with practical controls and evidence-backed posture management.

## Ownership boundary
### Security owns
- security policy and control definitions
- security posture review, audit interpretation, and residual-risk framing
- security-specific research intake and conversion into controls, guidance, or backlog
- security decision logging and escalation for material risk or exception handling
- product-level security requirements for deployment into consuming environments such as `pxs`
- security evidence loops and scorecarding

### Security reads but does not own
- product-specific implementation artifacts in Delivery, Improvement, Control Panel, Task Management, and other product domains
- runtime/config state owned by platform or product operators
- portfolio-level governance documents above product scope
- consuming-environment implementation details outside agreed deployment/security interfaces

### Security must never own
- general prioritization for unrelated product domains
- silent credential, access, or trust-boundary expansion without logged decision/escalation
- customer communications unless explicitly requested or part of an approved incident flow

## Data boundary
- handled data classes: internal policy, posture, evidence, audit outputs, incident records, risk assessments, security research
- sensitive handling rule: minimize retention of secrets and customer-private data in product artifacts
- tenant model: current mode is single-customer operational context via `pxs`; stronger isolation required before broader externalization
- audit rule: preserve decision/evidence traceability for material posture changes and residual-risk acceptance

## Runtime boundary
- primary unit: workspace-level docs, evidence loops, policies, and control definitions
- possible future unit: tooling or automation artifacts when justified
- secrets rule: Security may define secret-handling requirements but should not casually duplicate secret material into docs
- enforcement rule: prose is not the only control; config-level and runtime controls remain primary where available

## Dependency policy
### Allowed dependencies
- platform/shared capabilities
- governance records
- security evidence sources
- approved product interfaces
- security-relevant research in the knowledge library

### Prohibited dependencies
- hidden coupling to other product internals
- undocumented reliance on manual memory
- unreviewed external security tooling with broad privileges

### ADR / decision triggers
Raise explicit decisions for:
- new security tooling with elevated access
- new external exposure paths
- changes that alter trust boundaries, tenant assumptions, or credential scope

## Interface stance
Inbound sources include:
- audit/evidence outputs
- incident signals
- product review requests
- deployment changes requiring security review
- security research intake

Outbound outputs include:
- security requirements
- policy/control updates
- risk decisions
- remediation priorities
- posture summaries
- enforcement recommendations

## Operational boundary rule
Security governs across products, but does not silently take over implementation ownership inside those products.

## Commercialization boundary
Security is not currently modeled as multi-tenant-ready. Any move toward broader customer packaging requires stronger interface contracts, clearer packaging, and a more explicit tenant/isolation model.

# A-004 — Product Boundary

Status: Active draft v1
Product Name: Security
Product Owner: Lyra
Last updated: 2026-03-08

## Product Identity
- Product ID: A-004
- Product Name: Security
- Domain: OS
- Owner: Lyra
- Type: Internal (current) / customer-impacting through PXS deployment boundary

## 1) Product Mission
- Core problem solved: Ensure Lyra OS and current customer deployments operate within explicit, reviewable security boundaries with practical controls and evidence-backed posture management.
- Primary users: Peter; Lyra OS product owners/operators; PXS as the current consuming customer environment.
- Success outcome(s): Clear ownership of security posture; explicit residual-risk decisions; repeatable audit/evidence cadence; deployable security requirements for PXS.

## 2) Ownership Boundary
- What this product **owns**:
  - Security policy and control definitions
  - Security posture review, audit interpretation, and residual-risk framing
  - Security-specific research intake and conversion into controls, guidance, or backlog
  - Security decision logging and escalation for material risks/exceptions
  - Product-level security requirements for deployment into PXS
  - Security evidence loops and scorecarding
- What this product **reads but does not own**:
  - Product-specific implementation artifacts in Delivery, Improvement, Control Panel, and other product domains
  - Runtime/config state owned by platform or product operators
  - Governance documents with portfolio-wide authority above the Security product
  - PXS-local implementation details outside agreed deployment/security interfaces
- What this product **must never own**:
  - General product prioritization for unrelated domains
  - Silent credential, access, or trust-boundary expansion without logged decision/escalation
  - Customer communications except where explicitly requested or part of an approved incident flow

## 3) Data Boundary
- Data classes handled:
  - Internal policy, posture, evidence, audit outputs, incident records, risk assessments, and security research
- Sensitive/customer data handling:
  - Minimize retention of secrets and customer-private data in product artifacts
  - Security artifacts may reference sensitive posture or exposure details and should be handled as sensitive operational material
- Tenant model:
  - Current model: single-customer operational deployment context via PXS
  - Future target: stronger tenant/boundary model required before multi-customer packaging
- Retention/audit requirements:
  - Preserve decision/evidence traceability for material posture changes, incidents, and residual-risk acceptance

## 4) Runtime Boundary
- Runtime/deployment unit:
  - Primarily workspace-level docs, evidence loops, policies, and control definitions; may later include tooling/automation artifacts
- Secrets boundary:
  - Security may define secret-handling requirements but should not duplicate secret storage or casually copy secret values into docs
- Failure isolation expectations:
  - Security controls should reduce blast radius and make exposure visible; failures in Security product docs must not be the only enforcement layer where config-level controls are required

## 5) Dependency Policy
- Allowed dependencies:
  - Platform/shared capabilities, governance records, security evidence sources, approved product interfaces, and security-relevant research in the library
- Prohibited dependencies:
  - Hidden coupling to other product internals; undocumented reliance on manual memory; unreviewed external security tooling with broad privileges
- Required ADR triggers for dependency exceptions:
  - New security tooling with elevated access
  - New external exposure paths
  - Changes that alter trust boundaries, tenant assumptions, or credential scope

## 6) Interface Contracts
- Inbound interfaces (API/events):
  - Audit/evidence outputs, incident signals, product review requests, deployment changes requiring security review, research intake
- Outbound interfaces (API/events):
  - Security requirements, policy/control updates, risk decisions, remediation priorities, posture summaries, enforcement recommendations
- Contract versioning strategy:
  - Documented product artifacts and explicit decision records until stronger schema-based contracts are introduced

## 7) Reuse Strategy
- Candidate shared components:
  - Security review checklist(s), posture baseline template(s), evidence-ingestion conventions, residual-risk decision pattern, control taxonomy
- Why shared (vs duplicate):
  - Security consistency matters across products, and repeated ad hoc interpretations increase both risk and noise
- Support/maintenance owner:
  - Security product owner unless a shared platform component is explicitly transferred elsewhere

## 8) Product Assembly (Required)
- Artifact types included (service / skill-pack / policy-pack / schema-pack / ops-pack):
  - Current: policy-pack, ops-pack, management artifacts, evidence artifacts/research references
  - Future possible: schema-pack, tooling/service support
- Versioning strategy per artifact:
  - Document versioning in product artifacts now; stronger release/version semantics later if/when packaged externally
- Consumer-facing package/version identifier:
  - Not yet defined; current customer-facing consumption is via workspace/PXS deployment boundary

## 9) Distribution & Activation (Required)
- Distribution lane per artifact (daemon/cron, workspace-skills/managed-skills/extraDirs/plugin, submodule/subtree/release):
  - Management artifacts=`workspace`
  - Policy/ops artifacts=`workspace|submodule|subtree|release` depending on future packaging
  - Evidence loops=`cron|workspace docs`
- Activation mechanism per artifact:
  - Via documented product operating cadence, security reviews, evidence production, and explicit deployment into PXS where applicable
- Override precedence and conflict policy:
  - Config-level/hard controls override prose; portfolio governance overrides product-local interpretation; undocumented exceptions are invalid

## 10) Operational Controls
- Required metrics:
  - Critical/warn posture counts, residual-risk status, review freshness, research-to-action conversion rate, recurring finding count
- Required audit artifacts (WO/CA/ADR):
  - Decision records for material risk acceptance/exceptions; evidence files for posture checks; work artifacts for remediation/change work as appropriate
- Security controls:
  - Least privilege, trust-boundary clarity, explicit risk acceptance, evidence-backed review cadence, no silent widening of access/exposure
- Required enforcement gates/checks:
  - Escalation for trust-boundary, credential, access, and external exposure changes; routine security audit evidence; verification before declaring posture improvement complete

## 11) Commercialization Readiness (if relevant)
- What blocks external release today:
  - Single-customer assumptions, incomplete packaging boundary, partial manual controls, and insufficient multi-tenant isolation model
- Steps to SaaS readiness:
  - Stronger control packaging, explicit interface/schema contracts, tenant/isolation model, and clearer deployment/compliance support
- Regulatory/compliance considerations:
  - Depends on customer segment and data scope; not yet scoped for externalized product release

## 12) Decision Log
- ADR links:
  - `governance/TRUST_BOUNDARY_POLICY_RECORD_2026-03-04.md`
  - `governance/GO_RISK_DECISION_2026-03-06.md`
- Open decisions:
  - Product/customer naming alignment beyond current PXS scope
  - Whether security deployment baseline lives inside product management or separate deployment artifacts
  - Future packaging/distribution model for reusable security controls
- Next review date:
  - 2026-03-22

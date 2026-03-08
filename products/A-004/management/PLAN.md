# A-004 — Plan

Status: Active v1
Product Name: Security
Product Owner: Lyra
Last updated: 2026-03-08

## Now
- Initiative ID: A-004-I1
  - Problem: Security exists as a role and set of scattered artifacts, but not yet as an activated product with clear ownership and management documents.
  - Expected outcome: A-004 becomes the canonical operating layer for Security in this workspace.
  - Dependencies:
    - Product management template pack
    - Existing governance/security documents
    - Existing security evidence and research in the library
  - Acceptance criteria:
    - Vision, Goals, Plan, Decisions, Improvement Log, and Scorecard are populated
    - Portfolio registry identifies A-004 as Security
    - Product boundary document is created and linked
  - Evidence required:
    - Updated files under `products/A-004/management/`
    - Updated `PRODUCT_PORTFOLIO_REGISTRY.md`

- Initiative ID: A-004-I2
  - Problem: Security scope across Lyra OS and PXS is implicit, which creates ambiguity about ownership, deployment scope, and what belongs in the Security product.
  - Expected outcome: Security boundary is explicit across controls, research, evidence, and deployment obligations.
  - Dependencies:
    - Product boundary template
    - Current product-portfolio rules
    - Existing trust-boundary and risk records
  - Acceptance criteria:
    - Product boundary document names owned/non-owned domains
    - PXS deployment/customer scope is explicit
    - Key interfaces and enforcement expectations are stated
  - Evidence required:
    - `products/A-004/management/PRODUCT_BOUNDARY.md`

- Initiative ID: A-004-I3
  - Problem: Security research and evidence are present, but not yet organized into a current product-level execution agenda.
  - Expected outcome: Immediate Security priorities reflect the real current posture and known risk themes.
  - Dependencies:
    - `governance/TRUST_BOUNDARY_POLICY_RECORD_2026-03-04.md`
    - `governance/GO_RISK_DECISION_2026-03-06.md`
    - Current security audit evidence and related research
  - Acceptance criteria:
    - Near-term plan names current risk/posture themes
    - At least one decision records how Security will operate under the new product model
    - Scorecard categories reflect actual operating signals
  - Evidence required:
    - Updated `DECISIONS.md`, `SCORECARD.md`, and `IMPROVEMENT_LOG.md`

## Next
- Initiative ID: A-004-I4
  - Problem: PXS security posture is partially documented through scattered evidence and governance records, but not yet summarized as a product deployment baseline.
  - Expected outcome: A concise Security deployment baseline exists for PXS, including active controls, accepted residual risks, and verification cadence.
  - Dependencies:
    - Current evidence files
    - Product boundary and decision records
    - PXS deployment docs and lock/state where relevant
  - Acceptance criteria:
    - Baseline note or deployment artifact exists
    - Residual risk items are linked to evidence/decisions
    - Review trigger for baseline refresh is defined
  - Evidence required:
    - `products/A-004/management/PXS_SECURITY_DEPLOYMENT_BASELINE.md`

- Initiative ID: A-004-I5
  - Problem: Security work can remain reactive unless research intake and control uplift are turned into a standing product loop.
  - Expected outcome: Security has a lightweight recurring review for research intake, posture drift, and control improvement.
  - Dependencies:
    - Existing continuous-improvement process
    - Security research library
    - Product owner operating cadence
  - Acceptance criteria:
    - Intake/review cadence is documented
    - Improvement log gets updated from actual triggers
    - Security research can be triaged into adopt / watch / reject / backlog states
  - Evidence required:
    - Decision or process note plus first reviewed set of items

## Later
- Initiative ID: A-004-I6
  - Problem: Security assurance still relies heavily on manual interpretation of evidence and config posture.
  - Expected outcome: Selected security controls and posture checks become more machine-checkable without widening risk.
  - Dependencies:
    - Stable control definitions
    - Delivery support for automation
    - Clear evidence contracts
  - Acceptance criteria:
    - At least one useful control/evidence loop is automated
    - Automation reduces ambiguity or operator burden
    - False-positive/noise rate stays acceptable
  - Evidence required:
    - Tooling/code change artifacts and before/after notes

- Initiative ID: A-004-I7
  - Problem: Security productization is currently focused on internal and single-customer operation; external scaling would require clearer packaging and commercialization boundaries.
  - Expected outcome: Security has an explicit readiness view for future multi-customer or SaaS-candidate use.
  - Dependencies:
    - Product portfolio evolution
    - Tenant and deployment model decisions
    - Harder interface contracts and stronger isolation model
  - Acceptance criteria:
    - Readiness gaps are documented
    - Multi-tenant blockers are explicit
    - Boundary, data, and deployment requirements are stated before expansion
  - Evidence required:
    - Decision memo or boundary revision

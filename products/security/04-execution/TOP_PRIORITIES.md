# TOP_PRIORITIES

Product: Security
Last updated: 2026-03-14
Owner: Product Owner / Control Tower

## Priority 1
**Title:** Enforce the OS↔PXS boundary as a real control
**Why this matters now:** The single most material current security risk is that the declared boundary model is not yet enforced in the Vega/PXS context, where cross-domain reads are still possible.
**Current status:** Highest-risk execution reality gap; acceptance evidence currently records boundary failure.
**Next concrete step:** close the current FAIL on cross-domain reads, align Vega/PX boundary enforcement with the declared model, and re-run the acceptance boundary test to PASS with committed evidence.
**Links:** `products/security/04-execution/PLAN.md`, `products/security/04-execution/RISKS.md`, `products/security/06-architecture/BOUNDARY.md`, `governance/VEGA_ACCEPTANCE_TEST_RUN_SHEET_V1.md`

## Priority 2
**Title:** Harden the tool and evidence execution surfaces that function as policy-enforcement points
**Why this matters now:** Security posture is weakest where execution still depends on sharp procedural paths instead of deterministic hardened controls.
**Current status:** Adoption-plan direction exists, but the highest-risk execution surfaces are not yet fully hardened.
**Next concrete step:** eliminate shell-based evidence ingestion paths, pin command/environment assumptions, and treat evidence/tooling surfaces as security-critical controls with explicit verification.
**Links:** `products/security/04-execution/PLAN.md`, `products/security/04-execution/RISKS.md`, `SECURITY_ADOPTION_PLAN.md`, `products/security/07-decisions/DECISIONS.md`

## Priority 3
**Title:** Close the posture → evidence → enforcement loop for PXS consumption
**Why this matters now:** Security requirements for consuming environments only become trustworthy when they are backed by reproducible evidence and narrow promotion checks rather than prose alone.
**Current status:** Baseline and boundary artifacts exist, but some references still depend on local/latest evidence and the full consumption loop is not yet tight enough.
**Next concrete step:** update baseline-critical references toward committed/reproducible evidence, run one full Security Guardrails VERIFY cycle with recorded evidence, and define a narrow set of checks that must pass before security-impacting versions are promoted into PXS.
**Links:** `products/security/05-performance/PXS_DEPLOYMENT_BASELINE.md`, `products/security/06-architecture/INTERFACES.md`, `products/security/04-execution/RISKS.md`

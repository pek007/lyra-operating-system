# TOP_PRIORITIES

Product: Security
Last updated: 2026-03-14
Owner: Product Owner / Control Tower

## Priority 1
**Title:** Keep the active security posture explicit
**Why this matters now:** Security posture loses value quickly if it fragments across audits, notes, and scattered evidence instead of remaining inspectable from the product model.
**Current status:** Core priority and active risk area.
**Next concrete step:** Consolidate posture-critical material into the canonical Security model and keep the baseline artifacts current.
**Links:** `products/security/04-execution/PLAN.md`, `products/security/04-execution/RISKS.md`, `products/security/05-performance/PXS_DEPLOYMENT_BASELINE.md`

## Priority 2
**Title:** Tie important risks to decisions or remediation work
**Why this matters now:** Risks that are visible but not linked to action create slow drift and weak follow-through.
**Current status:** Risks are explicit, but remediation linkage should become more systematic.
**Next concrete step:** Ensure each major active security risk is linked either to an explicit decision, remediation path, or owning follow-up.
**Links:** `products/security/04-execution/RISKS.md`, `products/security/07-decisions/DECISIONS.md`, `products/security/04-execution/ROADMAP.md`

## Priority 3
**Title:** Maintain clear deployment security requirements for consuming environments
**Why this matters now:** Downstream workspaces such as `pxs` need clear baseline and boundary expectations, not inferred security behavior.
**Current status:** Baseline and boundary artifacts exist, but they need to remain the live source of truth for consumers.
**Next concrete step:** Keep deployment baseline, boundary, and interface artifacts aligned with actual consuming-workspace expectations.
**Links:** `products/security/05-performance/PXS_DEPLOYMENT_BASELINE.md`, `products/security/06-architecture/BOUNDARY.md`, `products/security/06-architecture/INTERFACES.md`

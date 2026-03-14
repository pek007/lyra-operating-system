# TOP_PRIORITIES

Product: Improvement
Last updated: 2026-03-14
Owner: Product Owner / Control Tower

## Priority 1
**Title:** Converge improvement execution into one canonical TDE-first system of record
**Why this matters now:** Improvement cannot become evidence-backed, comparable, or safely automatable if work still leaks into multiple tracking surfaces instead of one canonical execution substrate.
**Current status:** Strategic intent is clear, but the operating reality still shows legacy and generated surfaces competing with TDE-first control.
**Next concrete step:** remove legacy routing dependencies for improvement work, define the canonical improvement queue/ID/linkage expectations in TDE terms, and update improvement runbooks/specs to use that substrate consistently.
**Links:** `products/improvement/04-execution/PLAN.md`, `products/improvement/04-execution/RISKS.md`, `products/improvement/03-operating-model/OPERATING_MODEL.md`

## Priority 2
**Title:** Ship A-005 into PXS through a pinned lane with version truth, rollback, and verification semantics
**Why this matters now:** Interim-copy verification is a useful baseline, but the main current deployment risk is still source/install drift until pinned-lane distribution becomes real.
**Current status:** Deployment design is credible and interim verification exists, but the target lane is not yet the lived mechanism.
**Next concrete step:** implement the pinned lane as an operational path with machine-checkable installed-version truth, explicit rollback behavior, and a verification pass that closes the interim-drift gap.
**Links:** `products/improvement/04-execution/PLAN.md`, `products/improvement/04-execution/RISKS.md`, `products/improvement/06-architecture/INTERFACES.md`

## Priority 3
**Title:** Roll out the minimum improvement interface across active products, starting with mandatory incident-to-improvement conversion
**Why this matters now:** Improvement compounds when signals from incidents, repeated misses, and synthesis outputs consistently become owned execution artifacts with evidence and review, not just narrative observations.
**Current status:** Policy intent is strong, but the minimum interface is not yet explicit enough across all active products.
**Next concrete step:** define and deploy the minimum product-side improvement interface: intake/log mechanism, linkage rules, review cadence, and mandatory incident-to-improvement conversion for material cases.
**Links:** `products/improvement/04-execution/PLAN.md`, `products/improvement/06-architecture/INTERFACES.md`, `products/improvement/07-decisions/DECISIONS.md`

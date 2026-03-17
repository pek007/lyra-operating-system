# TOP_PRIORITIES

Product: Improvement
Last updated: 2026-03-17 (03:00 CET overnight cycle)
Owner: Product Owner / Control Tower

## Priority 1
**Title:** Converge improvement execution into one canonical TDE-first system of record
**Why this matters now:** Improvement cannot become evidence-backed, comparable, or safely automatable if work still leaks into multiple tracking surfaces instead of one canonical execution substrate. The Jobs Review (2026-03-16) added new ops tasks that further expand the backlog without a canonical improvement queue or linkage rules in place.
**Current status:** Strategic intent is clear. No new completion evidence — canonical TDE improvement substrate (queue ID, linkage rules, intake format) remains undefined. Improvement items continue to be created ad hoc rather than through a defined canonical intake mechanism.
**Next concrete step:** Define the canonical improvement execution substrate in TDE terms (queue ID, linkage rules, intake format); update improvement runbooks to use that substrate; remove legacy routing dependencies for improvement work.
**Links:** `products/improvement/04-execution/PLAN.md`, `products/improvement/04-execution/RISKS.md`, `products/improvement/03-operating-model/OPERATING_MODEL.md`

## Priority 2
**Title:** Ship A-005 into PXS through a pinned lane with version truth, rollback, and verification semantics
**Why this matters now:** Interim-copy verification is still the baseline mechanism. The pinned-lane target is not yet the lived distribution path. Deployment drift risk continues to accumulate passively.
**Current status:** No progress since last report. Interim-copy lanes still in use. Vega/PXS boundary narrowing (2026-03-16) addressed access topology but not A-005 assembly delivery specifically.
**Next concrete step:** Implement the pinned lane as an operational path with machine-checkable installed-version truth, explicit rollback behavior, and a verification pass that closes the interim-drift gap.
**Links:** `products/improvement/04-execution/PLAN.md`, `products/improvement/04-execution/RISKS.md`, `products/improvement/06-architecture/INTERFACES.md`

## Priority 3
**Title:** Roll out the minimum improvement interface across active products, starting with mandatory incident-to-improvement conversion
**Why this matters now:** The first complete incident-to-improvement conversion cycle is done (IMP-ERR-20260315-ARCHIVED-REPO-MISUSE-01 closed 2026-03-17). The template is set. Jobs Review (2026-03-16) generated 4 new improvement-eligible signals now formally in TDE Inbox (OPS-2026-066 through 069 — covering JOB-CI-001 cron delivery, JOB-SEC-001 stale-finding SLA, proof-case retirement, and stale security finding disposition). The minimum interface has not yet been formally specified or deployed across active products.
**Current status:** P3 test case complete — IMP-ERR-20260315-ARCHIVED-REPO-MISUSE-01 closed (Done) as of 2026-03-17T00:36Z. 4 new Jobs Review signals ingested into TDE Inbox with canonical intake packets (OPS-2026-066 through 069). No minimum interface spec deployed yet.
**Next concrete step:** Formalize the minimum product-side improvement interface (intake format, linkage rules, review cadence, mandatory conversion rule for material incidents) using IMP-ERR-20260315 as the reference pattern; begin deploying across active products.
**Links:** `products/improvement/04-execution/PLAN.md`, `products/improvement/06-architecture/INTERFACES.md`, `products/improvement/07-decisions/DECISIONS.md`, `ARCHIVED_REPO_MISUSE_ERROR_REPORT_2026-03-15.md`, `products/improvement/04-execution/intake/`

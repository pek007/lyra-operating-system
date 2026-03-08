# A-004 — Vision

Status: Active draft v1
Product Name: Security
Product Owner: Lyra
Last updated: 2026-03-08

## Mission
Protect Lyra OS, Peter, and current customer environments by making security an owned product capability: explicit boundaries, practical controls, usable guardrails, and evidence-backed reduction of real risk.

## Customers
Primary customers:
- Peter as risk owner and portfolio sponsor
- PXS as the current customer environment consuming Lyra OS capabilities

Primary internal customers:
- Lyra OS product owners who need clear security requirements, controls, and review paths
- Delivery and Improvement functions that need security to be operable, not just advisory

Secondary customers:
- Future customer workspaces consuming product deployments from Lyra OS
- Future operators of security tooling, policies, and evidence loops

## Problems / Jobs
1. Security work can become fragmented across incidents, audits, docs, and ad hoc reviews without a single owning product.
2. Product teams need clear boundaries for what security owns versus what security governs.
3. Security research exists in the library, but it is not yet organized as an operating asset with explicit product relevance.
4. Current risk posture depends on a mix of policy, runtime config, habit, and evidence; weak joins between them create drift.
5. PXS deployment needs a clear statement of what security controls are active, accepted, deferred, or blocked.
6. Important security posture decisions need traceability so residual risk is deliberate rather than accidental.

## Value Proposition
Security gives Lyra OS a working security operating system:
- explicit ownership of security controls, policies, reviews, and evidence loops
- a practical way to convert security research into decisions, controls, and deployment requirements
- visibility into real posture, not just abstract best practice
- product-facing guardrails that reduce downside without freezing delivery
- a deployment stance for PXS that is intentional, reviewable, and improvable over time

In practice, Security owns both:
- protecting the system and customer environments
- improving how security is designed, verified, and operated across products

## Non-goals
- Becoming a generic approval bottleneck for all work
- Owning every product decision that merely has a security implication
- Chasing theoretical hardening at the expense of the current operating model
- Silent changes to trust boundaries, credentials, access posture, or external exposure without explicit logging and escalation
- Treating research accumulation as progress when controls, decisions, or evidence are missing

## Success Definition (qualitative)
Security is successful when:
- every active product knows the security boundary it operates within
- important risks are visible, prioritized, and tied to explicit decisions or remediation work
- PXS deployment has a clear security posture statement with known residual risks
- security evidence is routine enough to catch drift early without creating noisy theater
- Peter is informed on material security decisions and exceptions without having to micromanage routine control work
- security acts as an enabling constraint: strong enough to prevent obvious failure modes, practical enough to keep the system moving

# A-004 — Goals

Status: Active v1
Product Name: Security
Product Owner: Lyra
Last updated: 2026-03-08

## Goal A-004-G1 — Establish Security as an active product with explicit ownership boundaries
- Outcome: Security has a clear operating model, ownership boundary, and product management pack that can be used as the source of truth for security work.
- Leading indicators:
  - A-004 management artifacts are fully populated and maintained
  - A-004 is explicitly registered in the product portfolio
  - Product boundary and decision rights are documented
- Lagging indicators:
  - Less ambiguity about what Security owns versus influences
  - Fewer security decisions repeated informally in chat without durable records
- Guardrails:
  - Keep the operating model practical and lightweight
  - Do not centralize routine decisions unnecessarily
- Owner job role: Security Product Owner
- Exit criteria: A-004 is the canonical management layer for security work in Lyra OS

## Goal A-004-G2 — Make current security posture and residual risk explicit for PXS
- Outcome: PXS has a documented security posture baseline covering active controls, accepted risks, open issues, and verification cadence.
- Leading indicators:
  - Boundary doc references current deployment/customer scope
  - Known posture items and residual risks are linked to decisions or evidence
  - Review cadence for audit evidence is explicit
- Lagging indicators:
  - Fewer surprises in audits or config reviews
  - Faster triage when posture warnings recur
- Guardrails:
  - No hidden acceptance of material risk
  - Material trust-boundary or credential changes are surfaced to Peter
- Owner job role: Security Product Owner / Head of Security
- Exit criteria: Current PXS posture can be understood quickly from product artifacts and linked evidence

## Goal A-004-G3 — Convert security research and incidents into operational controls and backlog
- Outcome: Security research, audit findings, and incidents reliably feed decisions, plans, and improvements rather than remaining passive library content.
- Leading indicators:
  - Current plan initiatives reference real research/evidence inputs
  - Improvement log records actual control/process changes
  - Decision log captures risk acceptance, policy choices, and prioritization trade-offs
- Lagging indicators:
  - Lower recurrence of already-understood security issues
  - More evidence that research influences concrete controls and operating changes
- Guardrails:
  - Favor reversible controls and staged rollout where possible
  - Separate evidence, decision, and enforcement so exceptions remain visible
- Owner job role: Security Product Owner / Auditor interface
- Exit criteria: Security work shows a repeatable research → decision → control → evidence loop

## Goal A-004-G4 — Strengthen continuous security assurance without excessive noise
- Outcome: Security runs an evidence-backed review rhythm that detects drift and material exposure changes early while staying low-noise enough to sustain.
- Leading indicators:
  - Scorecard is defined and used
  - Audit/verification cadence is documented
  - Improvement entries and decisions reference evidence artifacts when posture changes
- Lagging indicators:
  - Stable zero-critical baseline sustained over time
  - Reduced manual effort to understand current posture
- Guardrails:
  - No alert theater
  - Automation must not mutate trust boundaries, secrets, or exposure posture without explicit decisioning
- Owner job role: Security Product Owner
- Exit criteria: Security assurance operates as a routine capability, not an occasional scramble

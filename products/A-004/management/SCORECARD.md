# A-004 — Scorecard

Status: Active v1
Product Name: Security
Product Owner: Lyra
Last updated: 2026-03-08

- Customer value signal:
  - PXS deployment has a current, understandable security posture baseline with known residual risks and review cadence.
  - Primary measure: baseline status = missing / partial / current.

- Reliability/quality signal:
  - Security controls and posture records stay aligned with actual runtime/deployment reality.
  - Primary measures: count of known posture documents older than target review window; count of repeated findings caused by drift.

- Flow signal:
  - Security findings and research are converted into decisions, controls, or backlog without long passive decay.
  - Primary measures: median age of open material security items; count of reviewed research items converted into adopt/watch/reject/backlog states.

- Risk/compliance signal:
  - Maintain zero critical findings in routine security audit evidence and explicit handling of warnings/residual risks.
  - Primary measures: critical count; warning count trend; status of `security.trust_model.multi_user_heuristic`; count of material risks without linked decision/evidence.

- Cost-efficiency signal:
  - Security assurance stays low-noise enough to sustain and does not create unnecessary process drag.
  - Primary measures: number of recurring review steps that produce no useful signal over time; time spent re-establishing posture after change due to missing records.

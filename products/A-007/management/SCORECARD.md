# A-007 — Scorecard

Status: Active

- Customer value signal:
  - `pxs` has a documented way to submit work to TDE and receive outputs without bespoke operator interpretation.
  - Baseline status: not yet achieved; interface/pilot still to be completed.

- Reliability/quality signal:
  - TDE shadow-state parity remains healthy; latest readiness verdict is `GO_CANDIDATE`, not yet canonical GO.
  - Baseline status: technically promising; cutover evidence still incomplete.

- Flow signal:
  - Time from accepted work item to visible execution evidence and outcome is measurable through TDE artifacts/job ticks.
  - Baseline status: instrumentation exists, but real consumer flow is still thin.

- Risk/compliance signal:
  - Readiness gate closure, explicit cutover decision, rollback path, and residual risk acceptance are documented.
  - Baseline status: partially present; owner approval to proceed when requirements are fulfilled is now available, but final GO record is not yet written.

- Cost-efficiency signal:
  - Reusable task/decision automation reduces manual orchestration effort without increasing governance noise or hidden support burden.
  - Baseline status: expected benefit clear; measured efficiency impact not yet established.

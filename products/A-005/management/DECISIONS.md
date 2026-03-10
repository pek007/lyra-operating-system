# A-005 — Decisions

Status: Active
Last updated: 2026-03-08

## Decision A-005-D1
- Context: Portfolio-wide product management framework adoption.
- Decision: Instantiate required artifact set for this product.
- Trade-offs: Minimal setup overhead for better governance consistency.
- Impacted artifacts/processes: Product management artifacts.
- Reversal conditions: N/A

## Decision A-005-D2
- Context: Peter assigned Lyra, in this session/channel, as Product Owner for the Improvement Product with responsibility for continuous improvement across products and ownership of the deployment mechanism to users via the PXS workspace.
- Decision: Operate A-005 as the portfolio improvement control function: run improvement continuously, define the common process, and enable products to execute locally within that process.
- Trade-offs:
  - Gain: clearer ownership, faster improvement execution, better cross-product consistency
  - Cost: higher coordination responsibility concentrated in A-005
  - Risk: over-centralization if product-local autonomy is not preserved
- Impacted artifacts/processes:
  - `products/A-005/management/*`
  - `CONTINUOUS_IMPROVEMENT_PROCESS_V1.md`
  - A-005 deployment into PXS
- Reversal conditions: Revisit if the role should be split between portfolio process ownership and product-local execution ownership

## Decision A-005-D3
- Context: Current A-005 deployment to PXS uses interim-copy, which is acceptable temporarily but creates drift risk.
- Decision: Keep interim-copy as the current operating lane for A-005 only until verification baseline is complete and pinned-lane migration prerequisites are defined; treat pinned dependency as the target state.
- Trade-offs:
  - Gain: fast activation in PXS without blocking on packaging maturity
  - Cost: manual sync/traceability overhead and drift risk
  - Risk: divergence between source assembly and consumed assembly if not actively managed
- Impacted artifacts/processes:
  - `assemblies/continuous-improvement/v0.1/*`
  - `pxs/PXS_ASSEMBLY_LOCK.md`
  - `pxs/docs/assemblies/*`
- Reversal conditions: If pinned-lane packaging proves operationally worse than expected, revisit distribution design with explicit decision packet

## Decision A-005-D4
- Context: Repeated operational misses and incidents only create portfolio learning if they are consistently written down, linked to action, and verified.
- Decision: Establish a mandatory incident-to-improvement loop under A-005. For every material error, incident, or repeated near-miss, the operating system must create a written record, define a preventive action, route it into execution, and verify closure. "Recover and move on" is no longer considered a complete response.
- Trade-offs:
  - Gain: stronger learning rate, lower recurrence, better traceability, clearer ownership
  - Cost: more discipline and modest documentation overhead after failures
  - Risk: process drag if applied to trivial noise instead of material signals
- Impacted artifacts/processes:
  - `products/A-005/management/INCIDENT_TO_IMPROVEMENT_LOOP.md`
  - `products/A-005/management/IMPROVEMENT_LOG.md`
  - `CONTINUOUS_IMPROVEMENT_PROCESS_V1.md`
  - `INCIDENT_LOG.md`
  - related product/task/decision artifacts created from prevention work
- Reversal conditions: Revisit only if a better portfolio-wide closed-loop mechanism replaces it with equal or better traceability and prevention effectiveness

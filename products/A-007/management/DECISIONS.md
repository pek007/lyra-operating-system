# A-007 — Decisions

Status: Active
Product: Task Management / TDE
Product Owner: Lyra
Last updated: 2026-03-09

## Decision A-007-D1
- Context: Portfolio-wide product management framework adoption.
- Decision: Instantiate required artifact set for this product.
- Trade-offs: Minimal setup overhead for better governance consistency.
- Impacted artifacts/processes: Product management artifacts.
- Reversal conditions: N/A

## Decision A-007-D2
- Context: The TDE Product Owner instruction requires active work, blockers, decisions, evidence, and improvement capture to be visible in the canonical operating layer. The TDE product itself was still operating with placeholder management artifacts.
- Decision: Treat activation of the A-007 management artifact set as immediate product work rather than waiting for a later cleanup pass.
- Trade-offs:
  - Pros: Better visibility, clearer goals, less governance drift, stronger weekly review readiness.
  - Cons: Some near-term time spent on product hygiene instead of forward feature/interface work.
- Impacted artifacts/processes:
  - `products/A-007/management/GOALS.md`
  - `products/A-007/management/PLAN.md`
  - `products/A-007/management/IMPROVEMENT_LOG.md`
  - `products/A-007/management/SCORECARD.md`
  - `products/A-007/management/VISION.md`
- Reversal conditions: If artifact overhead materially outweighs decision quality and execution visibility gains.

## Decision A-007-D3
- Context: The product risk profile shows that technical deployment alone is not sufficient; `pxs` must be able to consume TDE via a clear interface.
- Decision: Prioritize a minimal consumer-usable interface definition and pilot path before treating TDE as broadly successful as a product.
- Trade-offs:
  - Pros: Keeps product success tied to real consumption and customer value.
  - Cons: May delay declarations of completion while consumer usability is hardened.
- Impacted artifacts/processes:
  - `products/A-007/management/INTERFACES.md`
  - interface/pilot planning
  - readiness evidence expectations
- Reversal conditions: If product scope changes such that `pxs` is no longer the first downstream consumer.

## Decision A-007-D4
- Context: Continuous improvement guidance for Lyra and product owners requires recurring friction to become visible work and blocked judgment-dependent work to become explicit decisions.
- Decision: Use the following default thresholds for the TDE product:
  - recurring friction observed twice -> create improvement item
  - blocked by trade-off, approval, or prioritization judgment -> create/attach decision record
  - meaningful completion without evidence -> treat as not fully done
- Trade-offs:
  - Pros: Increases consistency, reduces hidden governance debt, improves auditability.
  - Cons: Slightly higher documentation discipline required.
- Impacted artifacts/processes:
  - product-owner workflow
  - weekly reviews
  - improvement log discipline
- Reversal conditions: If thresholds prove too heavy for actual operating tempo and need calibration.

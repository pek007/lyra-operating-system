# Risks

## Purpose
Track the current risks that could prevent Task Management from becoming a reliable and reusable product.

## Current risks

### R-001 — Vega/PXS boundary readiness failure blocks safe downstream consumption
- Description: The current acceptance evidence shows blocking failures in the Vega/PXS boundary model, including cross-domain reads still being allowed.
- Consequence: downstream consumption can become unsafe, ad hoc, or coupled across domains.
- Mitigation: treat boundary readiness as a first-class gating dependency and rerun the acceptance sheet to PASS with evidence.

### R-002 — Readiness description can outrun readiness evidence
- Description: Task Management has strong readiness language and gates, but downstream confidence weakens if canonical-state claims remain provisional or insufficiently evidenced.
- Consequence: consumers build on a moving or ambiguously proven substrate.
- Mitigation: keep readiness tied to explicit evidence, decision records, and compact review surfaces.

### R-003 — Downstream consumption remains softer than the internal product model suggests
- Description: The product model can become elegant while the `pxs` consumption contract still lacks executable schemas/examples and explicit transport semantics.
- Consequence: consumer adoption remains bespoke and fragile.
- Mitigation: make the consumption contract executable, versioned, and example-backed.

### R-004 — Boundary blur between product and coordination layers
- Description: Task Management can unintentionally absorb responsibilities that belong to governance, delivery, or workspace-local operating structures.
- Consequence: hidden coupling, unclear ownership, and weaker product discipline.
- Mitigation: keep provider/consumer boundaries explicit while the downstream consumption path hardens.

### R-005 — Shadow operating state
- Description: Important active work may continue to live in chat or side lists rather than the canonical operating substrate.
- Consequence: lost visibility, weak traceability, and degraded control.
- Mitigation: continue reinforcing TDE as the system of record for active product work.

## Risk posture
Current risk posture is manageable, but the strongest immediate blocker is the unsafe or incomplete downstream consumption path rather than TDE core mechanics alone.

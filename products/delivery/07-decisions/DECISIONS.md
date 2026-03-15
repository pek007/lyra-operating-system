# Decisions

### D-001 — Delivery is treated as a product
- Decision: Delivery is managed as an explicit product capability rather than a background function only.
- Why it matters: This creates ownership for the system that turns intent into shipped capability.

### D-002 — Delivery-as-Code is the target operating pattern
- Decision: Delivery should evolve from document-led coordination toward Delivery-as-Code, where delivery units, gates, evidence, approvals, and rendered outputs are managed from canonical machine-readable state.
- Why it matters: This is the control layer required for high-quality autonomous end-to-end execution with professional auditability.
- Reference: `06-architecture/DELIVERY_AS_CODE_DESIGN_V1.md`

### D-003 — Delivery accepts bounded participation in the One-Iteration TDE UI Pilot
- Decision: Delivery accepts bounded participation in the One-Iteration TDE UI Pilot and will shape the pilot into a bounded Delivery-side contract rather than waiting for the full long-term coordination model.
- Why it matters: This established Delivery as a gate-owning participant in the pilot even though the inbox mechanism used during the experiment has now been superseded.
- References:
  - `products/delivery/04-execution/TDE_UI_PILOT_DELIVERY_CONTRACT_V1.md`
  - `ONE_ITERATION_TDE_UI_PILOT_V1.md`

### D-004 — Delivery adopts an artifact-first research layer with broad radar and bounded deep dives
- Decision: Delivery adopts `08-research/` as a canonical product layer, using a broad domain map and radar for awareness plus a limited set of active deep dives for detailed analysis. Research is valid only when it updates doctrine, implications, decisions, plans, controls, or other canonical product artifacts.
- Why it matters: This makes Delivery learning cumulative, keeps the product broad enough to avoid blind spots, preserves context separation from Control Tower, and prevents research from degrading into prompt theater or low-signal reporting.

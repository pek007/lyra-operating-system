# Decisions

### D-001 — Delivery is treated as a product
- Decision: Delivery is managed as an explicit product capability rather than a background function only.
- Why it matters: This creates ownership for the system that turns intent into shipped capability.

### D-002 — Delivery-as-Code is the target operating pattern
- Decision: Delivery should evolve from document-led coordination toward Delivery-as-Code, where delivery units, gates, evidence, approvals, and rendered outputs are managed from canonical machine-readable state.
- Why it matters: This is the control layer required for high-quality autonomous end-to-end execution with professional auditability.
- Reference: `06-architecture/DELIVERY_AS_CODE_DESIGN_V1.md`

### D-003 — Delivery accepts bounded participation in the One-Iteration TDE UI Pilot
- Decision: Delivery accepts the first inbox-based cross-product request from Task Management and will shape the pilot into a bounded Delivery-side contract rather than waiting for the full long-term coordination model.
- Why it matters: This turns the interim coordination pattern into a real operational test and keeps Delivery active as a gate-owning product rather than a passive observer.
- References:
  - `products/delivery/08-inbox/REQ-20260312-001__from-task-management__tde-ui-pilot-delivery-support.md`
  - `ONE_ITERATION_TDE_UI_PILOT_V1.md`

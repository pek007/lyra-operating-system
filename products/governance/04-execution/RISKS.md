# Risks

### R-001 — Governance product can lag behind the standards it expects from other products
- Description: Governance may demand explicit goals, evidence, and control discipline from the portfolio while its own product execution remains less concrete or measurable.
- Consequence: credibility loss, weak review discipline, and slower governance improvement.
- Mitigation: keep Governance operated as a real product with explicit priorities, plan, metrics, and reviewable outcomes.

### R-002 — Governance assembly remains scaffolded rather than truly consumable
- Description: The governance assembly can appear ready at the manifest level while still depending on external canonical sources and under-specified packaging decisions.
- Consequence: downstream adoption remains partial, verification becomes shallow, and install/promote semantics stay weaker than intended.
- Mitigation: make the assembly packaging decision explicit, keep verify aligned with the chosen packaging model, and treat assembly completeness as a tracked product outcome.

### R-003 — Machine-checkable governance does not yet cover the governance assembly surface strongly enough
- Description: Repo validation is a major governance leverage point, but assembly integrity/completeness is not yet fully part of that enforcement surface.
- Consequence: governance packaging can drift outside the very control model Governance is meant to provide.
- Mitigation: treat assembly validation/completeness as a next-step governance implementation priority.

### R-004 — Registry and source-of-truth relationships can drift
- Description: portfolio/product/assembly layers can answer different questions, but if their relationships are not explicit enough they create ambiguity about what is canonical for product state versus packaging state.
- Consequence: stale metadata, unclear progress tracking, and avoidable governance confusion.
- Mitigation: keep product priorities, assembly state, and adoption status explicitly linked in Governance artifacts.

# Decisions

### D-001 — Control Panel is treated as an explicit product
- Decision: The control surface is managed as a product with its own boundary and operating model.
- Why it matters: This preserves architectural discipline and future optionality.

### D-002 — Control Panel scope includes operator-facing stewardship of the Lyra OS Model
- Decision: Control Panel is expanded to include the operator-facing maintenance, coherence review, and improvement-routing layer for the Lyra OS Model.
- Why it matters: Once Lyra OS has an explicit Model, the system needs a product that helps operators inspect model coherence, surface drift, and coordinate model evolution without collapsing all underlying domain ownership into one product.

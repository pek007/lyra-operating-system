# Risks

### R-001 — Interfaces identity and ownership collision
- Description: Interfaces currently risks collision between the cross-cutting interfaces product/assembly and provider-specific interface artifacts owned by other products.
- Consequence: governance confusion, approval ambiguity, and downstream integration drift.
- Mitigation: make Interfaces ownership explicit as standards/packaging/change-governance owner, not owner of every concrete provider API/interface.

### R-002 — Assembly packaging is not yet self-consistent
- Description: The Interfaces assembly has had a mismatch between declared paths/links and actual on-disk packaging.
- Consequence: verification, installation, and pinned-lane migration become shallow or impossible.
- Mitigation: keep the assembly self-consistent, installable, and explicit about exported artifacts.

### R-003 — Verification remains thinner than promotion requires
- Description: Interfaces has strong contract ideas and evaluation concepts, but activation/verify mechanics are still too light to function as a real promotion gate.
- Consequence: downstream consumers may pin or trust an interface pack without strong proof of behavioral value.
- Mitigation: require one real workflow evidence link, explicit installation/audit checks, and a drift guard for contract changes.

### R-004 — Export-scope creep
- Description: Interfaces can become a residual catch-all for boundary problems or stealth expansion of OS exports into PXS.
- Consequence: weak product boundaries and hidden coupling across the portfolio.
- Mitigation: keep export scope and provider-vs-standard ownership explicit.

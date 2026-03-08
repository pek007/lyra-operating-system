# A-007 — Risks

Status: Active

## Risk A-007-R1 — Premature cutover
- Description: Declaring TDE fully deployed before the technical gate is truly closed could create silent reliability or rollback problems.
- Control: Use `TDE_PRODUCTION_READINESS_GATE_V1.md` as the minimum cutover gate; require evidence-backed closure and a recorded GO decision.
- Reopen trigger: Any unresolved gate item, rollback-test weakness, or unexplained parity drift.

## Risk A-007-R2 — Product deployed technically but unusable by consumers
- Description: TDE could be live internally while `pxs` still lacks a clear way to consume it.
- Control: Treat interface contract and consumer pilot as first-class product work; do not equate engine activation with product success.
- Reopen trigger: Repeated bespoke/manual workarounds for consumer use.

## Risk A-007-R3 — Boundary erosion through convenience integration
- Description: Pressure to make `pxs` consumption easy could lead to undocumented cross-workspace coupling.
- Control: Follow `LYRA_OS_PXS_INTEGRATION_PLAN_V1.md`; prefer explicit handoff/capability interfaces.
- Reopen trigger: Hidden cross-domain reads/writes, undocumented dependencies, or authority ambiguity.

## Risk A-007-R4 — Delegated deployment authority used without enough visibility
- Description: Having advance approval could tempt overly narrow internal interpretation of "requirements fulfilled."
- Control: Record evidence, decision, and residual risks clearly at cutover; keep Peter informed on larger decisions and any real-world-impacting activation.
- Reopen trigger: Material new risk, unclear evidence, or scope expansion at cutover.

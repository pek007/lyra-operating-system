# Decisions

### D-001 — Security is treated as a product
- Decision: Security is managed as an explicit product rather than only a cross-cutting concern.
- Why it matters: This creates ownership, continuity, and operable controls.

### D-002 — Security owns controls, posture, and security research conversion; it does not own all execution
- Decision: Security owns security policy/control design, posture assessment, residual-risk decision support, research intake for security topics, and deployment security requirements. Product teams still own implementation inside their boundaries unless work is explicitly transferred.
- Why it matters: This preserves domain ownership in each product while keeping Security authoritative on security posture.

### D-003 — Routine Security work is autonomous; material security changes are surfaced to Peter
- Decision: Routine low-risk Security product work may be executed without prior approval. Material trust-boundary shifts, credential/access changes, unresolved significant risk acceptance, or broad cross-product consequences are surfaced to Peter promptly.
- Why it matters: This maintains speed for normal work while keeping human oversight where downside matters.

### D-004 — Maintain a standing `pxs` deployment baseline as a Security-owned posture artifact
- Decision: Security maintains a concise product-owned baseline artifact for `pxs` that summarizes active controls, accepted residual risks, open non-blocking issues, and mandatory review triggers.
- Why it matters: This makes posture review, change control, and handoff clearer and less dependent on scattered evidence.

### D-005 — Security adopts an artifact-first research layer with broad radar and bounded deep dives
- Decision: Security adopts `08-research/` as a canonical product layer, using a broad domain map and radar for awareness plus a limited set of active deep dives for detailed analysis. Research is valid only when it updates doctrine, implications, decisions, plans, controls, or other canonical product artifacts.
- Why it matters: This makes Security learning cumulative, keeps the product broad enough to avoid blind spots, preserves context separation from Control Tower, and prevents research from degrading into prompt theater or low-signal reporting.

### D-006 — Security maintains an explicit estate-and-surface model across Lyra OS and `pxs`
- Decision: Security should maintain a canonical picture of the environments, trust boundaries, identity surfaces, execution surfaces, and major platform/integration surfaces it is responsible for across Lyra OS and `pxs`.
- Why it matters: Security strategy and control design degrade when the estate grows faster than the canonical picture of what exists.

### D-007 — Material surface change must trigger explicit Security review
- Decision: Material new platforms, integrations, identity/admin surfaces, external write paths, or other meaningful attack-surface expansions should be recorded explicitly and translated into posture, capability, and planning consequences.
- Why it matters: This prevents new exposure from becoming normal by drift before Security has assessed what changed.

### D-008 — Upstream OpenClaw change monitoring is an operational Security function
- Decision: Monitoring OpenClaw releases, security fixes, changed defaults, and other upstream security-relevant changes is part of Security’s ongoing operating responsibility, not optional background research.
- Why it matters: Local posture can change relative to upstream risk reality even when local configuration stays stable.

### D-009 — External wrappers and ecosystem patterns are intelligence inputs, not automatic adoption candidates
- Decision: External wrappers, hardening approaches, and practitioner patterns should be assessed primarily as sources of design intelligence and capability insight. Direct adoption is optional and should occur only when fit is strong.
- Why it matters: This allows Security to learn from the ecosystem without turning every external artifact into an impulsive tooling decision.

### D-010 — Accepted current-state posture must be kept separate from future hardening work
- Decision: Security should distinguish clearly between what is accepted as current Phase 1 posture and what remains future hardening or externalization work.
- Why it matters: This prevents the product from either overstating current assurance or repeatedly presenting accepted conditions as unresolved blockers.

### D-011 — Auditability and traceability are explicit Security capability concerns
- Decision: Security should treat the ability to reconstruct material actions, failures, and control-relevant events as an explicit capability area, beginning with a narrow first standard for high-risk actions and surfaces.
- Why it matters: Control verification, incident reconstruction, and learning loops remain too weak if traceability is assumed rather than designed.

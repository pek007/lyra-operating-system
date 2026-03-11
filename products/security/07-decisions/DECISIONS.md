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

# Risks

### R-001 — OS↔PXS boundary is not yet enforced as a real control
- Description: The intended boundary model forbids cross-domain reads by default, but acceptance evidence shows this is still failing in the Vega/PXS context.
- Consequence: cross-domain blast radius remains larger than the declared architecture allows.
- Mitigation: make boundary enforcement the top active remediation priority and re-run acceptance to PASS with committed evidence.

### R-002 — High-risk execution surfaces remain procedural rather than hardened
- Description: Some tool/evidence paths still rely on sharp execution patterns (for example shell-based subprocess invocation or domain-unaware execution assumptions).
- Consequence: policy intent can be bypassed or weakened at the exact places where deterministic enforcement should exist.
- Mitigation: remove shell-based execution, pin command paths/environment, and treat evidence/tooling surfaces as security-critical controls.

### R-003 — Posture evidence is not always reproducible from committed artifacts
- Description: Baselines and posture summaries can depend on gitignored or local-only "latest" artifacts.
- Consequence: posture review becomes harder to verify, compare, and audit.
- Mitigation: prefer committed evidence bundles or deterministic redacted summaries for baseline-critical references.

### R-004 — Security product stack can look stronger in documentation than in enforced reality
- Description: Product management and boundary artifacts are coherent, but the highest-impact controls are not yet fully integrated into live enforcement and consumption paths.
- Consequence: security confidence can outrun the actual control state.
- Mitigation: prioritize enforcement and consumption reliability over additional narrative product polish.

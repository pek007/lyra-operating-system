# Risks

Status: Active
Product: Security (`A-004`)
Owner: Lyra
Date: 2026-03-19

## Purpose
Record the current material Security risks across Lyra OS and `pxs` in a way that distinguishes:
- accepted current-state posture
- active risk requiring remediation or tighter control
- future hardening work that should not be misrepresented as a present blocker

## Risk framing rule
A risk may be real even when the current operating posture is still accepted.
Security should keep current-state acceptance honest without collapsing future hardening needs into false current-state failure.

## Active risks

### R-001 — High-risk execution surfaces remain more procedural than deterministic
- **Description:** Some tool, automation, and evidence paths still depend too much on careful operating behavior rather than stronger deterministic controls.
- **Affected scope:** Lyra OS, downstream `pxs` surfaces that rely on Lyra OS control integrity
- **Consequence:** Security intent can drift from runtime reality at the exact places where enforcement matters most.
- **Current posture:** Accepted as a Phase 1 condition in limited contexts, but still a top hardening priority.
- **Mitigation direction:** Narrow and harden the highest-risk execution surfaces first, especially where external write, evidence generation, or privilege-sensitive actions are involved.

### R-002 — Posture evidence is not always reproducible from committed artifacts
- **Description:** Baselines and posture summaries can still depend partly on local-only or latest-state references rather than committed deterministic evidence bundles.
- **Affected scope:** Lyra OS, `pxs`, Security review and auditability
- **Consequence:** Review, comparison, and audit confidence weaken when baseline-critical posture claims are not easily reproducible.
- **Current posture:** Active risk; not necessarily a blocker to current operation, but a reliability and assurance weakness.
- **Mitigation direction:** Prefer committed evidence bundles or deterministic redacted summaries for baseline-critical references and promotion decisions.

### R-003 — Security estate growth can outpace explicit posture translation
- **Description:** The operating estate now includes more than the original boundary-and-baseline frame, including Google Workspace and other expanding external/integration surfaces.
- **Affected scope:** `pxs`, Google Workspace, integrations, communication/document surfaces
- **Consequence:** New attack surfaces may become operationally normal before their security implications, capabilities, and minimum posture expectations are made explicit.
- **Current posture:** Newly elevated active risk.
- **Mitigation direction:** Use `ESTATE_MAP.md`, `SURFACE_CHANGE_LOG.md`, and `CAPABILITY_MAP.md` to force explicit review and posture translation whenever a material new platform or surface is introduced.

### R-004 — Upstream OpenClaw change can alter local risk faster than the product stack adapts
- **Description:** OpenClaw evolves quickly, including fixes for known weaknesses and changes to behavior or defaults. Local posture can drift relative to upstream risk reality even without local configuration changes.
- **Affected scope:** Lyra OS directly; `pxs` indirectly through dependency on Lyra OS controls
- **Consequence:** Version drift or unassessed upstream changes can leave Security carrying unclear residual risk.
- **Current posture:** Active risk now explicitly recognized as a standing Security concern.
- **Mitigation direction:** Run explicit upstream monitoring and classify changes into watch, plan, update-now, or defer-with-risk-note dispositions.

### R-005 — Auditability and traceability are still underdefined for the highest-risk actions
- **Description:** Security increasingly depends on being able to reconstruct what happened, what failed, and whether controls actually fired, but the current minimum standard for high-value traceability is still incomplete.
- **Affected scope:** Lyra OS, `pxs`, external write surfaces, automation-heavy paths
- **Consequence:** Investigation, control verification, and post-incident learning remain weaker than they should be.
- **Current posture:** Active capability gap rather than proof of immediate failure.
- **Mitigation direction:** Define a narrow first traceability/logging standard for the highest-risk actions and surfaces.

## Accepted current-state conditions that should not be misread as unresolved blockers

### A-001 — Phase 1 accepted boundary posture is not the same as long-term hard compartmentalization
- **Description:** Current accepted posture does not yet claim full long-term compartmentalization across all contexts.
- **Why this matters:** Security should not keep presenting accepted current-state conditions as though they remain undecided blockers.
- **Current stance:** Accepted for Phase 1 with explicit future hardening still open.
- **Reopen triggers:** stronger confidentiality requirements, broader multi-user exposure, or changes that materially widen current trust assumptions.

## Maintenance rule
Keep this artifact focused on material active risks and accepted current-state conditions that need disciplined framing. Do not overload it with every minor warning or every future nice-to-have improvement.

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
- **Description:** The operating estate now includes more than the original boundary-and-baseline frame, including Google Workspace and other expanding external/integration surfaces, and the current gap is no longer recognition alone but standing translation into baseline, risk, review, and direct-evidence expectations.
- **Affected scope:** `pxs`, Google Workspace, integrations, communication/document surfaces, critical-account/admin surfaces
- **Consequence:** New attack surfaces may become operationally normal before their security implications, minimum posture expectations, and direct provider/admin proof requirements are made explicit on standing control surfaces.
- **Current posture:** Active risk with sharper evidence on 2026-04-02/2026-04-03; current priority is integration and closure rather than further broad discovery.
- **Mitigation direction:** Use `ESTATE_MAP.md`, `SURFACE_CHANGE_LOG.md`, `CAPABILITY_MAP.md`, `2026-04-02_GOOGLE_WORKSPACE_MINIMUM_POSTURE_CHECKLIST__PXS.md`, `2026-04-03_ESTATE_BASELINE_RISK_ALIGNMENT_STEP.md`, and `2026-04-03_GOOGLE_WORKSPACE_PROOF_GAP_STATUS_MATRIX__PXS.md` to force explicit review and posture translation whenever a material new platform or surface is introduced and to keep the remaining direct-proof items compact and operator-facing.

### R-004 — Upstream OpenClaw change can alter local risk faster than the product stack adapts
- **Description:** OpenClaw evolves quickly, including fixes for known weaknesses and changes to behavior or defaults. Local posture can drift relative to upstream risk reality even without local configuration changes.
- **Affected scope:** Lyra OS directly; `pxs` indirectly through dependency on Lyra OS controls
- **Consequence:** Version drift or unassessed upstream changes can leave Security carrying unclear residual risk.
- **Current posture:** Active risk now explicitly recognized as a standing Security concern.
- **Mitigation direction:** Run explicit upstream monitoring and classify changes into watch, plan, update-now, or defer-with-risk-note dispositions.

### R-005 — Auditability and traceability are still underdefined for the highest-risk actions
- **Description:** Security increasingly depends on being able to reconstruct what happened, what failed, and whether controls actually fired, and current evidence now shows that execution success, routing success, and outbound delivery success are distinct truth surfaces that can diverge even when job intent looks correct.
- **Affected scope:** Lyra OS, `pxs`, external write surfaces, automation-heavy paths, messaging/delivery paths, approval/admin-sensitive actions
- **Consequence:** Investigation, control verification, and post-incident learning remain weaker than they should be, and recurring-output surfaces can look healthier than their real end-to-end closure state.
- **Current posture:** Active capability gap with a first minimum standard and first applied evidence note now in place; the remaining gap is adoption across standing control surfaces.
- **Mitigation direction:** Apply `2026-04-02_MINIMUM_TRACEABILITY_STANDARD_FOR_HIGH_RISK_ACTIONS.md`, `2026-04-02_TELEGRAM_OUTBOUND_DELIVERY_PATH_EVIDENCE_NOTE.md`, and `2026-04-03_ESTATE_BASELINE_RISK_ALIGNMENT_STEP.md` so high-risk paths keep execution, routing, delivery, and evidence status distinct.

### R-006 — Prompt injection exposure is not yet coherently translated into standing security controls
- **Description:** Lyra/OpenClaw operates in an environment where untrusted content, browser/tool use, external messaging, and broad runtime authority can combine into meaningful prompt injection risk, but current defenses are still only partially translated into explicit standing security controls and review routines.
- **Affected scope:** Lyra OS, `pxs`, browser/web-fetch paths, tool-using runtimes, outbound communication paths, shared-trust contexts
- **Consequence:** Prompt injection remains a live cross-cutting risk whose blast radius may exceed current control clarity, especially in paths that combine untrusted content with powerful runtime actions.
- **Current posture:** Active risk newly translated from research into a draft Security capability posture; controls exist in part but are not yet unified or fully reviewed as a coherent defense capability.
- **Mitigation direction:** Use `2026-04-03_PROMPT_INJECTION_DEFENSE_CAPABILITY.md`, `2026-04-03_PROMPT_INJECTION_DEFENSE_CONTROL_CHECKLIST.md`, and `2026-04-03_PROMPT_INJECTION_DEFENSE_PLAN.md` to move from research posture into standing review and targeted hardening.

## Accepted current-state conditions that should not be misread as unresolved blockers

### A-001 — Phase 1 accepted boundary posture is not the same as long-term hard compartmentalization
- **Description:** Current accepted posture does not yet claim full long-term compartmentalization across all contexts.
- **Why this matters:** Security should not keep presenting accepted current-state conditions as though they remain undecided blockers.
- **Current stance:** Accepted for Phase 1 with explicit future hardening still open.
- **Reopen triggers:** stronger confidentiality requirements, broader multi-user exposure, or changes that materially widen current trust assumptions.

## Maintenance rule
Keep this artifact focused on material active risks and accepted current-state conditions that need disciplined framing. Do not overload it with every minor warning or every future nice-to-have improvement.

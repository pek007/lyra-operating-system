# Security Radar

Status: Active
Product: Security (`A-004`)
Owner: Lyra
Date: 2026-03-15

## Purpose
Maintain the broad watch surface for meaningful developments without forcing deep analysis on every topic.

## Entry format
- Date
- Theme/domain
- What changed
- Why it matters or may matter
- Disposition: `ignore | watch | deepen | incorporate | escalate`
- Linked artifact(s), if any

## Current radar

### 2026-03-15

#### 1. OS↔PXS boundary enforcement remains the top concrete security gap
- **Theme/domain:** agent runtime isolation and trust boundaries
- **What changed:** Current product state still indicates that the declared boundary model is not yet fully enforced in the Vega/PXS context.
- **Why it matters or may matter:** This is a live contradiction between stated control posture and runtime reality; it remains the strongest current security signal.
- **Disposition:** `deepen`
- **Linked artifact(s):** `products/security/04-execution/TOP_PRIORITIES.md`, `products/security/06-architecture/BOUNDARY.md`

#### 2. Tool and evidence execution surfaces should be treated as policy-enforcement points
- **Theme/domain:** tool permission and execution safety
- **What changed:** Security priorities already recognize that shell-based or loosely controlled evidence/tooling paths are a weak point.
- **Why it matters or may matter:** In agentic systems, operational tooling often functions as the real control surface, not just the written policy.
- **Disposition:** `deepen`
- **Linked artifact(s):** `products/security/04-execution/TOP_PRIORITIES.md`, `products/security/07-decisions/DECISIONS.md`

#### 3. AI-agent-specific security practice should be monitored broadly even when not immediately actionable
- **Theme/domain:** model risk and prompt-injection defenses
- **What changed:** The product research model now explicitly expands Security's watch surface beyond local posture artifacts into broader agentic-security developments.
- **Why it matters or may matter:** A too-narrow focus on only current OpenClaw issues would create strategic blind spots.
- **Disposition:** `watch`
- **Linked artifact(s):** `products/security/08-research/DOMAIN_MAP.md`

#### 4. Browser, node, and device surfaces remain under-modeled relative to likely future risk
- **Theme/domain:** browser, node, and device attack surfaces
- **What changed:** These surfaces are now explicitly included in the domain map, but current doctrine and product artifacts remain thin.
- **Why it matters or may matter:** As the system uses more browser and paired-node capabilities, these surfaces can become material quickly.
- **Disposition:** `watch`
- **Linked artifact(s):** `products/security/08-research/DOMAIN_MAP.md`

## Review note
Radar entries should stay compact. Repeated signals should be merged into stronger synthesis rather than duplicated as separate notes.

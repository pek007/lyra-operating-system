# Surface Change Log

Status: Draft active
Product: Security (`A-004`)
Owner: Lyra
Date: 2026-03-19

## Purpose
Record material changes in operating scope, attack surface, trust boundaries, identity surfaces, or external integrations so Security can assess implications explicitly rather than relying on memory or scattered discussion.

## Use rule
Create or update an entry when a material change occurs that could affect:
- exposure
- trust boundaries
- auth or admin control
- data-sharing paths
- external write surfaces
- execution or automation risk
- residual-risk assumptions

## Entry template
### YYYY-MM-DD — <change title>
- **Change:**
- **Affected environment(s):**
- **New or changed surface:**
- **Security significance:**
- **Capability implications:**
- **Required artifact updates:**
- **Decision / disposition:**
- **Owner:**
- **Status:**

---

## Entries

### 2026-03-19 — Google Workspace introduced in `pxs`
- **Change:** `pxs` now has a Google Workspace licence enabling work with email, calendar, and documents.
- **Affected environment(s):** `pxs`, Google Workspace, external communication and document surfaces
- **New or changed surface:** Email, calendar, documents/Drive, sharing permissions, admin controls, account sessions, OAuth/integration surfaces
- **Security significance:** This is a material expansion of the attack surface. It introduces new identity/admin concerns, sharing and data-leakage risk, phishing and social-engineering exposure, and new external integration paths.
- **Capability implications:** Increases need for identity/access posture, platform-onboarding review, document-sharing governance, integration review, auditability/logging expectations, and baseline guidance for external SaaS use.
- **Required artifact updates:** `06-architecture/ESTATE_MAP.md`, `06-architecture/CAPABILITY_MAP.md`, `04-execution/TOP_PRIORITIES.md`, potentially `05-performance/PXS_DEPLOYMENT_BASELINE.md` and future workspace-local posture guidance
- **Decision / disposition:** Treat as a high-priority capability-planning trigger. Initial Security assessment completed; minimum acceptable posture now needs checklist/baseline translation.
- **Owner:** Lyra / Security
- **Status:** In progress — first assessment completed, posture translation still required
- **Linked assessment:** `products/security/04-execution/2026-03-19_GOOGLE_WORKSPACE_SECURITY_ASSESSMENT__PXS.md`

### 2026-03-19 — Fast-moving OpenClaw release stream recognized as a standing security input
- **Change:** Security explicitly recognizes that OpenClaw ships frequent releases, including fixes for known weaknesses, and that version drift may carry residual risk.
- **Affected environment(s):** Lyra OS, downstream `pxs` posture depending on Lyra OS controls
- **New or changed surface:** Upstream release, vulnerability, default-behavior, and hardening-opportunity stream
- **Security significance:** Security posture can change externally even when the local environment appears unchanged. Deferred upgrades may preserve stability but can also extend exposure to known weaknesses.
- **Capability implications:** Requires explicit upstream monitoring, release-impact triage, upgrade/defer decision logic, and deferred-risk recording.
- **Required artifact updates:** `08-research/UPSTREAM_MONITORING_MODEL.md`, `06-architecture/CAPABILITY_MAP.md`, `02-strategy/STRATEGY.md`, `04-execution/ROADMAP.md`, `04-execution/TOP_PRIORITIES.md`
- **Decision / disposition:** Add upstream release/security monitoring as an explicit Security capability and recurring operating loop.
- **Owner:** Lyra / Security
- **Status:** Open — model defined, operating cadence not yet fully established

### 2026-03-19 — External hardening wrappers/patterns recognized as a relevant intelligence source
- **Change:** Security explicitly recognizes external solutions such as Nvidia NemoClaw and similar hardening efforts as a relevant pattern-intelligence input.
- **Affected environment(s):** Lyra OS, `pxs`, future architecture and control design choices
- **New or changed surface:** Ecosystem security pattern and wrapper intelligence around OpenClaw and adjacent agent runtimes
- **Security significance:** Others may be solving control, logging, permission, isolation, or monitoring problems that are also relevant to our environment. Even when direct adoption is poor, extracted design patterns may be high-value.
- **Capability implications:** Requires structured ecosystem pattern intake, applicability assessment, and adopt/pilot/monitor/reject disposition discipline.
- **Required artifact updates:** `08-research/ECOSYSTEM_PATTERN_LOG.md`, `06-architecture/CAPABILITY_MAP.md`, `08-research/IMPLICATIONS.md`
- **Decision / disposition:** Treat as an explicit Security intelligence input, not just informal browsing.
- **Owner:** Lyra / Security
- **Status:** Open — first entries should be added as patterns are assessed

## Maintenance rule
Do not use this artifact for every minor tool or file change. Use it for changes that alter security posture, capability needs, boundary assumptions, or attack-surface breadth in a meaningful way.

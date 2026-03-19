# Security Capability Map

Status: Draft active
Product: Security (`A-004`)
Owner: Lyra
Date: 2026-03-19

## Purpose
Define the capability set Security needs in order to govern Lyra OS and `pxs` effectively as the operating estate, attack surface, upstream platform, and ecosystem context evolve.

## Design principle
Security capability planning should be driven by:
- the environments we actually operate
- the attack surfaces we actually expose
- the upstream platform changes we depend on
- the external patterns that reveal useful controls or capability gaps

Security should not be limited to static posture statements or reactive audits.
It should maintain the capability set required to keep the current security picture usable and actionable.

## Capability inventory

### 1. Estate and exposure mapping
- **Purpose:** Maintain a current map of the environments, trust boundaries, major surfaces, and material changes in scope
- **Primary environments served:** Lyra OS, `pxs`, Google Workspace, browser/device surfaces, integrations
- **Current maturity:** Emerging
- **Current owner:** Security
- **Current gaps:** Previously implicit rather than canonical; new surfaces can appear faster than the canonical map updates
- **Priority:** High
- **Linked artifacts:** `06-architecture/ESTATE_MAP.md`, `04-execution/SURFACE_CHANGE_LOG.md`
- **Upgrade trigger:** Any recurring ambiguity about what is in scope or where a material surface sits

### 2. Security baseline and posture management
- **Purpose:** Maintain explicit accepted posture, baseline expectations, residual-risk framing, and review triggers
- **Primary environments served:** Lyra OS, `pxs`
- **Current maturity:** Usable
- **Current owner:** Security
- **Current gaps:** Some baseline assumptions still rely on narrative clarity rather than stronger verification
- **Priority:** High
- **Linked artifacts:** `05-performance/PXS_DEPLOYMENT_BASELINE.md`, `05-performance/METRICS.md`, `03-operating-model/*`
- **Upgrade trigger:** When environment complexity or externalization expectations outgrow the current baseline format

### 3. Boundary and trust-surface governance
- **Purpose:** Define, review, and keep honest the critical trust boundaries and high-risk interaction surfaces
- **Primary environments served:** Lyra OS ↔ `pxs`, external integration surfaces, human/admin ↔ automation boundaries
- **Current maturity:** Usable
- **Current owner:** Security
- **Current gaps:** Some accepted Phase 1 conditions still leave future hardening work open
- **Priority:** High
- **Linked artifacts:** `06-architecture/BOUNDARY.md`, `06-architecture/INTERFACES.md`, `07-decisions/DECISIONS.md`
- **Upgrade trigger:** When confidentiality or stronger compartmentalization requirements become active

### 4. Auditability, logging, and traceability
- **Purpose:** Ensure that material actions, failures, and control-relevant events can be reconstructed and investigated
- **Primary environments served:** Lyra OS, `pxs`, external write surfaces, automation flows
- **Current maturity:** Early / uneven
- **Current owner:** Security with provider implementation distributed
- **Current gaps:** Logging and traceability expectations are not yet defined clearly enough as a capability with minimum standards
- **Priority:** High
- **Linked artifacts:** `04-execution/SURFACE_CHANGE_LOG.md`, future posture/evidence artifacts, review outputs
- **Upgrade trigger:** Recurring ambiguity about what happened, what failed, or whether controls actually fired

### 5. Upstream release and vulnerability impact assessment
- **Purpose:** Monitor OpenClaw and other key upstream changes and classify their local impact
- **Primary environments served:** Lyra OS, downstream `pxs` posture dependent on Lyra OS
- **Current maturity:** Emerging
- **Current owner:** Security
- **Current gaps:** Monitoring and triage logic were previously implicit rather than codified
- **Priority:** High
- **Linked artifacts:** `08-research/UPSTREAM_MONITORING_MODEL.md`, `04-execution/SURFACE_CHANGE_LOG.md`
- **Upgrade trigger:** Frequent release drift, security-fix deferrals, or uncertainty about upgrade urgency

### 6. Ecosystem pattern intake and applicability assessment
- **Purpose:** Learn from wrappers, hardening approaches, and community/security ecosystem patterns without drifting into unsystematic browsing
- **Primary environments served:** Lyra OS, `pxs`, future architecture/control design
- **Current maturity:** Emerging
- **Current owner:** Security
- **Current gaps:** Useful external signals can be noticed but not consistently converted into local implications or decisions
- **Priority:** Medium-high
- **Linked artifacts:** `08-research/ECOSYSTEM_PATTERN_LOG.md`, `08-research/IMPLICATIONS.md`
- **Upgrade trigger:** Repeated discovery of useful external ideas with no consistent translation path

### 7. Integration and platform onboarding review
- **Purpose:** Assess new platforms and services for security implications before or shortly after they become material parts of the operating environment
- **Primary environments served:** `pxs`, external SaaS/services, communication and document platforms
- **Current maturity:** Early
- **Current owner:** Security with environment-owner coordination
- **Current gaps:** New service introduction can outpace explicit posture translation; Google Workspace is a current test case
- **Priority:** High
- **Linked artifacts:** `06-architecture/ESTATE_MAP.md`, `04-execution/SURFACE_CHANGE_LOG.md`, workspace-local posture artifacts as they emerge
- **Upgrade trigger:** New SaaS or external platforms entering active use

### 8. Identity, access, and secret posture
- **Purpose:** Keep human/admin identities, sessions, credentials, service authority, and privilege boundaries understandable and proportionate to risk
- **Primary environments served:** Lyra OS, `pxs`, Google Workspace, messaging/integration surfaces
- **Current maturity:** Partial
- **Current owner:** Security
- **Current gaps:** Identity growth may outpace explicit auth/admin/session posture documentation
- **Priority:** High
- **Linked artifacts:** `06-architecture/ESTATE_MAP.md`, baseline docs, governance and future platform-specific guidance
- **Upgrade trigger:** Additional admin roles, service accounts, integrations, or durable credentials becoming material

### 9. Security review and evidence loop
- **Purpose:** Detect posture drift, risk signals, and remediation needs through recurring review and evidence generation
- **Primary environments served:** Lyra OS, `pxs`
- **Current maturity:** Usable
- **Current owner:** Security
- **Current gaps:** Review-to-remediation and research-to-action conversion still need tightening in some areas
- **Priority:** High
- **Linked artifacts:** review artifacts, evidence outputs, `04-execution/PLAN.md`, `04-execution/TOP_PRIORITIES.md`
- **Upgrade trigger:** If review produces narrative without clear disposition or action

### 10. Capability planning and prioritization
- **Purpose:** Translate estate changes, upstream changes, and ecosystem findings into strategy, roadmap, priorities, and explicit investment choices
- **Primary environments served:** Security product as a whole
- **Current maturity:** Emerging
- **Current owner:** Security / Product Owner / Control Tower coordination
- **Current gaps:** The product has priorities and roadmap, but not yet a fully explicit capability-planning layer tied to the broader security estate
- **Priority:** High
- **Linked artifacts:** `02-strategy/STRATEGY.md`, `04-execution/ROADMAP.md`, `04-execution/TOP_PRIORITIES.md`, this artifact
- **Upgrade trigger:** When major environment or platform changes occur without a clear translation into Security strategy

## Current priority interpretation
The highest current leverage areas are:
1. estate and exposure clarity
2. upstream release/security impact assessment
3. integration onboarding review for new SaaS surfaces such as Google Workspace
4. auditability/logging/traceability maturity
5. stronger capability-planning translation into strategy and priorities

## Maintenance rule
Do not let this become a static taxonomy. Update it when the estate changes, when recurring security work reveals a capability gap, or when the strategy/roadmap needs a more explicit capability rationale.

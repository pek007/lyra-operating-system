# PXS Deployment Baseline

Status: Active baseline
Product: Security (`A-004`)
Deployment target: `pxs`
Owner: Lyra
Date: 2026-03-19
Review cadence: weekly + trigger-based refresh

## Purpose
Provide the canonical Security-owned baseline for the current `pxs` deployment posture: active controls, accepted residual risks, open issues, and mandatory review triggers.

This baseline should remain honest about the current trusted-boundary model while also recognizing that `pxs` now sits inside a broader evolving security estate that includes additional external and platform surfaces.

## Current posture summary
Current baseline status: **current**

High-level assessment:
- current operating mode remains **GO** under a trusted-operator Phase 1 posture
- this baseline does **not** claim hostile multi-tenant isolation
- current posture reflects accepted current-state conditions plus explicit future hardening work
- Google Workspace and similar expanding platform surfaces now increase the importance of explicit capability and posture translation beyond the original baseline frame

## Active controls
### Boundary and access controls
- trust-boundary model: one gateway = one trusted operator boundary
- trusted operator set: Peter + Lyra acting on Peter’s authority
- Telegram group access policy: allowlist only
- sender allowlists are explicit
- group-specific allow-from rules remain explicit for the active group
- gateway bind posture: loopback
- trusted proxies limited to loopback addresses

### Filesystem and runtime controls
- main trusted boundary uses workspace-only filesystem posture
- runtime tools remain intentionally available in trusted contexts
- current main execution posture keeps sandbox mode off for workflow stability inside the trusted boundary
- accepted current-state posture does not claim fully hardened compartmentalization across every context

### Evidence and review controls
- security audit evidence is generated routinely
- deeper audit is required after significant config changes
- trust-boundary posture has an explicit policy record
- GO/risk stance has an explicit decision record
- Security now also tracks estate growth, material surface change, and upstream release/security impact as part of posture maintenance

## Accepted residual risk
### R1 — `security.trust_model.multi_user_heuristic`
- **Status:** accepted residual warning
- **Why it exists:**
  - group/channel configuration plus powerful tools creates a heuristic multi-user posture signal
  - main execution lane is intentionally not fully sandboxed
- **Why currently accepted:**
  - the declared operating model is a trusted-operator boundary, not a hostile multi-tenant environment
  - group access is limited through allowlists and explicit trusted sender control
  - this warning is already documented in policy and GO-risk decisions
- **Reopen triggers:**
  - group membership expands beyond mutually trusted operators
  - additional identities get tool-steering authority
  - gateway exposure expands beyond current local/trusted posture
  - security audit returns critical findings or unguarded runtime/filesystem contexts

### R2 — Current `pxs` baseline remains narrower than the full evolving Security estate
- **Status:** accepted current-state limitation
- **Why it exists:**
  - this baseline was originally shaped around the immediate `pxs` deployment posture and boundary model
  - Security scope now includes additional platform and ecosystem concerns that are broader than this single deployment artifact
- **Why currently accepted:**
  - the broader Security product model now carries estate, capability, upstream, and ecosystem visibility separately
  - this artifact remains useful as the concise `pxs` posture baseline rather than trying to absorb the entire Security product
- **Reopen triggers:**
  - `pxs` adds major new platforms, identities, or integrations without corresponding baseline translation
  - `pxs` posture can no longer be summarized honestly without a broader workspace-specific baseline model

## Open issues
### O1 — Google Workspace posture for `pxs` is not yet explicitly defined
- **Status:** open, material new-surface assessment needed
- **Impact:** identity, communication, sharing, document, and integration surfaces have expanded without a complete explicit baseline yet
- **Recommended handling:** assess the minimum acceptable Google Workspace posture and record resulting baseline or workspace-local posture controls

### O2 — High-risk execution and automation surfaces still need stronger deterministic control
- **Status:** open, active hardening need
- **Impact:** some high-risk actions still depend too much on procedure and operator sharpness
- **Recommended handling:** define and implement a narrow first control package for high-risk execution, automation, and evidence paths

### O3 — Posture-critical evidence should become more reproducible
- **Status:** open, active assurance improvement need
- **Impact:** reviewability and audit confidence weaken when baseline-critical posture depends on local/latest references
- **Recommended handling:** tighten baseline-critical references toward committed or deterministic evidence bundles

### O4 — `px-internal-dev` broader filesystem posture
- **Status:** open, needs explicit review
- **Impact:** acceptable only if intentional, tightly scoped, and not reachable from broader-than-intended contexts
- **Recommended handling:**
  - verify whether the wider filesystem scope is still necessary
  - document purpose and boundary explicitly if it remains
  - otherwise tighten toward workspace-only posture

### O5 — Gateway service uses version-manager Node
- **Status:** open, non-blocking platform hardening item
- **Impact:** reliability and maintainability risk during upgrades/restarts
- **Recommended handling:** migrate to a system-managed Node runtime in a planned change window

## What this baseline does not claim
- it does not claim multi-tenant isolation
- it does not claim prose alone is sufficient enforcement
- it does not claim that all non-main agent contexts are equally hardened
- it does not claim that new external/service surfaces inherit adequate posture automatically without explicit review

## Mandatory refresh triggers
- any credential, access, or trust-boundary change
- any new externally reachable surface
- any major new platform/service added to `pxs`
- any critical security finding
- any change that expands tool authority in shared/group contexts
- any decision to broaden `pxs` or add another customer environment
- any upstream change that materially alters accepted posture assumptions

## Current recommendation
Maintain operational GO under the current trusted-boundary model only while prioritizing the next highest-leverage improvements:
- keep accepted Phase 1 posture explicit and honest
- assess Google Workspace as a new `pxs` security surface
- strengthen deterministic control for the highest-risk execution and automation paths
- improve reproducibility of posture-critical evidence
- continue tightening filesystem-scope exceptions such as `px-internal-dev` where justified

## Linked references
- `governance/TRUST_BOUNDARY_POLICY_RECORD_2026-03-04.md`
- `governance/GO_RISK_DECISION_2026-03-06.md`
- `governance/VEGA_ACCEPTANCE_TEST_RUN_SHEET_V1.md`
- `products/security/06-architecture/ESTATE_MAP.md`
- `products/security/06-architecture/CAPABILITY_MAP.md`
- `products/security/04-execution/SURFACE_CHANGE_LOG.md`
- `knowledge/evidence/latest-security-audit.json`
- `knowledge/evidence/latest-doctor.txt`

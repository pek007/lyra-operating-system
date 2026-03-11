# PXS Deployment Baseline

Status: Active baseline
Product: Security (`A-004`)
Deployment target: `pxs`
Owner: Lyra
Date: 2026-03-11
Review cadence: weekly + trigger-based refresh

## Purpose
Provide the canonical Security-owned baseline for the current `pxs` deployment posture: active controls, accepted residual risks, open non-blocking issues, and mandatory review triggers.

## Current posture summary
Current baseline status: **current**

High-level assessment:
- no critical findings in the latest security audit
- one expected warning remains: `security.trust_model.multi_user_heuristic`
- Telegram group ingress is restricted by allowlists
- main trusted-boundary file access is constrained to workspace scope
- current operating model is a hardened single trusted operator boundary, not hostile multi-tenant isolation

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

### Evidence and review controls
- security audit evidence is generated routinely
- deeper audit is required after significant config changes
- trust-boundary posture has an explicit policy record
- GO/risk stance has an explicit decision record

## Accepted residual risk
### R1 — `security.trust_model.multi_user_heuristic`
- Status: accepted residual warning
- Why it exists:
  - group/channel configuration plus powerful tools creates a heuristic multi-user posture signal
  - main execution lane is intentionally not fully sandboxed
- Why currently accepted:
  - the declared operating model is a trusted-operator boundary, not a hostile multi-tenant environment
  - group access is limited through allowlists and explicit trusted sender control
  - this warning is already documented in policy and GO-risk decisions
- Reopen triggers:
  - group membership expands beyond mutually trusted operators
  - additional identities get tool-steering authority
  - gateway exposure expands beyond current local/trusted posture
  - security audit returns critical findings or unguarded runtime/filesystem contexts

## Open non-blocking issues
### O1 — Telegram privacy-mode advisory
- Status: open, non-blocking operational warning
- Impact: reliability/operability more than direct security degradation
- Recommended handling: confirm intended privacy-mode configuration per bot and restart gateway after any change

### O2 — `px-internal-dev` broader filesystem posture
- Status: open, needs explicit review
- Impact: acceptable only if intentional, tightly scoped, and not reachable from broader-than-intended contexts
- Recommended handling:
  - verify whether the wider filesystem scope is still necessary
  - document purpose and boundary explicitly if it remains
  - otherwise tighten toward workspace-only posture

### O3 — Gateway service uses version-manager Node
- Status: open, non-blocking platform hardening item
- Impact: reliability and maintainability risk during upgrades/restarts
- Recommended handling: migrate to a system-managed Node runtime in a planned change window

## What this baseline does not claim
- it does not claim multi-tenant isolation
- it does not claim prose alone is sufficient enforcement
- it does not claim that all non-main agent contexts are equally hardened

## Mandatory refresh triggers
- any credential, access, or trust-boundary change
- any new externally reachable surface
- any critical security finding
- any change that expands tool authority in shared/group contexts
- any decision to broaden `pxs` or add another customer environment

## Current recommendation
Maintain operational GO under the current trusted-boundary model, but prioritize one targeted review next:
- verify whether `px-internal-dev` still needs broader filesystem scope than the main trusted boundary

## Linked references
- `governance/TRUST_BOUNDARY_POLICY_RECORD_2026-03-04.md`
- `governance/GO_RISK_DECISION_2026-03-06.md`
- `knowledge/evidence/latest-security-audit.json`
- `knowledge/evidence/latest-doctor.txt`

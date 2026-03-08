# A-004 — PXS Security Deployment Baseline

Status: Active baseline v1
Product Name: Security
Product Owner: Lyra
Deployment target: PXS (current customer environment)
Last updated: 2026-03-08
Next review due: 2026-03-15

## 1) Purpose
Provide a concise, reviewable statement of the current security posture for PXS consumption of Lyra OS capabilities: what controls are active, what risks are accepted, what remains open, and what should trigger review.

## 2) Current posture summary
Current baseline status: **current**

High-level assessment:
- No critical findings in latest security audit
- One expected warning remains: `security.trust_model.multi_user_heuristic`
- Telegram group ingress is restricted by allowlists
- Workspace file access is constrained by `tools.fs.workspaceOnly=true` in the main trusted boundary
- Current operating model is **hardened single trusted operator boundary**, not hostile multi-tenant isolation

## 3) Active controls
### Boundary and access controls
- Trust-boundary model: one gateway = one trusted operator boundary
- Trusted operator set: Peter + Lyra acting on Peter’s authority
- Telegram group access policy: allowlist only
- Telegram sender allowlists are explicit
- Group-specific allowFrom remains explicit for the active group
- Gateway bind posture: loopback
- Trusted proxies limited to loopback addresses

### Filesystem and runtime controls
- Main trusted boundary uses `tools.fs.workspaceOnly=true`
- Runtime tools remain intentionally available in trusted contexts
- Current main execution posture keeps sandbox mode off for workflow stability in the trusted boundary

### Evidence and review controls
- Security audit evidence is being generated routinely
- Deep audit is required after significant config changes
- Trust-boundary posture has an explicit policy record
- GO/risk stance has an explicit decision record

## 4) Accepted residual risks
### R1 — `security.trust_model.multi_user_heuristic`
- Status: accepted residual warning
- Why it exists:
  - Group/channel configuration plus powerful tools creates a heuristic multi-user posture signal
  - Main execution lane is intentionally not fully sandboxed
- Why currently accepted:
  - The declared operating model is a trusted-operator boundary, not a hostile multi-tenant environment
  - Group access is limited through allowlists and explicit trusted sender control
  - This warning is already documented in policy and GO-risk decisions
- Source records:
  - `governance/TRUST_BOUNDARY_POLICY_RECORD_2026-03-04.md`
  - `governance/GO_RISK_DECISION_2026-03-06.md`
  - `knowledge/evidence/latest-security-audit.json`
- Reopen triggers:
  - Group membership expands beyond mutually trusted operators
  - Additional identities get tool-steering authority
  - Gateway exposure expands beyond the current local/trusted posture
  - Security audit returns critical findings or unguarded runtime/fs contexts

## 5) Open non-blocking issues
### O1 — Telegram privacy-mode advisory
- Status: open, non-blocking operational warning
- Description:
  - Doctor reports that `requireMention=false` is configured, but Telegram Bot API privacy mode may still block many unmentioned group messages unless disabled in BotFather.
- Impact:
  - Primarily reliability/operability, not direct security degradation
  - Can create false assumptions about what the bot will see in groups/topics
- Recommended handling:
  - Confirm intended privacy-mode configuration per bot and restart gateway after any change
- Source:
  - `knowledge/evidence/latest-doctor.txt`

### O2 — `px-internal-dev` context has broader filesystem posture than main
- Status: open, needs explicit review
- Description:
  - Latest security audit mentions `agents.list.px-internal-dev` with `fs.workspaceOnly=false`
- Impact:
  - Acceptable only if intentional, tightly scoped, and not reachable from untrusted or broader-than-intended contexts
  - This is the most important review item in the current baseline after the accepted trust-model warning
- Recommended handling:
  - Verify whether this wider filesystem scope is still necessary
  - If necessary, document purpose and boundary explicitly
  - If not necessary, tighten to workspace-only or equivalent narrower posture
- Source:
  - `knowledge/evidence/latest-security-audit.json`

### O3 — Gateway service uses version-manager Node
- Status: open, non-blocking platform hardening item
- Description:
  - Doctor reports the gateway service uses Node from an nvm path and recommends migration to system Node 22+
- Impact:
  - Reliability and maintainability risk during upgrades/restarts
  - Not a direct security breach, but relevant to operational resilience
- Recommended handling:
  - Move to system-managed Node runtime on a planned change window
- Source:
  - `knowledge/evidence/latest-doctor.txt`

## 6) What is explicitly not claimed
- This baseline does **not** claim multi-tenant isolation
- This baseline does **not** claim that prose alone is sufficient enforcement; config-level controls remain primary where available
- This baseline does **not** claim that all non-main agent contexts are equally hardened

## 7) Review cadence
### Routine
- Weekly review of current baseline status
- Review immediately after material config or trust-boundary changes

### Mandatory refresh triggers
- Any credential, access, or trust-boundary change
- Any new externally reachable surface
- Any critical security finding
- Any change that expands tool authority in shared/group contexts
- Any decision to broaden PXS or add another customer environment

## 8) Current recommendation
Maintain operational GO under the current trusted-boundary model, but prioritize one targeted review next:
1. verify whether `px-internal-dev` still needs broader filesystem scope than the main trusted boundary

That is the most leverage-heavy open posture question in the current baseline.

## 9) Linked sources
- `governance/TRUST_BOUNDARY_POLICY_RECORD_2026-03-04.md`
- `governance/GO_RISK_DECISION_2026-03-06.md`
- `knowledge/evidence/latest-security-audit.json`
- `knowledge/evidence/latest-doctor.txt`

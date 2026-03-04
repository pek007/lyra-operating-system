---
title: "Boundary and Ownership Model for Gateway Dashboard and Control Panel"
date: 2026-03-01
source: deepresearch
ingest_from: "knowledge/inbox/external-analysis-dropzone/deep-research-report (20).md"
tags: [external-analysis, deepresearch]
decision_relevance: tbd
confidence: tbd
status: archived-source
---

# Boundary and Ownership Model for Gateway Dashboard and Control Panel

## Executive recommendation

Control Panel should be a **separate, domain-specific decision cockpit** that **references** (and occasionally invokes) the Gateway Dashboard for **platform-native operations and telemetry**, rather than trying to be a superset or a full overlay replacement.

This is the most stable boundary because the Gateway Dashboard is not “just charts”—it is the **admin Control UI served by the Gateway** and authenticated at the **Gateway WebSocket handshake**; it is explicitly positioned as an operator/admin surface (chat, config, sessions, approvals) and comes with strong security guidance (treat it as privileged; avoid public exposure). citeturn0search0turn0search8turn1search1

The “separate cockpit” model also matches how the Gateway is described architecturally: the Gateway is the **single long-lived control plane** and “single source of truth” for runtime concerns like sessions, routing, channel connections, and control-plane clients over WebSocket. citeturn0search2turn0search5turn1search6turn1search1  
Trying to re-create this operational core inside Control Panel invites permanent duplication, protocol drift, and security/authorization complexity.

What Control Panel should **own** instead is the layer the Gateway intentionally does not try to be: **decision support** across time, work streams, and “so what?” context—prioritization, blockers, executive summaries, risk posture, and business/decision operations. This separation aligns with the way entity["company","Google","tech company"]’s SRE guidance frames dashboards: a dashboard summarizes core service metrics (often including golden signals), and *may* include team information like queue length and high-priority bugs—yet those belong as *team/business context around operations*, not as a reimplementation of the operational control plane itself. citeturn7view0

Local-first constraints further push toward this boundary: a local-first app treats the user’s local copy as primary and treats remote services as secondary replicas that assist with sync/access—this is naturally suited to decision records, notes, prioritization, and planning artifacts, but is a poor fit for being the “owner” of a live control plane whose authoritative state is on the Gateway. citeturn0search15

**Concrete instruction (the boundary in one sentence):**  
Gateway Dashboard owns **operating the Gateway**; Control Panel owns **operating the business and decisions *about* the Gateway’s work**—with Control Panel embedding *summaries* and *links* to Gateway-native details, not duplicating the Gateway-native screens.

**Do not build (explicit guardrails):** do **not** build a second “mini Gateway Dashboard” in Control Panel—specifically, do not rebuild (a) pairing/token management, (b) channel connection management, (c) raw session/chat UIs that compete with Control UI/WebChat, (d) a parallel approvals queue UI that tries to become the authoritative approval surface, or (e) a config editor/hot-reload console. These are already first-class Gateway concerns, implemented through the Gateway’s WebSocket control plane and Control UI. citeturn0search0turn1search0turn1search1turn1search6turn1search8

*Implementation note on evidence:* this recommendation is grounded in the publicly documented Gateway Dashboard/Protocol. I was not able to directly inspect the private `pek007/control-panel` repository content via the connector in this run; therefore, Control Panel specifics below are based on your described feature inventory (executive summaries, tasks/work views, risk/security, build visibility, capabilities, changes) and on the boundary principles above.

## Responsibility matrix

The matrix below defines **ownership** (who builds the “real” surface), **source of truth** (who owns canonical state), and the **allowed integration shape** (deep link vs embed summary vs bidirectional action).

| Domain / capability area | Gateway Dashboard ownership | Control Panel ownership | Source of truth | Integration shape (allowed) |
|---|---|---|---|---|
| Gateway runtime health, uptime, connectivity | ✅ Full | ⚠️ Summary only | Gateway | Embed: “health tile” + deep link to Gateway details |
| Sessions, runs, transcripts (raw) | ✅ Full | ⚠️ Annotate + summarize | Gateway | Embed: run list summary; deep link for transcript/diff detail |
| Nodes/devices presence, pairing, device tokens | ✅ Full | ❌ | Gateway | Deep link only |
| Channels/providers status (WhatsApp/Telegram/etc.), routing rules | ✅ Full | ⚠️ Business impact framing | Gateway | Embed: “channel incidents” summary; deep link for config actions |
| Approvals (exec approval requests/resolution) | ✅ Full | ✅ Decision context + policy view | Gateway for state; Control Panel for decision record | Embed: approval queue summary + “review context” in CP; resolve via Gateway (link or invoke) |
| Configuration editing and hot-reload | ✅ Full | ❌ | Gateway | Deep link only |
| Audit/security mechanics (auth mode, tokens/passwords, bind modes) | ✅ Full | ⚠️ Risk register + controls evidence | Gateway for mechanics; CP for risk posture | Embed: posture summaries; deep link for mechanical changes |
| Executive summaries (what happened / what matters / next actions) | ❌ | ✅ Full | Control Panel | CP primary; may cite Gateway run IDs/events |
| Work management: tasks, priorities, blockers, capabilities mapping | ❌ | ✅ Full | Control Panel | CP primary; references Gateway state (run/session IDs) |
| Build visibility + “changes narrative” (what changed, why, impact) | ⚠️ Proof/raw artifacts view | ✅ Portfolio-level change story | Federated: artifacts in Gateway; narrative in CP | CP stores narrative + links to Gateway artifact viewers |
| Decision log / approvals rationale / sign-offs | ❌ | ✅ Full | Control Panel | CP primary; may attach Gateway proof bundles |
| Fleet/multi-gateway portfolio (if applicable) | ⚠️ Each Gateway only | ✅ Cross-gateway view | Control Panel for aggregation; Gateway for node state | CP aggregates; links into per-gateway dashboards |

This matrix is consistent with how the Gateway is documented: the Gateway Dashboard is the Control UI served by the Gateway, and the Gateway WebSocket protocol is the unified control plane exposing status/sessions/nodes/approvals, with authentication and device identity at connect time. citeturn0search0turn1search1turn1search6turn1search0

## Overlap heatmap

The goal of the heatmap is to surface where duplication is **most likely** given your current Control Panel feature set (summaries, task/work views, risk/security, build visibility, capabilities, changes) and the Gateway Dashboard feature intent (chat/config/sessions/admin). citeturn0search0turn0search2turn1search1

| Likely overlap area | Duplication risk | Resolution class | Decision rule (short) |
|---|---:|---|---|
| “Status / health” pages (uptime, connectivity) | High | Federated/shared | Gateway is SoT; CP only shows rollups + last-seen freshness with link |
| Session list / run history UI | High | Federated/shared | Gateway owns canonical run/session browsing; CP shows filtered “what matters” and links to native details |
| Raw chat/transcript viewing and sending | High | Keep in Gateway only | CP must not become a competing chat client; reference run IDs + summarized outcomes |
| Approvals queue UI | High | Federated/shared | Gateway is SoT for approval state; CP adds risk context + rationale; resolution happens via Gateway API/UI |
| Config editor / environment settings | High | Keep in Gateway only | CP must not implement config management; deep link only |
| Nodes/devices management & pairing | High | Keep in Gateway only | CP shows “device trust posture” summary only; no pairing flows |
| Risk/security “controls” | Medium | Split by layer | Gateway owns *mechanisms* (auth, tokens, bind); CP owns *governance* (risk register, acceptance, evidence) |
| “Changes” / diffs / artifacts viewer | Medium | Federated/shared | Gateway stores/serves proof-level artifacts; CP owns narrative, impact and stakeholder framing |
| Task/work views vs “sessions” | Medium | Keep in CP only | CP owns work objects; Gateway owns runtime objects; map via references (runId/sessionId) |
| Capability mapping (“what this system can do”) | Low | Keep in CP only | CP is the product/ops handbook; Gateway UI is for operating mechanics |

Key evidence that drives these resolutions: the Gateway protocol is explicitly the single control plane for clients and exposes the gateway API surface (status/sessions/nodes/approvals/etc.), and events are not replayed (clients must refresh on gaps), making it risky to build an alternative “authoritative” operational UI without adopting the same control-plane semantics. citeturn1search1turn1search6

## Target architecture

The architecture below enforces the “decision cockpit” boundary by making Gateway data **referential** in Control Panel and making Control Panel’s decision data **local-first primary**.

### Boundary and interfaces

**Gateway side (platform operations layer):**
- **Gateway Dashboard / Control UI** served by the Gateway (browser UI). citeturn0search0turn0search8  
- **Gateway WebSocket protocol** as the primary integration surface for control-plane clients, including roles/scopes, device identity, token-based auth, and protocol version negotiation. citeturn1search1turn1search4  
- Optional **HTTP endpoints** where enabled (e.g., OpenResponses-compatible `POST /v1/responses`), authenticated via the same gateway auth configuration. citeturn1search3

**Control Panel side (business/decision operations layer):**
- Local-first data store (primary) for:
  - Executive summaries and decision records
  - Task/work objects, priorities, blockers
  - Risk register and security posture (non-mechanical)
  - Change narratives and stakeholder framing  
  This aligns with local-first principles: the local device copy is treated as the primary copy; remote systems are secondary replicas that aid multi-device access. citeturn0search15

### Data model boundary (pragmatic contract)

Use **composition, not duplication**:

- Gateway-owned entities (immutable in Control Panel):
  - `GatewayInstance` (id, URL/bind identity, environment label)
  - `Session` / `Run` references (IDs, timestamps, status, minimal metadata)
  - `ApprovalRequest` references (IDs, type, requested_at, current state)
  - `HealthSnapshot` (state + last_updated)  
  These are reflectors of gateway state, not editable truth.

- Control Panel-owned extensions (editable locally):
  - `RunBrief` = `{ runId, “what happened”, priority, blockers, owner, tags }`
  - `ApprovalRationale` = `{ approvalId, risk_assessment, decision, approver, evidence_links }`
  - `RiskItem` linked to gateway controls as evidence (not as config)
  - `ChangeNarrative` linked to run artifacts (proof bundles, diffs)

### Integration patterns (freshness and conflict behavior)

**Primary pattern: event-driven bridge + snapshot reconcile.**  
The Gateway protocol is WebSocket-based, requires a `connect` handshake with auth and protocol versioning, and supports server-push events; however, events may not be replayed, which forces clients to refresh state after gaps. citeturn1search1turn1search6  
Therefore, Control Panel should implement:

- **On connect:** pull a compact “current state snapshot” (health, approvals count, active sessions list) and persist it as a `state_version` baseline.
- **During connect:** ingest server-push events into an append-only local timeline (for “what just happened”).
- **On disconnect/gap:** mark gateway-derived data as “stale”; on reconnect, do a snapshot reconcile before trusting incremental events again.

**Conflict handling:**
- Gateway state is authoritative; Control Panel never tries to “win” conflicts on gateway-owned fields.
- Control Panel’s decision objects are authoritative; Gateway may be referenced (or injected) only as annotations.  
This mirrors the local-first model where local decision data remains primary, while gateway data is treated as a referenced external system-of-record for runtime truth. citeturn0search15turn0search2

**When actions are needed:**  
If Control Panel needs to trigger operational actions (e.g., resolving an exec approval), it should do so **via the Gateway protocol** under appropriate scopes (e.g., approval resolution is an operator action), rather than reimplementing mechanics. citeturn1search1turn1search4

## UX model

The UX goal is a **single cognitive home** (Control Panel) without becoming a single operational surface that duplicates the Gateway Dashboard.

### Navigation principles

**Control Panel is the starting point for “what should we do?”**  
It should answer:
- What matters right now?
- What is blocked?
- What changed that impacts risk or schedule?
- What decisions are pending and why?  
This aligns with decision-support needs that sit above telemetry.

**Gateway Dashboard is the place for “operate the gateway.”**  
It is the Control UI served by the Gateway for chat/config/sessions and privileged admin operations. citeturn0search0turn0search8

### Concrete handoff rules (embed vs deep-link)

**Embed in Control Panel (summarized Gateway-derived signals):**
- A “Gateway health tile” with: status, last heartbeat/last seen, connected channels count, active sessions count, approvals pending count.  
This draws on the operational concept of dashboards summarizing core service metrics (including golden signals) while keeping noise low. citeturn7view0turn1search6
- A “Work-in-progress” panel that maps tasks → run/session IDs → current status.
- A “Pending approvals” panel showing *why it matters* (risk, impact, deadline), with the actual approval object still treated as gateway-owned.

**Deep-link to Gateway Dashboard when:**
- The user needs to **change configuration**, bind/auth modes, or troubleshoot auth/connect problems. citeturn0search0turn1search7turn1search8
- The user needs **raw session history, transcript inspection, or chat operations** supported by WebChat/Control UI methods (history/send/inject). citeturn1search0
- The user needs to manage **nodes/devices**, pairing approvals, or device token rotation/revocation. citeturn1search1turn1search4

### A crisp “handoff affordance” pattern

Adopt a consistent pattern for any Gateway-derived widget in Control Panel:

- **Summary card** (Control Panel): shows “what’s important” and “what’s next.”
- **One-click “Open in Gateway”** (deep link) for the full operational page.
- **Optional safe action** from Control Panel only if:
  - It maps to a single Gateway API call, and
  - It is idempotent/safely retryable, and
  - Authorization/scopes are explicit and auditable. citeturn1search1turn1search6

This reduces UI duplication while preserving a fast operator loop.

## Implementation roadmap

The roadmap is designed for **1–2 sprints** and focuses on eliminating duplication now, while setting up stable contracts to prevent it from reappearing.

### Sprint N

Deliver a hard boundary quickly, even if integration is initially shallow.

**Define and publish a “Surface Ownership Spec” (1 pager + checklist).**  
Include the responsibility matrix + overlap heatmap as the decision record. Tie it to PR review: any new Control Panel screen must declare its owner class (CP-only / Gateway-only / Federated). This helps keep “signal high, noise low,” echoing SRE guidance on monitoring/alerting and dashboard intent. citeturn7view0

**Ship UX handoffs before deep integration.**
- Add “Open in Gateway” links from any Control Panel areas that currently overlap (sessions, approvals, config-like pages).
- Replace duplicated deep views with summarized placeholders (counts + last seen + status).  
The Gateway Dashboard is already the privileged admin surface; deep linking is the correct early move. citeturn0search0turn1search1

**Implement the minimal Gateway signal ingest (read-only).**
- Configure Control Panel with `gateway_url` + auth token (stored securely; avoid copy/pasting in URL patterns).
- Pull/subscribe to: gateway health + approvals pending count + active sessions count.
- Display “freshness” explicitly (“updated 12s ago”), and mark stale when disconnected, since events are not replayed and clients must refresh after gaps. citeturn1search6turn1search1

**Do-not-build enforcement (practical):**
- Remove or freeze any Control Panel work that expands duplicated operational views (chat UI, config editor, node manager). The Gateway already supports these through its Control UI and protocol. citeturn0search0turn1search1

### Sprint N+1

Deepen federation in the places where decision support adds concrete value.

**Approvals: add “context-first” approval workflow.**
- In Control Panel: show approval requests with risk framing (what could go wrong, blast radius, deadline, affected assets) and capture rationale.
- Resolve approvals via Gateway (deep link first; optionally implement resolve via protocol under operator scopes after audit logging is ready). citeturn1search1turn1search4

**Run/Change narrative: introduce a unified “Run Brief” object.**
- Auto-create a Control Panel `RunBrief` when a new run/session appears.
- Populate with minimal gateway metadata; user adds: priority, blockers, outcome summary, links to artifacts/diffs.

**Introduce a reconciliation loop (reconnect correctness).**
- On reconnect: snapshot → then event stream.
- Detect gaps and resync because events are not replayed. citeturn1search6turn1search1

**Protocol governance scaffolding.**
- Record the Gateway protocol version negotiated at connect time; fail fast on mismatch; track supported version ranges.
- Add contract tests pinned to protocol schemas to prevent silent drift. citeturn1search1

## Risks and mitigations

**Risk: “Single pane of glass” pressure recreates Gateway inside Control Panel.**  
This is the most common way duplication creeps back: incremental “just one more operational tab” until Control Panel becomes a second dashboard.  
Mitigation: treat “Gateway-only vs CP-only vs Federated” as a governance rule with PR checks and explicit deprecation outcomes for overlaps. Reinforce with the SRE principle that effective dashboards/alerts must stay simple to keep signal high. citeturn7view0

**Risk: Security regression via token handling and remote exposure.**  
The Gateway Dashboard is explicitly treated as an admin surface with guidance to avoid public exposure; it stores a token client-side after first connect. Control Panel could accidentally become an easier-to-expose administrative front door. citeturn0search0turn1search8  
Mitigation: Control Panel must default to localhost/local network use; store tokens in OS keychain/secure storage (not in URLs); prefer secure tunnels/VPN approaches when connecting remotely (e.g., via entity["company","Tailscale","vpn software company"] or SSH tunneling as recommended patterns). citeturn0search0turn1search6

**Risk: Data freshness and “false green” due to event gaps.**  
Gateway documentation indicates events are not replayed; clients must refresh on gaps. citeturn1search6turn1search1  
Mitigation: explicit stale-state UI, reconnect snapshot reconciliation, and “last updated” indicators on every gateway-derived widget.

**Risk: Protocol drift breaks Control Panel integrations.**  
The Gateway protocol is versioned; clients negotiate min/max protocol and can be rejected on mismatch. citeturn1search1  
Mitigation: pin supported protocol ranges, add compatibility tests, and treat Gateway upgrades as contract-impacting changes with a clear upgrade playbook.

**Risk: Decision context becomes untrustworthy if it diverges from runtime truth.**  
Example: Control Panel says “approved” while Gateway says “pending,” or Control Panel shows a run status that is no longer current.  
Mitigation: strict source-of-truth rules: Gateway is canonical for runtime state; Control Panel is canonical for rationale/intent. Any shared view must show which fields are gateway-derived vs locally-authored, and must refresh gateway-derived fields on reconnect. citeturn1search6turn0search15

**Risk: Building “local-first for everything” creates unnecessary complexity.**  
Local-first principles are powerful, but not every operational datum should be replicated and conflict-resolved locally; the Gateway is already the authoritative operational store. citeturn0search15turn0search2  
Mitigation: apply local-first primarily to decision artifacts (summaries, tasks, risk, narratives). For operational telemetry, store only what you need for context, and treat Gateway data as referenced truth with freshness semantics.
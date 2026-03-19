# Security Estate Map

Status: Draft active
Product: Security (`A-004`)
Owner: Lyra
Date: 2026-03-19

## Purpose
Define the operating estate Security is responsible for across Lyra OS and `pxs`, so posture, review, capability planning, and change assessment are grounded in a current picture of what exists.

## Scope rule
Security should maintain a current, practical map of material operating environments, trust boundaries, identity surfaces, execution surfaces, data surfaces, and external interfaces.

This artifact is not a full asset inventory. It is the canonical high-level security estate view used to answer:
- what environments are in scope
- what major surfaces exist
- where trust boundaries sit
- what changes are material enough to trigger Security review

## In-scope environments

### 1. Lyra OS
The control-plane and operating-system layer that coordinates the broader environment.

Key surfaces:
- runtimes, sessions, and tools
- shell execution and file mutation paths
- browser control and user-browser attach flows
- cron, config, gateway, and update paths
- node/device interfaces
- memory, governance, knowledge, and evidence stores

Security significance:
- highest leverage control plane
- trust-boundary definition and enforcement point
- many downstream claims depend on this layer being narrow, understandable, and reviewable

### 2. `pxs` workspace
The downstream operating workspace and implementation environment used for active company work.

Key surfaces:
- product and delivery artifacts
- working documents and project material
- execution and automation paths
- downstream process and operating-package artifacts
- integrations used for external-facing or customer-relevant work

Security significance:
- contains real operational content and downstream execution surfaces
- posture depends partly on Lyra OS controls and partly on workspace-local discipline

### 3. Google Workspace within `pxs`
A newly material platform surface inside the `pxs` operating environment.

Key surfaces:
- email
- calendar
- documents and Drive
- sharing and permission model
- account/admin controls
- third-party integrations and OAuth grants

Security significance:
- creates new identity, communication, sharing, and social-engineering surfaces
- increases data-leakage, access-governance, and integration-review needs
- should be treated as a material attack-surface expansion, not just a convenience tool addition

### 4. Browser and user-interaction surfaces
Surfaces where browser automation, user browser attachment, relay mechanisms, or rendered content can affect security posture.

Key surfaces:
- isolated browser automation
- user-browser attach / relay flows
- downloaded or uploaded content
- web sessions and cookies
- prompt-injection or content-manipulation opportunities through browser-mediated flows

Security significance:
- blends trusted local control with untrusted remote content
- can bypass assumptions if not clearly bounded and reviewed

### 5. Node / device surfaces
Companion devices and node-mediated capabilities.

Key surfaces:
- screen access
- camera access
- location access
- notifications
- paired-device permissions

Security significance:
- creates higher-sensitivity sensor and device-control surfaces
- requires explicit permission and boundary awareness

### 6. External communication and integration surfaces
Channels and systems that allow information flow out of the local operating environment.

Key surfaces:
- Telegram and other messaging channels
- email via Google Workspace
- external APIs and web services
- cross-system automations and integrations

Security significance:
- external write/action surfaces create both data-exposure and reputation risk
- high-value for auditability and approval semantics

## Trust-boundary view

### Boundary A — Lyra OS ↔ `pxs`
This remains the primary architectural security boundary.
- Security should keep this boundary explicit, reviewable, and honest about current enforcement limits.
- Phase 1 posture may be accepted without long-term hard compartmentalization being complete.

### Boundary B — Internal environments ↔ external services
This includes browsers, APIs, SaaS platforms, communications channels, and third-party integrations.
- Any expansion here should be treated as a material surface change when it introduces new write, auth, or data-sharing paths.

### Boundary C — Human identities / admin control ↔ automated execution
This includes service accounts, tokens, user sessions, automation identities, and delegated capabilities.
- Security should maintain clarity on where durable authority sits and how automated actions are constrained.

## Identity surfaces
Current material identity surfaces include:
- Peter’s human/operator identity
- Lyra runtime authority and tool permissions
- Google Workspace identities and admin roles
- messaging/service identities
- browser-authenticated sessions
- future service-account / integration identities

Current concern:
- identity growth should not outpace clarity on auth, session, secret, and privilege boundaries

## Execution surfaces
Material execution surfaces include:
- tool execution in Lyra OS
- shell and file operations
- browser actions
- cron jobs and scheduled automation
- workspace-local operational scripts and routines
- external integrations that trigger actions or data movement

Current concern:
- the highest-risk execution surfaces should move over time from mainly procedural handling to more deterministic control and verification

## Data surfaces
Material data surfaces include:
- governance and product artifacts
- memory and knowledge stores
- evidence and audit outputs
- `pxs` documents and workspace files
- Google Docs / Drive content
- email and calendar contents
- messaging content and attachments

Current concern:
- document and communication surfaces now deserve more explicit treatment as part of posture and sharing governance

## Material-change triggers
Security review should be triggered when any of the following occurs:
- new platform/service added to Lyra OS or `pxs`
- new identity or admin surface introduced
- new external write/integration path added
- new automation or high-privilege execution surface added
- trust-boundary assumptions materially changed
- upstream platform changes alter expected posture or exposure

## Current known gaps
- the estate view is now explicit, but still high-level and incomplete in some integration details
- Google Workspace has entered scope but has not yet been fully translated into required controls and baseline posture
- some current posture assumptions still rely on narrative clarity more than machine-checkable assurance

## Maintenance rule
Update this artifact whenever a material environment, identity, integration, or execution-surface change occurs that could affect Security posture or capability needs.

# Google Workspace Security Assessment for `pxs`

Status: Draft active assessment
Product: Security (`A-004`)
Owner: Lyra
Date: 2026-03-19
Assessed environment: `pxs`

## Purpose
Assess Google Workspace as a new material security surface inside `pxs`, determine the main local attack-surface implications, define a first minimum acceptable posture, and identify the resulting Security capability and execution needs.

## Trigger
`pxs` has obtained a Google Workspace licence for email, calendar, and documents.

This is a material expansion of the operating estate because it adds:
- a new identity and admin surface
- a new communication surface
- a new document and sharing surface
- new integration / OAuth surfaces
- additional opportunities for social engineering, leakage, and privilege drift

## Assessment scope
This assessment is a first-pass Security review of the Google Workspace introduction.
It is not yet a full admin configuration audit.

Current assessed surfaces:
- Gmail
- Calendar
- Google Docs / Drive
- sharing and permission behavior
- account/admin posture
- third-party integrations and OAuth grants
- session/device implications where they materially affect security posture

## Current-state judgment
### Overall judgment
Google Workspace is a justified and useful platform addition for `pxs`, but it should be treated as a meaningful attack-surface expansion rather than a neutral tooling upgrade.

### Core security significance
The highest-value shift is not just “more data in another place.”
It is that `pxs` now gains:
- a durable external communication channel
- a broader document-sharing and collaboration model
- a stronger account/identity dependency
- new integration and delegated-access paths

This means Security must now think about `pxs` not only as a local workspace with downstream execution surfaces, but also as a workspace with a live SaaS identity/document/communication layer.

## Main risk areas

### 1. Identity and admin control risk
Google Workspace creates a new admin and account-control surface.

Risk themes:
- weak or inconsistent MFA/session posture
- unclear admin-role scope
- durable access persisting longer than intended
- recovery and account-control paths being weaker than the importance of the account

### 2. Email threat surface
Email adds a major external input and output channel.

Risk themes:
- phishing and social engineering
- malicious attachments or links
- impersonation and trust abuse
- accidental sensitive outbound communication

### 3. Document and Drive sharing risk
Docs and Drive create a flexible sharing model that can drift into overexposure if not governed intentionally.

Risk themes:
- overly broad sharing defaults
- link-sharing that escapes intended control
- unclear ownership of sensitive documents
- long-lived external sharing persisting after the need passes

### 4. Calendar and social-engineering risk
Calendar is not just scheduling; it is also an influence and trust surface.

Risk themes:
- malicious meeting invites
- deceptive event links
- information leakage through event metadata
- trust abuse through appearing operationally routine

### 5. OAuth / integration risk
Google Workspace can become a bridge for third-party tools, delegated access, and automation.

Risk themes:
- overprivileged OAuth grants
- unclear review of new app connections
- durable third-party access to email, files, or calendar
- indirect exfiltration paths

### 6. Traceability and auditability risk
If the platform becomes important operationally, Security needs enough visibility to understand what changed and who did what.

Risk themes:
- insufficient logging/traceability for key admin or sharing changes
- inability to reconstruct exposure after an incident or near miss
- weak reviewability of permission drift

## Minimum acceptable posture — first pass
This is the first compact minimum acceptable posture for Google Workspace use in `pxs`.

### A. Identity and access
- MFA should be enabled for all materially privileged Google Workspace access.
- Admin authority should be kept as narrow as practical.
- Shared or ambiguous account ownership should be avoided.
- Recovery paths should be understood and intentionally controlled.

### B. Sharing and document handling
- Default sharing should bias toward the smallest practical audience.
- External sharing should be deliberate, not casual default behavior.
- Sensitive or important documents should have clear ownership.
- Link-based access should be treated as a posture decision, not just a convenience setting.

### C. Integrations and OAuth
- New third-party integrations should be treated as review-triggering events.
- OAuth grants should be kept narrow and reviewed for necessity.
- If an integration needs broad mail/file/calendar access, Security should treat it as a material trust expansion.

### D. Email and calendar hygiene
- External input should be treated as an attack surface, not an implicitly trusted workflow.
- High-value actions triggered by email should have extra skepticism and traceability.
- Calendar links and invites should not be treated as trustworthy just because they are operationally convenient.

### E. Traceability
- Material admin, sharing, and integration changes should be reviewable.
- Security should define which Google Workspace events matter most for posture review before trying to log everything.

## Capability implications
This platform addition increases the importance of these Security capabilities:
- integration and platform onboarding review
- identity, access, and secret posture
- auditability, logging, and traceability governance
- estate and exposure mapping
- capability planning and prioritization

## Recommended artifact consequences
This assessment should influence:
- `04-execution/SURFACE_CHANGE_LOG.md`
- `06-architecture/ESTATE_MAP.md`
- `06-architecture/CAPABILITY_MAP.md`
- `05-performance/PXS_DEPLOYMENT_BASELINE.md`
- future `pxs`-local posture or operating guidance if Google Workspace becomes deeply embedded in daily operations

## Immediate recommended next actions
1. Confirm the intended Google Workspace operating model for `pxs`
   - who has admin authority
   - whether there will be additional users later
   - whether external sharing is expected operationally

2. Define the first Google Workspace posture checklist
   - MFA
   - admin-role scope
   - sharing defaults
   - OAuth/integration review expectation
   - recovery-path clarity

3. Decide whether Google Workspace needs a `pxs`-local operating note or baseline extension
   - especially if email/docs/calendar become central operating surfaces

4. Add the first explicit traceability expectation
   - identify which admin/sharing/integration events should be reviewable first

## Current disposition
- **Platform value:** justified
- **Security posture:** acceptable only with explicit posture translation and disciplined operating assumptions
- **Urgency:** near-term priority, but not a stop-everything emergency
- **Recommended disposition:** continue adoption with explicit Security baseline work rather than treating Google Workspace as already covered by the prior `pxs` baseline

## Closing judgment
Google Workspace should be treated as the first concrete proof that Security now needs to operate from a broader estate-and-capability model.
It is not mainly a reason to panic; it is a reason to become more explicit, more selective, and more deliberate about platform onboarding and posture translation.

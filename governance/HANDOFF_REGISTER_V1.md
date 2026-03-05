# Handoff Register v1

Purpose: auditable log of explicit cross-domain artifacts exchanged between OS (Lyra) and PX (Vega).
Owner: Head of Internal Development
Review cadence: weekly

## Rules
- Every cross-domain transfer must have one handoff artifact.
- Missing owner, purpose, checksum, or approval = invalid handoff.
- Temporary handoffs must have `expires_at` and be removed/archived at expiry.

## Entries

| Date (UTC) | Handoff ID | From | To | Purpose | Classification | Owner | Approved By | Checksum | Expires At | Status | Evidence Ref |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-03-05 | HO-20260305-001 | os | px | Activate boundary model v1 and handoff protocol | internal | Lyra (main agent) | Peter Eklind | sha256:39672468bf4055352bd166e873371abcbd28445543048a4754541a8e2267fd07 | null | Open | governance/handoffs/HO-20260305-001.yaml |

## Status values
- Open: available for consumption
- Consumed: imported and recorded in destination domain
- Expired: no longer valid; access removed
- Rejected: failed validation
- Archived: closed and retained for audit only

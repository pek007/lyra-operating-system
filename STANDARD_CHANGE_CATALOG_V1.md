# STANDARD_CHANGE_CATALOG_V1

Status: Draft (proposed for immediate pilot)
Owner: Head of Control Tower
Effective: 2026-03-04

## Purpose

Define pre-authorized, low-risk change classes that may auto-promote when required evidence checks pass.

This catalog enables continuous execution while keeping higher-risk changes fail-closed.

## Core rule

A change is auto-promotable only if **all** conditions are true:

1. It matches a catalog class below.
2. It does not trigger any exclusion rule.
3. Required evidence checks are green.
4. WO + CA linkage is present.

If any condition fails, route to Normal/High-Risk approval flow.

## Promotion behavior by class

- **Standard / Pre-authorized**: Auto-promote when checks pass.
- **Normal / Medium risk**: Hold for delegated approver review.
- **High risk / External impact**: Explicit approval required (fail-closed on expiry).
- **Emergency**: Expedited approval path + post-audit obligations.

---

## Standard Change Classes (Pre-authorized)

### SC-01 Documentation clarity
Scope:
- Non-normative wording improvements
- Typos, formatting, heading structure, link fixes
- Added clarifying examples without policy/behavior change

Required checks:
- Markdown/link checks pass
- No policy keyword changes in governed files (see exclusions)

### SC-02 Non-behavioral code hygiene
Scope:
- Refactor comments/docstrings
- Rename internal symbols without logic changes
- Dead-code cleanup proven by tests

Required checks:
- Unit/integration test suite unchanged and green
- No config/schema/permission diffs

### SC-03 Low-risk internal tooling maintenance
Scope:
- Lint/test utility maintenance
- Report generation formatting/output improvements
- Internal script robustness changes without external side effects

Required checks:
- Tool tests green
- Dry-run output review artifact attached

### SC-04 Knowledge/evidence archival
Scope:
- Add reports, evidence notes, snapshots, closeout artifacts
- Update indexes/manifests for archival discoverability

Required checks:
- File naming convention compliance
- Registry/index links valid

### SC-05 Safe default config hardening (non-external)
Scope:
- Tightening defaults in local/internal contexts only
- No network exposure expansion, no identity/permission broadening

Required checks:
- Config diff review artifact
- Security checklist section marked green

---

## Exclusion Rules (force non-standard flow)

Any of the below disqualifies Standard auto-promotion:

1. Changes to authn/authz, trust boundaries, token/secret handling.
2. Network exposure, allowlists, ingress/egress, firewall, or gateway policy changes.
3. DB/schema migrations or data model compatibility changes.
4. Runtime routing/tool policy changes affecting execution rights.
5. External messaging behavior changes (channels, recipients, public outputs).
6. Any irreversible/destructive operation or unclear rollback.
7. Any change marked uncertain by classifier or reviewer.

When unsure: classify as High-Risk.

---

## Required Evidence Contract (for Standard auto-promotion)

Minimum artifacts per WO/CA:

- Work Order ID
- Change Artifact ID
- Diff summary (what changed / why)
- Check results (tests/lint/link checks as applicable)
- Classification record (`standard_class=SC-xx`)
- Rollback note (simple revert path)

Missing evidence => no auto-promotion.

---

## SLA + timeout behavior

- Standard changes: no manual approval required.
- Normal changes: delegated approver SLA applies; timeout => hold promotion.
- High-risk changes: explicit approval required; timeout => reject/expire.

Execution of unrelated work continues.

---

## Example routing table

| Example change | Class | Promotion |
|---|---|---|
| Fix typos in governance docs | SC-01 | Auto-promote |
| Add evidence markdown + index link | SC-04 | Auto-promote |
| Rename helper function; tests unchanged | SC-02 | Auto-promote |
| Modify gateway allowlist | High-risk | Explicit approval |
| DB migration for task schema | High-risk | Explicit approval |
| New feature behind flag with tests | Normal | Delegated approval |

---

## Pilot controls (first 2 weeks)

1. Auto-promotion limited to SC-01 + SC-04 initially.
2. Daily audit sample of 20% of auto-promoted changes.
3. Immediate rollback + reclassification on first policy miss.
4. Expand to SC-02/SC-03 only after zero critical misses in pilot window.

---

## Adoption checklist

- [ ] Register this catalog in process registry
- [ ] Add classifier output field in WO/CA templates
- [ ] Add CI guardrail to block auto-promotion on exclusion triggers
- [ ] Add audit log entry format for auto-promoted changes
- [ ] Publish delegated approver SLA references

---

## Versioning

- v1: Initial catalog proposal for controlled rollout

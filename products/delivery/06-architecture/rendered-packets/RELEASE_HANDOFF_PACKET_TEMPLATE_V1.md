# Release / Handoff Packet Template v1

Status: Template
Owner: Delivery
Applies to: Delivery Units in `release_recommended`, `awaiting_approval`, or `approved`

## Purpose
Assemble the professional recommendation packet for release or handoff.

## Template
- Delivery Unit ID: `{{delivery_unit_id}}`
- Title: `{{title}}`
- Generated at: `{{generated_at}}`
- Recommendation type: `{{recommendation_type}}`
- Recommendation: `{{recommendation}}`
- Approval profile: `{{approval_profile}}`
- Risk class: `{{risk_class}}`

## Executive recommendation
{{executive_recommendation}}

## Scope being released / handed off
{{scope_statement}}

## Evidence basis
{{#each selected_evidence}}
- `{{evidence_id}}` — {{evidence_type}} — {{summary}}
{{/each}}

## Known risks
{{#each known_risks}}
- {{this}}
{{/each}}

## Open exceptions
{{#each open_exceptions}}
- `{{exception_id}}` — {{exception_type}} — {{reason}} — {{status}}
{{/each}}

## Preconditions / conditions
{{#each conditions}}
- {{this}}
{{/each}}

## Release or handoff route
- Route: `{{route}}`
- Target: `{{target}}`
- Rollback / recovery note: `{{rollback_or_recovery_note}}`

## Decision request
- Requested decision: `{{requested_decision}}`
- Decision owner: `{{decision_owner}}`
- Required by: `{{required_by}}`

## Decision outcome
- Outcome: `{{decision_outcome}}`
- Rationale: `{{decision_rationale}}`
- Timestamp: `{{decision_timestamp}}`

# Approval Memo Template v1

Status: Template
Owner: Delivery
Applies to: Delivery Units crossing an approval boundary

## Purpose
Capture an approval or rejection decision in a concise auditable format.

## Template
- Delivery Unit ID: `{{delivery_unit_id}}`
- Title: `{{title}}`
- Memo generated at: `{{generated_at}}`
- Approval profile: `{{approval_profile}}`
- Requested decision: `{{requested_decision}}`

## Decision context
- Current state: `{{current_state}}`
- Risk class: `{{risk_class}}`
- Verification result: `{{verification_result}}`
- Recommendation reference: `{{recommendation_ref}}`

## Decision
- Outcome: `{{decision_outcome}}`
- Decision owner: `{{decision_owner}}`
- Timestamp: `{{decision_timestamp}}`

## Rationale
{{decision_rationale}}

## Conditions / follow-ups
{{#each conditions}}
- {{this}}
{{/each}}

## Evidence references
{{#each evidence_refs}}
- {{this}}
{{/each}}

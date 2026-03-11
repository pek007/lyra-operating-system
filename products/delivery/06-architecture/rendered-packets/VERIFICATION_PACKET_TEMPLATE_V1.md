# Verification Packet Template v1

Status: Template
Owner: Delivery
Applies to: Delivery Units entering or exiting `in_verification`

## Purpose
Summarize whether the Delivery Unit satisfies verification expectations strongly enough to recommend release or handoff.

## Template
- Delivery Unit ID: `{{delivery_unit_id}}`
- Title: `{{title}}`
- Generated at: `{{generated_at}}`
- Verification class: `{{verification_class}}`
- Risk class: `{{risk_class}}`
- Current state: `{{current_state}}`

## Verification summary
- Overall result: `{{verification_result}}`
- Verification decision: `{{verification_decision}}`
- Recommendation: `{{recommendation}}`

## Acceptance criteria status
{{#each acceptance_criteria}}
- {{id}} — {{statement}}
  - Status: `{{status}}`
  - Validation method: `{{validation_method}}`
{{/each}}

## Evidence reviewed
{{#each evidence_records}}
- `{{evidence_id}}` — {{evidence_type}} — {{validation_status}}{{#if artifact_path}} — `{{artifact_path}}`{{/if}}
{{/each}}

## Issues / defects / gaps
{{#each verification_gaps}}
- {{this}}
{{/each}}

## Exceptions impacting verification
{{#each exceptions}}
- `{{exception_id}}` — {{exception_type}} — {{status}} — {{reason}}
{{/each}}

## Risk note
{{risk_summary}}

## Verifier note
{{verifier_note}}

## Decision block
- Ready for release/handoff recommendation: `{{ready_for_release_recommendation}}`
- Additional work required: `{{additional_work_required}}`
- Escalation required: `{{escalation_required}}`

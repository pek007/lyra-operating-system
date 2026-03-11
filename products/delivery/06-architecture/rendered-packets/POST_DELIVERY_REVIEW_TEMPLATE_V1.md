# Post-Delivery Review Template v1

Status: Template
Owner: Delivery
Applies to: Delivery Units moving from `verified_in_use` to `closed`

## Purpose
Close the Delivery Unit with professional operational learning and verification-in-use evidence.

## Template
- Delivery Unit ID: `{{delivery_unit_id}}`
- Title: `{{title}}`
- Review generated at: `{{generated_at}}`
- Final state target: `closed`

## Outcome summary
{{outcome_summary}}

## Verification in use
- Operational status: `{{operational_status}}`
- Verification signal: `{{verification_signal}}`
- Incident/issues observed: `{{incident_summary}}`

## What was delivered
{{delivered_summary}}

## What worked well
{{#each strengths}}
- {{this}}
{{/each}}

## What did not go well
{{#each misses}}
- {{this}}
{{/each}}

## Exceptions carried or closed
{{#each exceptions}}
- `{{exception_id}}` — {{exception_type}} — {{status}} — {{closure_note}}
{{/each}}

## Follow-up actions
{{#each follow_ups}}
- {{this}}
{{/each}}

## Lessons / policy implications
{{lessons_summary}}

## Close decision
- Closure owner: `{{closure_owner}}`
- Closure timestamp: `{{closure_timestamp}}`
- References: `{{reference_summary}}`

# Delivery Brief Template v1

Status: Template
Owner: Delivery
Applies to: All Delivery Units

## Purpose
Provide a concise professional summary of a Delivery Unit before or during execution.
Rendered from canonical Delivery Unit state.

## Template
- Delivery Unit ID: `{{delivery_unit_id}}`
- Title: `{{title}}`
- Product: `{{product_id}}` {{product_name}}
- Work type: `{{work_type}}`
- Delivery mode: `{{delivery_mode}}`
- Owner: `{{owner.name}}`
- Risk class: `{{risk_class}}`
- Verification class: `{{verification_class}}`
- Current state: `{{current_state}}`
- Approval profile: `{{approval_profile}}`
- Objective link: `{{objective_link.type}}:{{objective_link.ref}}`

## Scope
{{scope_statement}}

## Non-goals
{{#each non_goals}}
- {{this}}
{{/each}}

## Acceptance criteria
{{#each acceptance_criteria}}
- {{id}} — {{statement}}
{{/each}}

## Dependencies
{{#each dependencies}}
- {{kind}}: `{{ref}}`{{#if status}} — {{status}}{{/if}}
{{/each}}

## Current recommendation
- Recommended next state/action: `{{recommended_next_action}}`
- Current blockers: `{{blocker_summary}}`
- Key evidence available: `{{evidence_summary}}`
- Key open decisions: `{{decision_summary}}`

## Notes
- This brief is a rendered operational view, not the canonical source of truth.

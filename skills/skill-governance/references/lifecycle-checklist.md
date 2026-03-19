# Skill lifecycle checklist

Use this checklist when creating, reviewing, improving, or retiring a skill.

## 1. Classification
- Is the skill `shared-platform`, `product-capability`, or `transitional-local`?
- Is that classification explicit in the registry?
- If transitional-local, is there a promotion path or retirement trigger?

## 2. Ownership
- Is the owner explicit?
- If product-capability, is the owning product explicit?
- Is the capability ID explicit?
- Is there an identified review cadence?

## 3. Delivery-mode fit
- Is the repeated problem actually skill-shaped?
- Would plugin, service, schema-pack, policy-pack, ops-pack, workspace artifact, or assembly be a better fit?
- Is the skill trying to cover several unrelated jobs?

## 4. Skill quality
- Is the frontmatter valid with `name` and `description`?
- Is the description good enough to trigger correctly?
- Is `SKILL.md` lean and procedural?
- Should some content move to `references/`?
- Should deterministic repeated logic move to `scripts/`?

## 5. Evidence and testing
- Has the skill been tested on at least one representative case?
- If it includes scripts, were they actually run?
- If it is a workflow skill, was at least one representative flow exercised?
- Is there evidence appropriate to the skill's role?

## 6. Lifecycle decision
Choose the next state:
- `proposed` -> good idea but not yet approved
- `approved` -> accepted for build
- `building` -> implementation underway
- `testing` -> representative checks underway
- `active` -> in use now
- `improving` -> active but needs material refinement
- `constrained` -> useful but materially limited
- `retiring` -> planned phase-out
- `retired` -> no longer active

## 7. Readiness decision
Choose the current readiness:
- `draft` -> concept or initial implementation
- `usable` -> works in bounded form
- `proven` -> evidence-backed and dependable for normal internal use
- `scaled` -> reusable across multiple consumers with explicit discipline

## 8. Action outputs
For every review, produce:
- classification
- lifecycle/readiness recommendation
- ownership/capability linkage result
- delivery-mode fit judgment
- next actions

## Typical next actions
- add or fix frontmatter
- split a mixed-purpose skill
- add references/examples
- add or test scripts
- create/update linked capability record
- add/update registry entry
- retire or archive obsolete skill

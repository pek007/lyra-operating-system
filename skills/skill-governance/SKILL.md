---
name: skill-governance
description: Govern the skill portfolio with lifecycle discipline. Use when creating, auditing, classifying, testing, improving, maintaining, constraining, or retiring Skills; when checking ownership or product/capability linkage; or when deciding whether a new capability should be delivered as a Skill at all.
---

# Skill Governance

Govern the skill portfolio as an architectural layer, not a loose collection of prompt folders.

## Do
1. Classify the skill as `shared-platform`, `product-capability`, or `transitional-local`.
2. Check ownership, review path, lifecycle state, and readiness.
3. For product-capability skills, verify:
   - owning product
   - capability ID
   - delivery mode rationale
   - evidence path
4. Decide whether `skill` is actually the right delivery mode.
5. Recommend the next lifecycle move:
   - create
   - approve
   - build
   - test
   - activate
   - improve
   - constrain
   - retire
6. Keep the skill narrow; split mixed-purpose skills where needed.
7. Keep `SKILL.md` lean and move detailed material into `references/` or `scripts/` when justified.
8. Update the registry and linked capability records when promotion or status changes occur.

## Evaluate with these questions
- What repeated problem does this skill solve?
- Who owns it?
- Is it shared-platform or product-capability?
- If product-owned, which capability does it serve?
- Why is `skill` the right delivery mode?
- What evidence shows it works?
- What would improve, constrain, or retire it?

## Escalate when
- ownership is ambiguous
- no valid product/capability link can be identified for a product-owned skill
- a different delivery mode is clearly more appropriate
- the proposed skill is trying to absorb several unrelated jobs
- the skill would create policy or authority drift

## Output
Produce:
- classification
- lifecycle/readiness recommendation
- ownership and capability-link check
- delivery-mode fit judgment
- concise next-action list

## References
- Read `references/lifecycle-checklist.md` for the portfolio review checklist and lifecycle heuristics.
- Read `SKILL_ARCHITECTURE_STANDARD_V1.md` and `SKILL_PORTFOLIO_REGISTRY.md` as the canonical governance surfaces.

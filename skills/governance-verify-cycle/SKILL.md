---
name: governance-verify-cycle
description: Run one bounded Governance VERIFY cycle with clear evidence output and minimal interpretation drift. Use when verifying one governance artifact, process, claim, packaging surface, or control condition; when a Governance lane or Control Panel handoff needs a pass/issue/decision-needed result; or when a scheduled governance review should execute one explicit verification target.
---

# Governance VERIFY Cycle

Run one bounded Governance VERIFY cycle. Keep scope tight, evidence explicit, and outcomes operational.

## Do
1. Identify the exact verification target and scope.
2. Confirm the verification objective:
   - pass/fail check
   - issue confirmation
   - decision-needed clarification
   - packaging/integrity check
3. Read only the necessary artifacts.
4. Execute one bounded VERIFY cycle.
5. Record the result in a deterministic evidence location.
6. Return a concise summary in one of these forms:
   - `pass`
   - `issue`
   - `blocked`
   - `decision-needed`
7. Update governance artifacts only when the cycle itself requires durable write-back.

## Escalate when
- authority or risk implications are material
- policy ambiguity blocks verification
- the result implies a material standards, boundary, or packaging decision
- no adequate evidence path exists
- the request is too broad to be one bounded VERIFY cycle

## Output
Produce:
- verification target
- evidence/result reference
- outcome (`pass|issue|blocked|decision-needed`)
- concise next action if needed

## References
- Read `references/verify-checklist.md` for the cycle checklist and output heuristics.
- Use `assemblies/governance-policy/v0.1/VERIFY.md` when the target is the governance assembly verification surface.

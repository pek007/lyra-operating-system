# Governance VERIFY checklist

Use this when running one bounded Governance VERIFY cycle.

## 1. Frame the target
- What exact artifact, process, claim, or control condition is being verified?
- Is the target narrow enough for one bounded cycle?
- What would count as `pass`, `issue`, `blocked`, or `decision-needed`?

## 2. Confirm inputs
- governance target/artifact
- verification objective
- evidence path
- output expectation
- boundary/risk notes

If any of these are missing, either infer conservatively from the request/artifacts or return `blocked`.

## 3. Read only what is needed
Typical targets:
- governance artifact or policy
- linked product artifact
- assembly verification surface
- decision or risk record
- evidence note or relevant report

Do not broaden into a general governance review unless explicitly asked.

## 4. Execute the VERIFY cycle
Typical cycle:
1. state the target
2. check the relevant artifact(s)
3. compare current state to the verification objective
4. determine outcome:
   - `pass`
   - `issue`
   - `blocked`
   - `decision-needed`
5. write evidence/output if required

## 5. Evidence/output guidance
Preferred outputs:
- governance evidence note
- product `PLAN.md` / `DECISIONS.md` / `RISKS.md` update when directly triggered
- job state update when the work is job-shaped

Keep evidence deterministic and reviewable.

## 6. Escalation tests
Escalate instead of pretending the cycle is complete when:
- authority or security posture changes are implicated
- the policy itself is ambiguous
- the result would force a broader architecture decision
- the evidence path is missing or non-deterministic

## 7. Return format
Use a concise structure:
- `target:`
- `outcome:`
- `evidence:`
- `note:`
- `next action:`

## Typical next actions
- record/refresh evidence
- update decision/risk artifact
- open a bounded follow-up verification cycle
- escalate to Governance owner / Control Panel

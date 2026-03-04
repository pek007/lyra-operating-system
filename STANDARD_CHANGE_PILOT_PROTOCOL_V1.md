# STANDARD_CHANGE_PILOT_PROTOCOL_V1

Status: Active pilot protocol
Window: 2026-03-04 to 2026-03-18
Owner: Head of Control Tower

## Objective

Run a controlled 2-week pilot for pre-authorized standard-change auto-promotion with deterministic guardrails and daily audit sampling.

## Scope

Allowed auto-promotion classes during pilot:
- SC-01 Documentation clarity
- SC-04 Knowledge/evidence archival

All other classes route to normal/high-risk flows.

## Entry criteria (per WO/CA)

Required metadata fields:
- Change class
- Standard class (if Standard)
- Auto-promotion requested (Yes/No)
- Exclusion trigger present (Yes/No)

Policy rule:
- If `Exclusion trigger present = Yes`, auto-promotion is blocked.

## Daily audit sample

- Sample size: 20% of auto-promoted changes (minimum 1/day when volume >0)
- Audit checks:
  1. Classification correctness (SC-01/SC-04)
  2. Exclusion trigger evaluation correctness
  3. Evidence completeness (WO+CA linkage, checks, rollback note)
  4. No external-impact side effects

## Logging format

Record each sampled item in `knowledge/evidence/` using:
- date
- WO/CA reference
- classifier outcome
- audit verdict (pass/fail)
- corrective action (if any)

## Fail-safe

- First policy-miss with material risk => immediate rollback to non-auto mode + reclassification of in-flight item(s).
- Pilot resumes only after corrective action note is published.

## Exit criteria

- Zero critical misses across pilot window.
- Daily sampling records complete.
- Recommendation issued: keep / expand / rollback.

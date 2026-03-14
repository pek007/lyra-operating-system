# Verification — Interfaces v0.1

## Goal
Verify that the Interfaces assembly is installable, usable in one real or representative workflow, and backed by enough evidence to support downstream consumption.

## Installation checks
- [ ] assembly installed through an approved lane
- [ ] lock/version reference present in the consumer scope
- [ ] packaged artifact paths resolve correctly

## Behavioral checks
- [ ] one real or representative workflow used the relevant prompt/interface guidance
- [ ] model-routing rationale recorded when non-default model choice was used
- [ ] evidence link recorded for the tested workflow

## Audit checks
- [ ] changelog reference present for the current version
- [ ] verification evidence path recorded
- [ ] next review/owner recorded where relevant

## Drift guard expectation
Meaningful interface-contract changes should not be treated as complete unless they have:
- a changelog entry
- linked verification evidence

## Verification outcome
Choose one:
- PASS
- FAIL
- PARTIAL / INCOMPLETE

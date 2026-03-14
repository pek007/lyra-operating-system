# Delivery Gate Checklist (A-006)

## Purpose
Apply a minimum delivery gate to release/change work so risk, evidence, and rollback expectations are explicit rather than improvised.

## Risk classes
Choose one:
- **Low** — low-consequence internal change with simple rollback and minimal blast radius
- **Medium** — meaningful internal change with non-trivial verification or coordination needs
- **High** — authority-impacting, customer-impacting, security-sensitive, or hard-to-reverse change

## Required fields
- Change/work identifier:
- Scope:
- Risk class:
- Acceptance/completion bar:
- Verification/evidence plan:
- Rollback path:

## Required checks by class
### All classes
- [ ] scope and risk classified
- [ ] acceptance/completion bar explicit
- [ ] verification/evidence plan explicit
- [ ] evidence artifacts recorded
- [ ] rollback path confirmed

### Medium and High
- [ ] dependencies/coordination impacts reviewed
- [ ] security implications reviewed
- [ ] post-change review scheduled

### High only
- [ ] explicit approval/escalation path checked
- [ ] stop-the-line trigger reviewed before change proceeds

## Required evidence outputs
At minimum capture:
- scope/change identifier
- gate completion result
- checks performed
- evidence references
- rollback notes
- operator/reviewer if relevant
- final verdict: pass / fail / partial

## Stop-the-line triggers
Do not proceed as a normal pass if:
- scope or risk class is unclear
- verification path is unclear
- evidence cannot be produced
- rollback path is not credible enough for the change class
- security/authority implications are unresolved for a Medium/High change

## Final verdict
Choose one:
- [ ] PASS
- [ ] FAIL
- [ ] PARTIAL / INCOMPLETE

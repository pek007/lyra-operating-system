# Skill Evidence Pack Template

## A) Identity
- Skill:
- Version pinned:
- Source:
- Owner:
- Risk class (S0-S3):
- Review date:

## B) Technical Review
- [ ] Full file inventory reviewed (scripts/resources)
- [ ] Runtime dependencies documented
- [ ] Network behavior documented (domains/endpoints)
- [ ] Filesystem read/write paths documented
- [ ] Diff reviewed vs prior release

## C) Secrets & Auth
- [ ] Credentials required (Y/N) documented
- [ ] Scope minimization documented
- [ ] Secret storage approved (vault/keyring/ephemeral env)
- [ ] Rotation/revocation plan documented
- [ ] Confirmed: no secrets in prompts/logs

## D) Control Validation
- [ ] Sandbox execution tested
- [ ] Path allowlist enforced
- [ ] Outbound allowlist enforced (if applicable)
- [ ] Approval gates tested for write/destructive actions
- [ ] Spend/cost guardrails tested (if external APIs/models)

## E) Functional Tests
- [ ] Read-only test passed
- [ ] Write-with-approval test passed
- [ ] Failure-mode test passed (timeout/429/auth failure)
- [ ] Rollback/recovery tested

## F) Monitoring
- [ ] Metrics defined (usage/errors/cost)
- [ ] Alerts configured (anomaly/high-risk action)
- [ ] Kill-switch tested
- [ ] Re-review cadence set

## G) Decision
- Status: [Reject / Sandbox-Only / Promote]
- Decision owner:
- Notes:

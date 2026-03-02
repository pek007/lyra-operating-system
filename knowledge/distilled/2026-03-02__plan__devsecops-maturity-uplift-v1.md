# DevSecOps Maturity Uplift Plan v1

Status: Active  
Owner: Peter (A), Lyra (R)

## Executive intent
Move from governance-by-doc to governance-enforced-by-pipeline with minimal overhead.

## Implemented now
1. Deep research report ingested and indexed.
2. Baseline CI workflow scaffold added for governance validation.
3. Review-date validator added to catch overdue process controls.

## Next high-leverage steps
1. Enable branch protection + required checks on `main` (manual repo setting).
2. Enable GitHub secret scanning + push protection (manual repo setting).
3. Add dependency review and SBOM generation workflow jobs.
4. Add policy-file schema checks and fail builds on violations.
5. Define dev/staging/prod promotion model (state-based rollout rules).

## Success criteria
- No direct pushes to main.
- All PRs run mandatory governance checks.
- Overdue process reviews are visible automatically.
- Security scanning baseline active in CI.

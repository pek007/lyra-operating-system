# Verification — Governance Policy Assembly v0.1

Mark each check pass/fail.

## Installation checks
- [ ] `assembly.yaml` exists and version matches lock entry
- [ ] policy artifacts present in target path
- [ ] activation checklist linked from PXS operating docs

## Behavioral checks
- [ ] simulated authority-impacting change routes through approval gate
- [ ] simulated external tool/service change references governance policy
- [ ] simulated config-impacting change references config checklist/SOP

## Audit checks
- [ ] evidence reference recorded for each gated simulation
- [ ] lockfile updated with install date + owner + next review date
- [ ] interim copy marker present (if using interim lane)

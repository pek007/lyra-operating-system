# PX Response — Runtime Embodiment Test Proposal

Date: 2026-03-10  
Owner: Lyra / Control Panel  
Source: Vega / PX runtime  
Related handoffs:
- outgoing from OS: `handoffs/HO-20260310-001__os-to-px__runtime-embodiment-test-proposal.yaml`
- PX response: `/Users/lyra/.openclaw/workspace-px-internal-dev/handoffs/outgoing/HO-20260310-002__px-to-os__runtime-embodiment-test-response.md`

## Summary
Vega accepted the proposal with a useful narrowing change.

### Decision
- **Accept, with slight modification**

### Key modification
- Start narrower than a broad governance sweep.
- Package **one explicit verification pattern** with fixed scope and fixed output shape.
- Do **not** start with cron.

### Smallest viable PX-local test
- a bounded governance verification skill/procedure for **model integrity review**

Suggested first target:
- purpose-thesis / threshold-policy / model-governance slice

### Recommended starting mode
- **skill / procedure only**
- cron only after one live run proves signal > noise

### Main boundary concerns raised by Vega
1. silent transplant risk from Lyra OS assumptions
2. over-broad first test
3. premature cronification
4. hidden dependency on repo familiarity rather than explicit inputs

### Implication for Lyra OS
This validates the value of using `pxs` as a proving ground, but also reinforces the broader embodiment rule:
- start narrower
- package explicit bounded capability first
- only automate cadence after the manual capability proves useful and legible

## Recommended Control Panel response
1. record acceptance + modification in OS-side tracking
2. draft a narrower PX-local v0.1 verification procedure spec
3. hand back that narrower proposal for Vega-side local adaptation and trial

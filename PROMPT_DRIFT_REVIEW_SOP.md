# PROMPT_DRIFT_REVIEW_SOP.md

Status: Active

## Purpose
Continuously adapt prompt templates to model/runtime changes and evolving best practices without introducing uncontrolled regressions.

## Cadence
- Weekly (15 min): signal scan
- Monthly (60 min): formal drift review
- Quarterly (90 min): major version/deprecation review

## Weekly scan checklist
- [ ] vendor model updates checked (Claude/OpenAI)
- [ ] notable failures from last week reviewed
- [ ] cost/latency anomalies reviewed
- [ ] safety incidents reviewed
- [ ] candidate template tweaks logged

## Monthly formal review process
1. Collect signals
2. Classify impact (low/medium/high)
3. Draft template changes with semver bump
4. Run validation tasks
5. Approve/reject
6. Publish changelog entry
7. Monitor post-change metrics for 1-2 weeks

## Validation set (minimum)
- 3 Claude Code plan prompts
- 3 Claude Code execution prompts
- 3 Deep Research public prompts
- 3 Deep Research private prompts

## Promotion criteria
- improved or non-inferior acceptance rate
- no increase in safety-boundary violations
- no unacceptable cost/latency regression
- handoff artifacts remain complete and usable

## Rollback criteria
- acceptance rate drop beyond threshold
- safety incidents increase
- cost spikes without quality gain
- recurring schema/handoff failures

## Output destination (Control Panel first)
- Weekly and monthly review outputs must be written to workspace artifacts (not Telegram posts by default).
- Primary path: `knowledge/evidence/YYYY-MM/prompt-drift-review-YYYY-MM-DD.md`
- Optional index/reference update: `knowledge/indexes/TOPIC_INDEX.md`
- Telegram should only receive a short exception alert when a critical regression is detected.

## Ownership
- Review owner: Lyra
- Approval owner: Peter
- Architecture reviewer: Chief Architect

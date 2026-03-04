# BUSINESS_CASE_THRESHOLD_RESEARCH_PROVIDERS.md

## Purpose
Decision threshold for adding paid external research/search providers.

## Baseline (current)
- Primary: internal reasoning + manual Deep Research + optional free Brave tier.
- Constraint: missing API-backed web discovery reduces autonomous research depth.

## Adopt Paid Provider When (any one true)
1. **Time ROI trigger**
   - Saves >= **10–15 minutes/day** on average over 2 weeks.
2. **Quality trigger**
   - Produces materially better source-grounded outputs for decision memos (fewer rewrites, clearer citations).
3. **Capacity trigger**
   - Free tier limits are hit repeatedly and block daily operations.
4. **Risk trigger**
   - Need stronger cross-source triangulation for high-stakes Type 1 decisions.

## Cost/Benefit Scoring (quick)
Score each 1–5:
- Time saved
- Output quality uplift
- Reliability/availability
- Integration friction (inverse)
- Monthly cost efficiency

Adopt if weighted score >= **18/25** and no red security/compliance concerns.

## Pilot Method (2 weeks)
1. Define 10 representative research tasks.
2. Compare baseline vs candidate provider.
3. Track:
   - time to first usable draft
   - number of edits required
   - citation quality/confidence
4. Decide: adopt now / continue pilot / defer.

## Recommended Candidate Ladder
1. Brave API (lowest-cost entry)
2. Add secondary synthesized provider only if ROI threshold met (e.g., Perplexity-style)

## Decision Record Requirement
Final decision must be logged in `DECISIONS.md` with:
- expected monthly cost
- expected monthly benefit (time/value)
- start date and review date

## Version
- v1.0
- Date: 2026-02-24

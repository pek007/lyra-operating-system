# PROMPT_CHANGELOG

## Format
- Date:
- Template:
- Version:
- Change type: MAJOR | MINOR | PATCH
- Summary:
- Rationale:
- Expected impact:
- Validation run:
- Owner:
- Rollback plan:

---

## Entries

### 2026-03-08
- Template: `prompts/claude-code/WO_execute.md`, `prompts/claude-code/WO_plan.md`, `CODEX_PROMPT_CONTRACT_TEMPLATE.md`, `prompts/deep-research/RO_public.md`, `prompts/deep-research/RO_private.md`, `prompts/deep-research/GUIDELINE.md`
- Version: 1.2.0 (WO_execute/WO_plan/CODEX contract), 1.1.0 (RO_public/RO_private/GUIDELINE)
- Change type: MINOR
- Summary: Added GPT-5.4-native prompt blocks for output contracts, dependency checks, tool persistence, research discipline, and completeness criteria.
- Rationale: Capture the quality gains of GPT-5.4 by making completion rules, tool-use expectations, and evidence structure more explicit.
- Expected impact: Better adherence to format, fewer incomplete/tool-light runs, more reliable verification and research outputs, lower verbosity drift.
- Validation run: Template review against OpenAI GPT-5.4 guidance + local artifact consistency pass; runtime shakedown pending.
- Owner: Peter + Lyra
- Rollback plan: Revert templates to previous versions if outputs become too rigid or if useful autonomy drops.

### 2026-03-03
- Template: `prompts/deep-research/RO_public.md`, `prompts/deep-research/RO_private.md`, `prompts/deep-research/GUIDELINE.md`
- Version: 1.0.1 (RO_public/RO_private), 1.0.0 (GUIDELINE)
- Change type: PATCH
- Summary: Added explicit hybrid style guidance combining expert-depth with concise decision-structured output; added deep-research prompting guideline.
- Rationale: Improve deep research quality without sacrificing actionability; standardize prompt-writing approach.
- Expected impact: Better technical depth, clearer recommendations, lower fluff, more consistent report quality.
- Validation run: Template conformance check (manual); next deep-research run to compare output quality.
- Owner: Peter + Lyra
- Rollback plan: Remove `<style>` blocks from RO templates and delete `prompts/deep-research/GUIDELINE.md`.

### 2026-02-28
- Template: Claude Code prompting schema + WO/Codex contract templates
- Version: 1.1.0 (templates), Prompting OS policy refresh
- Change type: MINOR
- Summary: Shifted to outcome-oriented prompts with explicit mode selection, mandatory verification blocks, explicit action intent, and fresh-context recovery rule.
- Rationale: Reduce over-specification and improve autonomy + verification quality in Claude Code execution.
- Expected impact: Higher first-pass usefulness, less prompt bloat, better verification discipline, fewer stuck correction loops.
- Validation run: Governance review + template conformance pass (runtime adoption pending).
- Owner: Peter + Lyra
- Rollback plan: Revert template files to v1.0.0 contracts and remove mode/recovery enforcement from PROMPTING_OS_V1.md.

### 2026-02-26
- Template: Prompting OS baseline (all v1 templates)
- Version: 1.0.0
- Change type: MAJOR
- Summary: Initial standardized prompting stack for Claude Code and Deep Research
- Rationale: Introduce repeatable, governable 3PP prompting process
- Expected impact: Better consistency, reduced ambiguity, improved handoff quality
- Validation run: Initial adoption; template-level structural review
- Owner: Peter + Lyra
- Rollback plan: Revert to prior ad-hoc prompts while preserving handoff artifact requirement

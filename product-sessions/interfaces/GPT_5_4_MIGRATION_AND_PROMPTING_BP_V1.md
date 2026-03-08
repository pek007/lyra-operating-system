# GPT-5.4 Migration + Prompting Best Practices (Interface Product)

Date: 2026-03-08
Owner: Lyra
Status: Draft v1 (ready for rollout)

## 1) Executive summary

Yes — there is a new OpenClaw release today (`2026.3.7`), and it includes support for `openai-codex/gpt-5.4` (Codex OAuth path).

For us, this means:
- We can stay inside Codex OAuth (OpenAI Pro-backed flow) and move from `gpt-5.3-codex` to `gpt-5.4`.
- We should do a controlled migration (baseline -> switch one agent -> eval -> switch second agent).
- Prompting should be tightened around output contracts, completion criteria, and tool-use discipline.

## 2) Evidence collected

### OpenClaw status (local runtime)
- Current installed version: `2026.3.2`
- Update available: `2026.3.7`
- Current default session model: `gpt-5.3-codex`

### OpenClaw package/release evidence for GPT-5.4 support
From `openclaw@2026.3.7` package `CHANGELOG.md`:
- “Models/OpenAI forward compat: add support for `openai/gpt-5.4`, `openai/gpt-5.4-pro`, and `openai-codex/gpt-5.4`…”
- “Models/default alias refresh: bump `gpt` to `openai/gpt-5.4`…”

From distributed code in the package:
- `OPENAI_CODEX_DEFAULT_MODEL = "openai-codex/gpt-5.4"`
- Explicit guidance strings include:
  - “Use `openai-codex/gpt-5.4` (OAuth) or set OPENAI_API_KEY to use `openai/gpt-5.4`.”

## 3) What this means for our setup (2 agents on gpt-5.3-codex)

1. **Compatibility path exists**: we do not need to leave Codex OAuth to use GPT-5.4.
2. **Upgrade dependency**: our current install (`2026.3.2`) does not expose `openai-codex/gpt-5.4` yet; we need to update OpenClaw first.
3. **Operational target**: after update, both agents should run `openai-codex/gpt-5.4` unless a specific workload benefits from pinning 5.3 temporarily.

## 4) GPT-5.4 prompting changes that matter in practice

Based on OpenAI’s new GPT-5.4 guidance, these are the high-value shifts:

1. **Explicit output contracts**
   - Specify exact sections/order/format.
   - Set length constraints per section.
   - Keep outputs concise but not under-specified.

2. **Reasoning effort by task shape**
   - Do not assume “higher = better.”
   - Default low/none for straightforward tasks; increase for complex multi-step reasoning.

3. **Tool-use persistence + dependency checks**
   - Enforce prerequisite lookups before actions.
   - Require retry with alternative strategy on partial/empty tool results.
   - Parallelize only independent retrieval tasks.

4. **Completion criteria**
   - Define what “done” means.
   - Require coverage checks for lists/batches and explicit `[blocked]` states.

5. **Instruction-priority clarity**
   - Newer user instructions override older style/format defaults.
   - Safety and permission constraints remain non-negotiable.

## 5) Interface Product standard prompt blocks (recommended)

Use these blocks in agent system/developer prompts:

- `<output_contract>`
- `<default_follow_through_policy>`
- `<instruction_priority>`
- `<tool_persistence_rules>`
- `<dependency_checks>`
- `<completeness_contract>`

Rationale: this aligns directly with GPT-5.4 guidance and reduces drift in long or tool-heavy flows.

## 6) Migration playbook (safe rollout)

### Step A — Upgrade runtime
- Update OpenClaw from `2026.3.2` -> `2026.3.7`.
- Verify with:
  - `openclaw --version`
  - `openclaw models list --all --plain` includes `openai-codex/gpt-5.4`

### Step B — Controlled cutover
1. Switch Agent 1 to `openai-codex/gpt-5.4`.
2. Run a fixed test battery (same prompts/tasks as current baseline).
3. Compare quality, latency, tool-call behavior, and retries vs `gpt-5.3-codex`.
4. If stable, switch Agent 2.

### Step C — Prompt hardening
- Add/update standardized prompt blocks above.
- Keep prompts functionally similar while changing model first, then tune prompts in small increments.

### Step D — Acceptance gate
Promote only if all pass:
- No regression on top 10 recurring workflows
- Equal or better completion reliability on multi-step tasks
- No increase in unsafe/unwanted autonomous actions
- Output format adherence >= baseline

## 7) Immediate recommendations

1. Approve OpenClaw update to `2026.3.7`.
2. Move one agent to `openai-codex/gpt-5.4` first (pilot).
3. Apply the prompt block standard above to both agents.
4. Review after 24-48h and then complete migration.

## 8) Source links

- OpenAI prompt guidance (GPT-5.4):
  - https://developers.openai.com/api/docs/guides/prompt-guidance/
- OpenAI latest model guide (Using GPT-5.4):
  - https://developers.openai.com/api/docs/guides/latest-model/
- OpenAI cookbook (GPT-5 prompting guide):
  - https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide
- OpenClaw releases:
  - https://github.com/openclaw/openclaw/releases

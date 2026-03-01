---
title: "Prompting Playbooks for Claude Code and OpenAI Deep Research in Lyra OpenClaw"
date: 2026-03-01
source: deepresearch
ingest_from: "knowledge/inbox/external-analysis-dropzone/deep-research-report (12).md"
tags: [external-analysis, deepresearch]
decision_relevance: tbd
confidence: tbd
status: archived-source
---

# Prompting Playbooks for Claude Code and OpenAI Deep Research in Lyra OpenClaw

## Why these two services need different prompt disciplines

Claude Code and OpenAI Deep Research look similar (both are “agentic”), but they sit on opposite sides of a key boundary: **code-editing with privileged local context** vs **research synthesis over potentially adversarial external text**. That difference changes what “good prompting” means.

For Claude Code, the prompt is best treated as an **implementation contract** that constrains file edits and tool use, then forces verifiable outcomes (diffs/tests). Claude Code explicitly supports *permission modes* (default, acceptEdits, plan, bypassPermissions), and Plan Mode is designed for read-only analysis and planning before any execution. citeturn18search0turn18search3

For OpenAI Deep Research, the prompt is best treated as a **research specification**: it should make the question fully-formed, define which sources are allowed, and define an evidence standard (citations). Deep research explicitly lets you choose sources (websites, uploads, connected apps) and in the UI you can restrict or prioritize specific sites. citeturn19view0 Deep Research’s official guidance also flags prompt-injection and data exfiltration risks when browsing the web or searching connected data sources, which is a core reason prompting needs extra “trust boundary” rigor. citeturn23view1turn20view2turn11search4turn12search0

A good meta-model to keep everyone honest: **prompting is interface design**. You want to (a) shrink the solution space only where you must, and (b) create hard gates where the model’s failures are most expensive or irreversible.

## What your current repos imply about your prompting maturity

Across your two repositories in entity["company","GitHub","code hosting"] (pek007/control-panel and pek007/lyra-operating-system), you already version prompt artifacts as first-class engineering objects—especially for Claude Code and Deep Research. Examples include:

- A Claude Code implementation prompt for Control Panel Sprint work: `docs/CLAUDE_CODE_PROMPT_S2_ROLE_KPI_CONTROL.md`. fileciteturn12file1L1-L1  
- A Deep Research architecture review prompt: `docs/DEEP_RESEARCH_PROMPT_S2_ARCH_REVIEW.md`. fileciteturn12file0L1-L1  
- A Claude Code prompt used to build the Control Panel MVP from a spec: `CLAUDE_CODE_PROMPT_CONTROL_PANEL_MVP.md` (lyra-operating-system). fileciteturn16file0L1-L1  

That’s notable because it enables two practices that the vendors themselves implicitly rely on:

1. **Prompt versioning and policy drift control** (treat prompts like code, not ad-hoc chat). OpenAI explicitly recommends pinning model snapshots and building evaluations to monitor prompt behavior over time. citeturn3search4  
2. **Stable “static prefix” prompts** (templates), which in API contexts also improves caching and repeatability. OpenAI’s prompt caching guidance is explicit: put static instructions early and keep variable details later. citeturn3search0  

Your internal Lyra multi-agent operating model also explicitly conceptualizes external workbenches (including Deep Research / workbench runs) as a dedicated “lane” that requires structured handoff back into OS artifacts. That’s a strong first-principles stance: it treats “manual 3PP prompting” as a governed interface, not a one-off conversation. fileciteturn17file7L1-L1

The remainder of this report assumes you want to **normalize this lane concept into a repeatable prompting protocol**.

## Foundations that generalize across both models

### Planning-then-execution is an empirically grounded shape, not a stylistic preference

The “plan first, then do” pattern isn’t folklore; it’s repeatedly rediscovered in prompting and agent literature.

- Plan-and-Solve (PS) explicitly decomposes tasks into subtasks via a planning phase, then executes according to the plan. citeturn9view0  
- ReAct interleaves reasoning traces with actions and tool use, reducing ungrounded hallucination by forcing the model to consult external sources during acting. citeturn10view0  
- Self-consistency shows that sampling multiple reasoning paths and selecting the most consistent final answer can materially improve correctness in reasoning tasks (a reminder that “single-shot clever prompts” are often dominated by “systematic multi-path variability + selection” when cost allows). citeturn10view1  
- Least-to-most prompting shows that graded decomposition (easy-to-hard) can generalize better than showing exemplars alone. citeturn9view1  

In practice, you don’t need to implement these papers verbatim. The takeaways that matter for your two tools are:

- **Claude Code:** use Plan Mode to force a “plan artifact” before edits. citeturn18search3  
- **Deep Research:** force an explicit plan + evidence standard before synthesis; the ChatGPT UI already supports plan review/edit. citeturn19view0turn24view0  

### Micromanagement is good at boundaries, bad in the interior

A useful operational definition:

- **Boundary micromanagement** = specifying invariants the model must not violate (security constraints, allowed tools, output schema, “no destructive side effects,” etc.). This is high leverage, low regret. It aligns with OWASP’s framing that prompt injection and insecure output handling are top-tier threats in real systems. citeturn12search0turn11search4  
- **Interior micromanagement** = dictating exact internal steps, naming conventions, or implementation details that you do *not* actually care about. This tends to reduce search/exploration, increases brittle compliance, and increases the risk that the model optimizes for “following instructions” rather than “being right.”

OpenAI’s reasoning guidance is a good sanity check here: for reasoning models, overly elaborate “think step by step” instruction can be unnecessary or harmful; clarity and delimiters tend to matter more than ritualized chain-of-thought. citeturn3search5

Anthropic’s guidance converges on a compatible principle: structure the prompt so the model doesn’t confuse context, instructions, and examples—e.g., via XML-style section tags. citeturn2search0

## Claude Code: prompting strategy, Plan Mode vs coding, and setup-level controls

### Mode choice

Anthropic’s official docs treat Plan Mode as a first-class permission mode for safe code analysis: multi-step changes, codebase exploration, and interactive direction-setting. citeturn18search3 In addition, Claude Code supports permission modes such as `default`, `acceptEdits`, `plan`, and `bypassPermissions` (the last requiring strong environmental safety assumptions). citeturn18search0turn18search2

A crisp operational recommendation:

- Default to **Plan Mode first** when *any* of the following are true:
  - multi-file edits are likely,  
  - you are not already certain about the change surface,  
  - the task mixes design and implementation,  
  - security/permissions are involved. citeturn18search3turn18search0

- Use **execution mode** (default or acceptEdits) when:
  - the plan is already accepted,
  - you want fast iteration on localized edits,
  - you have tests/gates to detect drift. citeturn18search2turn18search3

### Setup levers that matter more than prompt wording

Two configuration levers usually dominate outcome quality and risk in Claude Code:

1. **Tool/permission constraining**
   - Claude Code supports permission rules and default permission modes in settings (including setting Plan Mode as default). citeturn18search0turn18search3  
   - It also supports excluding sensitive files via `.claude/settings.json` deny rules, rendering them invisible to the agent (this is a concrete mitigation against accidental secret exposure). citeturn22search1  

2. **“System prompt” extension mechanisms**
   - Anthropic notes it does not publish the internal Claude Code system prompt; instead you should use `CLAUDE.md` files and/or `--append-system-prompt` to add repo-specific instructions. citeturn22search1  
   - In non-interactive (headless/print) usage, the SDK examples show you can pass `--append-system-prompt`, `--allowedTools`, and `--permission-mode` together—i.e., you can make your “prompt contract” programmatic and reusable. citeturn22search0turn22search4  

### Subagents as a prompting primitive, not a “nice to have”

Claude Code subagents are separate-context, tool-scoped specialists defined as markdown files (with YAML frontmatter), stored either per-project (`.claude/agents/`) or per-user (`~/.claude/agents/`). citeturn18search1turn18search4

For a team already running a multi-lane OS model, subagents are a natural way to encode consistent “expert reviewer” behaviors (e.g., security review, API contract review, test plan reviewer) with strict tool allowlists. This is essentially **internal governance-as-code** inside Claude Code’s workflow surface. citeturn18search1turn18search3

### Recommended Claude Code prompt shape

Claude’s own prompt-engineering guidance strongly supports **explicit structure** (e.g., XML tags) when prompts contain multiple components. citeturn2search0 Your internal Claude Code prompts already implement a similar decomposition (goal/scope/contracts/guardrails/tests/output), which is exactly the kind of structure that reduces “unhelpful creativity” while preserving flexibility (you micromanage the boundary, not the interior). fileciteturn12file1L1-L1

I recommend institutionalizing a two-phase standard:

#### Claude Code template: Plan phase (read-only)

Use in Plan Mode. The output should be an artifact you can “accept” explicitly.

```text
<role>
You are a principal engineer implementing changes in this repo. Prefer minimal, high-leverage diffs.
</role>

<context>
Repo: <repo name>
Branch: <branch>
Relevant docs/specs: <paths>
Constraints from governance/security: <paths or bullets>
</context>

<objective>
Deliver: <what must exist when done>
Non-goals: <explicitly out of scope>
</objective>

<constraints>
- Security invariants (must not violate): <bullets>
- Allowed tools/actions in this phase: READ-ONLY (no edits, no commands)
</constraints>

<acceptance>
- Tests that must pass: <bullets>
- Behavioral criteria: <bullets>
- Output contract: plan must include file list + step list + risk points + rollback notes
</acceptance>

<task>
Produce a plan only. Do not change files.
</task>
```

Why this works:
- It matches Claude Code’s own “Plan Mode for safe code analysis” intent. citeturn18search3  
- It uses clear delimitation, consistent with Anthropic’s guidance on structured prompts. citeturn2search0  

#### Claude Code template: Execution phase (edits + verification)

Run after plan approval; optionally switch to `acceptEdits` for speed if you’re in a controlled repo context. citeturn18search0turn18search2

```text
<role>
You are implementing the approved plan exactly, unless you discover a blocker. If you discover a blocker, stop and report.
</role>

<inputs>
Approved plan: <paste or reference>
Constraints: <same invariants as plan prompt>
</inputs>

<execution>
- Make edits as needed.
- Run or update tests as required.
- Keep diffs minimal; do not refactor unrelated code.
</execution>

<deliverable>
Return:
1) Summary of changes vs plan
2) Files changed
3) Unified diff
4) Test results
5) Manual verification checklist
6) Known limitations / follow-ups
</deliverable>
```

This mirrors the CLI/SDK reality that Claude Code can be run with explicit tool allowances and output formats (including JSON for automation); you’re defining an external contract rather than hoping for good taste. citeturn22search0turn22search4

## OpenAI Deep Research: prompting strategy, codebase context, and site targeting

### What the product explicitly supports (and therefore what you should exploit)

In ChatGPT, Deep research:
- works with uploads, public web *or specific sites*, and connected apps,  
- lets you choose sources,  
- creates a research plan you can review and edit before beginning,  
- allows interruption/refinement mid-run,  
- returns a structured report with citations/links. citeturn19view0

OpenAI’s product post further states you can connect deep research to MCP or apps and restrict web searches to trusted sites, and emphasizes real-time progress tracking and refinement. citeturn19view1

In the API documentation, Deep Research models (`o3-deep-research` / `o4-mini-deep-research`) require at least one data source (web search, remote MCP, or file search over vector stores) and are explicitly optimized for searching/browsing + analysis; function calling is not supported in the deep research models. citeturn20view2turn20view3

Even if you are primarily using the ChatGPT UI, the API guide contains two principles that generalize:

1. Deep research performs best when prompted with **fully-formed research tasks**; in the API it will not do a clarifying-questions step, and OpenAI explicitly describes an optional upstream “clarification and prompt rewriting” step for best results. citeturn24view0  
2. Safety risks (prompt injection, exfiltration) increase when you mix private sources with web browsing; OpenAI explicitly recommends phasing work (public-web stage first, then private-data stage without web search). citeturn20view2turn23view1  

### Site targeting: treat “sites” as a trust boundary, not a relevance hint

The UI explicitly supports either:  
- restricting research **only** to entered domains, or  
- prioritizing those sites while allowing full-web search. citeturn19view0  

Given OWASP’s classification of prompt injection as a top LLM application risk, the conservative stance is:

- Use *restrict-only* mode when dealing with anything that could leak sensitive implementation details (e.g., internal security posture, proprietary architecture, non-public repo contents). citeturn12search0turn23view1  
- Use *prioritize-but-allow-web* only when your question genuinely requires breadth (e.g., “survey ecosystem approaches,” “compare vendors,” “collect benchmarks”), and the output is not directly executable or operational without later security review.

This is consistent with OpenAI’s own agent safety guidance: treat untrusted inputs carefully, constrain downstream channels, and use structured outputs between nodes where possible. citeturn11search4

### Adding your codebases as context: when it helps, when it hurts

Adding codebase context (lyra-operating-system and control-panel) is valuable when your **research question is about your system** rather than about the world.

It tends to help most for:
- architecture critiques (e.g., “audit log/event sourcing tradeoffs in *our* code”),  
- threat modeling and guardrail design rooted in *actual* code paths,  
- refactor plans that need file-level specificity.

It tends to hurt (or at least increase risk/cost) when:
- the question is ecosystem-level and doesn’t require your code,  
- the prompt is already too broad—extra context just adds noise,  
- you also enable broad web search and the task exposes internal context to injection/exfiltration risks (explicitly flagged in OpenAI’s deep research safety guidance). citeturn23view1turn20view2  

A high-signal pattern (aligned with OpenAI’s “phase the work” recommendation): citeturn20view2  
- **Phase A (public):** Deep research with web search + restricted sites. No repo context. Goal: gather external best practices and known failure modes.  
- **Phase B (private):** Deep research with repo context and *tighter* site restrictions (or web off), producing an internal critique/design memo that maps findings onto your codebase.  

### Recommended Deep Research prompt shape

OpenAI’s reasoning best practices favor straightforward prompts and clear delimiters over chain-of-thought prompting. citeturn3search5 The Deep Research API guide also emphasizes that a “fully-formed” prompt matters, and gives guidance that the rewritten prompt should maximize specificity and include expected output structure. citeturn24view0  

A high-performance Deep Research prompt, in practice, looks like a constrained research brief:

```text
<role>
You are a research analyst + staff software architect doing an evidence-backed review.
</role>

<objective>
Produce: (a) findings, (b) recommended decision, (c) implications for implementation in our repos.
Audience: expert engineers.
</objective>

<scope>
In-scope: <bullet list>
Out-of-scope: <bullet list>
Time horizon: <e.g., 1–2 sprints>
</scope>

<sources>
- Treat repo context (if provided) as primary source for “what exists.”
- For external claims, cite primary/official sources (vendor docs, standards, peer-reviewed papers).
- Use only these sites/domains: <allowlist>
</sources>

<questions>
1) <question>
2) <question>
...
</questions>

<deliverable>
Return a structured report with:
- executive synthesis
- alternatives + tradeoffs
- risk register (failure mode, likelihood, impact, mitigation)
- mapping to codebase (file/module touchpoints if repo context is present)
- citations inline for non-trivial claims
</deliverable>

<constraints>
- Be specific and opinionated when tradeoffs exist.
- Flag unknowns explicitly.
</constraints>
```

Critically, none of this asks the model to expose chain-of-thought. It asks for **surface-level artifacts** (tradeoffs, risks, mappings) with citations—aligned both with OpenAI’s reasoning guidance and the Deep Research product’s “documented report” framing. citeturn3search5turn19view0turn24view0

## Unified recommendation: a prompt “operating system” for the two external lanes

### Normalize both lanes around the same artifact boundary

Your internal conventions already gesture at this: external workbench runs should produce structured handoffs back into your OS. fileciteturn17file7L1-L1 The most leverage comes from making that explicit and consistent:

- **Deep Research outputs** should land as a **Decision/Design Artifact** (DDA): evidence-backed, citation-heavy, with clear “must/should/nice” recommendations.
- **Claude Code outputs** should land as a **Change Artifact** (CA): diff/tests/checklist, with explicit constraint compliance.

This makes the two tools compose: Deep Research decides, Claude Code executes.

### Standardize on three prompt layers, reused across both tools

Layering is how you reconcile “don’t micromanage” with “don’t be vague.”

1. **Policy layer (stable, reusable):** security posture, tool boundaries, output requirements, format rules.  
   - For Claude Code, set via repo-level CLAUDE.md and `.claude/settings.json` (deny sensitive files, define default permission mode). citeturn22search1turn18search0  
   - For Deep Research, set via a reusable “Research Policy” block: allowed sources, evidence standards, injection resistance posture. citeturn19view0turn23view1  

2. **Work-order layer (semi-stable):** the template: objectives, constraints, acceptance tests, deliverable schema.  
   - This is what you already encode in prompt files in-repo. fileciteturn12file1L1-L1  

3. **Task layer (volatile):** the specific ask, references, and current context.

This separation matters because it makes iteration tractable: you can change the task without silently drifting policy, and you can change policy without rewriting every task prompt.

### Proposed “always include” phases

Because your audience is expert and your workflows are high-consequence (code + systems), I recommend always enforcing four phases—explicitly for Claude Code, and semi-explicitly for Deep Research:

- **Clarify (only if needed):** identify missing constraints or ambiguous acceptance criteria.  
  - Deep research in ChatGPT often does this via its plan step and follow-ups. citeturn19view0turn24view0  
- **Plan:** produce a plan artifact you can accept/reject.  
  - Claude Code Plan Mode exists specifically for this. citeturn18search3turn18search0  
- **Execute:** do the work with bounded permissions/sources.  
- **Verify:** tests/citations; produce a reusable artifact.

This is directly compatible with classic plan-then-execute prompting results (Plan-and-Solve) and tool-grounded agent behavior (ReAct). citeturn9view0turn10view0

### How detailed should prompts be?

A recommendation calibrated for expert teams:

- **Be maximally detailed about:**
  - invariants (security, safety, “never do X”),  
  - allowed tools/sources,  
  - acceptance criteria and evidence requirements,  
  - output schema (so the handoff is machine-checkable or at least review-checkable). citeturn11search4turn12search0turn19view0turn2search0  

- **Be minimally detailed about:**
  - implementation steps (unless you have a specific architectural reason),  
  - stylistic choices that aren’t tied to maintainability/consistency,  
  - “reasoning rituals” (especially for reasoning models, per OpenAI guidance). citeturn3search5  

This is the cleanest resolution of the micromanagement tradeoff: **constrain what must be true; don’t constrain how it becomes true**.

### Concrete templates to adopt in-repo

Given you already store prompts in-repo, I’d formalize a small library:

- `prompts/claude-code/WO_plan.md` and `prompts/claude-code/WO_execute.md`
- `prompts/deep-research/RO_public.md` and `prompts/deep-research/RO_private.md`
- `prompts/handoff/DDA_report.md` (research → decision)
- `prompts/handoff/CA_change.md` (implementation → verification)

Store them with explicit versioning (“prompt semver”) and tie them to eval tasks when you can. This aligns with OpenAI’s explicit recommendation to monitor prompts with evals and control drift across model upgrades. citeturn3search4turn3search1

If you want to go one step further in Claude Code: encode reviewers as subagents (`.claude/agents/security-reviewer.md`, `.claude/agents/api-contract-reviewer.md`) with strict tool allowlists. That takes “prompting craft” out of the heads of individual operators and puts it into shared, enforceable config. citeturn18search1turn18search4turn18search3
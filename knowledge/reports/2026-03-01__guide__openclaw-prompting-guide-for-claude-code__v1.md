---
title: "OpenClaw Prompting Guide for Claude Code"
date: 2026-03-01
source: guide
ingest_from: "knowledge/inbox/external-analysis-dropzone/OpenClaw-Claude-Code-Prompting-Guide-2026.md"
tags: [external-analysis, guide]
decision_relevance: tbd
confidence: tbd
status: archived-source
---

# OpenClaw Prompting Guide for Claude Code

Updated: 2026-02-28

## Purpose

This document updates how OpenClaw should write prompts for Claude Code.

The core change is simple: **stop over-specifying the path**. Claude Code performs best when the prompt clearly defines the **goal, context, constraints, and verification**, while leaving Claude room to explore, plan, and implement. Anthropic now explicitly frames Claude Code as an agentic environment where the user describes what they want and Claude figures out how to build it. Their current prompt guidance also says that, for reasoning, general instructions often outperform hand-written step-by-step plans. [1][2]

In practice, the strongest Claude Code workflows combine four things:

1. **High-quality task framing** - outcome, constraints, references, and success criteria.
2. **Good persistent context** - a concise `CLAUDE.md`, optional skills, and deterministic hooks.
3. **Incremental execution** - one coherent unit of work at a time, with fresh contexts when needed.
4. **Programmatic verification** - tests, screenshots, repro steps, expected outputs, and review passes. [1][3][4][6]

## What the best Claude Code users are actually doing

### 1) They prompt for outcomes, not choreography

The common beginner mistake is to turn the prompt into a detailed project plan with mandatory micro-steps: open file A, then grep B, then edit C, then run D, then write E. This usually reduces leverage. Anthropic's current prompt guide says to be clear and direct, but also notes that a prompt like "think thoroughly" often works better than a hand-written step-by-step reasoning plan. Anthropic also warns that newer Claude models are **more responsive to the system prompt than before**, so aggressive language such as "CRITICAL: you MUST use X" can cause over-triggering. Targeted guidance now beats blanket control. [2]

The high-performing pattern is:

- be explicit about the **desired end state**,
- give **relevant constraints**,
- point Claude to **source-of-truth files or examples**,
- define **how success will be verified**,
- and let Claude choose the best path unless order genuinely matters. [1][2][11]

### 2) They separate discovery, planning, and implementation

Anthropic's Claude Code docs recommend **explore first, then plan, then code** for tasks that are unclear, multi-file, or architecturally meaningful. For small changes where the diff is obvious, they recommend skipping the planning overhead and implementing directly. For larger features, Anthropic even recommends having Claude interview the user first, write a `SPEC.md`, and then starting a fresh implementation session with clean context. [1][4]

That means OpenClaw should not use one default prompt style for every task. It should choose a mode:

- **Direct implement** for small, clear, local changes.
- **Plan then implement** for multi-file or uncertain work.
- **Spec first** for ambiguous or product-level changes.
- **Review only** for audits, critique, or validation.
- **Continuation mode** for long-running tasks that span sessions. [1][4][6]

### 3) They provide better context, not just more context

Anthropic's guidance is very specific here: reference files directly, mention constraints, point to example patterns, and use rich inputs like screenshots, logs, and exact commands. In other words, **feed Claude the context that changes the decision**, not a giant generic memo. [1]

Practitioners do the same thing. Simon Willison's example Claude Code prompt works because it names the desired functionality, references existing tools in the same repo that Claude should imitate, and adds concrete UI constraints. Thoughtbot describes gathering discovery notes, personas, workflows, and screenshots into a single project context and then using that material to craft stronger prompts. [9][11]

So the move is not from "more context" to "less context". The move is from **unfocused context dumps** to **targeted context with clear anchors**.

### 4) They put stable instructions in the environment, not in every prompt

Anthropic is explicit that `CLAUDE.md` should be concise, specific, and limited to instructions that apply broadly. Files over roughly 200 lines reduce adherence and consume context. Their docs also say that if something must happen every time with zero exceptions, use a **hook**, because hooks are deterministic while `CLAUDE.md` is advisory. For occasional domain knowledge or reusable workflows, use **skills**. For isolated investigation or review, use **subagents**. [1][3]

This matters for OpenClaw because many prompt-writing problems are really **environment-design problems**. If OpenClaw keeps repeating the same testing rules, repo etiquette, build commands, path conventions, or safety guardrails inside every prompt, it is wasting tokens and increasing noise.

Strong teams externalize repeated instructions like this:

| Concern | Best home | Why |
|---|---|---|
| Stable repo-wide conventions | `CLAUDE.md` | Loaded every session; good for broad, persistent guidance |
| Must-happen rules | Hooks | Deterministic, not advisory |
| Reusable domain workflows | Skills | Loaded on demand; avoids bloating every session |
| Heavy investigation or specialist review | Subagents | Separate context window, cleaner main thread |
| One-off task framing | Prompt | Keeps each session scoped and current |

This is one of the highest-leverage changes OpenClaw can make. [1][3]

### 5) They treat verification as the main event

Anthropic's Claude Code best-practices page calls this the **single highest-leverage thing you can do**: give Claude a way to verify its own work. That means tests, expected outputs, screenshots, repro steps, or browser checks, not just a verbal request to "make this work". Anthropic's long-running agent research reached the same conclusion: absent explicit prompting, Claude often makes reasonable code changes but fails to verify end-to-end behavior. [1][6]

Practitioners echo this strongly. Harper Reed describes testing and test-driven development as especially effective for keeping Claude on task, and thoughtbot emphasizes maintaining test coverage while breaking work into small reviewable chunks. [8][10]

For OpenClaw, this means every implementation prompt should include:

- how to reproduce the problem or desired behavior,
- what commands to run,
- what outputs or checks define success,
- and what summary Claude should return after verification. [1][4][6]

### 6) They work incrementally and preserve state across sessions

Anthropic's research on long-running agents is especially relevant to OpenClaw. Their finding is not that a single beautiful prompt solves everything. It is that, for larger work, the harness needs explicit artifacts that survive context refreshes: an initializer step, a feature list or task list, a progress log, an `init.sh` or equivalent startup script, and a rule that the coding agent should make **incremental progress** and leave the repo in a clean state after each session. [5][6]

This lines up with practitioner workflows. Harper Reed uses `spec.md` and `prompt_plan.md` as durable artifacts. Thoughtbot describes rereading `CLAUDE.md` and scanning the codebase again when context gets compressed. [8][10]

For OpenClaw, the implication is important:

> For any task likely to span sessions or large amounts of context, OpenClaw should generate prompts that maintain external state, not rely on the conversation alone.

Recommended persistent artifacts for bigger tasks:

- `SPEC.md` - the canonical scope and requirements.
- `TASKS.md` or `feature_list.json` - explicit units of work and pass/fail state.
- `claude-progress.txt` - what changed, what remains, what to verify next.
- `init.sh` or equivalent - how to boot, test, and regain bearings quickly. [6][10]

### 7) They use fresh contexts strategically

Anthropic repeatedly emphasizes context as the main scarce resource. Their docs warn against "kitchen sink" sessions, recommend `/clear` between unrelated tasks, suggest restarting after two failed corrections, and encourage reviewer sessions or subagents with fresh context. They also recommend a writer/reviewer pattern, where one Claude implements and another reviews from a clean context. [1][5]

This is a major change for OpenClaw prompt design:

- Do not keep patching a polluted session forever.
- Do not ask one session to both explore the whole codebase and implement and audit and document and create the PR unless the task is actually small.
- Prefer new contexts for review, verification, and continuation. [1][5][6]

### 8) They improve prompts with evals, not taste alone

Anthropic's current guidance on agent evals is highly relevant: start early, use 20-50 real tasks, write unambiguous pass/fail criteria, build reference solutions, and **grade the output more than the exact path**. They explicitly note that testing whether the agent followed a very specific sequence of tool calls is usually too brittle and punishes valid solutions. [7]

That is the evaluation equivalent of not micromanaging prompts.

For OpenClaw, prompt quality should be measured on a small internal eval set such as:

- small bug fix,
- multi-file refactor,
- greenfield feature,
- ambiguous feature requiring clarification,
- review-only task,
- long-running continuation task.

And the grader should focus on what matters:

- correct outcome,
- no regressions,
- verification completed,
- adherence to critical constraints,
- clean handoff artifacts,
- no unnecessary complexity. [7]

## Recommendations for OpenClaw

### 1. Adopt an outcome-oriented default prompt schema

OpenClaw should generate prompts with a consistent structure. The exact syntax can vary, but the content should usually include the following sections:

- **Mode** - direct implement / plan then implement / spec first / review only / continuation.
- **Goal** - the user-visible outcome.
- **Context** - why it matters, relevant files, source-of-truth docs, analogous patterns.
- **Constraints** - architecture, compatibility, dependencies, non-goals, safety boundaries.
- **Verification** - commands, screenshots, repro steps, or acceptance checks.
- **Deliverable** - what Claude should leave behind: code, tests, spec update, PR summary, progress log.
- **Autonomy guidance** - prefer the simplest working solution; ask before destructive or externally visible actions. [1][2][6]

The crucial difference is that this schema describes the **problem space** and the **definition of done**, not a fully choreographed path.

### 2. Make mode selection explicit

OpenClaw should choose one of the following modes before generating the prompt:

| Mode | Use when | Default behavior |
|---|---|---|
| `direct_implement` | Small, obvious, local change | Implement directly and verify |
| `plan_then_implement` | Multi-file or uncertain change | Inspect first, produce a short plan, then implement |
| `spec_first` | Ambiguous, high-stakes, or product-level task | Clarify assumptions or interview, write `SPEC.md`, then use a fresh implementation session |
| `review_only` | Audit, critique, quality pass, security review | Read and report, do not modify unless later instructed |
| `continuation` | Work that spans sessions | Read progress artifacts, verify current state, complete one next unit |

OpenClaw should avoid mixing these modes in one prompt unless there is a compelling reason. [1][4][6]

### 3. Always tell Claude whether to act or only analyze

Anthropic's prompt guide notes that if you ask vaguely, Claude may suggest changes instead of implementing them. OpenClaw should therefore always be explicit about whether Claude should:

- implement,
- investigate,
- plan,
- review,
- or produce a spec. [2]

A surprising number of bad Claude Code sessions are just action-ambiguity.

### 4. Default to high-level process guidance, not mandatory micro-steps

OpenClaw should not tell Claude exactly which tools to use or what order to think in unless one of these is true:

- the order genuinely matters,
- a tool is clearly more context-efficient or safer,
- a deterministic workflow is required,
- or prior failures show that a narrower path is necessary. [1][2][7]

In practice, replace:

- "First grep X, then open Y, then use tool Z, then do A, then B..."

with:

- "Inspect the current implementation in @X and related patterns in @Y. Follow the simplest sound approach. If a specialized tool or CLI would materially improve accuracy or speed, use it." [1][2]

### 5. Put every implementation prompt on rails with verification

OpenClaw should reject or rewrite any implementation prompt that lacks verification.

Minimum verification block:

- reproduction or expected behavior,
- commands to run,
- tests to update or create,
- what constitutes passing,
- what Claude should report if something remains unverified. [1][4][6]

This is the easiest way to reduce hallucinated completeness.

### 6. Move repeated instructions out of prompts

OpenClaw should treat the prompt as the **task layer**, not the place to restate all organizational memory.

Recommended split:

- Put broad repo rules, testing commands, common gotchas, and style exceptions in `CLAUDE.md`.
- Put deterministic always-run requirements in hooks.
- Put specialized reusable workflows in skills.
- Put heavy reviewers or investigators in subagents.
- Keep prompts focused on the current task. [1][3]

This reduces prompt bloat and increases adherence.

### 7. For bigger tasks, generate artifacts Claude can continue from

For tasks likely to exceed one clean session, OpenClaw should generate prompts that create or update:

- `SPEC.md`,
- `TASKS.md` or `feature_list.json`,
- `claude-progress.txt`,
- and optionally `init.sh`. [6][10]

The continuation prompt should then instruct Claude to:

1. regain bearings,
2. verify the current state,
3. select exactly one next unit of work,
4. complete it cleanly,
5. update progress artifacts before ending. [5][6]

### 8. Use separate review contexts by default on important work

For substantial changes, OpenClaw should prefer a second pass in a fresh context rather than asking the implementing Claude to both write and objectively review its own code. Anthropic explicitly recommends multiple sessions and a writer/reviewer pattern. [1]

The reviewer prompt should focus on:

- edge cases,
- regressions,
- consistency with existing patterns,
- unnecessary complexity,
- missing tests,
- and security or data-handling risks. [1][4]

### 9. Restart rather than over-correct

If Claude has already been corrected twice on the same issue, OpenClaw should stop patching the current thread and regenerate a cleaner prompt for a fresh context. Anthropic explicitly recommends this. [1]

This rule alone will save a lot of wasted cycles.

### 10. Improve OpenClaw with an eval set

OpenClaw's prompt policy should be tested with a living eval set of real tasks and regressions. Anthropic recommends starting with 20-50 tasks from real manual checks, bug trackers, or user failures, and designing clear reference solutions and pass/fail criteria. [7]

Suggested OpenClaw eval dimensions:

- correctness,
- adherence to constraints,
- verification quality,
- token efficiency,
- unnecessary file creation or overengineering,
- quality of state handoff for continuation tasks,
- and consistency across repeat runs. [7]

## Recommended default template for OpenClaw

Use this as the baseline structure. It is intentionally concise.

```text
<mode>
plan_then_implement
</mode>

<goal>
Implement [desired outcome].
</goal>

<context>
- Business or product intent: [why this matters]
- Relevant files or directories: @[path1], @[path2]
- Existing patterns to follow: @[similar_file1], @[similar_file2]
- Source-of-truth docs or examples: [doc, screenshot, issue, log, URL]
</context>

<constraints>
- Preserve: [behavior / API / compatibility requirement]
- Avoid: [non-goals]
- Dependencies: [reuse before adding new ones]
- Safety: ask before destructive actions or actions visible to others
</constraints>

<verification>
- Reproduce or validate with: [exact command / workflow / screenshot check]
- Tests to run: [commands]
- Done means: [acceptance criteria]
- If anything cannot be verified, say so explicitly and explain why
</verification>

<execution>
- First inspect the relevant implementation and confirm the current behavior
- Then choose the simplest sound approach
- For larger changes, write a short plan before editing
- Implement in small, reviewable increments
- Before finishing, verify against the criteria above
</execution>

<deliverable>
- Make the code changes
- Update or add tests if needed
- Summarize changed files, key decisions, verification results, and any remaining risks
</deliverable>
```

### Mode-specific additions

**For `direct_implement`**

Add: "The change is small and well-scoped. Skip formal planning unless you discover hidden complexity."

**For `spec_first`**

Add: "Do not implement yet. Interview for missing decisions or write down assumptions and open questions. Produce `SPEC.md`. After the spec is complete, stop so a fresh implementation session can use it."

**For `review_only`**

Add: "Do not modify files. Read the relevant code and return findings grouped by severity, with file references and concrete fixes."

**For `continuation`**

Add: "Read `claude-progress.txt`, the recent git log, and the task list first. Verify the current state before starting new work. Complete exactly one meaningful next unit, then update the progress artifacts before ending." [6]

## What OpenClaw should stop doing

1. **Do not default to mandatory micro-steps.** Only specify sequence when order matters. [2][7]
2. **Do not stuff everything into one prompt.** Use `CLAUDE.md`, skills, hooks, and progress files. [1][3][6]
3. **Do not send implementation prompts without verification.** [1][6]
4. **Do not keep correcting a dirty session forever.** Restart after two failed corrections. [1]
5. **Do not use giant `CLAUDE.md` files as a dumping ground.** Keep them concise and specific. [1][3]
6. **Do not force tools or subagents aggressively by default.** Newer models are more responsive; over-prompting can over-trigger. [2]
7. **Do not ask for everything at once on large projects.** Use incremental units and persistent artifacts. [6][10]
8. **Do not grade prompts by whether Claude followed your preferred path.** Grade the output, verification, and constraints. [7]

## Example rewrite: from micromanaged to high-leverage

### Over-managed version

```text
Open auth.ts, then inspect session.ts, then grep for refresh token logic, then read env.ts, then add Google OAuth, then update the middleware, then write tests in auth.test.ts, then run npm test, then run npm run lint, then commit the code. Do not do anything else.
```

### Better version

```text
<mode>
plan_then_implement
</mode>

<goal>
Add Google OAuth to the existing authentication system.
</goal>

<context>
- Relevant areas: @src/auth, @src/session, @src/config/env.ts
- Follow patterns from @src/auth/password-login.ts and @src/session/create-session.ts
- We want parity with the current login/session model, not a parallel auth stack
</context>

<constraints>
- Preserve existing email/password login
- Reuse current session primitives if sound
- Avoid introducing new dependencies unless clearly justified
- Ask before destructive or externally visible actions
</constraints>

<verification>
- Existing login still works
- Google login creates a normal user session
- Run: npm test && npm run lint
- Summarize changed files, key tradeoffs, and remaining risks
</verification>

<execution>
- First inspect the current auth and session flow
- Then write a concise implementation plan
- Then implement in small, reviewable increments
- Before finishing, verify against the criteria above
</execution>
```

The improved version gives Claude room to reason while still constraining the outcome. It is specific where specificity matters, and open where Claude should exercise judgment. [1][2]

## Suggested rollout for OpenClaw

### Phase 1: Update the prompt generator

Implement:

- the default prompt schema,
- explicit mode selection,
- mandatory verification blocks,
- and file/example references by default.

### Phase 2: Reduce prompt bloat structurally

Move stable instructions into:

- `CLAUDE.md`,
- hooks,
- skills,
- and specialist subagents.

### Phase 3: Add eval-driven iteration

Create a small benchmark set from real tasks and regressions. Review transcripts and improve prompts based on observed failures, not opinion alone. [7]

## Bottom line

The new best practice is **not** "be vague." It is:

- be very clear about the destination,
- very clear about constraints,
- very clear about verification,
- and much less controlling about the exact route.

OpenClaw should therefore act less like a project manager dictating every keystroke and more like a strong technical lead who defines the outcome, points to the right context, sets the guardrails, and expects evidence that the work actually passes. That is where Claude Code currently gets its best leverage. [1][2][6][8][10][11]

## Sources

[1] Anthropic, [Best Practices for Claude Code](https://code.claude.com/docs/en/best-practices), accessed 2026-02-28.

[2] Anthropic, [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), accessed 2026-02-28.

[3] Anthropic, [How Claude remembers your project](https://code.claude.com/docs/en/memory), accessed 2026-02-28.

[4] Anthropic, [Common workflows](https://code.claude.com/docs/en/common-workflows), accessed 2026-02-28.

[5] Anthropic Engineering, [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), 2025-09-29.

[6] Anthropic Engineering, [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents), 2025-11-26.

[7] Anthropic Engineering, [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), 2026-01-09.

[8] thoughtbot, [Claude Code: Production ready code in a two-week sprint](https://thoughtbot.com/blog/claude-code-skills-production-ready-code-in-a-two-week-sprint), 2026-02-09.

[9] thoughtbot, [Rapid prototyping with Claude Code: How we transformed our design sprint process](https://thoughtbot.com/blog/rapid-prototyping-with-claude-code-how-we-transformed-our-design-sprint-process), 2026-01-13.

[10] Harper Reed, [Basic Claude Code](https://harper.blog/2025/05/08/basic-claude-code/), 2025-05-08.

[11] Simon Willison, [Building a tool to copy-paste share terminal sessions using Claude Code for web](https://simonwillison.net/2025/Oct/23/claude-code-for-web-video/), 2025-10-23.

[12] Shrivu Shankar, [AI Can't Read Your Docs](https://blog.sshh.io/p/ai-cant-read-your-docs), 2025-08-17.

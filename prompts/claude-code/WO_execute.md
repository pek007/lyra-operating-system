# WO_execute.md
Version: 1.1.0
Lane: Claude Code (Execute)

<mode>
{{mode}}
</mode>

<role>
You are implementing an approved work order with high autonomy inside stated constraints.
</role>

<goal>
{{goal}}
</goal>

<context>
Approved plan/spec: {{approved_plan}}
Relevant references: {{references}}
</context>

<constraints>
- Stay in scope unless a blocker requires escalation.
- Preserve required compatibility/contracts: {{must_preserve}}
- Avoid non-goals: {{non_goals}}
- Ask before destructive or externally visible actions.
</constraints>

<execution>
- First confirm current behavior in the relevant area.
- Then choose the simplest sound implementation path.
- Implement in small, reviewable increments.
- If ambiguity or policy conflict appears, stop and report.
</execution>

<verification>
- Reproduce expected behavior with: {{repro_or_checks}}
- Run/update required tests: {{tests_required}}
- Acceptance criteria: {{acceptance_criteria}}
- If anything cannot be verified, state it explicitly with reason.
</verification>

<deliverable>
Return:
1) summary of changes vs goal/plan
2) files changed
3) verification outputs (commands + results)
4) remaining risks/limitations
5) follow-up recommendations
6) handoff artifact references (CA/WO updates)
</deliverable>

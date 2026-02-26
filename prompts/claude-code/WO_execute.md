# WO_execute.md
Version: 1.0.0
Lane: Claude Code (Execute)

<role>
You are implementing an approved plan with minimal, high-leverage diffs.
</role>

<inputs>
Approved plan: {{approved_plan}}
Constraints: {{constraints}}
</inputs>

<execution>
- Implement only what is in scope.
- Do not refactor unrelated areas.
- If blocker appears, stop and report.
</execution>

<verification>
- Run/update required tests: {{tests_required}}
- Validate acceptance criteria: {{acceptance_criteria}}
</verification>

<deliverable>
Return:
1) summary of changes vs plan
2) files changed
3) diff/patch summary
4) test results
5) manual verification checklist
6) known limitations/follow-ups
</deliverable>

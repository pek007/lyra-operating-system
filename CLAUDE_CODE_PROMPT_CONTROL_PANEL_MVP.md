# Claude Code Prompt — Control Panel MVP

Use this prompt in Claude Code for implementation.

---

Build a local-first **Control Panel MVP** from this spec file:
`BUILD_SPEC_CONTROL_PANEL_MVP.md`

## Requirements
- Use Node + TypeScript
- Use Express for API and Vite+React for web UI
- Use Zod for schema validation
- Parse markdown + YAML frontmatter from local files
- Implement 4 views: Now / Next / Watch / Change Feed
- Read from local workspace files only (read-only)

## Inputs (workspace data)
- `TASKS.md`
- `RISK_REGISTER.md`
- `PROCESS_REGISTRY.md`
- `SUBSCRIPTION_REGISTER.md`
- `knowledge/evidence/YYYY-MM/*.md`
- `knowledge/registries/agents/*.md`
- `knowledge/registries/routing/*.md`
- git history for recent changes

## API endpoints
- `GET /api/health`
- `GET /api/now`
- `GET /api/next`
- `GET /api/watch`
- `GET /api/changes?limit=50`

## Output expectations
1. Complete runnable repo structure
2. README with setup/run instructions
3. Minimal tests for parsers/services
4. Clear list of assumptions and known limitations

## Constraints
- Do not implement write-back to markdown files in MVP
- Keep architecture modular and easy to extend
- Keep UX high signal / low clutter

When done, provide:
- file tree
- run commands
- test output
- next iteration plan

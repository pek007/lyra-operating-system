# BUILD SPEC — Control Panel MVP Skeleton

## Objective
Build a lightweight Control Panel MVP that sits above existing OpenClaw operations and renders transparent operational state from our existing docs/evidence.

## Build Mode
- Primary implementation: Claude Code (run manually by Peter)
- Integration/final polish: Lyra (this session)

## Scope (MVP)
1. Parse and render key registries/docs
2. Render 4 operator views: Now / Next / Watch / Change Feed
3. Read evidence records generated in `knowledge/evidence/*`
4. Expose minimal local web UI (read-only)

## Non-goals (for MVP)
- Authentication/authorization layer
- Realtime websocket streaming
- Bi-directional edits back to all markdown files
- Full production deployment hardening

## Tech Recommendation
- **Node + TypeScript**
- **Express** for local API
- **Vite + React** for UI
- **Zod** for schema validation
- **gray-matter** for YAML frontmatter parsing

## Proposed Repo Structure
```text
control-panel-mvp/
  README.md
  package.json
  tsconfig.json
  .env.example
  /apps
    /api
      src/
        server.ts
        routes/
          health.ts
          now.ts
          next.ts
          watch.ts
          changes.ts
        services/
          fsLoader.ts
          evidenceService.ts
          tasksService.ts
          riskService.ts
          gitService.ts
        schemas/
          agentContract.ts
          routingRule.ts
          evidenceRecord.ts
          changeRecord.ts
    /web
      src/
        main.tsx
        App.tsx
        pages/
          NowPage.tsx
          NextPage.tsx
          WatchPage.tsx
          ChangeFeedPage.tsx
        components/
          StatusCard.tsx
          SectionTable.tsx
          FindingBadge.tsx
        lib/api.ts
```

## Data Inputs
Read-only from workspace root:
- `TASKS.md`
- `RISK_REGISTER.md`
- `PROCESS_REGISTRY.md`
- `SUBSCRIPTION_REGISTER.md`
- `knowledge/evidence/YYYY-MM/*.md`
- `knowledge/registries/agents/*.md`
- `knowledge/registries/routing/*.md`
- git log (for change feed)

## API Endpoints (MVP)
- `GET /api/health`
- `GET /api/now`
- `GET /api/next`
- `GET /api/watch`
- `GET /api/changes?limit=50`

### Endpoint Contracts (high-level)
- `/now`: active tasks, latest evidence status, open incidents summary
- `/next`: triage + upcoming scheduled reviews + pending decisions
- `/watch`: warnings/risks/cost watch signals
- `/changes`: recent git commits + change records

## Acceptance Criteria
1. App starts locally with one command (`pnpm dev` or equivalent)
2. All 4 views load from real local data files
3. Schema validation errors are surfaced clearly in UI/logs
4. No write operations to source files in MVP
5. README includes setup and troubleshooting

## Build Steps for Claude Code
1. Scaffold monorepo structure
2. Implement schema validators and file loaders
3. Implement API routes + mock-safe fallbacks
4. Implement UI pages with table/card summaries
5. Add README with setup commands
6. Add basic tests for parsers/services (at least 5)

## Run Commands (target)
```bash
pnpm install
pnpm dev
# api on :4010, web on :4011 (or similar)
```

## Handoff Deliverables Required
Claude Code should return:
1. Repo/branch link
2. Setup commands
3. Known limitations
4. Test results
5. Suggested next iteration items

## Integration Notes for Lyra
After handoff, Lyra will:
- run app locally
- fix small integration issues
- align naming/contracts to OS docs
- update PROCESS_REGISTRY and TASKS

## Version
- v1.0
- Date: 2026-02-25
- Owner: Peter + Lyra

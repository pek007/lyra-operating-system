# AI Agent Opportunity Scouting Operating Note

Date: 2026-03-26
Owner: Improvement Product

## Intent
Extend the Improvement product so it captures not only internal friction and review findings, but also high-signal external opportunities in AI agent systems generally and OpenClaw specifically.

## Operating goal
Create a compact, reusable opportunity-sensing loop that helps Lyra OS notice valuable external ideas early, filter out low-value noise, and route worthwhile items into explicit evaluation or adoption work.

## Minimum operating pattern
1. Scan bounded external sources for new use cases, workflows, tooling, release shifts, and operating practices.
2. Log only items with plausible relevance to Lyra OS, PX Strategy, or downstream workspaces.
3. Assign each logged item a clear disposition such as:
   - `watch`
   - `reject`
   - `worth_testing`
   - `routed`
   - `adopted`
4. For any item above lightweight watch level, record:
   - what it is
   - why it matters to us
   - likely area of application
   - what evidence would justify testing or adoption
   - next review or routing step
5. Route worthwhile items into explicit TDE-linked follow-up when the opportunity is concrete enough to test or adopt.

## Executive briefing use
A compact weekly executive briefing can summarize the most relevant newly observed opportunities, with emphasis on:
- likely leverage
- relevance to current operating priorities
- novelty versus existing capability
- recommended disposition

## Guardrail
This loop is for selective leverage discovery, not for maintaining a broad AI trend scrapbook.

# Runtime Model

Status: draft wiki page
Date: 2026-04-03
Domain: Architecture

## Summary
The runtime model describes how Lyra operates through agents, sessions, tools, channels, cron jobs, and workspaces.

Lyra is not a single monolithic loop. It operates through a set of interacting runtime surfaces that together form the working system.

## Why it matters
A large amount of confusion disappears once the runtime is seen as a model rather than just a chat interface.

The runtime model affects:
- where context lives
- how work is routed
- what authority a given runtime surface has
- how actions are audited or reviewed
- how cross-context coordination should happen

## Core runtime surfaces
- main session runtime
- named agent runtimes
- cron/session runtimes
- tool runtime surfaces
- channel bindings
- workspace-specific contexts

## Current practical understanding
Lyra operates across multiple overlapping runtime forms:
- direct chat/session interaction
- isolated or persistent cron-driven agent work
- tool-mediated actions
- workspace-based artifact creation
- channel-bound message delivery

This means the runtime model is inherently multi-surface.

## Key implications
- not all work belongs in the main chat session
- context routing matters
- authority and blast radius vary by runtime surface
- operational truth should not depend only on transcript memory

## Related pages
- [Trust Boundary Model](../controls-security/trust-boundary-model.md)
- [Memory Architecture](./memory-architecture.md)

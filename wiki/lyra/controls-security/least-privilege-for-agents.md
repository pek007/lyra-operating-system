# Least Privilege for Agents

Status: draft wiki page
Date: 2026-04-03
Domain: Controls & Security

## Summary
Least privilege for agents means restricting tool access, data access, permissions, credentials, and action scope to the minimum necessary for the task at hand.

## Why it matters
Prompt injection becomes much more dangerous when a model has broad authority. Least privilege reduces blast radius even when adversarial steering or control failure occurs.

## Practical implications
- prefer task-scoped access over general access
- restrict dangerous tools by default
- separate app/service credentials from broad user authority where possible
- keep sensitive data access narrow and deliberate
- combine least privilege with approval gates and sandboxing

## Why it is a Lyra-level pattern
This is not only a product-specific control. It is a reusable pattern across Lyra capabilities, runtimes, and workspace contexts.

## Related pages
- [Prompt Injection](./prompt-injection.md)
- [Prompt Injection Defense](./prompt-injection-defense.md)
- [Trust Boundary Model](./trust-boundary-model.md)

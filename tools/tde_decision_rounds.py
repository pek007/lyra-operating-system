#!/usr/bin/env python3
from __future__ import annotations

from typing import Any


def next_research_round(metadata: dict[str, Any]) -> int:
    current = metadata.get("decision_research_round")
    if not isinstance(current, int) or current < 0:
        current = 0
    return current + 1


def research_budget_exhausted(envelope: dict[str, Any] | None, next_round: int) -> bool:
    if not isinstance(envelope, dict):
        return False
    budget = envelope.get("research_budget")
    if not isinstance(budget, dict):
        return False
    max_rounds = budget.get("max_rounds")
    if not isinstance(max_rounds, int):
        return False
    return next_round > max_rounds

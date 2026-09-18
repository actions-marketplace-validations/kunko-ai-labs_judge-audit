"""Pluggable judge interface. Anything that maps (state, questions) -> judgments fits."""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class QuestionType(str, Enum):
    CHOICE = "choice"   # pick one of options
    SCORE = "score"     # rate against ordered levels
    NOUL = "noul"       # probability a yes/no claim is true


@dataclass
class Question:
    name: str
    type: QuestionType
    instructions: str
    options: list[str] = field(default_factory=list)  # for CHOICE


@dataclass
class Judgment:
    question: str
    decision: str        # the chosen option / level / "true"/"false"
    confidence: float    # 0..1 — the number we're here to audit
    latency_s: float = 0.0
    cost_usd: float = 0.0
    raw: dict = field(default_factory=dict)


class Judge:
    """Implement decide(); judge-audit handles the rest."""

    name: str = "judge"

    def decide(self, state: str, questions: list[Question]) -> list[Judgment]:
        raise NotImplementedError

"""Shadow-mode runner: judge every labeled row, record everything, automate nothing."""
from __future__ import annotations

import json
from dataclasses import dataclass, field

from .judges.base import Judge, Question, QuestionType
from .metrics.calibration import (
    accuracy_coverage, expected_calibration_error, reliability_bins,
    zero_error_coverage,
)


@dataclass
class AuditResult:
    judge: str
    n: int
    accuracy: float
    ece: float
    reliability: list[dict] = field(default_factory=list)
    curve: list[dict] = field(default_factory=list)
    zero_error: dict = field(default_factory=dict)
    total_cost_usd: float = 0.0
    p50_latency_s: float = 0.0
    p99_latency_s: float = 0.0

    def to_dict(self) -> dict:
        return {
            "judge": self.judge, "n": self.n, "accuracy": self.accuracy,
            "ece": self.ece, "reliability_bins": self.reliability,
            "accuracy_coverage": self.curve, "zero_error_coverage": self.zero_error,
            "total_cost_usd": round(self.total_cost_usd, 6),
            "p50_latency_s": round(self.p50_latency_s, 3),
            "p99_latency_s": round(self.p99_latency_s, 3),
        }


def _percentile(xs: list[float], p: float) -> float:
    if not xs:
        return 0.0
    s = sorted(xs)
    return s[min(int(p / 100 * len(s)), len(s) - 1)]


def run_audit(judge: Judge, rows: list[dict]) -> AuditResult:
    """rows: [{state, questions: [{name, type, instructions, options?}], labels: {name: expected}}]"""
    confidences: list[float] = []
    correct: list[bool] = []
    latencies: list[float] = []
    cost = 0.0
    hits = 0
    total = 0

    for row in rows:
        questions = [Question(name=q["name"],
                              type=QuestionType(q.get("type", "choice")),
                              instructions=q.get("instructions", ""),
                              options=q.get("options", []))
                     for q in row["questions"]]
        labels: dict = row.get("labels", {})
        for judgment in judge.decide(row["state"], questions):
            expected = labels.get(judgment.question)
            if expected is None:
                continue
            ok = str(judgment.decision).strip().lower() == str(expected).strip().lower()
            confidences.append(max(0.0, min(1.0, judgment.confidence)))
            correct.append(ok)
            latencies.append(judgment.latency_s)
            cost += judgment.cost_usd
            hits += ok
            total += 1

    return AuditResult(
        judge=judge.name, n=total,
        accuracy=round(hits / total, 4) if total else 0.0,
        ece=round(expected_calibration_error(confidences, correct), 4),
        reliability=reliability_bins(confidences, correct),
        curve=accuracy_coverage(confidences, correct),
        zero_error=zero_error_coverage(confidences, correct),
        total_cost_usd=cost,
        p50_latency_s=_percentile(latencies, 50),
        p99_latency_s=_percentile(latencies, 99),
    )


def load_jsonl(path: str) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]

"""TypeSafe Jev judge adapter. API-only; key never leaves your machine."""
from __future__ import annotations

import json
import os
import time
import urllib.request

from .base import Judge, Judgment, Question, QuestionType

ENDPOINT = "https://api.typesafe.ai/v1/systemone"
INPUT_PRICE_PER_MTOK = 0.042  # USD, per TypeSafe's published pricing


class JevJudge(Judge):
    name = "jev"

    def __init__(self, api_key: str | None = None, model: str = "jev-latest",
                 base_url: str = ENDPOINT):
        self.api_key = api_key or os.environ.get("TYPESAFE_API_KEY", "")
        if not self.api_key:
            raise RuntimeError("Set TYPESAFE_API_KEY (waitlist: https://typesafe.ai)")
        self.model = model
        self.base_url = base_url

    def decide(self, state: str, questions: list[Question]) -> list[Judgment]:
        payload = {
            "model": self.model,
            "state": state,
            "questions": {
                q.name: {
                    "type": q.type.value,
                    "instructions": q.instructions,
                    **({"options": q.options} if q.options else {}),
                }
                for q in questions
            },
        }
        req = urllib.request.Request(
            self.base_url,
            data=json.dumps(payload).encode(),
            headers={"Authorization": f"Bearer {self.api_key}",
                     "Content-Type": "application/json"},
        )
        t0 = time.monotonic()
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = json.load(resp)
        latency = time.monotonic() - t0

        out: list[Judgment] = []
        for q in questions:
            ans = body.get(q.name, {})
            decision, confidence = self._parse(q, ans)
            # Cost estimate from input tokens; output is unmetered ("too cheap to meter").
            in_tok = body.get("usage", {}).get("input_tokens", 0)
            out.append(Judgment(
                question=q.name, decision=decision, confidence=confidence,
                latency_s=latency / max(len(questions), 1),
                cost_usd=in_tok / 1e6 * INPUT_PRICE_PER_MTOK,
                raw=ans,
            ))
        return out

    @staticmethod
    def _parse(q: Question, ans: dict) -> tuple[str, float]:
        if q.type is QuestionType.NOUL:
            p = float(ans.get("noul", 0.5))
            return ("true" if p >= 0.5 else "false"), max(p, 1 - p)
        if q.type is QuestionType.CHOICE:
            probs = ans.get("probabilities", {}) or {}
            best = max(probs, key=lambda k: probs[k]) if probs else ""
            return best, float(ans.get("confidence", probs.get(best, 0.0) if best else 0.0))
        # SCORE
        return str(ans.get("score", ans.get("level", ""))), float(ans.get("confidence", 0.5))

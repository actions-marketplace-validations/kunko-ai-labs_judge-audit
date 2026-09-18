# judge-audit

**Independent calibration audits for AI judges.** Moody's for AI judgment — not another wrapper.

Everyone is building *on* judgment models (TypeSafe's Jev, LLM-as-judge, guardrails). Nobody is *verifying* them. Vendors self-report "calibrated confidence"; production workloads need proof.

`judge-audit` runs any judge in **shadow mode** against human-labeled decisions and answers the only questions that matter before you automate:

- When it says 80% confident, is it right 80% of the time? (calibration)
- What share of work can I automate at zero observed errors? (accuracy-coverage)
- What does it really cost, and how bad is the latency tail? (cost/p99)
- Has calibration drifted since last week? (CI gate)

## Quickstart

```bash
pip install judge-audit
export TYPESAFE_API_KEY="sk-..."   # or plug in your own judge
judge-audit run examples/email-routing/labels.jsonl --judge jev --out report/
```

Produces `report.md`: reliability diagram data, ECE, accuracy-coverage curve, cost and latency percentiles, and a verdict.

## How it works

1. **Labeled dataset** — JSONL rows: `{state, questions, label}`. Your humans already made these decisions; the judge must reproduce them.
2. **Shadow run** — the judge scores every row. Nothing is automated; everything is recorded: decision, confidence, latency, tokens.
3. **Audit report** — calibration (ECE + reliability bins), selective prediction (accuracy at every coverage level), cost, latency tail.
4. **CI gate** — `judge-audit check --baseline baseline.json --max-ece-drift 0.02` fails the build when the judge degrades.

## Judge interface

Anything that maps `(state, questions) -> (decision, confidence)` plugs in:

```python
from judge_audit.judges.base import Judge, Question, Judgment

class MyJudge(Judge):
    def decide(self, state: str, questions: list[Question]) -> list[Judgment]:
        ...
```

Ships with `JevJudge` (TypeSafe API). LLM-as-judge adapters welcome as PRs.

## Why calibration, not accuracy

Accuracy tells you who wins a benchmark. Calibration tells you what you can automate safely. A 96% accurate judge whose errors cluster below 70% confidence (like Jev on a 1,565-email benchmark) lets you auto-route 85% of traffic with zero observed errors and send the rest to a human. An uncalibrated 98% judge can't tell you which 2% to doubt. **Audit the honesty, not the trophy.**

## Roadmap

- [ ] `Judge Arena` — public, continuously updated calibration leaderboard across judges
- [ ] AI Act evidence dossier export (logging / human oversight / accuracy evidence, adapted — not a certification)
- [ ] Production drift monitor — Datadog for judge calibration
- [ ] Spanish-language audit packs for regulated sectors (banca, seguros, legal)

## Status

Early scaffold. The architecture (pluggable judge, stdlib-only core) is the point — API keys and datasets are yours.

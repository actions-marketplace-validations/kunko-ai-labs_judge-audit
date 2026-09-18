"""Markdown audit report + CI drift gate."""
from __future__ import annotations

import json

from .runner import AuditResult


def render_markdown(result: AuditResult) -> str:
    d = result.to_dict()
    lines = [
        f"# Audit report — {d['judge']}",
        "",
        f"**n={d['n']}** · accuracy **{d['accuracy']:.1%}** · ECE **{d['ece']:.4f}**",
        f"· cost **${d['total_cost_usd']:.4f}** · p50 **{d['p50_latency_s']}s** · p99 **{d['p99_latency_s']}s**",
        "",
        "## Can I automate this?",
        "",
        f"Zero observed errors through the most confident **{d['zero_error_coverage']['coverage']:.1%}** "
        f"({d['zero_error_coverage']['n']} decisions, confidence ≥ {d['zero_error_coverage']['threshold']}).",
        "Retrospective on this dataset — not a production guarantee.",
        "",
        "## Accuracy vs coverage",
        "",
        "| coverage | accuracy | min confidence | n |",
        "|---|---|---|---|",
    ]
    for row in d["accuracy_coverage"][::4]:  # every 5%
        lines.append(f"| {row['coverage']:.0%} | {row['accuracy']:.1%} | "
                     f"{row['min_confidence']:.2f} | {row['n']} |")
    lines += ["", "## Calibration (reliability bins)", "",
              "| confidence bin | avg confidence | accuracy | n |",
              "|---|---|---|---|"]
    for b in d["reliability_bins"]:
        if b["n"]:
            lines.append(f"| {b['bin']} | {b['avg_confidence']:.3f} | "
                         f"{b['accuracy']:.1%} | {b['n']} |")
    lines += ["", "_A perfectly honest judge sits on the diagonal: "
                  "avg confidence == accuracy in every bin._"]
    return "\n".join(lines) + "\n"


def check_drift(current: AuditResult, baseline_path: str,
                max_ece_drift: float = 0.02, max_acc_drop: float = 0.01) -> list[str]:
    """CI gate: fail the build when the judge degrades vs baseline."""
    with open(baseline_path, encoding="utf-8") as f:
        base = json.load(f)
    failures = []
    ece_drift = current.ece - base.get("ece", current.ece)
    if ece_drift > max_ece_drift:
        failures.append(f"ECE drifted +{ece_drift:.4f} (>{max_ece_drift}): "
                        "the judge is less honest than baseline.")
    acc_drop = base.get("accuracy", current.accuracy) - current.accuracy
    if acc_drop > max_acc_drop:
        failures.append(f"Accuracy dropped {acc_drop:.2%} (>{max_acc_drop:.0%}).")
    return failures

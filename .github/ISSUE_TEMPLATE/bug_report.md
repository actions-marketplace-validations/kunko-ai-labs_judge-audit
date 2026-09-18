---
name: "🐛 Bug Report"
about: "A wrong metric, a crash, a fabricated confidence or an integration that does not behave as documented"
title: "[BUG] "
labels: ["type:bug", "priority:medium", "status:todo"]
assignees: ""
---

<!--
╔══════════════════════════════════════════════════════════════════════════════╗
║  🐛 BUG REPORT — how to use this template                                     ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Pipeline: Triage (Sev) → MRE (failing test) → Root cause → Fix + test →      ║
║            Review → Release → Lessons learned                                 ║
║                                                                               ║
║  1. Pick the severity with the decision tree below (first match, top-down)    ║
║  2. Apply labels: severity:sev0..sev3 and priority (Sev0→critical,            ║
║     Sev1→high, Sev2→medium, Sev3→low)                                         ║
║  3. Wrong metric? Fill the "Measurement" block — it is the evidence we need  ║
║  4. Security issue (key logged / secret committed / fabricated confidence    ║
║     presented as measured)? Do NOT file here — use the private advisory      ║
╚══════════════════════════════════════════════════════════════════════════════╝
-->

## 🔄 Remediation pipeline

> The assignee ticks these as the bug moves. Sev0/Sev1 require the root-cause block below before the PR.

- [ ] **1 · Triage** — severity and priority labels set
- [ ] **2 · MRE** — a failing test reproduces it (fixture under `examples/` if a dataset is involved)
- [ ] **3 · Root cause** — the function/line that is wrong, and why it was written that way
- [ ] **4 · Fix + test** — PR `fix(scope): [BUG] …` with the minimal change, test now green
- [ ] **5 · Review** — CI green, maintainer approval
- [ ] **6 · Release** — shipped in vX.Y.Z; release notes mention it
- [ ] **7 · Lessons learned** — one line in the PR: what would have caught this earlier

---

## 🐛 Description

<!-- What happens, in one paragraph. -->

---

## 🚨 Severity — decision tree

> Tick the **first** condition that applies, top-down. When in doubt, pick the more severe.

- [ ] **Sev0** — a metric is presented as measured while it was fabricated or guessed; an API key is logged, committed or sent anywhere but the judge's own endpoint
- [ ] **Sev1** — a metric computes the wrong value on valid input and corrupts a report; a crash on a valid dataset; a judge adapter silently drops questions
- [ ] **Sev2** — wrong bin, wrong percentile, malformed report format (MD/HTML/JSON); a CLI flag misbehaves
- [ ] **Sev3** — cosmetic: wording, ordering, docs mismatch

---

## 🧪 Reproduction

**Version / environment:** `judge-audit --version`, Python, OS

**Command(s):**

```bash

```

**Dataset** (attach or link the JSONL rows; redact anything personal):

```json

```

---

## 📏 Measurement (wrong-metric bugs)

| | |
|---|---|
| **Metric** | ECE / MCE / accuracy-coverage / zero-error coverage / cost / latency |
| **The tool said** | paste the report section |
| **It should have said** | with hand-computed values |
| **Function in question** | link the function in `src/judge_audit/metrics/` |

---

## ✅ Expected behaviour

---

## 🔍 Root cause (assignee; required for Sev0/Sev1)

<!-- Why 1 → Why 2 → Why 3 → … until a function, a default or a missing test. -->

- **Why 1:**
- **Why 2:**
- **Why 3:**
- **Fix:**
- **Test that would have caught it:**

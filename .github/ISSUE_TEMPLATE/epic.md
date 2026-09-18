---
name: "🎯 Epic"
about: "A capability made of several User Stories, with a product goal and a metric"
title: "[EP-XXX] Epic name"
labels: ["epic", "status:todo"]
assignees: ""
---

<!--
╔══════════════════════════════════════════════════════════════════════════════╗
║  🎯 EPIC — how to use this template                                           ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Use an Epic when:                                                            ║
║  ✅ the work spans several User Stories (> 1 week)                            ║
║  ✅ it adds or changes a capability of the product (a new judge adapter,      ║
║     a new metric, a new evidence format, a new distribution surface)          ║
║  ✅ it has a product goal a user would recognise, and a metric                ║
║                                                                               ║
║  Use a User Story instead when it is one scoped change (1–5 days).            ║
║                                                                               ║
║  Title: [EP-XXX] Name in English — XXX is the next free number               ║
╚══════════════════════════════════════════════════════════════════════════════╝
-->

# 🎯 EPIC: [Name]

## 🧭 Product block

| Field | Value |
|-------|-------|
| **Bet** | now (this release) / next / later / tech-health |
| **Persona** | Developer / Reviewer / CISO / Auditor |
| **Milestone** | vX.Y.0 |
| **Primary success metric** | e.g. *"sample report renders ECE + reliability + accuracy-coverage from 200 labeled rows"* — never "feature shipped" |
| **Guardrail metric** | what must NOT get worse — e.g. *"metrics stay deterministic"*, *"no API key ever logged"* |
| **Explicit out-of-scope** | what this epic will NOT build |

---

## 📝 Description

<!-- The problem, in the user's words. Why now. Link docs/landscape-brief.md if a positioning angle matters. -->

## 🎯 Goals

- [ ] Goal 1
- [ ] Goal 2

## 📖 User Stories

<!-- Create each with the User Story template; list them here as they are opened. -->

| ID | Title | Status |
|----|-------|--------|
| US-XXX-001 | | `status:todo` |
| US-XXX-002 | | `status:todo` |

## ✅ Epic acceptance

- [ ] All stories closed and released
- [ ] Success metric measured and recorded in the milestone notes
- [ ] Guardrail metric intact
- [ ] Docs updated (`README.md` only for first-time readers; detail in `docs/`)

## 🔗 Dependencies

- Depends on: #
- Blocks: #

## 🔐 House rules check

- [ ] Metrics stay deterministic — no LLM in the measurement
- [ ] No fabricated confidence anywhere in the pipeline
- [ ] API keys never logged or committed

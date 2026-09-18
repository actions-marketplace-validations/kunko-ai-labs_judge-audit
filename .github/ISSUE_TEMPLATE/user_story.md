---
name: "📖 User Story"
about: "One scoped change (1–5 days) with acceptance criteria and a Definition of Done"
title: "[US-XXX-YYY] Title in English"
labels: ["type:story", "priority:medium", "status:todo"]
assignees: ""
---

<!--
╔══════════════════════════════════════════════════════════════════════════════╗
║  📖 USER STORY — how to use this template                                     ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Title: [US-XXX-YYY] Title — XXX = Epic number, YYY = story number            ║
║  Stories without an Epic use EP-000 (backlog): [US-000-YYY]                   ║
║                                                                               ║
║  Labels to apply: type:story · priority:critical|high|medium|low             ║
║                   area:judge|runner|metrics|report|integration|docs|ci       ║
║                   good-first-issue if a newcomer can do it in one sitting     ║
║                                                                               ║
║  A story is done when the Definition of Done at the bottom is all ticked.    ║
╚══════════════════════════════════════════════════════════════════════════════╝
-->

## Story ID: US-XXX-YYY

| Field | Value |
|-------|-------|
| **Epic** | EP-XXX — name |
| **Priority** | Critical / High / Medium / Low |
| **Area** | Judge / Runner / Metrics / Report / Integration / Docs / CI |
| **Persona** | Developer / Reviewer / CISO / Auditor |
| **Estimate** | X days |
| **Milestone** | vX.Y.0 |

---

## 📖 User Story

**As a** [persona],
**I want** [capability],
**so that** [outcome I can see or prove].

---

## ✅ Acceptance Criteria

<!-- Given / When / Then. Each criterion maps to at least one test. -->

- [ ] **Given** … **when** … **then** …
- [ ] **Given** … **when** … **then** …

---

## 📋 Technical Notes

<!-- Files to touch, shape of the change, pointers to similar code. -->

- Entry point:
- Similar code:
- Fixture / example to add under `examples/`:

---

## 🔗 Dependencies

- Depends on: #
- Blocks: #

---

## 🔐 Security & house rules

- [ ] Metrics are deterministic — no LLM in the measurement
- [ ] A judge adapter never fabricates confidence; unknown confidence is reported, not invented
- [ ] API keys never logged, never committed; network only inside judge adapters
- [ ] Sample datasets contain no real personal data; simulated judges are labeled SIMULATED

---

## 📄 Documentation

- [ ] `docs/` updated if behavior, metrics or formats changed
- [ ] `README.md` only if a first-time reader needs it

---

## 🏁 Definition of Done

- [ ] Code + tests merged into `main` via PR titled `type(scope): [US-XXX-YYY] …`
- [ ] Fixture in `examples/` if a dataset, judge or report format was added
- [ ] `pytest -q` green on 3.10–3.12
- [ ] Docs updated per the list above
- [ ] Epic table updated (`status:done`)

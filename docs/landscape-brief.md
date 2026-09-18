# Brief: landscape de auditoría de jueces IA (18/09/2026)

Investigación para posicionar judge-audit. Fuentes con URL en cada sección.

## 1. La categoría está vacía

Hay jueces cada vez más baratos (Jev, Glider de Patronus, Luna de Galileo) y
plataformas que los usan (Galileo, Patronus AI, Braintrust, Arize Phoenix,
DeepEval, Ragas). **Ninguno audita la calibración del juez como producto.**
Todos evalúan aplicaciones *usando* jueces; nadie publica "¿es honesta la
confianza de tu juez?".

Analogía: hay laboratorios que venden termómetros, pero ninguna entidad que
verifique que los termómetros miden bien.

- Galileo: métricas y guardrails con modelos Luna propietarios (caja negra —
  no puedes auditar al auditor). Precios enterprise.
- Patronus: Lynx y Glider open-source (auditables), pero sin informes de calibración.
- Braintrust: agrega scores, no curvas de calibración; retención corta (30 días en Pro).
- DeepEval: framework open-source ideal sobre el que *construir* el módulo de
  calibración — no un competidor.

Fuentes: https://thenewstack.io/galileo-agent-control-open-source/ ·
https://siliconangle.com/2024/12/19/patronus-ai-releases-glider-small-high-performance-ai-evaluator-model-models/ ·
https://deepeval.com

## 2. Estándares de calibración

El "paquete mínimo creíble" de un informe de auditoría:
- **ECE** (Expected Calibration Error) — estándar de facto (Naeini et al. 2015,
  Guo et al. 2017). https://link.springer.com/article/10.1007/s10994-023-06336-7
- **Reliability diagrams** — precisión vs confianza por bin, diagonal = honestidad.
- **Curvas accuracy-coverage** (selective prediction) — qué % automatizo con qué error.
  Es lo que hizo el benchmark viral de nikhilmudholkar.
  https://x.com/nikhilmudholkar/status/2100604560335139083

Diferenciadores: **MCE** (Maximum Calibration Error, worst-case — lo que pregunta
un regulador) y **conformal prediction** (garantías de cobertura; línea de
investigación, no afirmarlo aún).

## 3. Lo que exige el AI Act (Reglamento UE 2024/1689)

Aplica a sistemas de alto riesgo (Anexo III: scoring crediticio, selección de
personal, seguros, justicia). Un juez IA en esos contextos cae dentro.
Entrada en vigor de los requisitos: **2 dic 2027** → ventana de ~15 meses para
ser el estándar de facto antes de que sea obligatorio.

- **Art. 12 (registro):** logs automáticos durante toda la vida útil del sistema.
  → Cada juicio debe emitir un "recibo": hash del input, decisión, confianza,
  umbral aplicado, timestamp, versión del modelo, si escaló a humano.
- **Art. 14 (vigilancia humana):** el supervisor debe entender capacidades y
  *limitaciones* del sistema y poder anular decisiones.
  → El informe de calibración es la evidencia: "a <70% de confianza falla la
  mitad de las veces, por eso el umbral de escalado está en X". Sin números,
  la vigilancia humana es teatro.
- **Art. 15 (precisión/robustez):** (3) las métricas de precisión "se declararán
  en las instrucciones de uso"; (2) la Comisión *fomentará el desarrollo de
  benchmarks y metodologías de medición*.
  → El Art. 15(2) es una invitación regulatoria explícita a construir esto.

El "evidence dossier" mínimo: (i) recibos por decisión, (ii) informe de
calibración que fundamente el umbral de escalado, (iii) métricas declaradas,
(iv) monitor de drift en producción, (v) doc técnica Art. 11/Anexo IV.
*(Interpretación a partir de los artículos — validación legal pendiente.)*

Fuentes: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14 ·
https://artificialintelligenceact.eu/article/15/

## 4. Leaderboards existentes (ninguno de calibración)

- JudgeBench (ICLR 2025): rankea jueces por accuracy — no calibración.
  https://arxiv.org/abs/2410.12784v2
- "Judge's Verdict" (2025): 54 jueces por correlación con humanos — no calibración.
  https://arxiv.org/pdf/2510.09738
- JudgeBiasBench / MM-JudgeBench: miden sesgos — no calibración.
- LMSYS Chatbot Arena: preferencia humana sobre modelos — no jueces.

**No existe ningún leaderboard público que rankee jueces por calibración.**
(Ausencia de evidencia, no evidencia de ausencia — re-verificar antes de
declararlo públicamente.)

## 5. Riesgos

- Si Galileo/Braintrust añaden "calibration reports", compiten por arriba.
  Defensa: open-source, portable (CI-first, sin lock-in de datos) y europeo
  (residencia UE, narrativa AI Act).
- Pendiente verificar: precios oficiales Galileo/Confident AI; conformal
  prediction como estándar; composición exacta del dossier (abogado).

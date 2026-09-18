# judge-audit — visión: el Moody's de los jueces IA

## La tesis en una frase

Cada vendor publica sus propios benchmarks. Ninguna empresa regulada puede
desplegar un juez basándose en la palabra del vendor. Alguien tiene que ser
la autoridad independiente que califica a los jueces. Ese alguien somos nosotros.

## Por qué ahora

- TypeSafe sale de stealth (15/09/2026, $40M) con la afirmación central de
  "confianza calibrada" vía RLCD. Afirmación estadística, testeable, sin
  verificación independiente.
- El benchmark manual de nikhilmudholkar (1.565 emails, 111k views) demuestra
  que la comunidad *quiere* auditorías independientes. Lo hizo a mano, una vez.
- LangChain ya integra Jev (`langchain-typesafe`, AutoModeMiddleware): el
  ecosistema de consumidores crece; el de verificadores está vacío.

## Las cuatro capas (de open-source a compañía)

### 1. Harness open-source (esto, ahora)
`judge-audit run` — shadow mode contra decisiones humanas etiquetadas.
Métricas: ECE, reliability bins, curva accuracy-coverage, zero-error coverage,
coste real, p99. CI gate anti-drift. Juez intercambiable (Jev hoy, cualquiera mañana).

### 2. Judge Arena — el leaderboard de la honestidad (distribución)
Ranking público y continuo de jueces por **calibración**, no por accuracy.
Los leaderboards son máquinas de distribución (Chatbot Arena lo demostró).
Cada participante aporta su dataset (opt-in, anonimizado) → el dataset agregado
se convierte en el moat. Tesis de la casa: el moat es distribución + data gravity.

### 3. Evidence dossier para AI Act (ingresos)
Las empresas europeas que despliegan jueces necesitan evidencia para:
Art. 12 (logging), Art. 14 (human oversight), Art. 15 (accuracy/robustness).
Vendemos el *dossier de evidencia* generado automáticamente, no una certificación.
Posicionamiento obligatorio: `adapted`, nunca "certificado/conforme".

### 4. Monitor continuo (recurrencia)
"Datadog para jueces": vigilancia de calibración en producción, alerta cuando
el drift supera el umbral, con el umbral de escalado a humano como producto.

## Cuña España/UE

Primer auditoría de jueces "AI Act-ready" en español. Sectores regulados
(banca, seguros, legal) *tienen* que demostrar oversight humano: no les vendemos
el juez, les vendemos la prueba de que su juez es de fiar. Jueces propios
especializados en español como fase 2 (idea 29 del backlog).

## Sinergia con Agent Assurance

- Agent Assurance = capa determinística (declared vs observed, bloquea).
- judge-audit = capa probabilística (¿es honesto el juez?, audita).
- Juntas: el stack europeo de "agent assurance" completo. Determinista donde se
  puede probar, probabilístico donde hay que medir.

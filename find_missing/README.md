# NKO find_missing

Consulta si una entidad con LEI tiene correspondencia de alta confianza en el registro mercantil nacional que su jurisdiccion declarada haria esperable (UK Companies House, ES BORME, FR SIRENE). Nunca afirma ilegalidad/fraude - solo 'sin correspondencia de alta confianza', con la regla de expectativa siempre en la respuesta. Nombres ambiguos devuelven candidates[] sin veredicto (Tarea 4a).

**Clase:** A

**Estado:** PASS (2026-09-01) — pasó el `commercial_filter_gate.py` (6 preguntas + ORGANIC_DISCOVERY). SIGNAL_EXPERIMENT en curso: v0 gratuito, mide demanda real antes de fijar precio.

**Las 7 preguntas del gate:**

| Pregunta | Respuesta |
|---|---|
| DEMAND | YES — adyacente probada (KYB self-service ~2 USD/consulta, decenas de proveedores) |
| DELTA | YES — regla de expectativa + matching + evidencia estructurada, no descargable suelto |
| RIGHTS | YES — GLEIF GREEN; registros nacionales en review (atribución obligatoria) |
| DISTRIBUTION | YES — FastAPI en vivo, openapi.json real, cliente PyPI preparado |
| REPEATABILITY | YES — coste marginal ~0, escala a cualquier entidad con LEI |
| NKO_ADVANTAGE | YES — ya construido y probado, coste de probarlo ~0 |
| ORGANIC_DISCOVERY | score 2 — canal real (PyPI/directorios de API/MCP), educación de cliente LOW |

**Coste por ejecucion:** 1-2 llamadas HTTP a api.gleif.org, <1s

**Fuentes:** [{"id": "global-gleif-lei-registry", "gate_verdict": "GREEN"}, {"id": "uk-companies-house/es-borme/fr-sirene", "gate_verdict": "review (atribucion obligatoria)"}]

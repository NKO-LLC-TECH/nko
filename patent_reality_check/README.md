# NKO Reality Check #001 — Patent legal state

Consulta el estado legal de una patente de EEUU tal como lo muestra Google Patents y lo cruza contra los avisos semanales reales del Official Gazette de la USPTO de caducidad por impago de tasas de mantenimiento (35 U.S.C. 41, 37 CFR 1.362(g)) - un hecho oficial primario, nunca una inferencia. Hallazgo real: en una muestra aleatoria n=50 sobre 179.840 caducidades reales confirmadas por la Gazette, Google Patents seguia mostrando 'Active' en 14/50 (28,0%, IC95% 17,5-41,7%) - caracterizado como una ventana de retraso de actualizacion de ~2-5 meses, no un fallo persistente (ver gazette_crosscheck_result.md para el detalle completo).

**Clase:** A

**Estado:** PASS_PUBLISHED — PUBLICAR YA. Los 20 casos ya convertidos a nko-patent-confidence-patch/1.0 (14 discrepancias + 6 contrastes correctos, doble evidencia Google+Gazette, basis=observed) son exactamente lo que necesito como demo publica.

**Coste por ejecucion:** 1 fetch HTTP real a patents.google.com por patente (~1-2s), busqueda en indice en memoria de 179.840 registros para el ground truth (<1ms)

**Fuentes:** [{"id": "USPTO Official Gazette (Notice of Expiration of Patents Due to Failure to Pay Maintenance Fee)", "gate_verdict": "GREEN, US Government Work - dominio publico"}, {"id": "Google Patents (legal status display, licenciado de IFI CLAIMS)", "gate_verdict": "review - fuente de terceros citada, nunca redistribuida como propia"}]

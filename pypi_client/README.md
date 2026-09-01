# nko

Cliente mínimo para **NKO find_missing v0** — consulta si una entidad con LEI tiene correspondencia de alta confianza en el registro mercantil nacional que su propia jurisdicción declarada haría esperable (UK Companies House, España BORME, Francia SIRENE).

```python
import nko

nko.find_missing("name", "Tesco PLC", jurisdiction="GB")
# {'entity_seen_in': [...], 'expected_in': [...], 'verdict': 'CONSISTENT', ...}
```

Nunca afirma ilegalidad, fraude o entidades ficticias — solo "sin correspondencia de alta confianza en `<registro>`", con la regla de expectativa (por qué debería aparecer ahí) siempre incluida en la respuesta.

v0, gratuito, límite 100 llamadas/mes por clave. Clave por email en https://nkodatalabs.com/find-missing.

Fuente: [api.gleif.org](https://www.gleif.org) (LEI global, sin autenticación) contrastado contra la regla de expectativa por país.

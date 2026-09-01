"""Cliente minimo para NKO find_missing v0. Publicado en PyPI el
2026-09-01 (v0.1.0) el mismo dia que se desplego la API real en
https://api.nkodatalabs.com - consigue una clave gratuita con
POST /v0/keys ({"email": "tu@email.com"}), 100 llamadas/mes."""
from __future__ import annotations

import httpx

DEFAULT_BASE_URL = "https://api.nkodatalabs.com"


def find_missing(
    identifier_type: str,
    identifier: str,
    jurisdiction: str | None = None,
    *,
    api_key: str | None = None,
    base_url: str = DEFAULT_BASE_URL,
) -> dict:
    """Consulta si una entidad con LEI tiene correspondencia de alta
    confianza en el registro mercantil nacional esperado.

    >>> import nko
    >>> nko.find_missing("name", "Tesco PLC", jurisdiction="GB")
    {'entity_seen_in': [...], 'verdict': 'CONSISTENT', ...}
    """
    headers = {"x-api-key": api_key} if api_key else {}
    payload = {"identifier_type": identifier_type, "identifier": identifier}
    if jurisdiction:
        payload["jurisdiction"] = jurisdiction
    resp = httpx.post(f"{base_url}/v0/find_missing", json=payload, headers=headers, timeout=20.0)
    resp.raise_for_status()
    return resp.json()

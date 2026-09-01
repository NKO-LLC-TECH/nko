"""Cliente minimo para NKO find_missing v0. Nombre de paquete 'nko'
verificado libre en PyPI el 2026-08-31 (API JSON -> 404 Not Found).
NO publicado todavia - requiere el token de PyPI del usuario."""
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

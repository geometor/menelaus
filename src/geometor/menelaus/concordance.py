"""Concordance and scholarly apparatus registry loader for ``geometor-menelaus``."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

__all__ = [
    "DEFAULT_RESOURCES_DIR",
    "load_apparatus_registries",
    "load_concordance",
    "load_sources_manifest",
]

DEFAULT_RESOURCES_DIR: Path = Path(__file__).resolve().parents[3] / "resources" / "sphaerica"


def _read_json(path: Path) -> Any:
    if not path.is_file():
        raise FileNotFoundError(f"Apparatus resource file not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def load_concordance(resources_dir: Path | None = None) -> list[dict[str, Any]]:
    """Load the cross-tradition proposition concordance (Halley 1758 / Maurolico / Björnbo / Euclid)."""
    base = resources_dir or DEFAULT_RESOURCES_DIR
    data = _read_json(base / "concordance.json")
    return list(data["entries"]) if isinstance(data, dict) and "entries" in data else list(data)


def load_sources_manifest(resources_dir: Path | None = None) -> dict[str, Any]:
    """Load the public-domain primary-source provenance manifest."""
    base = resources_dir or DEFAULT_RESOURCES_DIR
    return dict(_read_json(base / "sources_manifest.json"))


def load_apparatus_registries(resources_dir: Path | None = None) -> dict[str, dict[str, Any]]:
    """Load ``persons.json``, ``citations.json``, and ``glossary.json``."""
    base = resources_dir or DEFAULT_RESOURCES_DIR
    return {
        "persons": dict(_read_json(base / "persons.json")),
        "citations": dict(_read_json(base / "citations.json")),
        "glossary": dict(_read_json(base / "glossary.json")),
    }

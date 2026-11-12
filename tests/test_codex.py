"""Tests for Book Codex tracks, standalone .euclid-graphic SVGs, and public-domain apparatus."""

from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path

from geometor.menelaus.concordance import (
    load_apparatus_registries,
    load_concordance,
    load_sources_manifest,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCSRC = REPO_ROOT / "docsrc"
FIGURES_DIR = DOCSRC / "_static" / "figures"

EXPECTED_SVGS = [
    "menelaus-planar-parallel.svg",
    "menelaus-rational-trig.svg",
    "menelaus-external-bisectors.svg",
    "menelaus-desargues-axis.svg",
    "menelaus-pascal-hexagram.svg",
    "menelaus-monge-circles.svg",
    "spherical-excess-polar.svg",
    "spherical-menelaus-3d.svg",
    "spherical-cross-ratio-pencil.svg",
    "menelaus-ceva-trilinear-polar.svg",
]


def test_all_ten_euclid_graphic_svgs_valid() -> None:
    for name in EXPECTED_SVGS:
        svg_path = FIGURES_DIR / name
        assert svg_path.is_file(), f"Missing standalone SVG figure: {svg_path}"
        text = svg_path.read_text(encoding="utf-8")
        assert 'class="euclid-graphic"' in text
        assert "data-ref=" in text

        root = ET.fromstring(text)
        ns = {"svg": "http://www.w3.org/2000/svg"}
        assert root.find("svg:defs", ns) is not None
        elements = root.find("svg:g[@id='elements']", ns)
        assert elements is not None
        for group_id in ("graphics", "highlights", "points", "labels"):
            assert elements.find(f"svg:g[@id='{group_id}']", ns) is not None


def test_apparatus_registries_and_public_domain_compliance() -> None:
    manifest = load_sources_manifest()
    assert manifest

    concordance = load_concordance()
    assert len(concordance) >= 12

    regs = load_apparatus_registries()
    assert len(regs["persons"]) >= 20
    assert len(regs["citations"]) >= 15
    assert len(regs["glossary"]) >= 14

    # Enforce strict exclusion of modern copyrighted Menelaus editions (Krause 1936, Rashed/Papadopoulos)
    forbidden_tokens = ("krause", "rashed", "papadopoulos")
    for reg_name, reg_data in regs.items():
        serialized = str(reg_data).lower()
        for tok in forbidden_tokens:
            assert tok not in serialized, f"Forbidden modern reference {tok!r} found in {reg_name}"


def test_four_unit_book_codex_tracks_and_zero_embedded_py_file() -> None:
    for unit_num in (1, 2, 3, 4):
        unit_dir = DOCSRC / "sphaerica" / f"unit-{unit_num}"
        for track in ("en", "la", "summary", "notes"):
            rst_path = unit_dir / f"unit-{unit_num}-{track}.rst"
            assert rst_path.is_file(), f"Missing codex track file: {rst_path}"
            content = rst_path.read_text(encoding="utf-8")
            assert ":layout: book" in content
            assert f".. _unit-{unit_num}-{track}:" in content
            assert ".. py_file::" not in content

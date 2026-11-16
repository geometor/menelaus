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


def test_canonical_book_codex_tracks_and_zero_embedded_py_file() -> None:
    sphaerica_dir = DOCSRC / "sphaerica"

    # Abolished unit directories must not exist
    for unit_num in (1, 2, 3, 4):
        assert not (sphaerica_dir / f"unit-{unit_num}").exists(), f"Legacy unit-{unit_num} directory still exists!"

    # Verify canonical books
    expected_books = {
        "liber_i": [
            "praefatio",
            "definitiones",
            "prop_01",
            "prop_04_05",
            "prop_08_10",
            "prop_11",
            "prop_17",
        ],
        "liber_ii": [
            "prop_01",
            "prop_10",
            "prop_11_12",
        ],
        "liber_iii": [
            "prop_01",
            "scholion",
            "lemmata",
            "ptolemy_i_13",
            "prop_02_03",
            "prop_06",
            "prop_08",
            "prop_09",
            "prop_10",
            "prop_11_25",
        ],
    }

    for book_name, sections in expected_books.items():
        book_dir = sphaerica_dir / book_name
        assert book_dir.is_dir(), f"Missing book directory: {book_dir}"
        book_index = book_dir / "index.rst"
        assert book_index.is_file(), f"Missing book index: {book_index}"
        index_content = book_index.read_text(encoding="utf-8")
        assert ":layout: book" in index_content
        assert ":folio:" in index_content

        for sec in sections:
            sec_dir = book_dir / sec
            assert sec_dir.is_dir(), f"Missing section directory: {sec_dir}"
            for track_file in ("index.rst", "la.rst", "summary.rst", "notes.rst"):
                track_path = sec_dir / track_file
                assert track_path.is_file(), f"Missing atomic track file: {track_path}"
                content = track_path.read_text(encoding="utf-8")
                assert ":layout: book" in content
                assert ":folio:" in content
                assert ":tracks:" in content

    # Verify legacy anchors preserved on containers
    liber_i_content = (sphaerica_dir / "liber_i" / "index.rst").read_text(encoding="utf-8")
    assert ".. _unit-1-en:" in liber_i_content
    assert ".. _unit-1-la:" in liber_i_content

    liber_ii_content = (sphaerica_dir / "liber_ii" / "index.rst").read_text(encoding="utf-8")
    assert ".. _unit-2-en:" in liber_ii_content
    assert ".. _unit-2-la:" in liber_ii_content

    liber_iii_content = (sphaerica_dir / "liber_iii" / "index.rst").read_text(encoding="utf-8")
    assert ".. _unit-3-en:" in liber_iii_content
    assert ".. _unit-4-en:" in liber_iii_content

    # Strict zero .. py_file:: across docsrc
    for rst in DOCSRC.rglob("*.rst"):
        content = rst.read_text(encoding="utf-8")
        assert ".. py_file::" not in content, f"Forbidden .. py_file:: found in {rst}"

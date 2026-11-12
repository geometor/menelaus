"""Exact symbolic tests for projective Ceva–Menelaus duality and ETC trilinear polars."""

from __future__ import annotations

import pytest
import sympy as sp
import sympy.geometry as spg
from geometor.model import is_harmonic

from geometor.menelaus.duality_ceva import (
    construct_trilinear_polar,
    etc_trilinear_polar_catalogue,
    harmonic_conjugate_collinear,
    verify_projective_menelaus_ceva_duality,
)


def test_harmonic_conjugate_collinear() -> None:
    P, Q, R = spg.Point(0, 0), spg.Point(10, 0), spg.Point(4, 0)
    R_conj = harmonic_conjugate_collinear(P, Q, R)
    assert R_conj == spg.Point(-20, 0)
    assert is_harmonic(P, Q, R, R_conj)

    with pytest.raises(ValueError, match="Midpoint"):
        harmonic_conjugate_collinear(P, Q, spg.Point(5, 0))


def test_construct_trilinear_polar_exact() -> None:
    model, data = construct_trilinear_polar()
    for elem in model.keys():
        if isinstance(elem, spg.Point2D):
            assert not elem.x.has(sp.Float)
            assert not elem.y.has(sp.Float)

    assert data["ceva_ratios"]["signed_product"] == 1
    assert data["menelaus_report"].signed_product == -1
    assert data["menelaus_report"].collinear is True
    assert data["cross_ratios"] == {"BC": -1, "CA": -1, "AB": -1}


def test_projective_menelaus_ceva_duality() -> None:
    res = verify_projective_menelaus_ceva_duality()
    assert res["ceva_concurrency_det"] == 0
    assert res["menelaus_collinearity_det"] == 0
    assert res["ceva_barycentric_product"] == 1
    assert res["menelaus_barycentric_product"] == -1


def test_etc_trilinear_polar_catalogue() -> None:
    cat = etc_trilinear_polar_catalogue()
    assert set(cat.keys()) == {"X(1)", "X(2)", "X(4)", "X(7)"}

    assert cat["X(1)"]["perspector"] == spg.Point(1, 2)
    assert cat["X(1)"]["signed_product"] == -1
    # X(1) trilinear polar matches the external bisector axis traces (-21,0), (21,-21/2), (63/13,-84/13)
    assert cat["X(1)"]["menelaus_traces"][0] == spg.Point(-21, 0)

    assert cat["X(2)"]["ceva_product"] == 1
    assert cat["X(2)"]["parallel_medial_sides"] is True

    assert cat["X(4)"]["signed_product"] == -1
    assert cat["X(7)"]["signed_product"] == -1

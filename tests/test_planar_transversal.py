"""Exact symbolic tests for Planar Menelaus, Converse constructions, and Rational Trigonometry."""

from __future__ import annotations

import pytest
import sympy as sp
import sympy.geometry as spg
from geometor.model import ProofAssertionError

from geometor.menelaus.planar_transversal import (
    construct_desargues_axis,
    construct_external_bisector_axis,
    construct_menelaus_planar,
    construct_monge_exsimilicenters,
    construct_pascal_hexagram,
    menelaus_product,
    menelaus_rational_trig_invariants,
    signed_segment_ratio,
    verify_menelaus_converse,
    verify_planar_menelaus_universal,
)


def _assert_model_has_no_floats(model) -> None:
    for elem in model.keys():
        if isinstance(elem, spg.Point2D):
            assert not elem.x.has(sp.Float)
            assert not elem.y.has(sp.Float)


def test_construct_menelaus_planar_default() -> None:
    model, data = construct_menelaus_planar()
    _assert_model_has_no_floats(model)

    assert data["E"] == spg.Point(7, 2)
    assert data["H"] == spg.Point(sp.Rational(3, 2), 3)

    ratios = data["ratios"]
    assert ratios["AF_FB"] == sp.Rational(1, 2)
    assert ratios["BD_DC"] == sp.Integer(-4)
    assert ratios["CE_EA"] == sp.Rational(1, 2)
    assert ratios["signed_product"] == sp.Integer(-1)
    assert ratios["unsigned_product"] == sp.Integer(1)


def test_float_coordinates_rejected() -> None:
    with pytest.raises(TypeError, match="Floating-point"):
        construct_menelaus_planar(A_coords=(3.0, 6))
    with pytest.raises(TypeError, match="sp.Float"):
        construct_menelaus_planar(F_coords=(sp.Float("2.0"), 4))


def test_three_external_cuts_case() -> None:
    # Transversal x + y = -2 cuts all three sides externally!
    # A=(0,4), B=(0,0), C=(4,0) -> AB (x=0) at F=(0,-2), BC (y=0) at D=(-2,0), CA (x+y=4) parallel?
    # Use A=(0,6), B=(0,0), C=(4,0) and transversal x + 2y = -4:
    # F on AB(x=0): (0, -2); D on BC(y=0): (-4, 0)
    model, data = construct_menelaus_planar(
        A_coords=(0, 6),
        B_coords=(0, 0),
        C_coords=(4, 0),
        D_coords=(-4, 0),
        F_coords=(0, -2),
    )
    _assert_model_has_no_floats(model)
    ratios = data["ratios"]
    assert ratios["AF_FB"] < 0
    assert ratios["BD_DC"] < 0
    assert ratios["CE_EA"] < 0
    assert ratios["signed_product"] == sp.Integer(-1)


def test_universal_planar_menelaus_and_converse() -> None:
    res = verify_planar_menelaus_universal()
    assert res["identity_residual"] == 0
    assert res["signed_product"] == -1


def test_rational_trigonometry_invariants() -> None:
    model, data = construct_menelaus_planar()
    rt = menelaus_rational_trig_invariants(model, data)
    assert rt["Q_AF"] == 5
    assert rt["Q_FB"] == 20
    assert rt["Q_BD"] == 144
    assert rt["Q_DC"] == 9
    assert rt["Q_CE"] == 8
    assert rt["Q_EA"] == 32
    assert rt["quadrance_lhs"] == 5760
    assert rt["quadrance_rhs"] == 5760
    assert rt["quadrance_ratio"] == 1
    assert rt["spread_product"] == 1
    for val in rt.values():
        assert not sp.sympify(val).has(sp.Float)


def test_converse_rejects_non_collinear_traces() -> None:
    A, B, C = spg.Point(0, 6), spg.Point(0, 0), spg.Point(6, 0)
    # Midpoints have product (+1)*(+1)*(+1) == +1 != -1 (Ceva medial configuration)
    D, E, F = spg.Point(3, 0), spg.Point(3, 3), spg.Point(0, 3)
    assert menelaus_product(A, B, C, D, E, F)["signed_product"] == 1
    with pytest.raises(ProofAssertionError):
        verify_menelaus_converse(A, B, C, D, E, F)

    with pytest.raises(ValueError, match="not collinear"):
        signed_segment_ratio(A, B, spg.Point(1, 1))


def test_external_bisector_axis_converse() -> None:
    model, data = construct_external_bisector_axis()
    _assert_model_has_no_floats(model)
    assert data["I"] == spg.Point(1, 2)
    assert data["De"] == spg.Point(-21, 0)
    assert data["Ee"] == spg.Point(21, sp.Rational(-21, 2))
    assert data["Fe"] == spg.Point(sp.Rational(63, 13), sp.Rational(-84, 13))
    assert data["report"].signed_product == -1
    assert data["report"].collinear is True


def test_desargues_axis_converse() -> None:
    model, data = construct_desargues_axis()
    _assert_model_has_no_floats(model)
    assert data["report"].signed_product == -1
    assert data["report"].collinear is True
    for sub in data["sub_menelaus"].values():
        assert sub["signed_product"] == -1


def test_pascal_hexagram_converse() -> None:
    model, data = construct_pascal_hexagram()
    _assert_model_has_no_floats(model)
    assert data["L"] == spg.Point(sp.Rational(90, 13), sp.Rational(20, 13))
    assert data["M"] == spg.Point(sp.Rational(-4, 3), -6)
    assert data["N"] == spg.Point(sp.Rational(5, 2), sp.Rational(-5, 2))
    assert data["report"].signed_product == -1
    assert data["report"].collinear is True


def test_monge_exsimilicenters_converse() -> None:
    model, data = construct_monge_exsimilicenters()
    _assert_model_has_no_floats(model)
    assert data["report"].signed_product == -1
    for mix_rep in data["mixed_reports"]:
        assert mix_rep.signed_product == -1
        assert mix_rep.collinear is True

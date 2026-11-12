"""Exact symbolic tests for 3D unit-sphere geometry and Spherical Menelaus (*Sphaerica* I & III)."""

from __future__ import annotations

import pytest
import sympy as sp

from geometor.menelaus.spherical import (
    GreatCircle,
    SphericalPoint,
    SphericalTriangle,
    gnomonic_projection_menelaus,
    polar_triangle,
    spherical_excess_report,
    spherical_menelaus_default,
    spherical_orthocenter_menelaus,
    verify_spherical_cross_ratio_invariance,
    verify_spherical_menelaus_universal,
)


def test_spherical_point_validation_and_float_rejection() -> None:
    p = SphericalPoint(sp.Rational(3, 5), sp.Rational(4, 5), 0, label="P")
    assert p.x**2 + p.y**2 + p.z**2 == 1

    with pytest.raises(ValueError, match="unit sphere"):
        SphericalPoint(1, 1, 0)

    with pytest.raises(TypeError, match="Floating-point"):
        SphericalPoint(0.6, 0.8, 0)

    with pytest.raises(TypeError, match="sp.Float"):
        GreatCircle(sp.Float("1.0"), 0, 0)


def test_spherical_excess_and_law_of_sines() -> None:
    res_men = spherical_menelaus_default()
    exc = spherical_excess_report(res_men.triangle)
    assert exc["tan_half_excess"] == sp.Rational(1, 17)
    assert exc["excess_greater_than_zero"] is True
    assert not exc["tan_half_excess"].has(sp.Float)

    # Tri-rectangular octant triangle: A=(1,0,0), B=(0,1,0), C=(0,0,1) -> excess E = pi/2, tan(E/2) = 1
    oct_tri = SphericalTriangle(
        SphericalPoint(1, 0, 0),
        SphericalPoint(0, 1, 0),
        SphericalPoint(0, 0, 1),
    )
    oct_exc = spherical_excess_report(oct_tri)
    assert oct_exc["tan_half_excess"] == 1
    assert oct_exc["excess_symbolic"] == sp.pi / 2


def test_polar_triangle_duality_and_aaa_congruence() -> None:
    tri = spherical_menelaus_default().triangle
    polar, info = polar_triangle(tri)
    assert info["aaa_uniquely_determines_sides"] is True
    assert sp.simplify(polar.side_cosines()["cos_a"] + tri.dihedral_cosines()["cos_A"]) == 0
    assert sp.simplify(polar.side_cosines()["cos_b"] + tri.dihedral_cosines()["cos_B"]) == 0
    assert sp.simplify(polar.side_cosines()["cos_c"] + tri.dihedral_cosines()["cos_C"]) == 0


def test_spherical_menelaus_sines_and_ptolemaic_chords() -> None:
    res = spherical_menelaus_default()
    assert res.sin_AF_FB == sp.Rational(5, 6)
    assert res.sin_BD_DC == sp.Rational(-18, 5)
    assert res.sin_CE_EA == sp.Rational(1, 3)
    assert res.signed_sine_product == sp.Integer(-1)
    assert res.unsigned_chord_product == sp.Integer(1)
    for coord in (res.D.x, res.D.y, res.D.z, res.E.x, res.F.x):
        assert not coord.has(sp.Float)


def test_gnomonic_projection_and_universal_3d_menelaus() -> None:
    res = spherical_menelaus_default()
    gnom = gnomonic_projection_menelaus(res)
    assert gnom["planar_signed_product"] == -1

    univ = verify_spherical_menelaus_universal()
    assert univ["universal_signed_product"] == -1


def test_spherical_cross_ratio_pencil_invariance() -> None:
    cr = verify_spherical_cross_ratio_invariance()
    assert cr["cross_ratio_g1"] == sp.Integer(-2)
    assert cr["cross_ratio_g2"] == sp.Integer(-2)
    assert cr["difference"] == 0
    assert cr["harmonic_cross_ratio_g1"] == sp.Integer(-1)
    assert cr["harmonic_cross_ratio_g2"] == sp.Integer(-1)


def test_spherical_orthocenter_concurrency() -> None:
    ortho = spherical_orthocenter_menelaus()
    H = ortho["orthocenter"]
    assert sp.simplify(H.x**2 + H.y**2 + H.z**2) == 1
    for alt in ortho["altitudes"]:
        assert alt.contains(H)
    assert ortho["spherical_ceva_product"] == 1

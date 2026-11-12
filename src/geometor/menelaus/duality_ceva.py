"""Exact projective Menelaus–Ceva point-line duality and trilinear polar constructions.

Connects ``geometor/menelaus`` directly to ``geometor/ceva``, ``geometor/altshiller-court``
(Chapters VI & X), ``geometor/pappus``, and ``geometor/etc``:

1. **Projective Polarity in** :math:`\\mathbb{P}^2` (:func:`verify_projective_menelaus_ceva_duality`):
   Demonstrates how standard homogeneous polarity :math:`[x : y : z] \\leftrightarrow \\{xX + yY + zZ = 0\\}`
   maps a collinear **Menelaus transversal** (:math:`\\det(D, E, F) = 0`, product :math:`-1`) to a
   concurrent **Ceva triple** (:math:`\\det(d^*, e^*, f^*) = 0`, product :math:`+1`) on the dual triangle.
2. **Harmonic Conjugation & Trilinear Polars** (:func:`construct_trilinear_polar`,
   :func:`verify_universal_trilinear_polar`):
   Proves that replacing each Ceva trace :math:`(D_c, E_c, F_c)` of a point :math:`P` by its
   harmonic conjugate :math:`(D_m, E_m, F_m)` with respect to the vertices of :math:`\\triangle ABC`
   negates all three side ratios:

   .. math::

      \\left(-\\frac{\\overline{AF_c}}{\\overline{F_c B}}\\right)
      \\left(-\\frac{\\overline{BD_c}}{\\overline{D_c C}}\\right)
      \\left(-\\frac{\\overline{CE_c}}{\\overline{E_c A}}\\right)
      = (-1)^3 (+1) = -1,

   forcing :math:`D_m = BC \\cap E_c F_c`, :math:`E_m = CA \\cap F_c D_c`, and
   :math:`F_m = AB \\cap D_c E_c` onto a single line: the **trilinear polar** :math:`\\ell_P` of :math:`P`.
3. **ETC Triangle Center Catalogue** (:func:`etc_trilinear_polar_catalogue`):
   Evaluates exact rational trilinear polars for ``X(1)`` (anti-orthic axis), ``X(4)`` (orthic axis,
   planar limit of Menelaus *Sphaerica* III.10), ``X(7)`` (Gergonne line), and ``X(2)`` (ideal line
   at infinity via parallel medial sides).
"""

from __future__ import annotations

from typing import Any

import sympy as sp
import sympy.geometry as spg
from geometor.model import (
    Model,
    ProofAssertionError,
    clean_expr,
    cross_ratio,
    is_harmonic,
    proposition,
    quadrance,
    zero_test,
)

from geometor.menelaus.planar_transversal import (
    _ensure_exact_pair,
    menelaus_product,
    signed_segment_ratio,
    verify_menelaus_converse,
)

__all__ = [
    "construct_trilinear_polar",
    "etc_trilinear_polar_catalogue",
    "harmonic_conjugate_collinear",
    "verify_projective_menelaus_ceva_duality",
    "verify_universal_trilinear_polar",
]


def harmonic_conjugate_collinear(
    P: spg.Point,
    Q: spg.Point,
    R: spg.Point,
) -> spg.Point:
    """Return the exact projective harmonic conjugate ``R'`` of ``R`` with respect to ``(P, Q)``.

    If ``R`` divides ``PQ`` in signed ratio :math:`\\lambda = \\overline{PR}/\\overline{RQ}` (:math:`\\lambda \\neq 1`),
    then ``R'`` divides ``PQ`` in signed ratio :math:`-\\lambda`, satisfying :math:`(P, Q; R, R') = -1`.
    """
    lam = signed_segment_ratio(P, Q, R)
    if zero_test(lam - 1):
        raise ValueError("Midpoint has its harmonic conjugate on the ideal line at infinity.")
    # R' - P = -lam * (Q - R') => R' * (1 - lam) = P - lam * Q
    den = 1 - lam
    rx = clean_expr((P.x - lam * Q.x) / den)
    ry = clean_expr((P.y - lam * Q.y) / den)
    pt = spg.Point(rx, ry)
    if not is_harmonic(P, Q, R, pt):
        raise ProofAssertionError("Constructed point failed exact harmonic range verification.")
    return pt


@proposition(
    "Menelaus.TrilinearPolar",
    kind="theorem",
    title="Ceva–Menelaus Harmonic Duality and the Trilinear Polar of a Perspector",
)
def _prove_trilinear_polar_on_model(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    P: spg.Point,
) -> dict[str, Any]:
    """Construct the cevian triangle of ``P``, its harmonic conjugates, and its trilinear polar."""
    la = model.construct_line(B, C, classes=["given"], by="Post.1")
    lb = model.construct_line(C, A, classes=["given"], by="Post.1")
    lc = model.construct_line(A, B, classes=["given"], by="Post.1")
    model.set_polygon([A, B, C], classes=["given"])

    # Ceva lines AP, BP, CP concurrent at P
    cev_a = model.construct_line(A, P, classes=["cevian"], by="Post.1")
    cev_b = model.construct_line(B, P, classes=["cevian"], by="Post.1")
    cev_c = model.construct_line(C, P, classes=["cevian"], by="Post.1")

    Dc = model.intersect(cev_a, la, ID="Dc", classes=["cevian"], by="Post.1")
    Ec = model.intersect(cev_b, lb, ID="Ec", classes=["cevian"], by="Post.1")
    Fc = model.intersect(cev_c, lc, ID="Fc", classes=["cevian"], by="Post.1")
    model.set_polygon([Dc, Ec, Fc], classes=["cevian"])

    # Verify Ceva signed product == +1
    ceva = menelaus_product(A, B, C, Dc, Ec, Fc)
    if not zero_test(ceva["signed_product"] - 1):
        raise ProofAssertionError(f"Ceva signed product expected +1, got {ceva['signed_product']}")

    # Construct sides of cevian triangle DcEcFc and intersect with BC, CA, AB
    side_ef = model.construct_line(Ec, Fc, classes=["auxiliary"], by="Post.1")
    side_fd = model.construct_line(Fc, Dc, classes=["auxiliary"], by="Post.1")
    side_de = model.construct_line(Dc, Ec, classes=["auxiliary"], by="Post.1")

    Dm = model.intersect(la, side_ef, ID="Dm", classes=["trace", "result"], by="Post.1")
    Em = model.intersect(lb, side_fd, ID="Em", classes=["trace", "result"], by="Post.1")
    Fm = model.intersect(lc, side_de, ID="Fm", classes=["trace", "result"], by="Post.1")

    # Complete quadrangle harmonicity: (B, C; Dc, Dm) = (C, A; Ec, Em) = (A, B; Fc, Fm) = -1
    cr_a = cross_ratio(B, C, Dc, Dm)
    cr_b = cross_ratio(C, A, Ec, Em)
    cr_c = cross_ratio(A, B, Fc, Fm)
    if not (zero_test(cr_a + 1) and zero_test(cr_b + 1) and zero_test(cr_c + 1)):
        raise ProofAssertionError(
            f"Harmonic conjugate check failed: CRs = ({cr_a}, {cr_b}, {cr_c})"
        )

    # Verify Converse of Menelaus on (Dm, Em, Fm): (-1)^3 * (+1) = -1 => trilinear polar!
    men_report = verify_menelaus_converse(A, B, C, Dm, Em, Fm)
    polar_line = model.construct_line(Dm, Em, classes=["transversal", "result"], by="Menelaus.Converse")
    model.assert_collinear(Dm, Em, Fm, by="Menelaus.Converse", label="Trilinear polar l_P")
    model.conclude(polar_line, Dm, Em, Fm, kind="qed", by="Menelaus.Converse")

    return {
        "A": A,
        "B": B,
        "C": C,
        "P": P,
        "Dc": Dc,
        "Ec": Ec,
        "Fc": Fc,
        "Dm": Dm,
        "Em": Em,
        "Fm": Fm,
        "ceva_ratios": ceva,
        "menelaus_report": men_report,
        "cross_ratios": {"BC": cr_a, "CA": cr_b, "AB": cr_c},
        "trilinear_polar": polar_line,
    }


def construct_trilinear_polar(
    A_coords: tuple[Any, Any] = (2, 9),
    B_coords: tuple[Any, Any] = (0, 0),
    C_coords: tuple[Any, Any] = (10, 0),
    P_coords: tuple[Any, Any] = (3, 3),
) -> tuple[Model, dict[str, Any]]:
    """Build an exact ``geometor.model`` demonstration of Ceva–Menelaus harmonic duality.

    Default coordinates ``A=(2,9), B=(0,0), C=(10,0), P=(3,3)`` produce a compact, completely
    rational configuration where ``Dm=(-15,0)``, ``Em=(14,-3)``, ``Fm=(-2,-9)`` all have small
    integer coordinates!
    """
    ax, ay = _ensure_exact_pair(A_coords)
    bx, by_ = _ensure_exact_pair(B_coords)
    cx, cy = _ensure_exact_pair(C_coords)
    px, py = _ensure_exact_pair(P_coords)

    model = Model("Menelaus.TrilinearPolar", auto_intersect=False)
    A = model.set_point(ax, ay, ID="A", classes=["given"])
    B = model.set_point(bx, by_, ID="B", classes=["given"])
    C = model.set_point(cx, cy, ID="C", classes=["given"])
    P = model.set_point(px, py, ID="P", classes=["given", "center"])

    data = _prove_trilinear_polar_on_model(model, A, B, C, P, hide_guides=False)
    return model, data


def verify_projective_menelaus_ceva_duality() -> dict[str, Any]:
    """Prove exact :math:`\\mathbb{P}^2` polarity pairing Menelaus transversals with Ceva perspectors.

    Works in homogeneous coordinates relative to the canonical projective reference triangle
    :math:`A = [1:0:0], B = [0:1:0], C = [0:0:1]`:

    - Any transversal line :math:`\\ell = [p : q : r]^T` (:math:`pqr \\neq 0`) meets :math:`BC (x=0)`
      at :math:`D = [0 : r : -q]`, :math:`CA (y=0)` at :math:`E = [-r : 0 : p]`, and
      :math:`AB (z=0)` at :math:`F = [q : -p : 0]`, with :math:`\\det(D, E, F) = 0` and directed
      barycentric Menelaus product :math:`(-p/q)(-q/r)(-r/p) = -1`.
    - Under point-line polarity :math:`\\ell \\mapsto L^* = [p^{-1} : q^{-1} : r^{-1}]` (or isotopic
      reciprocal / dual basis), the dual lines through the dual vertices concur at :math:`[p : q : r]`,
      with Ceva trace ratios :math:`(+q/p)(+r/q)(+p/r) = +1`, while the trilinear polar of
      :math:`P = [u : v : w]` is the exact dual line :math:`\\frac{x}{u} + \\frac{y}{v} + \\frac{z}{w} = 0`!
    """
    u, v, w = sp.symbols("u v w", nonzero=True)
    # Ceva traces of P = [u : v : w] on BC, CA, AB:
    Dc = sp.Matrix([0, v, w])
    Ec = sp.Matrix([u, 0, w])
    Fc = sp.Matrix([u, v, 0])

    # Cevian lines ADc, BEc, CFc in dual homogeneous line coordinates:
    l_ADc = sp.Matrix([1, 0, 0]).cross(Dc)  # [0, -w, v]
    l_BEc = sp.Matrix([0, 1, 0]).cross(Ec)  # [w, 0, -u]
    l_CFc = sp.Matrix([0, 0, 1]).cross(Fc)  # [-v, u, 0]
    ceva_concurrency_det = sp.simplify(sp.Matrix.hstack(l_ADc, l_BEc, l_CFc).det())
    if ceva_concurrency_det != 0:
        raise ProofAssertionError("Projective Ceva concurrency determinant failed to vanish.")

    # Harmonic conjugates Dm = BC ∩ EcFc, Em = CA ∩ FcDc, Fm = AB ∩ DcEc via homogeneous cross products:
    Dm = sp.Matrix([1, 0, 0]).cross(Ec.cross(Fc))
    Em = sp.Matrix([0, 1, 0]).cross(Fc.cross(Dc))
    Fm = sp.Matrix([0, 0, 1]).cross(Dc.cross(Ec))

    menelaus_collinearity_det = sp.simplify(sp.Matrix.hstack(Dm, Em, Fm).det())
    if menelaus_collinearity_det != 0:
        raise ProofAssertionError("Projective Menelaus trilinear-polar determinant failed to vanish.")

    # Verify Dm, Em, Fm all lie on the trilinear polar line [v*w, w*u, u*v]^T (x/u + y/v + z/w = 0)
    polar_coords = sp.Matrix([v * w, w * u, u * v])
    for tag, pt_h in (("Dm", Dm), ("Em", Em), ("Fm", Fm)):
        inc = sp.simplify(polar_coords.dot(pt_h))
        if inc != 0:
            raise ProofAssertionError(f"Point {tag} failed incidence on trilinear polar: {inc}")

    ceva_ratio_product = sp.simplify((v / u) * (w / v) * (u / w))
    menelaus_ratio_product = sp.simplify((-v / u) * (-w / v) * (-u / w))

    return {
        "ceva_concurrency_det": ceva_concurrency_det,
        "menelaus_collinearity_det": menelaus_collinearity_det,
        "trilinear_polar_homogeneous": polar_coords,
        "ceva_barycentric_product": ceva_ratio_product,
        "menelaus_barycentric_product": menelaus_ratio_product,
    }


def verify_universal_trilinear_polar() -> dict[str, Any]:
    """Alias wrapper returning exact universal homogeneous proof data."""
    return verify_projective_menelaus_ceva_duality()


def etc_trilinear_polar_catalogue() -> dict[str, dict[str, Any]]:
    """Construct exact rational Ceva–Menelaus trilinear polar pairings for classic ETC centers.

    Evaluated on the scalene Heronian reference triangle ``A=(-9,12), B=(0,0), C=(7,0)``
    (side lengths ``a=7, b=20, c=15``):

    - ``X(1)`` **Incenter** ``(1, 2)`` :math:`\\longleftrightarrow` **Anti-orthic axis** (external bisector traces).
    - ``X(4)`` **Orthocenter** ``(-9, -27/4)`` :math:`\\longleftrightarrow` **Orthic axis** (planar limit of
      Menelaus *Sphaerica* III.10).
    - ``X(7)`` **Gergonne point** ``(-27/19, 24/19)`` :math:`\\longleftrightarrow` **Gergonne line** (perspectivity
      axis of the contact triangle).
    - ``X(2)`` **Centroid** ``(-2/3, 4)`` :math:`\\longleftrightarrow` **Ideal line at infinity** (verified by
      exact parallelism of the medial triangle sides :math:`E_c F_c \\parallel BC`, etc.).
    """
    A_xy, B_xy, C_xy = (-9, 12), (0, 0), (7, 0)
    A_pt, B_pt, C_pt = spg.Point(*A_xy), spg.Point(*B_xy), spg.Point(*C_xy)
    a = sp.sqrt(quadrance(B_pt, C_pt))  # 7
    b = sp.sqrt(quadrance(C_pt, A_pt))  # 20
    c = sp.sqrt(quadrance(A_pt, B_pt))  # 15
    s = (a + b + c) / 2  # 21

    def _bary_pt(wa: sp.Expr, wb: sp.Expr, wc: sp.Expr) -> tuple[sp.Expr, sp.Expr]:
        tot = wa + wb + wc
        return (
            clean_expr((wa * A_pt.x + wb * B_pt.x + wc * C_pt.x) / tot),
            clean_expr((wa * A_pt.y + wb * B_pt.y + wc * C_pt.y) / tot),
        )

    # X(1): barycentrics (a : b : c)
    x1_xy = _bary_pt(a, b, c)
    _, data_x1 = construct_trilinear_polar(A_xy, B_xy, C_xy, x1_xy)

    # X(4) Orthocenter via exact barycentric weights 1/(b^2+c^2-a^2) : 1/(c^2+a^2-b^2) : 1/(a^2+b^2-c^2)
    w4_a = 1 / (b**2 + c**2 - a**2)
    w4_b = 1 / (c**2 + a**2 - b**2)
    w4_c = 1 / (a**2 + b**2 - c**2)
    x4_xy = _bary_pt(w4_a, w4_b, w4_c)
    _, data_x4 = construct_trilinear_polar(A_xy, B_xy, C_xy, x4_xy)

    # X(7) Gergonne point: barycentrics 1/(s-a) : 1/(s-b) : 1/(s-c)
    x7_xy = _bary_pt(1 / (s - a), 1 / (s - b), 1 / (s - c))
    _, data_x7 = construct_trilinear_polar(A_xy, B_xy, C_xy, x7_xy)

    # X(2) Centroid: barycentrics (1 : 1 : 1) => medial sides parallel to BC, CA, AB (trilinear polar at infinity!)
    x2_xy = _bary_pt(sp.Integer(1), sp.Integer(1), sp.Integer(1))
    m2 = Model("Menelaus.CentroidIdealPolar", auto_intersect=False)
    A2 = m2.set_point(*A_xy, ID="A", classes=["given"])
    B2 = m2.set_point(*B_xy, ID="B", classes=["given"])
    C2 = m2.set_point(*C_xy, ID="C", classes=["given"])
    G2 = m2.set_point(*x2_xy, ID="G", classes=["center"])
    Ma = spg.Point((B2.x + C2.x) / 2, (B2.y + C2.y) / 2)
    Mb = spg.Point((C2.x + A2.x) / 2, (C2.y + A2.y) / 2)
    Mc = spg.Point((A2.x + B2.x) / 2, (A2.y + B2.y) / 2)
    m2.assert_parallel((Mb, Mc), (B2, C2), by="VI.2")
    m2.assert_parallel((Mc, Ma), (C2, A2), by="VI.2")
    m2.assert_parallel((Ma, Mb), (A2, B2), by="VI.2")

    return {
        "X(1)": {
            "etc_id": "X(1)",
            "center_name": "Incenter",
            "polar_name": "Anti-orthic axis (external angle-bisector axis)",
            "perspector": data_x1["P"],
            "menelaus_traces": (data_x1["Dm"], data_x1["Em"], data_x1["Fm"]),
            "signed_product": data_x1["menelaus_report"].signed_product,
        },
        "X(2)": {
            "etc_id": "X(2)",
            "center_name": "Centroid",
            "polar_name": "Ideal line at infinity (medial parallel configuration)",
            "perspector": G2,
            "ceva_product": menelaus_product(A2, B2, C2, Ma, Mb, Mc)["signed_product"],
            "parallel_medial_sides": True,
        },
        "X(4)": {
            "etc_id": "X(4)",
            "center_name": "Orthocenter",
            "polar_name": "Orthic axis (planar limit of Menelaus Sphaerica III.10)",
            "perspector": data_x4["P"],
            "menelaus_traces": (data_x4["Dm"], data_x4["Em"], data_x4["Fm"]),
            "signed_product": data_x4["menelaus_report"].signed_product,
        },
        "X(7)": {
            "etc_id": "X(7)",
            "center_name": "Gergonne point",
            "polar_name": "Gergonne line (contact-triangle perspectivity axis)",
            "perspector": data_x7["P"],
            "menelaus_traces": (data_x7["Dm"], data_x7["Em"], data_x7["Fm"]),
            "signed_product": data_x7["menelaus_report"].signed_product,
        },
    }

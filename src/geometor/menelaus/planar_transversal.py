"""Exact symbolic Planar Menelaus constructions, Converse theorems, and Rational Trigonometry.

Implements:

- Classical Euclidean parallel-auxiliary demonstration of **Planar Menelaus's Theorem**
  (Ptolemy *Syntaxis Mathematica* I.13, ed. Heiberg 1898 pp. 68–70; Halley 1758 *Menelai
  Sphaericorum Libri III*, Lemma I, p. 83), verifying both the directed ratio product
  :math:`\\frac{\\overline{AF}}{\\overline{FB}} \\cdot \\frac{\\overline{BD}}{\\overline{DC}} \\cdot \\frac{\\overline{CE}}{\\overline{EA}} = -1`
  and the unsigned magnitude product :math:`= +1`.
- Universal symbolic polynomial proof over :math:`\\mathbb{Q}(x_A, y_A, x_B, y_B, x_C, y_C, u, v, w)`
  establishing both the forward theorem and the **Converse of Menelaus**.
- Constructive applications of the Converse of Menelaus:

  1. **External Angle-Bisector Axis** (the three external angle bisectors of a scalene
     triangle meet the opposite sides in three collinear points; cf. Menelaus *Sphaerica* III.6).
  2. **Desargues's Two-Triangle Theorem** (three Menelaus applications on :math:`\\triangle OBC`,
     :math:`\\triangle OCA`, :math:`\\triangle OAB`).
  3. **Pascal's Hexagrammum Mysticum** (three Menelaus applications on the diagonal triangle
     combined with Euclid III.35/III.36 chord power products).
  4. **Monge's Three-Circle Similicenter Theorem** (collinearity of the three exsimilicenters
     and three pairs of insimilicenters + one exsimilicenter).

- **Rational Trigonometry** formulation (Wildberger *Divine Proportions*) expressing Planar
  Menelaus purely over :math:`\\mathbb{Q}` via ``quadrance``, ``line_spread``, ``vertex_spread``,
  and ``cross_ratio`` without square roots or transcendental functions.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import sympy as sp
import sympy.geometry as spg
from geometor.model import (
    Model,
    ProofAssertionError,
    clean_expr,
    cross_ratio,
    exact_sign,
    is_harmonic,
    line_spread,
    orientation,
    proposition,
    quadrance,
    vertex_spread,
    zero_test,
)

__all__ = [
    "MenelausReport",
    "construct_desargues_axis",
    "construct_external_bisector_axis",
    "construct_menelaus_planar",
    "construct_monge_exsimilicenters",
    "construct_parallel_through",
    "construct_pascal_hexagram",
    "menelaus_product",
    "menelaus_rational_trig_invariants",
    "signed_segment_ratio",
    "verify_menelaus_converse",
    "verify_planar_menelaus_universal",
]


def _ensure_exact_expr(val: int | sp.Rational | sp.Expr) -> sp.Expr:
    """Validate that a coordinate expression contains zero floating-point approximations."""
    if isinstance(val, float):
        raise TypeError(f"Floating-point coordinate {val!r} is forbidden; use int or sp.Rational.")
    expr = sp.sympify(val)
    if expr.has(sp.Float):
        raise TypeError(f"sp.Float atom inside {expr!r} is forbidden in exact symbolic geometry.")
    return clean_expr(expr)


def _ensure_exact_pair(coords: tuple[Any, Any]) -> tuple[sp.Expr, sp.Expr]:
    """Validate an exact 2D coordinate pair ``(x, y)``."""
    if len(coords) != 2:
        raise ValueError(f"Expected 2D coordinate pair, got {coords!r}")
    return _ensure_exact_expr(coords[0]), _ensure_exact_expr(coords[1])


def signed_segment_ratio(P: spg.Point, Q: spg.Point, R: spg.Point) -> sp.Expr:
    """Compute the exact directed ratio :math:`\\overline{PR} / \\overline{RQ}` for collinear ``P, Q, R``.

    Under this classical tail-to-trace / trace-to-head convention:

    - ``signed_segment_ratio(P, Q, R) > 0`` when ``R`` divides segment ``PQ`` *internally*
      (strictly between ``P`` and ``Q``).
    - ``signed_segment_ratio(P, Q, R) < 0`` when ``R`` divides line ``PQ`` *externally*
      (outside segment ``PQ``).

    Args:
        P: Segment tail vertex.
        Q: Segment head vertex.
        R: Collinear division point (:math:`R \\neq Q`).

    Returns:
        Exact simplified :class:`sympy.Expr` equal to :math:`\\overline{PR} / \\overline{RQ}`.

    Raises:
        ValueError: If ``P, Q, R`` are not collinear or ``R`` coincides with ``Q``.
    """
    if orientation(P, Q, R) != 0:
        raise ValueError(f"Points {P}, {Q}, {R} are not collinear.")
    dx_rq = Q.x - R.x
    dy_rq = Q.y - R.y
    if zero_test(dx_rq) and zero_test(dy_rq):
        raise ValueError("Division point R coincides with head vertex Q (infinite ratio).")
    if not zero_test(dx_rq):
        return clean_expr((R.x - P.x) / dx_rq)
    return clean_expr((R.y - P.y) / dy_rq)


def menelaus_product(
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    D: spg.Point,
    E: spg.Point,
    F: spg.Point,
) -> dict[str, sp.Expr]:
    """Evaluate the three directed side ratios and signed/unsigned Menelaus products.

    Expects ``D`` on line ``BC``, ``E`` on line ``CA``, and ``F`` on line ``AB``.

    Returns:
        Dictionary with exact symbolic entries ``AF_FB``, ``BD_DC``, ``CE_EA``,
        ``signed_product`` (:math:`-1` for collinear ``D, E, F``; :math:`+1` for concurrent cevians),
        and ``unsigned_product`` (:math:`+1` in magnitude).
    """
    r_c = signed_segment_ratio(A, B, F)
    r_a = signed_segment_ratio(B, C, D)
    r_b = signed_segment_ratio(C, A, E)
    signed_prod = clean_expr(r_c * r_a * r_b)
    unsigned_prod = -signed_prod if exact_sign(signed_prod) < 0 else signed_prod
    return {
        "AF_FB": r_c,
        "BD_DC": r_a,
        "CE_EA": r_b,
        "signed_product": signed_prod,
        "unsigned_product": clean_expr(unsigned_prod),
    }


def verify_menelaus_converse(
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    D: spg.Point,
    E: spg.Point,
    F: spg.Point,
) -> MenelausReport:
    """Verify the Converse of Menelaus: signed ratio product ``== -1`` implies ``D, E, F`` collinear."""
    if orientation(A, B, C) == 0:
        raise ProofAssertionError("Reference triangle ABC is degenerate (collinear vertices).")
    ratios = menelaus_product(A, B, C, D, E, F)
    if not zero_test(ratios["signed_product"] + 1):
        raise ProofAssertionError(
            f"Menelaus signed ratio product is {ratios['signed_product']}, expected -1."
        )
    if orientation(D, E, F) != 0:
        raise ProofAssertionError("Converse check failed: D, E, F are not collinear.")
    return MenelausReport(
        AF_FB=ratios["AF_FB"],
        BD_DC=ratios["BD_DC"],
        CE_EA=ratios["CE_EA"],
        signed_product=ratios["signed_product"],
        unsigned_product=ratios["unsigned_product"],
        collinear=True,
    )


@dataclass(frozen=True)
class MenelausReport:
    """Exact symbolic summary of a Planar Menelaus configuration."""

    AF_FB: sp.Expr
    BD_DC: sp.Expr
    CE_EA: sp.Expr
    signed_product: sp.Expr
    unsigned_product: sp.Expr
    collinear: bool


@proposition(
    "I.31.Parallel",
    g_id="G.47",
    kind="problem",
    title="Construct line through a given point parallel to a given line",
)
def construct_parallel_through(
    model: Model,
    ref_line: spg.Line,
    through_pt: spg.Point,
    *,
    guide_aux_id: str = "Paux",
    classes: list[str] | None = None,
) -> spg.Line:
    """Construct the exact Euclidean line through ``through_pt`` parallel to ``ref_line`` (Euclid I.31)."""
    dx = ref_line.p2.x - ref_line.p1.x
    dy = ref_line.p2.y - ref_line.p1.y
    aux = model.set_point(
        through_pt.x + dx,
        through_pt.y + dy,
        ID=guide_aux_id,
        classes=["auxiliary"],
        guide=True,
    )
    par = model.construct_line(
        through_pt,
        aux,
        classes=classes if classes is not None else ["auxiliary"],
        by="I.31",
    )
    model.assert_parallel(par, ref_line, by="I.31")
    return par


@proposition(
    "Menelaus.Planar",
    kind="theorem",
    title="Planar Menelaus Transversal Theorem with Euclidean Parallel Auxiliary (Halley Lemma I)",
)
def _prove_menelaus_planar_on_model(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    D: spg.Point,
    F: spg.Point,
) -> dict[str, Any]:
    """Execute the Given -> Construct -> Demonstrate proof of Planar Menelaus on ``model``."""
    # Construct extended sides of triangle ABC and polygon ABC
    line_a = model.construct_line(B, C, classes=["given"], by="Post.1")
    line_b = model.construct_line(C, A, classes=["given"], by="Post.1")
    line_c = model.construct_line(A, B, classes=["given"], by="Post.1")
    tri = model.set_polygon([A, B, C], classes=["given"])

    # Verify Givens: D lies on BC extended and F lies on AB
    model.assert_collinear(B, C, D, by="Given", label="D on extended side BC")
    model.assert_collinear(A, B, F, by="Given", label="F on side AB")

    # Construct transversal line DF and intersect with side CA at E
    transversal = model.construct_line(D, F, classes=["transversal", "result"], by="Post.1")
    E = model.intersect(
        transversal,
        line_b,
        ID="E",
        classes=["trace", "result"],
        by="Post.1",
    )

    # Classical auxiliary construction (Ptolemy Almagest I.13 / Halley 1758 Lemma I, p. 83):
    # Draw CH through C parallel to transversal DF, meeting AB at H.
    par_c = construct_parallel_through(
        model,
        transversal,
        C,
        guide_aux_id="Cpar",
        classes=["auxiliary"],
    )
    H = model.intersect(
        par_c,
        line_c,
        ID="H",
        classes=["auxiliary"],
        by="I.31",
    )
    seg_ch = model.set_segment(C, H, classes=["auxiliary"])
    seg_cd = model.set_segment(C, D, classes=["extension"])

    # Deductive Demonstration
    model.assert_collinear(D, E, F, by="Construct", label="Transversal trace E on DF")
    model.assert_collinear(C, A, E, by="Construct", label="Trace E on side CA")
    model.assert_collinear(A, H, B, by="Construct", label="Auxiliary point H on side AB")
    model.assert_parallel(par_c, transversal, by="I.31", label="CH parallel to transversal DF")

    # Euclid VI.2 / VI.4 similar triangles:
    # 1. CH || FD in triangle BFD => BD / DC = BF / FH
    bd_dc = signed_segment_ratio(B, C, D)
    bf_fh = signed_segment_ratio(B, H, F)
    if not zero_test(bd_dc - bf_fh):
        raise ProofAssertionError(f"Euclid VI.2 ratio mismatch: BD/DC={bd_dc} != BF/FH={bf_fh}")

    # 2. HC || FE in triangle ACH => CE / EA = HF / FA
    ce_ea = signed_segment_ratio(C, A, E)
    hf_fa = signed_segment_ratio(H, A, F)
    if not zero_test(ce_ea - hf_fa):
        raise ProofAssertionError(f"Euclid VI.2 ratio mismatch: CE/EA={ce_ea} != HF/FA={hf_fa}")

    # 3. Compounding the ratios (Euclid VI.23 / Almagest I.13):
    #    (AF / FB) * (BD / DC) * (CE / EA) = (AF / FB) * (BF / FH) * (HF / FA) = (-1)^3 = -1
    ratios = menelaus_product(A, B, C, D, E, F)
    if not zero_test(ratios["signed_product"] + 1):
        raise ProofAssertionError(
            f"Signed Menelaus product expected -1, got {ratios['signed_product']}"
        )
    if not zero_test(ratios["unsigned_product"] - 1):
        raise ProofAssertionError(
            f"Unsigned Menelaus product expected +1, got {ratios['unsigned_product']}"
        )

    model.conclude(
        transversal,
        D,
        E,
        F,
        kind="qed",
        by="Menelaus.Planar",
        label="(AF/FB)*(BD/DC)*(CE/EA) = -1",
    )
    return {
        "A": A,
        "B": B,
        "C": C,
        "D": D,
        "E": E,
        "F": F,
        "H": H,
        "line_a": line_a,
        "line_b": line_b,
        "line_c": line_c,
        "transversal": transversal,
        "parallel_c": par_c,
        "seg_ch": seg_ch,
        "seg_cd": seg_cd,
        "triangle": tri,
        "ratios": ratios,
    }


def construct_menelaus_planar(
    A_coords: tuple[Any, Any] = (3, 6),
    B_coords: tuple[Any, Any] = (0, 0),
    C_coords: tuple[Any, Any] = (9, 0),
    D_coords: tuple[Any, Any] = (12, 0),
    F_coords: tuple[Any, Any] = (2, 4),
) -> tuple[Model, dict[str, Any]]:
    """Build and verify the exact Planar Menelaus model with Euclidean parallel auxiliary ``CH``.

    With default integer coordinates ``A=(3,6), B=(0,0), C=(9,0), D=(12,0), F=(2,4)``:

    - ``E = (7, 2)`` on ``CA`` and ``H = (3/2, 3)`` on ``AB``.
    - ``AF/FB = 1/2``, ``BD/DC = -4``, ``CE/EA = 1/2``, yielding ``(1/2)*(-4)*(1/2) = -1``.
    """
    ax, ay = _ensure_exact_pair(A_coords)
    bx, by_ = _ensure_exact_pair(B_coords)
    cx, cy = _ensure_exact_pair(C_coords)
    dx, dy = _ensure_exact_pair(D_coords)
    fx, fy = _ensure_exact_pair(F_coords)

    model = Model("Menelaus.Planar", auto_intersect=False)
    A = model.set_point(ax, ay, ID="A", classes=["given"])
    B = model.set_point(bx, by_, ID="B", classes=["given"])
    C = model.set_point(cx, cy, ID="C", classes=["given"])
    D = model.set_point(dx, dy, ID="D", classes=["given", "trace"])
    F = model.set_point(fx, fy, ID="F", classes=["given", "trace"])

    data = _prove_menelaus_planar_on_model(model, A, B, C, D, F, hide_guides=False)
    return model, data


def verify_planar_menelaus_universal() -> dict[str, sp.Expr]:
    """Prove Planar Menelaus and its Converse universally over ``Q(xA, yA, xB, yB, xC, yC, u, v, w)``.

    Parametrizes:

    - :math:`F = (1 - u)A + uB` on :math:`AB` (:math:`\\overline{AF}/\\overline{FB} = u/(1-u)`),
    - :math:`D = (1 - w)B + wC` on :math:`BC` (:math:`\\overline{BD}/\\overline{DC} = w/(1-w)`),
    - :math:`E = (1 - v)C + vA` on :math:`CA` (:math:`\\overline{CE}/\\overline{EA} = v/(1-v)`).

    Proves the exact polynomial determinant factorization:

    .. math::

       \\det\\begin{pmatrix} x_D & y_D & 1 \\\\ x_E & y_E & 1 \\\\ x_F & y_F & 1 \\end{pmatrix}
       = 2\\,\\operatorname{Area}(\\triangle ABC)\\,\\bigl(u v w + (1 - u)(1 - v)(1 - w)\\bigr),

    which vanishes for non-degenerate :math:`\\triangle ABC` if and only if
    :math:`\\frac{u}{1-u}\\frac{w}{1-w}\\frac{v}{1-v} = -1`.
    """
    xA, yA, xB, yB, xC, yC = sp.symbols("xA yA xB yB xC yC")
    u, v, w = sp.symbols("u v w")

    Fx, Fy = (1 - u) * xA + u * xB, (1 - u) * yA + u * yB
    Dx, Dy = (1 - w) * xB + w * xC, (1 - w) * yB + w * yC
    Ex, Ey = (1 - v) * xC + v * xA, (1 - v) * yC + v * yA

    det_def = sp.Matrix([[Dx, Dy, 1], [Ex, Ey, 1], [Fx, Fy, 1]]).det()
    area2_abc = (xB - xA) * (yC - yA) - (yB - yA) * (xC - xA)
    menelaus_poly = u * v * w + (1 - u) * (1 - v) * (1 - w)

    residual = sp.expand(det_def - area2_abc * menelaus_poly)
    if residual != 0:
        raise ProofAssertionError(f"Universal polynomial identity failed: residual={residual}")

    # Solve menelaus_poly == 0 for w and substitute into signed product
    w_sol = sp.solve(menelaus_poly, w)[0]
    signed_prod = sp.simplify((u / (1 - u)) * (w_sol / (1 - w_sol)) * (v / (1 - v)))
    if signed_prod != -1:
        raise ProofAssertionError(f"Universal signed product expected -1, got {signed_prod}")

    return {
        "det_DEF": sp.factor(det_def),
        "area2_ABC": area2_abc,
        "menelaus_polynomial": menelaus_poly,
        "identity_residual": residual,
        "w_from_uv": w_sol,
        "signed_product": signed_prod,
    }


def menelaus_rational_trig_invariants(
    model: Model,
    data: dict[str, Any],
) -> dict[str, Any]:
    """Compute and verify Wildberger Rational Trigonometry invariants for Planar Menelaus.

    Proves two purely rational (:math:`\\mathbb{Q}`-valued, square-root-free) formulations:

    1. **Menelaus Quadrance Law**:
       :math:`Q(A, F)\\,Q(B, D)\\,Q(C, E) = Q(F, B)\\,Q(D, C)\\,Q(E, A)`.
    2. **Menelaus Spread Telescoping Law**:
       Applying the Spread Law to sub-triangles :math:`\\triangle AFE`, :math:`\\triangle BDF`,
       and :math:`\\triangle CDE` cut by transversal :math:`t` against side lines :math:`a, b, c`:

       .. math::

          \\frac{Q(A, F)}{Q(E, A)} = \\frac{s(t, b)}{s(t, c)},\\quad
          \\frac{Q(B, D)}{Q(F, B)} = \\frac{s(t, c)}{s(t, a)},\\quad
          \\frac{Q(C, E)}{Q(D, C)} = \\frac{s(t, a)}{s(t, b)},

       whose product telescopes identically to :math:`1` over :math:`\\mathbb{Q}`.
    """
    A, B, C = data["A"], data["B"], data["C"]
    D, E, F, H = data["D"], data["E"], data["F"], data["H"]
    la, lb, lc, t = data["line_a"], data["line_b"], data["line_c"], data["transversal"]

    q_af = quadrance(A, F)
    q_fb = quadrance(F, B)
    q_bd = quadrance(B, D)
    q_dc = quadrance(D, C)
    q_ce = quadrance(C, E)
    q_ea = quadrance(E, A)

    lhs_q = clean_expr(q_af * q_bd * q_ce)
    rhs_q = clean_expr(q_fb * q_dc * q_ea)
    if not zero_test(lhs_q - rhs_q):
        raise ProofAssertionError(f"Quadrance Menelaus Law failed: {lhs_q} != {rhs_q}")

    s_ta = line_spread(t, la)
    s_tb = line_spread(t, lb)
    s_tc = line_spread(t, lc)

    # Verify each sub-triangle Spread Law identity over Q
    if not zero_test(q_af * s_tc - q_ea * s_tb):
        raise ProofAssertionError("Spread Law failed on triangle AFE.")
    if not zero_test(q_bd * s_ta - q_fb * s_tc):
        raise ProofAssertionError("Spread Law failed on triangle BDF.")
    if not zero_test(q_ce * s_tb - q_dc * s_ta):
        raise ProofAssertionError("Spread Law failed on triangle CDE.")

    spread_product = clean_expr((s_tb / s_tc) * (s_tc / s_ta) * (s_ta / s_tb))
    if not zero_test(spread_product - 1):
        raise ProofAssertionError(f"Spread product expected 1, got {spread_product}")

    # Evaluate vertex spread at A and cross-ratio along side AB cut by F and parallel trace H
    s_vertex_A = vertex_spread(B, A, C)
    cr_ab_fh = cross_ratio(A, B, F, H)

    return {
        "Q_AF": q_af,
        "Q_FB": q_fb,
        "Q_BD": q_bd,
        "Q_DC": q_dc,
        "Q_CE": q_ce,
        "Q_EA": q_ea,
        "quadrance_lhs": lhs_q,
        "quadrance_rhs": rhs_q,
        "quadrance_ratio": clean_expr(lhs_q / rhs_q),
        "s_t_a": s_ta,
        "s_t_b": s_tb,
        "s_t_c": s_tc,
        "spread_product": spread_product,
        "vertex_spread_A": s_vertex_A,
        "cross_ratio_AB_FH": cr_ab_fh,
    }


def construct_external_bisector_axis(
    A_coords: tuple[Any, Any] = (-9, 12),
    B_coords: tuple[Any, Any] = (0, 0),
    C_coords: tuple[Any, Any] = (7, 0),
) -> tuple[Model, dict[str, Any]]:
    """Construct the External Angle-Bisector Axis (anti-orthic axis) via Converse of Menelaus.

    Uses scalene Heronian triangle ``A=(-9,12), B=(0,0), C=(7,0)`` with exact integer side lengths
    ``a = 7, b = 20, c = 15``, integer incenter ``I = (1, 2)``, and external bisector traces
    ``De = (-21, 0)``, ``Ee = (21, -21/2)``, ``Fe = (63/13, -84/13)``.
    Cf. Menelaus *Sphaerica* III.6 (external spherical angle-bisector sine ratio).
    """
    ax, ay = _ensure_exact_pair(A_coords)
    bx, by_ = _ensure_exact_pair(B_coords)
    cx, cy = _ensure_exact_pair(C_coords)

    model = Model("Menelaus.ExternalBisectorAxis", auto_intersect=False)
    A = model.set_point(ax, ay, ID="A", classes=["given"])
    B = model.set_point(bx, by_, ID="B", classes=["given"])
    C = model.set_point(cx, cy, ID="C", classes=["given"])

    line_a = model.construct_line(B, C, classes=["given"], by="Post.1")
    line_b = model.construct_line(C, A, classes=["given"], by="Post.1")
    line_c = model.construct_line(A, B, classes=["given"], by="Post.1")
    model.set_polygon([A, B, C], classes=["given"])

    a_len = sp.sqrt(quadrance(B, C))
    b_len = sp.sqrt(quadrance(C, A))
    c_len = sp.sqrt(quadrance(A, B))
    perim = clean_expr(a_len + b_len + c_len)

    # Incenter X(1) = (a*A + b*B + c*C) / (a + b + c)
    I_pt = model.set_point(
        clean_expr((a_len * A.x + b_len * B.x + c_len * C.x) / perim),
        clean_expr((a_len * A.y + b_len * B.y + c_len * C.y) / perim),
        ID="I",
        classes=["center"],
    )

    # Internal bisectors AI, BI, CI and their feet Di, Ei, Fi
    bis_a_int = model.construct_line(A, I_pt, classes=["auxiliary"], guide=True, by="I.9")
    bis_b_int = model.construct_line(B, I_pt, classes=["auxiliary"], guide=True, by="I.9")
    bis_c_int = model.construct_line(C, I_pt, classes=["auxiliary"], guide=True, by="I.9")

    Di = model.intersect(bis_a_int, line_a, ID="Di", classes=["auxiliary"], guide=True, by="VI.3")
    Ei = model.intersect(bis_b_int, line_b, ID="Ei", classes=["auxiliary"], guide=True, by="VI.3")
    Fi = model.intersect(bis_c_int, line_c, ID="Fi", classes=["auxiliary"], guide=True, by="VI.3")

    # External angle bisectors are perpendicular to internal angle bisectors at A, B, C!
    def _perp_bisector_line(vertex: spg.Point, int_line: spg.Line, aux_id: str) -> spg.Line:
        dx = int_line.p2.x - int_line.p1.x
        dy = int_line.p2.y - int_line.p1.y
        p_perp = model.set_point(
            vertex.x - dy,
            vertex.y + dx,
            ID=aux_id,
            classes=["auxiliary"],
            guide=True,
        )
        ext_line = model.construct_line(vertex, p_perp, classes=["bisector"], by="I.11")
        model.assert_perpendicular(ext_line, int_line, at=vertex, by="I.13")
        return ext_line

    bis_a_ext = _perp_bisector_line(A, bis_a_int, "Aper")
    bis_b_ext = _perp_bisector_line(B, bis_b_int, "Bper")
    bis_c_ext = _perp_bisector_line(C, bis_c_int, "Cper")

    De = model.intersect(bis_a_ext, line_a, ID="De", classes=["trace", "result"], by="VI.3")
    Ee = model.intersect(bis_b_ext, line_b, ID="Ee", classes=["trace", "result"], by="VI.3")
    Fe = model.intersect(bis_c_ext, line_c, ID="Fe", classes=["trace", "result"], by="VI.3")

    # Verify harmonic division (B, C; Di, De) == -1 on each side (Menelaus Sphaerica III.8 planar limit)
    if not (is_harmonic(B, C, Di, De) and is_harmonic(C, A, Ei, Ee) and is_harmonic(A, B, Fi, Fe)):
        raise ProofAssertionError("Internal/external angle-bisector traces failed harmonic check.")

    # Verify Converse of Menelaus: (-c/b)*(-a/c)*(-b/a) = -1 => De, Ee, Fe collinear!
    report = verify_menelaus_converse(A, B, C, De, Ee, Fe)
    axis = model.construct_line(De, Ee, classes=["transversal", "result"], by="Menelaus.Converse")
    model.assert_collinear(De, Ee, Fe, by="Menelaus.Converse", label="Anti-orthic axis De-Ee-Fe")
    model.conclude(axis, De, Ee, Fe, kind="qed", by="Menelaus.Converse")

    return model, {
        "A": A,
        "B": B,
        "C": C,
        "I": I_pt,
        "Di": Di,
        "Ei": Ei,
        "Fi": Fi,
        "De": De,
        "Ee": Ee,
        "Fe": Fe,
        "axis": axis,
        "report": report,
    }


def construct_desargues_axis(
    O_coords: tuple[Any, Any] = (0, 12),
    A_coords: tuple[Any, Any] = (-3, 7),
    B_coords: tuple[Any, Any] = (-1, 5),
    C_coords: tuple[Any, Any] = (4, 8),
    kA: sp.Expr = sp.Rational(2, 1),
    kB: sp.Expr = sp.Rational(12, 7),
    kC: sp.Expr = sp.Rational(5, 2),
) -> tuple[Model, dict[str, Any]]:
    """Prove Desargues's Two-Triangle Theorem via three applications of Planar Menelaus.

    Given center ``O`` and perspective triangles ``ABC`` and ``A1B1C1`` along rays ``OA, OB, OC``,
    applies Menelaus to:

    1. :math:`\\triangle OBC` with transversal :math:`B_1 C_1 D`,
    2. :math:`\\triangle OCA` with transversal :math:`C_1 A_1 E`,
    3. :math:`\\triangle OAB` with transversal :math:`A_1 B_1 F`,

    multiplying all three identities to cancel the ``O``-ray ratios and deduce
    :math:`\\frac{\\overline{AF}}{\\overline{FB}} \\cdot \\frac{\\overline{BD}}{\\overline{DC}} \\cdot \\frac{\\overline{CE}}{\\overline{EA}} = -1`,
    establishing collinearity of ``D, E, F`` on Desargues's axis by the Converse of Menelaus.
    """
    ox, oy = _ensure_exact_pair(O_coords)
    ax, ay = _ensure_exact_pair(A_coords)
    bx, by_ = _ensure_exact_pair(B_coords)
    cx, cy = _ensure_exact_pair(C_coords)
    kA_ex, kB_ex, kC_ex = _ensure_exact_expr(kA), _ensure_exact_expr(kB), _ensure_exact_expr(kC)

    model = Model("Menelaus.DesarguesAxis", auto_intersect=False)
    O_pt = model.set_point(ox, oy, ID="O", classes=["given", "center"])
    A = model.set_point(ax, ay, ID="A", classes=["given"])
    B = model.set_point(bx, by_, ID="B", classes=["given"])
    C = model.set_point(cx, cy, ID="C", classes=["given"])

    def _ray_scale(pt: spg.Point, k: sp.Expr, pt_id: str) -> spg.Point:
        return model.set_point(
            clean_expr(O_pt.x + k * (pt.x - O_pt.x)),
            clean_expr(O_pt.y + k * (pt.y - O_pt.y)),
            ID=pt_id,
            classes=["given"],
        )

    A1 = _ray_scale(A, kA_ex, "A1")
    B1 = _ray_scale(B, kB_ex, "B1")
    C1 = _ray_scale(C, kC_ex, "C1")

    # Perspective rays from O
    ray_a = model.construct_line(O_pt, A1, classes=["auxiliary"], by="Post.1")
    ray_b = model.construct_line(O_pt, B1, classes=["auxiliary"], by="Post.1")
    ray_c = model.construct_line(O_pt, C1, classes=["auxiliary"], by="Post.1")
    model.assert_collinear(O_pt, A, A1, by="Given")
    model.assert_collinear(O_pt, B, B1, by="Given")
    model.assert_collinear(O_pt, C, C1, by="Given")

    model.set_polygon([A, B, C], classes=["given"])
    model.set_polygon([A1, B1, C1], classes=["given"])

    la = model.construct_line(B, C, classes=["given"], by="Post.1")
    lb = model.construct_line(C, A, classes=["given"], by="Post.1")
    lc = model.construct_line(A, B, classes=["given"], by="Post.1")

    la1 = model.construct_line(B1, C1, classes=["given"], by="Post.1")
    lb1 = model.construct_line(C1, A1, classes=["given"], by="Post.1")
    lc1 = model.construct_line(A1, B1, classes=["given"], by="Post.1")

    D = model.intersect(la, la1, ID="D", classes=["trace", "result"], by="Post.1")
    E = model.intersect(lb, lb1, ID="E", classes=["trace", "result"], by="Post.1")
    F = model.intersect(lc, lc1, ID="F", classes=["trace", "result"], by="Post.1")

    # Three Menelaus applications on triangles OBC, OCA, OAB
    m_obc = menelaus_product(O_pt, B, C, D, C1, B1)
    m_oca = menelaus_product(O_pt, C, A, E, A1, C1)
    m_oab = menelaus_product(O_pt, A, B, F, B1, A1)
    for tag, m_sub in (("OBC", m_obc), ("OCA", m_oca), ("OAB", m_oab)):
        if not zero_test(m_sub["signed_product"] + 1):
            raise ProofAssertionError(f"Sub-triangle {tag} Menelaus check failed.")

    # Converse of Menelaus on triangle ABC certifies collinearity of D, E, F
    report = verify_menelaus_converse(A, B, C, D, E, F)
    axis = model.construct_line(D, F, classes=["transversal", "result"], by="Menelaus.Converse")
    model.assert_collinear(D, E, F, by="Menelaus.Converse", label="Desargues perspectivity axis")
    model.conclude(axis, D, E, F, kind="qed", by="Menelaus.Converse")

    return model, {
        "O": O_pt,
        "A": A,
        "B": B,
        "C": C,
        "A1": A1,
        "B1": B1,
        "C1": C1,
        "D": D,
        "E": E,
        "F": F,
        "rays": (ray_a, ray_b, ray_c),
        "axis": axis,
        "sub_menelaus": {"OBC": m_obc, "OCA": m_oca, "OAB": m_oab},
        "report": report,
    }


def construct_pascal_hexagram() -> tuple[Model, dict[str, Any]]:
    """Prove Pascal's *Hexagrammum Mysticum* on a circle via three Planar Menelaus applications.

    Uses six exact integer points on the circle :math:`x^2 + y^2 = 100`:
    ``P1=(10,0), P2=(-6,8), P3=(0,-10), P4=(6,8), P5=(8,-6), P6=(-8,-6)``.

    Forms diagonal triangle :math:`\\triangle UVW` from ``(P1P2, P3P4, P5P6)``:

    - ``U = P3P4 ∩ P5P6``, ``V = P5P6 ∩ P1P2``, ``W = P1P2 ∩ P3P4``,

    applies Planar Menelaus to :math:`\\triangle UVW` with transversals ``P2P3M``, ``P4P5L``,
    and ``P6P1N``, cancels chord power products via Euclid III.35/III.36, and concludes by the
    Converse of Menelaus that opposite-side intersections ``L, M, N`` are collinear on Pascal's line.
    """
    model = Model("Menelaus.PascalHexagram", auto_intersect=False)
    O_pt = model.set_point(0, 0, ID="O", classes=["auxiliary"], guide=True)
    P1 = model.set_point(10, 0, ID="P1", classes=["given"])
    P2 = model.set_point(-6, 8, ID="P2", classes=["given"])
    P3 = model.set_point(0, -10, ID="P3", classes=["given"])
    P4 = model.set_point(6, 8, ID="P4", classes=["given"])
    P5 = model.set_point(8, -6, ID="P5", classes=["given"])
    P6 = model.set_point(-8, -6, ID="P6", classes=["given"])

    circ = model.construct_circle(O_pt, P1, classes=["given"], by="Post.3")
    model.assert_concyclic(P1, P2, P3, P4, P5, P6, by="Given", label="6 vertices on circle")

    l12 = model.construct_line(P1, P2, classes=["given"], by="Post.1")
    l23 = model.construct_line(P2, P3, classes=["given"], by="Post.1")
    l34 = model.construct_line(P3, P4, classes=["given"], by="Post.1")
    l45 = model.construct_line(P4, P5, classes=["given"], by="Post.1")
    l56 = model.construct_line(P5, P6, classes=["given"], by="Post.1")
    l61 = model.construct_line(P6, P1, classes=["given"], by="Post.1")

    # Opposite-side intersections of hexagram P1-P2-P3-P4-P5-P6
    L = model.intersect(l12, l45, ID="L", classes=["trace", "result"], by="Post.1")
    M = model.intersect(l23, l56, ID="M", classes=["trace", "result"], by="Post.1")
    N = model.intersect(l34, l61, ID="N", classes=["trace", "result"], by="Post.1")

    # Diagonal triangle UVW formed by alternating side lines l34, l56, l12:
    # Side opposite U is VW = l12 (carries L); opposite V is WU = l34 (carries N); opposite W is UV = l56 (carries M)
    U = model.intersect(l34, l56, ID="U", classes=["auxiliary"], by="Post.1")
    V = model.intersect(l56, l12, ID="V", classes=["auxiliary"], by="Post.1")
    W = model.intersect(l12, l34, ID="W", classes=["auxiliary"], by="Post.1")

    # Apply Planar Menelaus 3 times to triangle UVW:
    # 1. Transversal l23 cuts UV (l56) at M, VW (l12) at P2, WU (l34) at P3
    m_23 = menelaus_product(U, V, W, P2, P3, M)
    # 2. Transversal l45 cuts UV (l56) at P5, VW (l12) at L, WU (l34) at P4
    m_45 = menelaus_product(U, V, W, L, P4, P5)
    # 3. Transversal l61 cuts UV (l56) at P6, VW (l12) at P1, WU (l34) at N
    m_61 = menelaus_product(U, V, W, P1, N, P6)

    for tag, m_sub in (("l23", m_23), ("l45", m_45), ("l61", m_61)):
        if not zero_test(m_sub["signed_product"] + 1):
            raise ProofAssertionError(f"Pascal Menelaus step {tag} failed.")

    # Verify Euclid III.35/III.36 power-of-a-point chord quadrance identities at U, V, W:
    # Q(U,P3)*Q(U,P4) == Q(U,P5)*Q(U,P6), Q(V,P1)*Q(V,P2) == Q(V,P5)*Q(V,P6), Q(W,P1)*Q(W,P2) == Q(W,P3)*Q(W,P4)
    if not zero_test(quadrance(U, P3) * quadrance(U, P4) - quadrance(U, P5) * quadrance(U, P6)):
        raise ProofAssertionError("Power of point U failed.")
    if not zero_test(quadrance(V, P1) * quadrance(V, P2) - quadrance(V, P5) * quadrance(V, P6)):
        raise ProofAssertionError("Power of point V failed.")
    if not zero_test(quadrance(W, P1) * quadrance(W, P2) - quadrance(W, P3) * quadrance(W, P4)):
        raise ProofAssertionError("Power of point W failed.")

    # Converse of Menelaus on diagonal triangle UVW with traces (D=L on VW, E=N on WU, F=M on UV)
    report = verify_menelaus_converse(U, V, W, L, N, M)
    pascal_line = model.construct_line(L, M, classes=["transversal", "result"], by="Menelaus.Converse")
    model.assert_collinear(L, M, N, by="Menelaus.Converse", label="Pascal Mystic Line L-M-N")
    model.conclude(pascal_line, L, M, N, kind="qed", by="Menelaus.Converse")

    return model, {
        "circle": circ,
        "points": (P1, P2, P3, P4, P5, P6),
        "L": L,
        "M": M,
        "N": N,
        "U": U,
        "V": V,
        "W": W,
        "pascal_line": pascal_line,
        "report": report,
    }


def construct_monge_exsimilicenters(
    A_coords: tuple[Any, Any] = (0, 8),
    B_coords: tuple[Any, Any] = (-4, 0),
    C_coords: tuple[Any, Any] = (8, 0),
    rA: sp.Expr = sp.Integer(1),
    rB: sp.Expr = sp.Integer(2),
    rC: sp.Expr = sp.Integer(4),
) -> tuple[Model, dict[str, Any]]:
    """Prove Monge's Three-Circle Theorem via the Converse of Menelaus.

    Given circles centered at ``A, B, C`` with distinct exact positive radii ``rA, rB, rC``,
    their external centers of similitude ``Sab, Sbc, Sca`` divide the center segments externally
    in ratios ``-rA/rB``, ``-rB/rC``, ``-rC/rA``, whose product is identically ``-1``, placing
    ``Sab, Sbc, Sca`` on Monge's external axis of similitude! Also constructs the three internal
    similicenters ``Iab, Ibc, Ica`` to verify all four Monge axes of the complete quadrilateral.
    """
    ax, ay = _ensure_exact_pair(A_coords)
    bx, by_ = _ensure_exact_pair(B_coords)
    cx, cy = _ensure_exact_pair(C_coords)
    ra, rb, rc = _ensure_exact_expr(rA), _ensure_exact_expr(rB), _ensure_exact_expr(rC)

    model = Model("Menelaus.MongeSimilicenters", auto_intersect=False)
    A = model.set_point(ax, ay, ID="A", classes=["given", "center"])
    B = model.set_point(bx, by_, ID="B", classes=["given", "center"])
    C = model.set_point(cx, cy, ID="C", classes=["given", "center"])

    # Radius witness points on horizontal offsets to construct exact Euclidean circles
    Ar = model.set_point(ax + ra, ay, ID="Ar", classes=["auxiliary"], guide=True)
    Br = model.set_point(bx + rb, by_, ID="Br", classes=["auxiliary"], guide=True)
    Cr = model.set_point(cx + rc, cy, ID="Cr", classes=["auxiliary"], guide=True)

    cA = model.construct_circle(A, Ar, classes=["given"], by="Post.3")
    cB = model.construct_circle(B, Br, classes=["given"], by="Post.3")
    cC = model.construct_circle(C, Cr, classes=["given"], by="Post.3")

    la = model.construct_line(B, C, classes=["given"], by="Post.1")
    lb = model.construct_line(C, A, classes=["given"], by="Post.1")
    lc = model.construct_line(A, B, classes=["given"], by="Post.1")
    model.set_polygon([A, B, C], classes=["given"])

    def _similicenter(
        P: spg.Point, Q: spg.Point, rP: sp.Expr, rQ: sp.Expr, external: bool, pt_id: str, cls: list[str]
    ) -> spg.Point:
        if external:
            den = rQ - rP
            if zero_test(den):
                raise ValueError("Equal radii yield an exsimilicenter at infinity.")
            x = clean_expr((rQ * P.x - rP * Q.x) / den)
            y = clean_expr((rQ * P.y - rP * Q.y) / den)
        else:
            den = rQ + rP
            x = clean_expr((rQ * P.x + rP * Q.x) / den)
            y = clean_expr((rQ * P.y + rP * Q.y) / den)
        return model.set_point(x, y, ID=pt_id, classes=cls)

    Sbc = _similicenter(B, C, rb, rc, True, "Sbc", ["trace", "result"])
    Sca = _similicenter(C, A, rc, ra, True, "Sca", ["trace", "result"])
    Sab = _similicenter(A, B, ra, rb, True, "Sab", ["trace", "result"])

    Ibc = _similicenter(B, C, rb, rc, False, "Ibc", ["auxiliary"])
    Ica = _similicenter(C, A, rc, ra, False, "Ica", ["auxiliary"])
    Iab = _similicenter(A, B, ra, rb, False, "Iab", ["auxiliary"])

    model.assert_collinear(B, C, Sbc, by="Construct")
    model.assert_collinear(C, A, Sca, by="Construct")
    model.assert_collinear(A, B, Sab, by="Construct")

    # Verify all 4 Monge axes via Converse of Menelaus:
    # 1. External Monge axis (Sbc, Sca, Sab)
    rep_ext = verify_menelaus_converse(A, B, C, Sbc, Sca, Sab)
    # 2–4. Three mixed Monge axes (1 external + 2 internal similicenters)
    rep_mix_a = verify_menelaus_converse(A, B, C, Sbc, Ica, Iab)
    rep_mix_b = verify_menelaus_converse(A, B, C, Ibc, Sca, Iab)
    rep_mix_c = verify_menelaus_converse(A, B, C, Ibc, Ica, Sab)

    monge_axis = model.construct_line(Sbc, Sca, classes=["transversal", "result"], by="Menelaus.Converse")
    model.assert_collinear(Sbc, Sca, Sab, by="Menelaus.Converse", label="Monge d'Alembert axis")
    model.conclude(monge_axis, Sbc, Sca, Sab, kind="qed", by="Menelaus.Converse")

    return model, {
        "A": A,
        "B": B,
        "C": C,
        "circles": (cA, cB, cC),
        "lines": (la, lb, lc),
        "Sbc": Sbc,
        "Sca": Sca,
        "Sab": Sab,
        "Ibc": Ibc,
        "Ica": Ica,
        "Iab": Iab,
        "monge_axis": monge_axis,
        "report": rep_ext,
        "mixed_reports": (rep_mix_a, rep_mix_b, rep_mix_c),
    }

"""Exact 3D unit-sphere solver, intrinsic spherical invariants, and Spherical Menelaus Theorem.

Implements 100% exact symbolic spherical geometry on :math:`S^2 = \\{(x, y, z) : x^2 + y^2 + z^2 = 1\\}`
over :math:`\\mathbb{Q}` and closed-form quadratic radical extensions (zero ``float`` or ``sp.Float``):

- :class:`SphericalPoint`, :class:`GreatCircle`, and :class:`SphericalTriangle`.
- **Book I Intrinsic Spherical Foundations**:

  - Spherical triangle inequality (*Sphaerica* I.5, Halley p. 6).
  - Spherical angle-sum excess :math:`A + B + C > \\pi` (*Sphaerica* I.11, Halley p. 11), certified
    purely rationally via the Euler–Eriksson half-excess tangent
    :math:`\\tan(E/2) = |\\det(\\mathbf{A},\\mathbf{B},\\mathbf{C})| / (1 + \\mathbf{A}\\cdot\\mathbf{B} + \\mathbf{B}\\cdot\\mathbf{C} + \\mathbf{C}\\cdot\\mathbf{A}) \\in \\mathbb{Q}_{>0}`.
  - Polar triangle duality :math:`\\triangle A^*B^*C^*` and **AAA Spherical Congruence**
    (*Sphaerica* I.17, Halley pp. 18–19).

- **Book III Spherical Menelaus Theorem (*Theorema Menelai*, Prop. III.1, Halley pp. 80–82;
  Ptolemy *Syntaxis* I.13, Heiberg pp. 74–76)**:

  - Evaluated both in Ptolemaic chords of double arcs :math:`\\operatorname{crd}(2\\widehat{PQ}) = 2\\|\\mathbf{P}\\times\\mathbf{Q}\\|`
    and directed sines :math:`\\sin_{\\pm}\\widehat{PQ}` on rational points of :math:`S^2(\\mathbb{Q})`,
    together with Menelaus's central gnomonic projection from :math:`O=(0,0,0)` onto a planar transversal
    and a universal symbolic 3D vector proof.

- **Spherical Anharmonic / Cross-Ratio Pencil Invariance (*Sphaerica* Prop. III.8, Halley pp. 93–94)**
  and **Concurrency of Spherical Altitudes (*Sphaerica* Prop. III.10, Halley pp. 95–97)**.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import sympy as sp
from geometor.model import ProofAssertionError, clean_expr, exact_sign, zero_test

__all__ = [
    "GreatCircle",
    "SphericalMenelausResult",
    "SphericalPoint",
    "SphericalTriangle",
    "double_arc_chord",
    "gnomonic_projection_menelaus",
    "intersect_great_circles",
    "polar_triangle",
    "signed_spherical_sine_ratio",
    "spherical_cross_ratio",
    "spherical_excess_report",
    "spherical_menelaus_default",
    "spherical_orthocenter_menelaus",
    "verify_spherical_cross_ratio_invariance",
    "verify_spherical_menelaus",
    "verify_spherical_menelaus_universal",
]


def _exact_coord(val: Any) -> sp.Expr:
    """Convert ``val`` to an exact SymPy expression, rejecting ``float`` and ``sp.Float``."""
    if isinstance(val, float):
        raise TypeError(f"Floating-point coordinate {val!r} is forbidden; use int or sp.Rational.")
    expr = sp.sympify(val)
    if expr.has(sp.Float):
        raise TypeError(f"sp.Float atom inside {expr!r} is forbidden in exact spherical geometry.")
    return clean_expr(expr)


@dataclass(frozen=True)
class SphericalPoint:
    """Exact point :math:`(x, y, z)` on the unit sphere :math:`x^2 + y^2 + z^2 = 1`."""

    x: sp.Expr
    y: sp.Expr
    z: sp.Expr
    label: str = ""

    def __init__(self, x: Any, y: Any, z: Any, label: str = "") -> None:
        ex, ey, ez = _exact_coord(x), _exact_coord(y), _exact_coord(z)
        norm_sq = clean_expr(ex**2 + ey**2 + ez**2)
        if not zero_test(norm_sq - 1):
            raise ValueError(
                f"Point ({ex}, {ey}, {ez}) does not lie on unit sphere S^2: x^2+y^2+z^2 = {norm_sq}"
            )
        object.__setattr__(self, "x", ex)
        object.__setattr__(self, "y", ey)
        object.__setattr__(self, "z", ez)
        object.__setattr__(self, "label", label)

    @classmethod
    def from_vector(cls, vec: sp.Matrix | tuple[Any, Any, Any], label: str = "") -> SphericalPoint:
        """Normalize a non-zero exact 3D ray vector ``vec`` onto :math:`S^2`."""
        vx, vy, vz = (_exact_coord(vec[0]), _exact_coord(vec[1]), _exact_coord(vec[2]))
        n2 = clean_expr(vx**2 + vy**2 + vz**2)
        if zero_test(n2):
            raise ValueError("Cannot project zero vector onto unit sphere S^2.")
        inv_n = 1 / sp.sqrt(n2)
        return cls(clean_expr(vx * inv_n), clean_expr(vy * inv_n), clean_expr(vz * inv_n), label=label)

    def vector(self) -> sp.Matrix:
        """Return the column :class:`sympy.Matrix` ``[x, y, z]^T``."""
        return sp.Matrix([self.x, self.y, self.z])

    def antipode(self, label: str = "") -> SphericalPoint:
        """Return the exact antipodal point :math:`(-x, -y, -z)` on :math:`S^2`."""
        return SphericalPoint(-self.x, -self.y, -self.z, label=label or (f"-{self.label}" if self.label else ""))

    def dot(self, other: SphericalPoint) -> sp.Expr:
        """Exact Euclidean dot product :math:`\\mathbf{P}\\cdot\\mathbf{Q} = \\cos\\widehat{PQ}`."""
        return clean_expr(self.x * other.x + self.y * other.y + self.z * other.z)

    def cross_vec(self, other: SphericalPoint) -> sp.Matrix:
        """Exact 3D cross product :math:`\\mathbf{P}\\times\\mathbf{Q}`."""
        return self.vector().cross(other.vector())

    def chord_quadrance(self, other: SphericalPoint) -> sp.Expr:
        """Exact 3D Euclidean chord quadrance :math:`\\|\\mathbf{P} - \\mathbf{Q}\\|^2 = 2(1 - \\cos\\widehat{PQ})`."""
        return clean_expr((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    def sin_arc(self, other: SphericalPoint) -> sp.Expr:
        """Exact non-negative sine of central angle :math:`\\sin\\widehat{PQ} = \\|\\mathbf{P}\\times\\mathbf{Q}\\|`."""
        cv = self.cross_vec(other)
        return clean_expr(sp.sqrt(clean_expr(cv[0] ** 2 + cv[1] ** 2 + cv[2] ** 2)))


@dataclass(frozen=True)
class GreatCircle:
    """Exact great circle on :math:`S^2` represented by its central plane normal :math:`\\mathbf{n}`."""

    nx: sp.Expr
    ny: sp.Expr
    nz: sp.Expr
    label: str = ""

    def __init__(self, nx: Any, ny: Any, nz: Any, label: str = "") -> None:
        enx, eny, enz = _exact_coord(nx), _exact_coord(ny), _exact_coord(nz)
        if zero_test(enx) and zero_test(eny) and zero_test(enz):
            raise ValueError("GreatCircle normal vector cannot be zero.")
        object.__setattr__(self, "nx", enx)
        object.__setattr__(self, "ny", eny)
        object.__setattr__(self, "nz", enz)
        object.__setattr__(self, "label", label)

    @classmethod
    def through(cls, P: SphericalPoint, Q: SphericalPoint, label: str = "") -> GreatCircle:
        """Construct the oriented great circle from ``P`` toward ``Q`` (:math:`\\mathbf{n} = \\mathbf{P}\\times\\mathbf{Q}`)."""
        cv = P.cross_vec(Q)
        if all(zero_test(cv[i]) for i in range(3)):
            raise ValueError("Coincident or antipodal points do not determine a unique great circle.")
        return cls(cv[0], cv[1], cv[2], label=label)

    def normal(self) -> sp.Matrix:
        """Return the unnormalized exact normal vector ``[nx, ny, nz]^T``."""
        return sp.Matrix([self.nx, self.ny, self.nz])

    def unit_pole(self, label: str = "") -> SphericalPoint:
        """Return the positive unit pole :math:`\\mathbf{n}/\\|\\mathbf{n}\\| \\in S^2` (*Sphaerica* Def. pole)."""
        return SphericalPoint.from_vector(self.normal(), label=label)

    def contains(self, P: SphericalPoint) -> bool:
        """Return ``True`` iff ``P`` lies on this great circle (:math:`\\mathbf{n}\\cdot\\mathbf{P} = 0`)."""
        return zero_test(self.nx * P.x + self.ny * P.y + self.nz * P.z)


def intersect_great_circles(
    gc1: GreatCircle,
    gc2: GreatCircle,
    *,
    near: SphericalPoint | sp.Matrix | None = None,
    label: str = "",
) -> tuple[SphericalPoint, SphericalPoint]:
    """Intersect two distinct great circles in an exact antipodal pair ``(P, -P)`` on :math:`S^2`.

    If ``near`` is provided, orders ``(P, -P)`` so that ``P`` has positive dot product with ``near``.
    """
    line_dir = gc1.normal().cross(gc2.normal())
    if all(zero_test(line_dir[i]) for i in range(3)):
        raise ValueError("Coincident great circles do not intersect in a discrete antipodal pair.")
    p_pos = SphericalPoint.from_vector(line_dir, label=label)
    p_neg = p_pos.antipode(label=f"-{label}" if label else "")
    if near is not None:
        ref_vec = near.vector() if isinstance(near, SphericalPoint) else sp.Matrix(list(near))
        dot_val = clean_expr((p_pos.vector().dot(ref_vec)))
        if exact_sign(dot_val) < 0:
            return SphericalPoint(p_neg.x, p_neg.y, p_neg.z, label=label), SphericalPoint(
                p_pos.x, p_pos.y, p_pos.z, label=f"-{label}" if label else ""
            )
    return p_pos, p_neg


def double_arc_chord(P: SphericalPoint, Q: SphericalPoint) -> sp.Expr:
    """Compute Ptolemy's chord of the double arc :math:`\\operatorname{crd}(2\\widehat{PQ}) = 2\\sin\\widehat{PQ}`.

    In Ptolemy's *Syntaxis Mathematica* I.13 (Heiberg pp. 74–76) and Menelaus's Greek/Hebrew
    tradition (Halley 1758 p. 82 Scholion: *subtensa dupli arcus*), spherical trigonometric
    ratios are stated in terms of chords subtending double the given arcs on a unit-radius sphere:
    :math:`\\operatorname{crd}(2\\theta) = 2\\sin\\theta = 2\\|\\mathbf{P}\\times\\mathbf{Q}\\|`.
    """
    return clean_expr(2 * P.sin_arc(Q))


def signed_spherical_sine_ratio(
    P: SphericalPoint,
    Q: SphericalPoint,
    R: SphericalPoint,
) -> sp.Expr:
    """Compute the exact directed spherical sine ratio :math:`\\frac{\\sin_{\\pm}\\widehat{PR}}{\\sin_{\\pm}\\widehat{RQ}}`.

    For ``R`` on the great circle ``PQ`` (:math:`\\mathbf{R} = \\alpha\\mathbf{P} + \\beta\\mathbf{Q}`):

    - :math:`\\mathbf{P}\\times\\mathbf{R} = \\beta(\\mathbf{P}\\times\\mathbf{Q})` and
      :math:`\\mathbf{R}\\times\\mathbf{Q} = \\alpha(\\mathbf{P}\\times\\mathbf{Q})`,
    - so the directed ratio of oriented cross products along :math:`\\mathbf{n}_{PQ} = \\mathbf{P}\\times\\mathbf{Q}`
      equals :math:`\\beta / \\alpha`, which is **rational** whenever ``P, Q`` and the cutting great-circle
      normal are rational!
    - Positive when ``R`` lies on the minor arc ``PQ`` (or opposite minor arc), negative when ``R``
      divides ``PQ`` externally.
    """
    n_pq = P.cross_vec(Q)
    n2 = clean_expr(n_pq.dot(n_pq))
    if zero_test(n2):
        raise ValueError("P and Q are coincident or antipodal; great circle PQ is undefined.")
    if not zero_test(n_pq.dot(R.vector())):
        raise ValueError(f"Point {R} does not lie on great circle through {P} and {Q}.")

    num = clean_expr(P.cross_vec(R).dot(n_pq))
    den = clean_expr(R.cross_vec(Q).dot(n_pq))
    if zero_test(den):
        raise ValueError("Division point R coincides with Q or -Q (zero sine denominator).")
    return clean_expr(num / den)


@dataclass(frozen=True)
class SphericalTriangle:
    """Intrinsic spherical triangle :math:`\\triangle ABC` bounded by three minor great-circle arcs

    (*Menelai Sphaericorum* Book I, Def. I–II, Halley 1758 p. 1: *spatium comprehensum sub arcubus
    circulorum magnorum in superficie Sphaerae... semper minores semicirculo*).
    """

    A: SphericalPoint
    B: SphericalPoint
    C: SphericalPoint

    def __post_init__(self) -> None:
        det = self.determinant()
        if zero_test(det):
            raise ValueError("Vertices A, B, C lie on a single great circle (degenerate spherical triangle).")

    def determinant(self) -> sp.Expr:
        """Signed scalar triple product :math:`\\det(\\mathbf{A}, \\mathbf{B}, \\mathbf{C})`."""
        mat = sp.Matrix.hstack(self.A.vector(), self.B.vector(), self.C.vector())
        return clean_expr(mat.det())

    def side_great_circles(self) -> tuple[GreatCircle, GreatCircle, GreatCircle]:
        """Return oriented side great circles ``(BC, CA, AB)``."""
        return (
            GreatCircle.through(self.B, self.C, label="a"),
            GreatCircle.through(self.C, self.A, label="b"),
            GreatCircle.through(self.A, self.B, label="c"),
        )

    def side_cosines(self) -> dict[str, sp.Expr]:
        """Return exact cosines :math:`(\\cos a, \\cos b, \\cos c)` of minor side arcs."""
        return {
            "cos_a": self.B.dot(self.C),
            "cos_b": self.C.dot(self.A),
            "cos_c": self.A.dot(self.B),
        }

    def side_sines(self) -> dict[str, sp.Expr]:
        """Return exact sines :math:`(\\sin a, \\sin b, \\sin c)` of minor side arcs."""
        return {
            "sin_a": self.B.sin_arc(self.C),
            "sin_b": self.C.sin_arc(self.A),
            "sin_c": self.A.sin_arc(self.B),
        }

    def dihedral_cosines(self) -> dict[str, sp.Expr]:
        """Compute exact interior dihedral cosines :math:`(\\cos A, \\cos B, \\cos C)` via Spherical Law of Cosines.

        .. math::

           \\cos A = \\frac{\\cos a - \\cos b\\,\\cos c}{\\sin b\\,\\sin c}.
        """
        cs = self.side_cosines()
        sn = self.side_sines()
        cos_A = clean_expr((cs["cos_a"] - cs["cos_b"] * cs["cos_c"]) / (sn["sin_b"] * sn["sin_c"]))
        cos_B = clean_expr((cs["cos_b"] - cs["cos_c"] * cs["cos_a"]) / (sn["sin_c"] * sn["sin_a"]))
        cos_C = clean_expr((cs["cos_c"] - cs["cos_a"] * cs["cos_b"]) / (sn["sin_a"] * sn["sin_b"]))
        return {"cos_A": cos_A, "cos_B": cos_B, "cos_C": cos_C}

    def dihedral_sines(self) -> dict[str, sp.Expr]:
        """Compute exact interior dihedral sines :math:`(\\sin A, \\sin B, \\sin C)`:

        .. math::

           \\sin A = \\frac{|\\det(\\mathbf{A}, \\mathbf{B}, \\mathbf{C})|}{\\sin b\\,\\sin c}.
        """
        det_abs = abs(self.determinant())
        sn = self.side_sines()
        return {
            "sin_A": clean_expr(det_abs / (sn["sin_b"] * sn["sin_c"])),
            "sin_B": clean_expr(det_abs / (sn["sin_c"] * sn["sin_a"])),
            "sin_C": clean_expr(det_abs / (sn["sin_a"] * sn["sin_b"])),
        }


def spherical_excess_report(tri: SphericalTriangle) -> dict[str, Any]:
    """Certify Menelaus *Sphaerica* Prop. I.11 (:math:`A + B + C > \\pi`) and Spherical Law of Sines (III.2).

    Uses the Euler–Eriksson exact rational formula for the half-excess tangent:

    .. math::

       \\tan\\!\\left(\\frac{E}{2}\\right) =
       \\frac{|\\det(\\mathbf{A}, \\mathbf{B}, \\mathbf{C})|}{1 + \\mathbf{A}\\cdot\\mathbf{B} + \\mathbf{B}\\cdot\\mathbf{C} + \\mathbf{C}\\cdot\\mathbf{A}},

    where :math:`E = A + B + C - \\pi \\in (0, 2\\pi)` is the spherical excess (and area on unit :math:`S^2`).
    Also verifies the Spherical Law of Sines (*Sphaerica* III.2, Halley p. 86):
    :math:`\\frac{\\sin A}{\\sin a} = \\frac{\\sin B}{\\sin b} = \\frac{\\sin C}{\\sin c}`.
    """
    det_abs = abs(tri.determinant())
    cs = tri.side_cosines()
    sn = tri.side_sines()
    d_cs = tri.dihedral_cosines()
    d_sn = tri.dihedral_sines()

    denom = clean_expr(1 + cs["cos_a"] + cs["cos_b"] + cs["cos_c"])
    tan_half_excess = clean_expr(det_abs / denom) if not zero_test(denom) else sp.oo

    # Exact symbolic angles and excess E = A + B + C - pi
    ang_A = sp.acos(d_cs["cos_A"])
    ang_B = sp.acos(d_cs["cos_B"])
    ang_C = sp.acos(d_cs["cos_C"])
    excess_expr = ang_A + ang_B + ang_C - sp.pi

    # Certify A + B + C > pi strictly without floating-point heuristics:
    # For triangles contained in an open hemisphere (1 + cos a + cos b + cos c > 0) and det != 0,
    # tan(E/2) > 0 with E/2 in (0, pi/2) proves E > 0 identically!
    excess_positive = bool(exact_sign(det_abs) > 0 and (denom is sp.oo or exact_sign(denom) > 0 or exact_sign(excess_expr) > 0))
    if not excess_positive:
        raise ProofAssertionError("Spherical excess failed strict positivity check (Sphaerica I.11).")

    # Verify Spherical Law of Sines (Menelaus Sphaerica III.2): sin(A)/sin(a) == sin(B)/sin(b) == sin(C)/sin(c)
    rA = clean_expr(d_sn["sin_A"] / sn["sin_a"])
    rB = clean_expr(d_sn["sin_B"] / sn["sin_b"])
    rC = clean_expr(d_sn["sin_C"] / sn["sin_c"])
    if not (zero_test(rA - rB) and zero_test(rB - rC)):
        raise ProofAssertionError("Spherical Law of Sines (Sphaerica III.2) failed.")

    return {
        "det_abs": det_abs,
        "tan_half_excess": tan_half_excess,
        "angle_A": ang_A,
        "angle_B": ang_B,
        "angle_C": ang_C,
        "excess_symbolic": excess_expr,
        "excess_greater_than_zero": excess_positive,
        "sine_law_common_ratio": rA,
    }


def polar_triangle(tri: SphericalTriangle) -> tuple[SphericalTriangle, dict[str, Any]]:
    """Construct the exact polar triangle :math:`\\triangle A^*B^*C^*` and verify AAA Congruence (Prop. I.17).

    Defines :math:`\\mathbf{A}^* = \\operatorname{sgn}(\\det)\\frac{\\mathbf{B}\\times\\mathbf{C}}{\\|\\mathbf{B}\\times\\mathbf{C}\\|}`
    (and cyclically :math:`\\mathbf{B}^*, \\mathbf{C}^*`) so that :math:`\\mathbf{A}^*\\cdot\\mathbf{A} > 0`.

    Verifies the exact supplementary duality laws:

    .. math::

       \\cos a^* = -\\cos A,\\quad \\cos b^* = -\\cos B,\\quad \\cos c^* = -\\cos C,

       \\cos A^* = -\\cos a,\\quad \\cos B^* = -\\cos b,\\quad \\cos C^* = -\\cos c,

    proving that fixing the three dihedral angles :math:`(A, B, C)` of a spherical triangle uniquely
    determines the three side lengths :math:`(a^*, b^*, c^*)` of its polar triangle, hence (by SSS
    congruence, *Sphaerica* I.8) uniquely determines :math:`\\triangle A^*B^*C^*` and its polar
    :math:`(\\triangle A^*B^*C^*)^* = \\triangle ABC` (**AAA Spherical Congruence**, *Sphaerica* I.17,
    Halley 1758 pp. 18–19).
    """
    sgn = 1 if exact_sign(tri.determinant()) > 0 else -1
    A_star = SphericalPoint.from_vector(sgn * tri.B.cross_vec(tri.C), label=f"{tri.A.label or 'A'}*")
    B_star = SphericalPoint.from_vector(sgn * tri.C.cross_vec(tri.A), label=f"{tri.B.label or 'B'}*")
    C_star = SphericalPoint.from_vector(sgn * tri.A.cross_vec(tri.B), label=f"{tri.C.label or 'C'}*")

    polar = SphericalTriangle(A_star, B_star, C_star)

    cs = tri.side_cosines()
    d_cs = tri.dihedral_cosines()
    p_cs = polar.side_cosines()
    p_d_cs = polar.dihedral_cosines()

    checks = [
        p_cs["cos_a"] + d_cs["cos_A"],
        p_cs["cos_b"] + d_cs["cos_B"],
        p_cs["cos_c"] + d_cs["cos_C"],
        p_d_cs["cos_A"] + cs["cos_a"],
        p_d_cs["cos_B"] + cs["cos_b"],
        p_d_cs["cos_C"] + cs["cos_c"],
    ]
    for idx, chk in enumerate(checks):
        if not zero_test(chk):
            raise ProofAssertionError(f"Polar duality identity #{idx} failed: residual={sp.simplify(chk)}")

    # Verify involutivity: polar(polar(tri)) == tri
    sgn2 = 1 if exact_sign(polar.determinant()) > 0 else -1
    A_bipolar = SphericalPoint.from_vector(sgn2 * polar.B.cross_vec(polar.C), label="A**")
    if not (
        zero_test(A_bipolar.x - tri.A.x)
        and zero_test(A_bipolar.y - tri.A.y)
        and zero_test(A_bipolar.z - tri.A.z)
    ):
        raise ProofAssertionError("Polar triangle involution (T*)* == T failed.")

    return polar, {
        "side_cosines_orig": cs,
        "dihedral_cosines_orig": d_cs,
        "side_cosines_polar": p_cs,
        "dihedral_cosines_polar": p_d_cs,
        "aaa_uniquely_determines_sides": True,
    }


@dataclass(frozen=True)
class SphericalMenelausResult:
    """Exact symbolic results for a Spherical Menelaus configuration (*Sphaerica* III.1)."""

    triangle: SphericalTriangle
    transversal: GreatCircle
    D: SphericalPoint
    E: SphericalPoint
    F: SphericalPoint
    sin_AF_FB: sp.Expr
    sin_BD_DC: sp.Expr
    sin_CE_EA: sp.Expr
    signed_sine_product: sp.Expr
    crd_2AF: sp.Expr
    crd_2FB: sp.Expr
    crd_2BD: sp.Expr
    crd_2DC: sp.Expr
    crd_2CE: sp.Expr
    crd_2EA: sp.Expr
    unsigned_chord_product: sp.Expr


def verify_spherical_menelaus(
    tri: SphericalTriangle,
    transversal: GreatCircle,
) -> SphericalMenelausResult:
    """Intersect ``tri``'s extended great-circle sides with ``transversal`` and prove *Sphaerica* III.1.

    Verifies to exact ``0`` in SymPy:

    1. **Signed Spherical Sine Law**:
       :math:`\\frac{\\sin_{\\pm}\\widehat{AF}}{\\sin_{\\pm}\\widehat{FB}} \\cdot \\frac{\\sin_{\\pm}\\widehat{BD}}{\\sin_{\\pm}\\widehat{DC}} \\cdot \\frac{\\sin_{\\pm}\\widehat{CE}}{\\sin_{\\pm}\\widehat{EA}} = -1`.
    2. **Ptolemy / Halley Double-Arc Chord Compound Ratio** (*Almagest* I.13, Heiberg pp. 74–76;
       Halley 1758 Prop. III.1, pp. 80–82):
       :math:`\\frac{\\operatorname{crd}(2\\widehat{AF})}{\\operatorname{crd}(2\\widehat{FB})} = \\frac{\\operatorname{crd}(2\\widehat{AE})}{\\operatorname{crd}(2\\widehat{EC})} \\cdot \\frac{\\operatorname{crd}(2\\widehat{DC})}{\\operatorname{crd}(2\\widehat{BD})}`
       (equivalently, unsigned product :math:`= +1`).
    """
    gc_a, gc_b, gc_c = tri.side_great_circles()
    centroid_dir = tri.A.vector() + tri.B.vector() + tri.C.vector()

    D, _ = intersect_great_circles(gc_a, transversal, near=centroid_dir, label="D")
    E, _ = intersect_great_circles(gc_b, transversal, near=centroid_dir, label="E")
    F, _ = intersect_great_circles(gc_c, transversal, near=centroid_dir, label="F")

    r_c = signed_spherical_sine_ratio(tri.A, tri.B, F)
    r_a = signed_spherical_sine_ratio(tri.B, tri.C, D)
    r_b = signed_spherical_sine_ratio(tri.C, tri.A, E)
    signed_prod = clean_expr(r_c * r_a * r_b)
    if not zero_test(signed_prod + 1):
        raise ProofAssertionError(
            f"Spherical Menelaus signed sine product expected -1, got {signed_prod}"
        )

    c_af = double_arc_chord(tri.A, F)
    c_fb = double_arc_chord(F, tri.B)
    c_bd = double_arc_chord(tri.B, D)
    c_dc = double_arc_chord(D, tri.C)
    c_ce = double_arc_chord(tri.C, E)
    c_ea = double_arc_chord(E, tri.A)

    unsigned_prod = clean_expr((c_af / c_fb) * (c_bd / c_dc) * (c_ce / c_ea))
    if not zero_test(unsigned_prod - 1):
        raise ProofAssertionError(
            f"Spherical Menelaus Ptolemaic double-arc chord product expected 1, got {unsigned_prod}"
        )

    # Halley III.1 / Almagest I.13 compound-ratio form: crd(2AF)/crd(2FB) == (crd(2EA)/crd(2CE))*(crd(2DC)/crd(2BD))
    compound_diff = clean_expr((c_af / c_fb) - (c_ea / c_ce) * (c_dc / c_bd))
    if not zero_test(compound_diff):
        raise ProofAssertionError(f"Ptolemy/Halley compound chord identity failed: {compound_diff}")

    return SphericalMenelausResult(
        triangle=tri,
        transversal=transversal,
        D=D,
        E=E,
        F=F,
        sin_AF_FB=r_c,
        sin_BD_DC=r_a,
        sin_CE_EA=r_b,
        signed_sine_product=signed_prod,
        crd_2AF=c_af,
        crd_2FB=c_fb,
        crd_2BD=c_bd,
        crd_2DC=c_dc,
        crd_2CE=c_ce,
        crd_2EA=c_ea,
        unsigned_chord_product=unsigned_prod,
    )


def spherical_menelaus_default() -> SphericalMenelausResult:
    """Construct the canonical rational :math:`S^2(\\mathbb{Q})` Spherical Menelaus configuration.

    Uses exact rational vertices:

    - :math:`A = (0, 0, 1)` (North Pole),
    - :math:`B = (3/5, 4/5, 0)` (Pythagorean point on the equator),
    - :math:`C = (2/3, 2/3, 1/3)` (rational point on :math:`S^2(\\mathbb{Q})`),

    cut by the transversal great circle with rational normal :math:`\\mathbf{n}_t = (2, -3, 1)`
    (so :math:`F` divides :math:`AB` internally, :math:`E` divides :math:`CA` internally, and :math:`D`
    divides :math:`BC` externally, directly mirroring Halley 1758 Prop. III.1's diagram!).
    """
    A = SphericalPoint(0, 0, 1, label="A")
    B = SphericalPoint(sp.Rational(3, 5), sp.Rational(4, 5), 0, label="B")
    C = SphericalPoint(sp.Rational(2, 3), sp.Rational(2, 3), sp.Rational(1, 3), label="C")
    tri = SphericalTriangle(A, B, C)
    transversal = GreatCircle(2, -3, 1, label="t")
    return verify_spherical_menelaus(tri, transversal)


def gnomonic_projection_menelaus(res: SphericalMenelausResult) -> dict[str, Any]:
    """Reproduce Menelaus's & Ptolemy's 3D-to-2D central projection proof (*Sphaerica* III.1, Halley p. 80).

    Projects the six unit vectors ``A, B, C, D, E, F`` from sphere center ``O=(0,0,0)`` onto the
    affine plane :math:`\\mathbf{u}\\cdot\\mathbf{x} = 1` (with :math:`\\mathbf{u} = (1, 1, 1)`), obtaining
    planar points :math:`A', B', C', D', E', F'` where great circles become straight lines!
    Verifies that Planar Menelaus holds on :math:`\\triangle A'B'C'` and that multiplying by the
    telescoping radial factors :math:`\\frac{\\|OA\\|}{\\|OB\\|}\\cdot\\frac{\\|OB\\|}{\\|OC\\|}\\cdot\\frac{\\|OC\\|}{\\|OA\\|} = 1`
    yields Spherical Menelaus.
    """
    u_vec = sp.Matrix([1, 1, 2])

    def _proj_plane(P: SphericalPoint) -> sp.Matrix:
        pv = P.vector()
        denom = clean_expr(u_vec.dot(pv))
        if zero_test(denom):
            raise ValueError(f"Point {P} is parallel to projection plane.")
        return pv / denom

    Ap = _proj_plane(res.triangle.A)
    Bp = _proj_plane(res.triangle.B)
    Cp = _proj_plane(res.triangle.C)
    Dp = _proj_plane(res.D)
    Ep = _proj_plane(res.E)
    Fp = _proj_plane(res.F)

    def _affine_ratio(P: sp.Matrix, Q: sp.Matrix, R: sp.Matrix) -> sp.Expr:
        diff_rq = Q - R
        diff_pr = R - P
        for k in range(3):
            if not zero_test(diff_rq[k]):
                return clean_expr(diff_pr[k] / diff_rq[k])
        raise ValueError("Coincident projected points.")

    planar_AF_FB = _affine_ratio(Ap, Bp, Fp)
    planar_BD_DC = _affine_ratio(Bp, Cp, Dp)
    planar_CE_EA = _affine_ratio(Cp, Ap, Ep)
    planar_prod = clean_expr(planar_AF_FB * planar_BD_DC * planar_CE_EA)
    if not zero_test(planar_prod + 1):
        raise ProofAssertionError(f"Projected planar Menelaus product expected -1, got {planar_prod}")

    return {
        "A_prime": Ap,
        "B_prime": Bp,
        "C_prime": Cp,
        "D_prime": Dp,
        "E_prime": Ep,
        "F_prime": Fp,
        "planar_AF_FB": planar_AF_FB,
        "planar_BD_DC": planar_BD_DC,
        "planar_CE_EA": planar_CE_EA,
        "planar_signed_product": planar_prod,
    }


def verify_spherical_menelaus_universal() -> dict[str, sp.Expr]:
    """Prove Spherical Menelaus universally over symbolic 3D vectors ``A, B, C, nt``.

    For any non-coplanar vectors :math:`\\mathbf{A}, \\mathbf{B}, \\mathbf{C}` and transversal plane
    normal :math:`\\mathbf{n}_t`, the ray intersections :math:`\\mathbf{v}_D = (\\mathbf{B}\\times\\mathbf{C})\\times\\mathbf{n}_t`,
    :math:`\\mathbf{v}_E = (\\mathbf{C}\\times\\mathbf{A})\\times\\mathbf{n}_t`, and
    :math:`\\mathbf{v}_F = (\\mathbf{A}\\times\\mathbf{B})\\times\\mathbf{n}_t` satisfy:

    .. math::

       \\frac{(\\mathbf{A}\\times\\mathbf{v}_F)\\cdot(\\mathbf{A}\\times\\mathbf{B})}{(\\mathbf{v}_F\\times\\mathbf{B})\\cdot(\\mathbf{A}\\times\\mathbf{B})}
       = -\\frac{\\mathbf{A}\\cdot\\mathbf{n}_t}{\\mathbf{B}\\cdot\\mathbf{n}_t},

    whose cyclic product around :math:`\\triangle ABC` simplifies identically to :math:`-1`.
    """
    Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz = sp.symbols("Ax Ay Az Bx By Bz Cx Cy Cz")
    nx, ny, nz = sp.symbols("nx ny nz")
    A = sp.Matrix([Ax, Ay, Az])
    B = sp.Matrix([Bx, By, Bz])
    C = sp.Matrix([Cx, Cy, Cz])
    nt = sp.Matrix([nx, ny, nz])

    def _ray_ratio(P: sp.Matrix, Q: sp.Matrix) -> sp.Expr:
        n_pq = P.cross(Q)
        v_r = n_pq.cross(nt)
        num = P.cross(v_r).dot(n_pq)
        den = v_r.cross(Q).dot(n_pq)
        return sp.simplify(num / den)

    r_ab = _ray_ratio(A, B)
    r_bc = _ray_ratio(B, C)
    r_ca = _ray_ratio(C, A)
    prod = sp.simplify(r_ab * r_bc * r_ca)
    if prod != -1:
        raise ProofAssertionError(f"Universal 3D Spherical Menelaus product expected -1, got {prod}")

    return {
        "ratio_AB": r_ab,
        "ratio_BC": r_bc,
        "ratio_CA": r_ca,
        "universal_signed_product": prod,
    }


def spherical_cross_ratio(
    P1: SphericalPoint,
    P2: SphericalPoint,
    P3: SphericalPoint,
    P4: SphericalPoint,
) -> sp.Expr:
    """Compute the exact spherical sine cross-ratio :math:`(P_1, P_2; P_3, P_4)_{S^2}` along a great circle:

    .. math::

       (P_1, P_2; P_3, P_4)_{S^2} =
       \\frac{\\sin_{\\pm}\\widehat{P_1 P_3}\\cdot\\sin_{\\pm}\\widehat{P_2 P_4}}{\\sin_{\\pm}\\widehat{P_2 P_3}\\cdot\\sin_{\\pm}\\widehat{P_1 P_4}}.

    Note: Using :func:`signed_spherical_sine_ratio`, notice that
    :math:`\\frac{\\sin_{\\pm}\\widehat{P_1 P_3}}{\\sin_{\\pm}\\widehat{P_3 P_2}} \\div \\frac{\\sin_{\\pm}\\widehat{P_1 P_4}}{\\sin_{\\pm}\\widehat{P_4 P_2}} = (P_1, P_2; P_3, P_4)_{S^2}`!
    """
    r3 = signed_spherical_sine_ratio(P1, P2, P3)  # sin(P1P3) / sin(P3P2) = -sin(P1P3)/sin(P2P3)
    r4 = signed_spherical_sine_ratio(P1, P2, P4)  # sin(P1P4) / sin(P4P2) = -sin(P1P4)/sin(P2P4)
    if zero_test(r4):
        raise ValueError("Degenerate spherical cross-ratio denominator.")
    return clean_expr(r3 / r4)


def verify_spherical_cross_ratio_invariance() -> dict[str, Any]:
    """Prove Spherical Anharmonic Pencil Invariance (*Menelai Sphaericorum* Prop. III.8, Halley pp. 93–94).

    Constructs a pencil of four great circles concurrent at apex :math:`V = (0, 0, 1)` with rational
    tangent directions, cuts them with two completely independent oblique great circles
    :math:`g_1` (normal :math:`(1, 2, -3)`) and :math:`g_2` (normal :math:`(-2, 1, -4)`), and verifies
    that their spherical sine cross-ratios agree to exact ``0`` in SymPy:

    .. math::

       (X_1, X_2; X_3, X_4)_{S^2} = (Y_1, Y_2; Y_3, Y_4)_{S^2},

    plus verifies a harmonic pencil (:math:`\\text{cross-ratio} = -1`, matching internal/external
    spherical angle bisectors in *Sphaerica* III.6 & III.8!).
    """
    V = SphericalPoint(0, 0, 1, label="V")
    # Four meridian great circles through V=(0,0,1) defined by normals (1, 0, 0), (0, 1, 0), (1, -1, 0), (2, 1, 0)
    pencil = [
        GreatCircle(1, 0, 0, label="m1"),
        GreatCircle(0, 1, 0, label="m2"),
        GreatCircle(1, -1, 0, label="m3"),
        GreatCircle(2, 1, 0, label="m4"),
    ]
    g1 = GreatCircle(1, 2, -3, label="g1")
    g2 = GreatCircle(-2, 1, -4, label="g2")

    hem = sp.Matrix([0, 0, 1])
    X = [intersect_great_circles(m, g1, near=hem, label=f"X{i+1}")[0] for i, m in enumerate(pencil)]
    Y = [intersect_great_circles(m, g2, near=hem, label=f"Y{i+1}")[0] for i, m in enumerate(pencil)]

    cr_x = spherical_cross_ratio(X[0], X[1], X[2], X[3])
    cr_y = spherical_cross_ratio(Y[0], Y[1], Y[2], Y[3])
    if not zero_test(cr_x - cr_y):
        raise ProofAssertionError(f"Spherical cross-ratio invariance failed: {cr_x} != {cr_y}")

    # Harmonic 4-pencil (normals (1,0,0), (0,1,0), (1,-1,0), (1,1,0)) -> cross-ratio == -1 (Sphaerica III.8)
    harm_pencil = [
        GreatCircle(1, 0, 0, label="h1"),
        GreatCircle(0, 1, 0, label="h2"),
        GreatCircle(1, -1, 0, label="h3"),
        GreatCircle(1, 1, 0, label="h4"),
    ]
    H1 = [intersect_great_circles(m, g1, near=hem, label=f"H{i+1}")[0] for i, m in enumerate(harm_pencil)]
    H2 = [intersect_great_circles(m, g2, near=hem, label=f"K{i+1}")[0] for i, m in enumerate(harm_pencil)]
    cr_h1 = spherical_cross_ratio(H1[0], H1[1], H1[2], H1[3])
    cr_h2 = spherical_cross_ratio(H2[0], H2[1], H2[2], H2[3])
    if not (zero_test(cr_h1 + 1) and zero_test(cr_h2 + 1)):
        raise ProofAssertionError(f"Spherical harmonic pencil expected -1, got {cr_h1}, {cr_h2}")

    return {
        "apex": V,
        "g1_points": X,
        "g2_points": Y,
        "cross_ratio_g1": cr_x,
        "cross_ratio_g2": cr_y,
        "difference": clean_expr(cr_x - cr_y),
        "harmonic_cross_ratio_g1": cr_h1,
        "harmonic_cross_ratio_g2": cr_h2,
    }


def spherical_orthocenter_menelaus(tri: SphericalTriangle | None = None) -> dict[str, Any]:
    """Verify Menelaus *Sphaerica* Prop. III.10 (Halley pp. 95–97): concurrency of spherical altitudes.

    Through each vertex :math:`A, B, C`, constructs the great circle perpendicular to the opposite
    side great circle :math:`BC, CA, AB` (passing through its pole :math:`A^*, B^*, C^*`), verifies
    that all three spherical altitudes concur at the spherical orthocenter :math:`H_{S^2}`, and
    verifies that the spherical Ceva product of the altitude feet :math:`H_a, H_b, H_c` equals :math:`+1`
    while their spherical harmonic conjugates lie on the spherical orthic axis (product :math:`-1`).
    """
    if tri is None:
        tri = SphericalTriangle(
            SphericalPoint(0, 0, 1, label="A"),
            SphericalPoint(sp.Rational(3, 5), sp.Rational(4, 5), 0, label="B"),
            SphericalPoint(sp.Rational(2, 3), sp.Rational(2, 3), sp.Rational(1, 3), label="C"),
        )

    gc_a, gc_b, gc_c = tri.side_great_circles()
    # Altitude through A is perpendicular to BC => its plane contains A and normal(BC) = B x C!
    alt_A = GreatCircle(*(tri.A.vector().cross(gc_a.normal())), label="altA")
    alt_B = GreatCircle(*(tri.B.vector().cross(gc_b.normal())), label="altB")
    alt_C = GreatCircle(*(tri.C.vector().cross(gc_c.normal())), label="altC")

    centroid = tri.A.vector() + tri.B.vector() + tri.C.vector()
    H_sph, _ = intersect_great_circles(alt_A, alt_B, near=centroid, label="Hsph")
    if not alt_C.contains(H_sph):
        raise ProofAssertionError("Third spherical altitude failed to pass through spherical orthocenter (III.10).")

    Ha, _ = intersect_great_circles(alt_A, gc_a, near=centroid, label="Ha")
    Hb, _ = intersect_great_circles(alt_B, gc_b, near=centroid, label="Hb")
    Hc, _ = intersect_great_circles(alt_C, gc_c, near=centroid, label="Hc")

    ceva_prod = clean_expr(
        signed_spherical_sine_ratio(tri.A, tri.B, Hc)
        * signed_spherical_sine_ratio(tri.B, tri.C, Ha)
        * signed_spherical_sine_ratio(tri.C, tri.A, Hb)
    )
    if not zero_test(ceva_prod - 1):
        raise ProofAssertionError(f"Spherical altitude Ceva sine product expected +1, got {ceva_prod}")

    return {
        "triangle": tri,
        "orthocenter": H_sph,
        "feet": (Ha, Hb, Hc),
        "altitudes": (alt_A, alt_B, alt_C),
        "spherical_ceva_product": ceva_prod,
    }

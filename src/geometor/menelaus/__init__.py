"""GEOMETOR Menelaus: Digital Scriptorium Codex of *Sphaerica* and Exact Symbolic Transversals.

Provides 100% exact SymPy & :mod:`geometor.model` constructions and theorems for:

- **Planar Menelaus & Converse** (:mod:`geometor.menelaus.planar_transversal`):
  Euclidean parallel-auxiliary proof (Ptolemy *Almagest* I.13 / Halley Lemma I), universal
  polynomial converse, External Angle-Bisector Axis, Desargues's Axis, Pascal's Hexagram,
  Monge's Three-Circle Similicenters, and Wildberger Rational Trigonometry invariants.
- **Intrinsic Spherical Geometry & Spherical Menelaus** (:mod:`geometor.menelaus.spherical`):
  Exact 3D unit-sphere solver (:math:`x^2 + y^2 + z^2 = 1`), spherical excess (:math:`A+B+C > \\pi`),
  polar triangle duality & AAA congruence (*Sphaerica* I.17), Spherical Menelaus (*Sphaerica* III.1)
  in both Ptolemaic double-arc chords and sines, spherical cross-ratio pencil invariance (III.8),
  and spherical orthocenter concurrency (III.10).
- **Projective Menelaus–Ceva Duality** (:mod:`geometor.menelaus.duality_ceva`):
  Homogeneous :math:`\\mathbb{P}^2` polarity, complete-quadrangle harmonic conjugation, and trilinear
  polars of classic ETC triangle centers (``X(1)``, ``X(2)``, ``X(4)``, ``X(7)``).
"""

from __future__ import annotations

__version__ = "0.1.0"

from geometor.menelaus.concordance import (
    load_apparatus_registries,
    load_concordance,
    load_sources_manifest,
)
from geometor.menelaus.duality_ceva import (
    construct_trilinear_polar,
    etc_trilinear_polar_catalogue,
    harmonic_conjugate_collinear,
    verify_projective_menelaus_ceva_duality,
    verify_universal_trilinear_polar,
)
from geometor.menelaus.planar_transversal import (
    MenelausReport,
    construct_desargues_axis,
    construct_external_bisector_axis,
    construct_menelaus_planar,
    construct_monge_exsimilicenters,
    construct_parallel_through,
    construct_pascal_hexagram,
    menelaus_product,
    menelaus_rational_trig_invariants,
    signed_segment_ratio,
    verify_menelaus_converse,
    verify_planar_menelaus_universal,
)
from geometor.menelaus.render import (
    export_planar_svg,
    export_spherical_svg,
    render_planar_svg,
    render_spherical_svg,
)
from geometor.menelaus.spherical import (
    GreatCircle,
    SphericalMenelausResult,
    SphericalPoint,
    SphericalTriangle,
    double_arc_chord,
    gnomonic_projection_menelaus,
    intersect_great_circles,
    polar_triangle,
    signed_spherical_sine_ratio,
    spherical_cross_ratio,
    spherical_excess_report,
    spherical_menelaus_default,
    spherical_orthocenter_menelaus,
    verify_spherical_cross_ratio_invariance,
    verify_spherical_menelaus,
    verify_spherical_menelaus_universal,
)

__all__ = [
    "__version__",
    "GreatCircle",
    "MenelausReport",
    "SphericalMenelausResult",
    "SphericalPoint",
    "SphericalTriangle",
    "construct_desargues_axis",
    "construct_external_bisector_axis",
    "construct_menelaus_planar",
    "construct_monge_exsimilicenters",
    "construct_parallel_through",
    "construct_pascal_hexagram",
    "construct_trilinear_polar",
    "double_arc_chord",
    "etc_trilinear_polar_catalogue",
    "export_planar_svg",
    "export_spherical_svg",
    "gnomonic_projection_menelaus",
    "harmonic_conjugate_collinear",
    "intersect_great_circles",
    "load_apparatus_registries",
    "load_concordance",
    "load_sources_manifest",
    "menelaus_product",
    "menelaus_rational_trig_invariants",
    "polar_triangle",
    "render_planar_svg",
    "render_spherical_svg",
    "signed_segment_ratio",
    "signed_spherical_sine_ratio",
    "spherical_cross_ratio",
    "spherical_excess_report",
    "spherical_menelaus_default",
    "spherical_orthocenter_menelaus",
    "verify_menelaus_converse",
    "verify_planar_menelaus_universal",
    "verify_projective_menelaus_ceva_duality",
    "verify_spherical_cross_ratio_invariance",
    "verify_spherical_menelaus",
    "verify_spherical_menelaus_universal",
    "verify_universal_trilinear_polar",
]

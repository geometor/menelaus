"""Generate all 10 interactive `.euclid-graphic` SVG figures into ``docsrc/_static/figures/``."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from geometor.menelaus import (  # noqa: E402
    GreatCircle,
    SphericalPoint,
    SphericalTriangle,
    construct_desargues_axis,
    construct_external_bisector_axis,
    construct_menelaus_planar,
    construct_monge_exsimilicenters,
    construct_pascal_hexagram,
    construct_trilinear_polar,
    export_planar_svg,
    export_spherical_svg,
    polar_triangle,
    spherical_menelaus_default,
    spherical_orthocenter_menelaus,
    verify_spherical_cross_ratio_invariance,
)

FIGURES_DIR = PROJECT_ROOT / "docsrc" / "_static" / "figures"


def build_all_figures(out_dir: Path = FIGURES_DIR) -> list[Path]:
    """Build and write all 10 standalone `.euclid-graphic` SVGs."""
    out_dir.mkdir(parents=True, exist_ok=True)
    built: list[Path] = []

    # 1. Planar Menelaus with parallel auxiliary CH || DF (Halley Lemma I / Almagest I.13)
    m_plan, _ = construct_menelaus_planar()
    built.append(export_planar_svg(m_plan, out_dir / "menelaus-planar-parallel.svg"))

    # 2. Rational Trigonometry sub-triangle configuration (scalene acute seed)
    m_rt, _ = construct_menelaus_planar(
        A_coords=(4, 8),
        B_coords=(0, 0),
        C_coords=(10, 0),
        D_coords=(15, 0),
        F_coords=(2, 4),
    )
    built.append(export_planar_svg(m_rt, out_dir / "menelaus-rational-trig.svg"))

    # 3. External Angle-Bisector Axis (anti-orthic axis on Heronian (7, 20, 15) triangle)
    m_bis, _ = construct_external_bisector_axis()
    built.append(export_planar_svg(m_bis, out_dir / "menelaus-external-bisectors.svg"))

    # 4. Desargues's Two-Triangle Perspectivity Axis
    m_des, _ = construct_desargues_axis()
    built.append(export_planar_svg(m_des, out_dir / "menelaus-desargues-axis.svg"))

    # 5. Pascal's Hexagrammum Mysticum
    m_pas, _ = construct_pascal_hexagram()
    built.append(export_planar_svg(m_pas, out_dir / "menelaus-pascal-hexagram.svg"))

    # 6. Monge's Three-Circle Similicenters
    m_mon, _ = construct_monge_exsimilicenters()
    built.append(export_planar_svg(m_mon, out_dir / "menelaus-monge-circles.svg"))

    # 7. Spherical Excess & Polar Triangle Duality (Book I Props. I.11 & I.17)
    A = SphericalPoint(0, 0, 1, label="A")
    B = SphericalPoint("4/5", 0, "3/5", label="B")
    C = SphericalPoint("12/25", "16/25", "3/5", label="C")
    tri_b1 = SphericalTriangle(A, B, C)
    pol_b1, _ = polar_triangle(tri_b1)
    built.append(
        export_spherical_svg(
            out_dir / "spherical-excess-polar.svg",
            points=[
                (tri_b1.A, "given"),
                (tri_b1.B, "given"),
                (tri_b1.C, "given"),
                (pol_b1.A, "auxiliary center"),
                (pol_b1.B, "auxiliary center"),
                (pol_b1.C, "auxiliary center"),
            ],
            arcs=[
                (tri_b1.A, tri_b1.B, "given", "/ A B /"),
                (tri_b1.B, tri_b1.C, "given", "/ B C /"),
                (tri_b1.C, tri_b1.A, "given", "/ C A /"),
                (pol_b1.A, pol_b1.B, "auxiliary", "/ A* B* /"),
                (pol_b1.B, pol_b1.C, "auxiliary", "/ B* C* /"),
                (pol_b1.C, pol_b1.A, "auxiliary", "/ C* A* /"),
            ],
            full_circles=[(GreatCircle(0, 0, 1, label="eq"), "auxiliary", "( Eq )")],
            azimuth_deg=32.0,
            elevation_deg=22.0,
        )
    )

    # 8. Spherical Menelaus Theorem (Book III Prop. III.1 — Theorema Menelai)
    sph = spherical_menelaus_default()
    gc_a, gc_b, gc_c = sph.triangle.side_great_circles()
    built.append(
        export_spherical_svg(
            out_dir / "spherical-menelaus-3d.svg",
            points=[
                (sph.triangle.A, "given"),
                (sph.triangle.B, "given"),
                (sph.triangle.C, "given"),
                (sph.D, "trace result"),
                (sph.E, "trace result"),
                (sph.F, "trace result"),
            ],
            arcs=[
                (sph.triangle.A, sph.triangle.B, "given", "/ A B /"),
                (sph.triangle.B, sph.triangle.C, "given", "/ B C /"),
                (sph.triangle.C, sph.triangle.A, "given", "/ C A /"),
                (sph.triangle.C, sph.D, "auxiliary", "/ C D /"),
                (sph.D, sph.E, "transversal result", "/ D E /"),
                (sph.E, sph.F, "transversal result", "/ E F /"),
            ],
            full_circles=[
                (gc_a, "auxiliary", "[ B C ]"),
                (sph.transversal, "transversal result", "[ D F ]"),
            ],
            azimuth_deg=42.0,
            elevation_deg=24.0,
        )
    )

    # 9. Spherical Cross-Ratio Pencil & Orthocenter (Book III Props. III.8 & III.10)
    cr_data = verify_spherical_cross_ratio_invariance()
    V_ap = cr_data["apex"]
    Xs = cr_data["g1_points"]
    Ys = cr_data["g2_points"]
    ortho = spherical_orthocenter_menelaus()
    _ = ortho  # verified exact concurrency during figure generation
    built.append(
        export_spherical_svg(
            out_dir / "spherical-cross-ratio-pencil.svg",
            points=[
                (V_ap, "given center"),
                *[(pt, "cevian") for pt in Xs],
                *[(pt, "trace result") for pt in Ys],
            ],
            arcs=[
                *[(V_ap, Ys[i], "auxiliary", f"/ V Y{i+1} /") for i in range(4)],
                (Xs[0], Xs[3], "cevian", "/ X1 X4 /"),
                (Ys[0], Ys[3], "transversal result", "/ Y1 Y4 /"),
            ],
            full_circles=[
                (GreatCircle(1, 2, -3, label="g1"), "cevian", "[ X1 X4 ]"),
                (GreatCircle(-2, 1, -4, label="g2"), "transversal result", "[ Y1 Y4 ]"),
            ],
            azimuth_deg=35.0,
            elevation_deg=26.0,
        )
    )

    # 10. Ceva–Menelaus Harmonic Duality & Trilinear Polar
    m_tri, _ = construct_trilinear_polar()
    built.append(export_planar_svg(m_tri, out_dir / "menelaus-ceva-trilinear-polar.svg"))

    return built


def main() -> None:
    paths = build_all_figures()
    for p in paths:
        print(f"Built SVG: {p.relative_to(PROJECT_ROOT)} ({p.stat().st_size} bytes)")


if __name__ == "__main__":
    main()

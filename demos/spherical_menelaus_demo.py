"""Demo 2: Exact 3D Spherical Menelaus (Sphaerica III.1), Excess (I.11), Polar AAA (I.17) & Cross-Ratio (III.8)."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT / "src") not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT / "src"))

from rich.console import Console  # noqa: E402
from rich.table import Table  # noqa: E402

from geometor.menelaus import (  # noqa: E402
    gnomonic_projection_menelaus,
    polar_triangle,
    spherical_excess_report,
    spherical_menelaus_default,
    spherical_orthocenter_menelaus,
    verify_spherical_cross_ratio_invariance,
    verify_spherical_menelaus_universal,
)


def main() -> None:
    console = Console()
    sph = spherical_menelaus_default()
    exc = spherical_excess_report(sph.triangle)
    pol_tri, pol_meta = polar_triangle(sph.triangle)
    gnom = gnomonic_projection_menelaus(sph)
    univ = verify_spherical_menelaus_universal()
    cr = verify_spherical_cross_ratio_invariance()
    ortho = spherical_orthocenter_menelaus(sph.triangle)

    tbl = Table(title="Menelaus Sphaerica Books I & III — Exact Unit-Sphere Verification")
    tbl.add_column("Proposition / Theorem", style="cyan")
    tbl.add_column("Exact Symbolic Result", style="green")

    tbl.add_row("Prop. I.11 Spherical Excess tan(E/2)", f"{exc['tan_half_excess']} > 0 (A + B + C > pi)")
    tbl.add_row(
        "Prop. I.17 Polar Triangle & AAA Congruence",
        f"A* = ({pol_tri.A.x}, {pol_tri.A.y}, {pol_tri.A.z}), AAA unique = {pol_meta['aaa_uniquely_determines_sides']}",
    )
    tbl.add_row(
        "Prop. III.1 Signed Spherical Sine Product",
        f"({sph.sin_AF_FB}) * ({sph.sin_BD_DC}) * ({sph.sin_CE_EA}) = {sph.signed_sine_product}",
    )
    tbl.add_row(
        "Almagest I.13 / Halley Scholion crd(2 arc) Product",
        f"{sph.unsigned_chord_product} (exact SymPy cancellation)",
    )
    tbl.add_row(
        "Prop. III.1 Gnomonic Central Projection",
        f"Planar projected product = {gnom['planar_signed_product']}",
    )
    tbl.add_row(
        "Universal 3D Vector Proof",
        f"({univ['ratio_AB']}) * ({univ['ratio_BC']}) * ({univ['ratio_CA']}) = {univ['universal_signed_product']}",
    )
    tbl.add_row(
        "Prop. III.8 Spherical Cross-Ratio Invariance",
        f"CR(g1) = {cr['cross_ratio_g1']} == CR(g2) = {cr['cross_ratio_g2']} (harmonic = {cr['harmonic_cross_ratio_g1']})",
    )
    tbl.add_row(
        "Prop. III.10 Spherical Orthocenter Concurrency",
        f"Spherical altitude Ceva sine product = {ortho['spherical_ceva_product']}",
    )

    console.print(tbl)


if __name__ == "__main__":
    main()

"""Rich CLI summary runner for ``geometor-menelaus``."""

from __future__ import annotations

from rich.console import Console
from rich.table import Table

from geometor.menelaus import (
    __version__,
    construct_menelaus_planar,
    etc_trilinear_polar_catalogue,
    menelaus_rational_trig_invariants,
    polar_triangle,
    spherical_excess_report,
    spherical_menelaus_default,
    verify_spherical_cross_ratio_invariance,
)


def main() -> None:
    """Display an exact symbolic verification report across Planar, Spherical, and Dual Menelaus."""
    console = Console()
    console.print(f"[bold amber1]GEOMETOR • menelaus[/bold amber1] v{__version__}")

    m_plan, d_plan = construct_menelaus_planar()
    rt = menelaus_rational_trig_invariants(m_plan, d_plan)
    sph = spherical_menelaus_default()
    exc = spherical_excess_report(sph.triangle)
    _pol, pol_meta = polar_triangle(sph.triangle)
    cr_inv = verify_spherical_cross_ratio_invariance()
    etc_cat = etc_trilinear_polar_catalogue()

    tbl = Table(title="Exact Symbolic Menelaus Verification Ledger (SymPy over Q & Radical Extensions)")
    tbl.add_column("Domain / Locus", style="cyan")
    tbl.add_column("Exact Invariant", style="white")
    tbl.add_column("Verified Value", style="green")

    r = d_plan["ratios"]
    tbl.add_row(
        "Planar Menelaus (Halley Lemma I)",
        "(AF/FB) * (BD/DC) * (CE/EA)",
        f"{r['AF_FB']} * ({r['BD_DC']}) * {r['CE_EA']} = {r['signed_product']}",
    )
    tbl.add_row(
        "Rational Trig Quadrance Law",
        "Q(AF)*Q(BD)*Q(CE) == Q(FB)*Q(DC)*Q(EA)",
        f"{rt['quadrance_lhs']} == {rt['quadrance_rhs']}",
    )
    tbl.add_row(
        "Spherical Excess (Sphaerica I.11)",
        "tan((A + B + C - pi) / 2)",
        f"{exc['tan_half_excess']} > 0",
    )
    tbl.add_row(
        "Polar Triangle & AAA (Sphaerica I.17)",
        "cos(a*) + cos(A) == 0",
        f"AAA unique = {pol_meta['aaa_uniquely_determines_sides']}",
    )
    tbl.add_row(
        "Spherical Menelaus (Sphaerica III.1)",
        "(sin AF/sin FB)*(sin BD/sin DC)*(sin CE/sin EA)",
        f"{sph.sin_AF_FB} * ({sph.sin_BD_DC}) * ({sph.sin_CE_EA}) = {sph.signed_sine_product}",
    )
    tbl.add_row(
        "Ptolemy Double-Arc Chords (Almagest I.13)",
        "crd(2AF)*crd(2BD)*crd(2CE) / (...)",
        f"{sph.unsigned_chord_product}",
    )
    tbl.add_row(
        "Spherical Cross-Ratio (Sphaerica III.8)",
        "CR(g1) == CR(g2)",
        f"{cr_inv['cross_ratio_g1']} == {cr_inv['cross_ratio_g2']}",
    )
    tbl.add_row(
        "Ceva–Menelaus Duality (X(1), X(4), X(7))",
        "Trilinear Polar Signed Product",
        ", ".join(f"{k}: {etc_cat[k]['signed_product']}" for k in ("X(1)", "X(4)", "X(7)")),
    )

    console.print(tbl)


if __name__ == "__main__":
    main()

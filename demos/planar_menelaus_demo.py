"""Demo 1: Exact Symbolic Planar Menelaus, Converse Applications, and Rational Trigonometry."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT / "src") not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT / "src"))

from rich.console import Console  # noqa: E402
from rich.table import Table  # noqa: E402

from geometor.menelaus import (  # noqa: E402
    construct_desargues_axis,
    construct_external_bisector_axis,
    construct_menelaus_planar,
    construct_monge_exsimilicenters,
    construct_pascal_hexagram,
    menelaus_rational_trig_invariants,
    verify_planar_menelaus_universal,
)


def main() -> None:
    console = Console()
    m_plan, d_plan = construct_menelaus_planar()
    rt = menelaus_rational_trig_invariants(m_plan, d_plan)
    univ = verify_planar_menelaus_universal()

    _, d_bis = construct_external_bisector_axis()
    _, d_des = construct_desargues_axis()
    _, d_pas = construct_pascal_hexagram()
    _, d_mon = construct_monge_exsimilicenters()

    tbl = Table(title="Planar Menelaus & Converse Constructions (100% Exact SymPy)")
    tbl.add_column("Construction", style="cyan")
    tbl.add_column("AF/FB", style="white")
    tbl.add_column("BD/DC", style="white")
    tbl.add_column("CE/EA", style="white")
    tbl.add_column("Signed Product", style="green")

    r0 = d_plan["ratios"]
    tbl.add_row(
        "Halley Lemma I / Almagest I.13 (Parallel CH || DF)",
        str(r0["AF_FB"]),
        str(r0["BD_DC"]),
        str(r0["CE_EA"]),
        str(r0["signed_product"]),
    )
    for title, rep in (
        ("External Angle-Bisector Axis (Sphaerica III.6 limit)", d_bis["report"]),
        ("Desargues's Perspectivity Axis (3x Menelaus)", d_des["report"]),
        ("Pascal's Hexagrammum Mysticum (Diagonal UVW)", d_pas["report"]),
        ("Monge's 3-Circle Exsimilicenters (r = 1, 2, 4)", d_mon["report"]),
    ):
        tbl.add_row(
            title,
            str(rep.AF_FB),
            str(rep.BD_DC),
            str(rep.CE_EA),
            str(rep.signed_product),
        )

    console.print(tbl)
    console.print(f"[bold]Universal determinant identity residual:[/bold] {univ['identity_residual']}")
    console.print(
        f"[bold]Rational Trig Quadrance Law:[/bold] "
        f"Q(AF)*Q(BD)*Q(CE) = {rt['quadrance_lhs']} == Q(FB)*Q(DC)*Q(EA) = {rt['quadrance_rhs']}"
    )
    console.print(
        f"[bold]Rational Trig Spread Telescoping:[/bold] "
        f"s(t,b)/s(t,c) * s(t,c)/s(t,a) * s(t,a)/s(t,b) = {rt['spread_product']}"
    )


if __name__ == "__main__":
    main()

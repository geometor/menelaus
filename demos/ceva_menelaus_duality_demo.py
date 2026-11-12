"""Demo 3: Projective Point-Line Duality between Menelaus (-1) and Ceva (+1) & ETC Trilinear Polars."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT / "src") not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT / "src"))

from rich.console import Console  # noqa: E402
from rich.table import Table  # noqa: E402

from geometor.menelaus import (  # noqa: E402
    construct_trilinear_polar,
    etc_trilinear_polar_catalogue,
    verify_projective_menelaus_ceva_duality,
)


def main() -> None:
    console = Console()
    _, data = construct_trilinear_polar()
    proj = verify_projective_menelaus_ceva_duality()
    cat = etc_trilinear_polar_catalogue()

    tbl = Table(title="Ceva (+1) <-> Menelaus (-1) Harmonic Duality & ETC Trilinear Polars")
    tbl.add_column("Perspector / Center", style="cyan")
    tbl.add_column("Dual Trilinear Polar Line", style="white")
    tbl.add_column("Verification", style="green")

    tbl.add_row(
        "General Perspector P = (3, 3)",
        f"Dm={data['Dm']}, Em={data['Em']}, Fm={data['Fm']}",
        f"Ceva = +{data['ceva_ratios']['signed_product']}, Menelaus = {data['menelaus_report'].signed_product}, CRs = {data['cross_ratios']}",
    )
    for k in ("X(1)", "X(2)", "X(4)", "X(7)"):
        entry = cat[k]
        ver = (
            f"Ceva = +{entry['ceva_product']} (medial parallel -> infinity)"
            if k == "X(2)"
            else f"Menelaus signed product = {entry['signed_product']}"
        )
        tbl.add_row(f"{k} {entry['center_name']}", entry["polar_name"], ver)

    console.print(tbl)
    console.print(
        f"[bold]Homogeneous P^2 Trilinear Polar of \\[u:v:w]:[/bold] "
        f"{list(proj['trilinear_polar_homogeneous'])} (det_Ceva={proj['ceva_concurrency_det']}, det_Menelaus={proj['menelaus_collinearity_det']})"
    )


if __name__ == "__main__":
    main()

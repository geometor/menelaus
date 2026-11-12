"""Publication-grade `.euclid-graphic` SVG renderer for 2D planar and 3D spherical Menelaus models.

Supports both:

1. **2D Planar** :class:`~geometor.model.Model` constructions (:func:`render_planar_svg`,
   :func:`export_planar_svg`), clipping infinite algebraic lines cleanly to a padded frame,
   rendering 3-vertex midpoint ``<path>`` segments, and avoiding point-label collisions.
2. **3D Unit-Sphere** :math:`S^2` constructions (:func:`render_spherical_svg`,
   :func:`export_spherical_svg`), projecting exact :class:`~geometor.menelaus.spherical.SphericalPoint`
   and :class:`~geometor.menelaus.spherical.GreatCircle` elements orthographically onto 2D
   while preserving full interactive ``svg.euclid-graphic`` ``data-ref`` wiring for ``publish``.
"""

from __future__ import annotations

import html
import math
from pathlib import Path
from typing import Any, Sequence

import sympy.geometry as spg
from geometor.model import Model

from geometor.menelaus.spherical import GreatCircle, SphericalPoint

__all__ = [
    "EMBEDDED_SVG_STYLE",
    "export_planar_svg",
    "export_spherical_svg",
    "render_planar_svg",
    "render_spherical_svg",
]

EMBEDDED_SVG_STYLE: str = """
  .euclid-graphic {
    --svg-bg: #fafaf9;
    --ink: #1c1917;
    --label-halo: rgba(250, 250, 249, 0.92);
    --given: #334155;
    --aux: #0284c7;
    --cevian: #059669;
    --transversal: #d97706;
    --limb: #64748b;
    --pt-given: #0f172a;
    --pt-trace: #d97706;
    --pt-cevian: #059669;
    --pt-aux: #0284c7;
    font-family: "Inter", "Segoe UI", system-ui, -apple-system, sans-serif;
  }
  @media (prefers-color-scheme: dark) {
    .euclid-graphic {
      --svg-bg: #141417;
      --ink: #f4f4f5;
      --label-halo: rgba(20, 20, 23, 0.92);
      --given: #cbd5e1;
      --aux: #38bdf8;
      --cevian: #34d399;
      --transversal: #fbbf24;
      --limb: #94a3b8;
      --pt-given: #f1f5f9;
      --pt-trace: #fbbf24;
      --pt-cevian: #34d399;
      --pt-aux: #38bdf8;
    }
  }
  .euclid-graphic .bg { fill: var(--svg-bg); }
  .euclid-graphic .geom-line { fill: none; stroke: var(--given); stroke-width: 1.75; stroke-linecap: round; }
  .euclid-graphic .geom-line.auxiliary, .euclid-graphic .geom-line.bisector { stroke: var(--aux); stroke-width: 1.45; stroke-dasharray: 6 4; opacity: 0.88; }
  .euclid-graphic .geom-line.cevian { stroke: var(--cevian); stroke-width: 1.65; stroke-dasharray: 4 3; }
  .euclid-graphic .geom-line.transversal, .euclid-graphic .geom-line.result { stroke: var(--transversal); stroke-width: 2.65; stroke-dasharray: none; }
  .euclid-graphic .geom-line.back-arc { stroke-dasharray: 3.5 4.5; opacity: 0.42; }
  .euclid-graphic .geom-segment { fill: none; stroke: var(--aux); stroke-width: 2.2; stroke-linecap: round; }
  .euclid-graphic .geom-segment.extension { stroke: var(--given); stroke-dasharray: 5 3.5; stroke-width: 1.6; }
  .euclid-graphic .geom-circle { fill: none; stroke: var(--given); stroke-width: 1.85; opacity: 0.88; }
  .euclid-graphic .geom-circle.sphere-limb { stroke: var(--limb); stroke-width: 2.2; fill: var(--aux); fill-opacity: 0.04; }
  .euclid-graphic .geom-polygon { fill: var(--aux); fill-opacity: 0.06; stroke: var(--given); stroke-width: 2.1; stroke-linejoin: round; }
  .euclid-graphic .geom-polygon.cevian { fill: var(--cevian); fill-opacity: 0.07; stroke: var(--cevian); stroke-width: 1.6; }
  .euclid-graphic .geom-point { fill: var(--pt-given); stroke: var(--svg-bg); stroke-width: 1.5; }
  .euclid-graphic .geom-point.trace, .euclid-graphic .geom-point.result { fill: var(--pt-trace); stroke-width: 1.8; }
  .euclid-graphic .geom-point.cevian { fill: var(--pt-cevian); }
  .euclid-graphic .geom-point.auxiliary, .euclid-graphic .geom-point.center { fill: var(--pt-aux); }
  .euclid-graphic .geom-label {
    fill: var(--ink);
    font-size: 14px;
    font-weight: 600;
    paint-order: stroke fill;
    stroke: var(--label-halo);
    stroke-width: 3.6px;
    stroke-linejoin: round;
    user-select: none;
  }
  .euclid-graphic .geom-label-sub { font-size: 10.5px; font-weight: 600; }
""".strip()

SVG_DEFS_TICKS: str = """  <defs>
    <path id="geom-tick-1" d="M 0,-5.5 L 0,5.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
    <path id="geom-tick-2" d="M -2.4,-5.5 L -2.4,5.5 M 2.4,-5.5 L 2.4,5.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
    <path id="geom-tick-3" d="M -4.2,-5.5 L -4.2,5.5 M 0,-5.5 L 0,5.5 M 4.2,-5.5 L 4.2,5.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
  </defs>"""


def _fmt(val: float) -> str:
    if abs(val - round(val)) < 1e-5:
        return str(int(round(val)))
    return f"{val:.2f}".rstrip("0").rstrip(".")


def _clip_line_to_rect(
    line: spg.Line,
    xmin: float,
    xmax: float,
    ymin: float,
    ymax: float,
) -> tuple[tuple[float, float], tuple[float, float]] | None:
    a_f = float(line.coefficients[0].evalf())
    b_f = float(line.coefficients[1].evalf())
    c_f = float(line.coefficients[2].evalf())
    eps = 1e-11
    hits: list[tuple[float, float]] = []

    if abs(b_f) > eps:
        for x_edge in (xmin, xmax):
            y_val = -(a_f * x_edge + c_f) / b_f
            if ymin - 1e-7 <= y_val <= ymax + 1e-7:
                hits.append((x_edge, min(max(y_val, ymin), ymax)))

    if abs(a_f) > eps:
        for y_edge in (ymin, ymax):
            x_val = -(b_f * y_edge + c_f) / a_f
            if xmin - 1e-7 <= x_val <= xmax + 1e-7:
                hits.append((min(max(x_val, xmin), xmax), y_edge))

    unique_hits: list[tuple[float, float]] = []
    for hx, hy in hits:
        if not any(math.hypot(hx - ux, hy - uy) < 1e-5 for ux, uy in unique_hits):
            unique_hits.append((hx, hy))
    if len(unique_hits) < 2:
        return None

    best_pair = (unique_hits[0], unique_hits[1])
    best_dist = -1.0
    for i in range(len(unique_hits)):
        for j in range(i + 1, len(unique_hits)):
            d = math.hypot(unique_hits[j][0] - unique_hits[i][0], unique_hits[j][1] - unique_hits[i][1])
            if d > best_dist:
                best_dist = d
                best_pair = (unique_hits[i], unique_hits[j])
    return best_pair


def _point_to_seg_dist(px: float, py: float, x1: float, y1: float, x2: float, y2: float) -> float:
    dx, dy = x2 - x1, y2 - y1
    l2 = dx * dx + dy * dy
    if l2 < 1e-12:
        return math.hypot(px - x1, py - y1)
    t = max(0.0, min(1.0, ((px - x1) * dx + (py - y1) * dy) / l2))
    return math.hypot(px - (x1 + t * dx), py - (y1 + t * dy))


def _split_label(pid: str, overrides: dict[str, str] | None = None) -> tuple[str, str]:
    txt = overrides.get(pid, pid) if overrides else pid
    if len(txt) >= 2 and txt[0].isalpha() and not txt.endswith("*"):
        return txt[0], txt[1:]
    return txt, ""


def _place_labels_non_overlapping(
    labeled_points: list[tuple[str, float, float, float]],
    segments_px: list[tuple[float, float, float, float]],
    width: float,
    height: float,
    overrides: dict[str, str] | None = None,
) -> list[str]:
    """Place SVG ``<text class="geom-label">`` elements with greedy collision avoidance."""
    angles = [
        -0.5 * math.pi,
        0.5 * math.pi,
        -0.25 * math.pi,
        -0.75 * math.pi,
        0.25 * math.pi,
        0.75 * math.pi,
        0.0,
        math.pi,
        -0.38 * math.pi,
        0.38 * math.pi,
    ]
    placed_boxes: list[tuple[float, float, float, float]] = []
    all_pts = [(sx, sy) for _pid, sx, sy, _r in labeled_points]
    out: list[str] = []

    for pid, sx, sy, rad in labeled_points:
        base_txt, sub_txt = _split_label(pid, overrides)
        est_w = 9.2 * len(base_txt) + 6.4 * len(sub_txt) + 4.0
        est_h = 14.5
        dist_r = rad + 12.5

        best_xy = (sx + 8.0, sy - 8.0)
        best_box = (sx, sy - est_h, sx + est_w, sy)
        best_score = -1e12

        for ang in angles:
            cx = sx + math.cos(ang) * (dist_r + 0.35 * est_w)
            cy = sy + math.sin(ang) * (dist_r + 0.25 * est_h)
            box = (cx - 0.5 * est_w, cy - 0.5 * est_h, cx + 0.5 * est_w, cy + 0.5 * est_h)
            score = 0.0
            if box[0] < 8 or box[2] > width - 8 or box[1] < 8 or box[3] > height - 8:
                score -= 600.0
            for ox, oy in all_pts:
                d_pt = math.hypot(cx - ox, cy - oy)
                if d_pt < 15.0:
                    score -= (15.0 - d_pt) * 45.0
            for bx0, by0, bx1, by1 in placed_boxes:
                if not (box[2] < bx0 - 2 or box[0] > bx1 + 2 or box[3] < by0 - 2 or box[1] > by1 + 2):
                    score -= 450.0
            for x1, y1, x2, y2 in segments_px:
                d_seg = _point_to_seg_dist(cx, cy, x1, y1, x2, y2)
                if d_seg < 10.0:
                    score -= (10.0 - d_seg) * 18.0
            if score > best_score:
                best_score = score
                best_xy = (cx, cy)
                best_box = box

        placed_boxes.append(best_box)
        lx, ly = best_xy[0] - 0.42 * est_w, best_xy[1] + 0.34 * est_h
        if sub_txt:
            inner = (
                f'{html.escape(base_txt)}'
                f'<tspan class="geom-label-sub" dy="3">{html.escape(sub_txt)}</tspan>'
            )
        else:
            inner = html.escape(base_txt)
        out.append(
            f'      <text class="geom-label" x="{_fmt(lx)}" y="{_fmt(ly)}" '
            f'data-ref="{html.escape(pid)}">{inner}</text>'
        )
    return out


def render_planar_svg(
    model: Model,
    *,
    graphic_id: str = "menelaus-planar",
    width: int = 760,
    height: int = 520,
    padding_px: float = 54.0,
    label_overrides: dict[str, str] | None = None,
) -> str:
    """Render a 2D :class:`~geometor.model.Model` into a complete `.euclid-graphic` SVG string."""
    vis_pts: list[spg.Point] = []
    vis_lines: list[spg.Line] = []
    vis_segs: list[spg.Segment] = []
    vis_circs: list[spg.Circle] = []
    vis_polys: list[spg.Polygon] = []

    for entity, details in model.items():
        if details.guide:
            continue
        if isinstance(entity, spg.Point):
            vis_pts.append(entity)
        elif isinstance(entity, spg.Line):
            vis_lines.append(entity)
        elif isinstance(entity, spg.Segment):
            vis_segs.append(entity)
        elif isinstance(entity, spg.Circle):
            vis_circs.append(entity)
        elif isinstance(entity, spg.Polygon):
            vis_polys.append(entity)

    xs: list[float] = []
    ys: list[float] = []
    for pt in vis_pts:
        xs.append(float(pt.x.evalf()))
        ys.append(float(pt.y.evalf()))
    for c in vis_circs:
        cx_f, cy_f, r_f = float(c.center.x.evalf()), float(c.center.y.evalf()), float(c.radius.evalf())
        xs.extend([cx_f - r_f, cx_f + r_f])
        ys.extend([cy_f - r_f, cy_f + r_f])

    if not xs:
        xs, ys = [-1.0, 1.0], [-1.0, 1.0]

    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    span_x = max(xmax - xmin, 1.0)
    span_y = max(ymax - ymin, 1.0)

    # Expand math clip box by 12% around all visible points/circles
    clip_xmin, clip_xmax = xmin - 0.12 * span_x, xmax + 0.12 * span_x
    clip_ymin, clip_ymax = ymin - 0.12 * span_y, ymax + 0.12 * span_y
    c_span_x = clip_xmax - clip_xmin
    c_span_y = clip_ymax - clip_ymin

    avail_w = width - 2 * padding_px
    avail_h = height - 2 * padding_px
    scale = min(avail_w / c_span_x, avail_h / c_span_y)
    mid_x = 0.5 * (clip_xmin + clip_xmax)
    mid_y = 0.5 * (clip_ymin + clip_ymax)

    def to_svg(mx: float, my: float) -> tuple[float, float]:
        return (0.5 * width + (mx - mid_x) * scale, 0.5 * height - (my - mid_y) * scale)

    pt_svg: dict[spg.Point, tuple[float, float]] = {
        p: to_svg(float(p.x.evalf()), float(p.y.evalf())) for p in vis_pts
    }

    graphics_elems: list[str] = []
    highlight_elems: list[str] = []
    segments_px: list[tuple[float, float, float, float]] = []

    # Polygons
    for poly in vis_polys:
        el = model[poly]
        pts_str = " ".join(
            f"{_fmt(to_svg(float(v.x.evalf()), float(v.y.evalf()))[0])},"
            f"{_fmt(to_svg(float(v.x.evalf()), float(v.y.evalf()))[1])}"
            for v in poly.vertices
        )
        v_ids = [model[v].ID for v in poly.vertices if v in model and model[v].ID]
        p_ref = f"< {' '.join(v_ids)} >"
        cls_extra = " cevian" if "cevian" in el.classes else ""
        graphics_elems.append(
            f'      <polygon class="geom-polygon{cls_extra}" points="{pts_str}" data-ref="{html.escape(p_ref)}"/>'
        )
        highlight_elems.append(
            f'      <polygon class="geom-polygon geom-highlight" points="{pts_str}" data-ref="{html.escape(p_ref)}"/>'
        )

    # Circles
    for circ in vis_circs:
        ccx, ccy = to_svg(float(circ.center.x.evalf()), float(circ.center.y.evalf()))
        rr = float(circ.radius.evalf()) * scale
        cid = model[circ].ID or "( O )"
        graphics_elems.append(
            f'      <circle class="geom-circle" cx="{_fmt(ccx)}" cy="{_fmt(ccy)}" r="{_fmt(rr)}" '
            f'data-ref="{html.escape(cid)}"/>'
        )

    # Lines (sorted so transversal/result draws on top of given/auxiliary)
    def _line_order(ln: spg.Line) -> int:
        c = model[ln].classes
        if "transversal" in c or "result" in c:
            return 30
        if "given" in c:
            return 20
        return 10

    for ln in sorted(vis_lines, key=_line_order):
        clipped = _clip_line_to_rect(ln, clip_xmin, clip_xmax, clip_ymin, clip_ymax)
        if clipped is None:
            continue
        (mx1, my1), (mx2, my2) = clipped
        sx1, sy1 = to_svg(mx1, my1)
        sx2, sy2 = to_svg(mx2, my2)
        smx, smy = 0.5 * (sx1 + sx2), 0.5 * (sy1 + sy2)
        segments_px.append((sx1, sy1, sx2, sy2))

        el = model[ln]
        cls_tags = [k for k in ("given", "auxiliary", "bisector", "cevian", "transversal", "result") if k in el.classes]
        cls_str = " ".join(["geom-line", *cls_tags])

        inc_ids: list[str] = []
        for pt in vis_pts:
            pid = model[pt].ID
            if pid and ln.contains(pt):
                inc_ids.append(pid)

        primary_ref = el.ID if el.ID else (f"[ {inc_ids[0]} {inc_ids[-1]} ]" if len(inc_ids) >= 2 else "")
        aliases: list[str] = []
        for i in range(len(inc_ids)):
            for j in range(i + 1, len(inc_ids)):
                for br_l, br_r in (("[", "]"), ("/", "/")):
                    cand = f"{br_l} {inc_ids[i]} {inc_ids[j]} {br_r}"
                    cand_rev = f"{br_l} {inc_ids[j]} {inc_ids[i]} {br_r}"
                    if cand != primary_ref:
                        aliases.append(cand)
                    if cand_rev != primary_ref:
                        aliases.append(cand_rev)

        ref_attr = f' data-ref="{html.escape(primary_ref)}"' if primary_ref else ""
        alias_attr = f' data-aliases="{html.escape(" | ".join(aliases))}"' if aliases else ""
        d_path = f"M {_fmt(sx1)} {_fmt(sy1)} L {_fmt(smx)} {_fmt(smy)} L {_fmt(sx2)} {_fmt(sy2)}"
        graphics_elems.append(f'      <path class="{cls_str}" d="{d_path}"{ref_attr}{alias_attr}/>')
        if primary_ref:
            highlight_elems.append(
                f'      <path class="geom-line geom-highlight" d="{d_path}"{ref_attr}{alias_attr}/>'
            )

    # Explicit segments (3-vertex midpoint path for tick markers)
    for seg in vis_segs:
        sx1, sy1 = to_svg(float(seg.p1.x.evalf()), float(seg.p1.y.evalf()))
        sx2, sy2 = to_svg(float(seg.p2.x.evalf()), float(seg.p2.y.evalf()))
        smx, smy = 0.5 * (sx1 + sx2), 0.5 * (sy1 + sy2)
        segments_px.append((sx1, sy1, sx2, sy2))
        el = model[seg]
        cls_tags = [k for k in ("auxiliary", "extension", "result") if k in el.classes]
        cls_str = " ".join(["geom-segment", *cls_tags])
        id1 = model[seg.p1].ID if seg.p1 in model else ""
        id2 = model[seg.p2].ID if seg.p2 in model else ""
        s_ref = f"/ {id1} {id2} /" if (id1 and id2) else el.ID
        d_path = f"M {_fmt(sx1)} {_fmt(sy1)} L {_fmt(smx)} {_fmt(smy)} L {_fmt(sx2)} {_fmt(sy2)}"
        graphics_elems.append(
            f'      <path class="{cls_str}" d="{d_path}" data-ref="{html.escape(s_ref)}"/>'
        )
        highlight_elems.append(
            f'      <path class="geom-segment geom-highlight" d="{d_path}" data-ref="{html.escape(s_ref)}"/>'
        )

    # Points & Labels
    point_elems: list[str] = []
    labeled_specs: list[tuple[str, float, float, float]] = []
    for pt in vis_pts:
        sx, sy = pt_svg[pt]
        el = model[pt]
        pid = el.ID
        cls_tags = [k for k in ("given", "trace", "result", "cevian", "auxiliary", "center") if k in el.classes]
        rad = 4.6 if ("result" in el.classes or "trace" in el.classes) else 3.9
        cls_str = " ".join(["geom-point", *cls_tags])
        tooltip = f"{pid} = ({pt.x}, {pt.y})"
        point_elems.append(
            f'      <circle class="{cls_str}" cx="{_fmt(sx)}" cy="{_fmt(sy)}" r="{_fmt(rad)}" '
            f'data-ref="{html.escape(pid)}"><title>{html.escape(tooltip)}</title></circle>'
        )
        if pid:
            labeled_specs.append((pid, sx, sy, rad))

    label_elems = _place_labels_non_overlapping(labeled_specs, segments_px, width, height, label_overrides)

    lines_out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'class="euclid-graphic" data-graphic-id="{html.escape(graphic_id)}">',
        f"  <style>\n{EMBEDDED_SVG_STYLE}\n  </style>",
        SVG_DEFS_TICKS,
        '  <rect class="bg" width="100%" height="100%"/>',
        '  <g id="elements">',
        '    <g id="graphics">',
        *graphics_elems,
        "    </g>",
        '    <g id="highlights" aria-hidden="true">',
        *highlight_elems,
        "    </g>",
        '    <g id="points">',
        *point_elems,
        "    </g>",
        '    <g id="labels">',
        *label_elems,
        "    </g>",
        "  </g>",
        "</svg>",
    ]
    return "\n".join(lines_out) + "\n"


def export_planar_svg(model: Model, output_path: Path | str, **kwargs: Any) -> Path:
    """Write a 2D :class:`~geometor.model.Model` SVG to ``output_path``."""
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    graphic_id = kwargs.pop("graphic_id", out.stem)
    svg = render_planar_svg(model, graphic_id=graphic_id, **kwargs)
    out.write_text(svg, encoding="utf-8")
    return out


def render_spherical_svg(
    *,
    points: Sequence[tuple[SphericalPoint, str]],
    arcs: Sequence[tuple[SphericalPoint, SphericalPoint, str, str]],
    full_circles: Sequence[tuple[GreatCircle, str, str]] = (),
    graphic_id: str = "menelaus-spherical",
    width: int = 640,
    height: int = 560,
    azimuth_deg: float = 36.0,
    elevation_deg: float = 24.0,
    label_overrides: dict[str, str] | None = None,
) -> str:
    """Render an orthographic 3D projection of :math:`S^2` as an interactive `.euclid-graphic` SVG.

    Args:
        points: Sequence of ``(SphericalPoint, css_role)`` (e.g. ``"given"``, ``"trace result"``).
        arcs: Sequence of ``(P, Q, css_role, data_ref)`` geodesic minor arcs on :math:`S^2`.
        full_circles: Sequence of ``(GreatCircle, css_role, data_ref)`` full great circles (front/back split).
        graphic_id: Interactive graphic ID.
        width: SVG width in pixels.
        height: SVG height in pixels.
        azimuth_deg: Camera azimuth angle in degrees.
        elevation_deg: Camera elevation angle in degrees.
        label_overrides: Optional label text map.
    """
    az = math.radians(azimuth_deg)
    el = math.radians(elevation_deg)

    # Orthonormal camera basis: cam_z points toward viewer; cam_x right; cam_y up
    cam_z = (math.cos(el) * math.cos(az), math.cos(el) * math.sin(az), math.sin(el))
    cam_x = (-math.sin(az), math.cos(az), 0.0)
    cam_y = (
        -math.sin(el) * math.cos(az),
        -math.sin(el) * math.sin(az),
        math.cos(el),
    )

    cx_px, cy_px = 0.5 * width, 0.5 * height
    radius_px = min(width, height) * 0.40

    def proj3(vx: float, vy: float, vz: float) -> tuple[float, float, float]:
        sx = cx_px + (vx * cam_x[0] + vy * cam_x[1] + vz * cam_x[2]) * radius_px
        sy = cy_px - (vx * cam_y[0] + vy * cam_y[1] + vz * cam_y[2]) * radius_px
        depth = vx * cam_z[0] + vy * cam_z[1] + vz * cam_z[2]
        return sx, sy, depth

    graphics_elems: list[str] = [
        f'      <circle class="geom-circle sphere-limb" cx="{_fmt(cx_px)}" cy="{_fmt(cy_px)}" '
        f'r="{_fmt(radius_px)}" data-ref="( S2 )"/>'
    ]
    highlight_elems: list[str] = []
    segments_px: list[tuple[float, float, float, float]] = []

    # Helper to sample a full great circle split into front/back polylines
    def _draw_great_circle(gc: GreatCircle, cls_role: str, ref_str: str, samples: int = 120) -> None:
        nx, ny, nz = float(gc.nx.evalf()), float(gc.ny.evalf()), float(gc.nz.evalf())
        nn = math.sqrt(nx * nx + ny * ny + nz * nz)
        nx, ny, nz = nx / nn, ny / nn, nz / nn
        # Orthonormal basis u1, u2 in the plane n . x = 0
        ref = (0.0, 0.0, 1.0) if abs(nz) < 0.85 else (1.0, 0.0, 0.0)
        u1x = ny * ref[2] - nz * ref[1]
        u1y = nz * ref[0] - nx * ref[2]
        u1z = nx * ref[1] - ny * ref[0]
        u1n = math.sqrt(u1x * u1x + u1y * u1y + u1z * u1z)
        u1 = (u1x / u1n, u1y / u1n, u1z / u1n)
        u2 = (ny * u1[2] - nz * u1[1], nz * u1[0] - nx * u1[2], nx * u1[1] - ny * u1[0])

        front_runs: list[list[tuple[float, float]]] = []
        back_runs: list[list[tuple[float, float]]] = []
        cur_front: list[tuple[float, float]] = []
        cur_back: list[tuple[float, float]] = []

        for k in range(samples + 1):
            th = 2.0 * math.pi * k / samples
            ct, st = math.cos(th), math.sin(th)
            vx = ct * u1[0] + st * u2[0]
            vy = ct * u1[1] + st * u2[1]
            vz = ct * u1[2] + st * u2[2]
            sx, sy, depth = proj3(vx, vy, vz)
            if depth >= -0.02:
                cur_front.append((sx, sy))
                if len(cur_back) >= 2:
                    back_runs.append(cur_back)
                cur_back = []
            else:
                cur_back.append((sx, sy))
                if len(cur_front) >= 2:
                    front_runs.append(cur_front)
                cur_front = []
        if len(cur_front) >= 2:
            front_runs.append(cur_front)
        if len(cur_back) >= 2:
            back_runs.append(cur_back)

        ref_attr = f' data-ref="{html.escape(ref_str)}"' if ref_str else ""
        for run in back_runs:
            d = "M " + " L ".join(f"{_fmt(x)} {_fmt(y)}" for x, y in run)
            graphics_elems.append(f'      <path class="geom-line {cls_role} back-arc" d="{d}"{ref_attr}/>')
        for run in front_runs:
            d = "M " + " L ".join(f"{_fmt(x)} {_fmt(y)}" for x, y in run)
            graphics_elems.append(f'      <path class="geom-line {cls_role}" d="{d}"{ref_attr}/>')
            if ref_str:
                highlight_elems.append(f'      <path class="geom-line geom-highlight" d="{d}"{ref_attr}/>')

    for gc, role, ref_s in full_circles:
        _draw_great_circle(gc, role, ref_s)

    # Geodesic arcs between P and Q
    for P, Q, role, ref_s in arcs:
        p_vec = (float(P.x.evalf()), float(P.y.evalf()), float(P.z.evalf()))
        q_vec = (float(Q.x.evalf()), float(Q.y.evalf()), float(Q.z.evalf()))
        dot_pq = max(-1.0, min(1.0, p_vec[0] * q_vec[0] + p_vec[1] * q_vec[1] + p_vec[2] * q_vec[2]))
        omega = math.acos(dot_pq)
        sin_om = math.sin(omega)
        steps = max(24, int(omega * 36))
        pts_2d: list[tuple[float, float]] = []
        for k in range(steps + 1):
            t = k / steps
            if sin_om < 1e-8:
                vx = (1 - t) * p_vec[0] + t * q_vec[0]
                vy = (1 - t) * p_vec[1] + t * q_vec[1]
                vz = (1 - t) * p_vec[2] + t * q_vec[2]
            else:
                w1 = math.sin((1 - t) * omega) / sin_om
                w2 = math.sin(t * omega) / sin_om
                vx = w1 * p_vec[0] + w2 * q_vec[0]
                vy = w1 * p_vec[1] + w2 * q_vec[1]
                vz = w1 * p_vec[2] + w2 * q_vec[2]
            sx, sy, _d = proj3(vx, vy, vz)
            pts_2d.append((sx, sy))

        for i in range(0, len(pts_2d) - 1, 4):
            j = min(i + 4, len(pts_2d) - 1)
            segments_px.append((pts_2d[i][0], pts_2d[i][1], pts_2d[j][0], pts_2d[j][1]))

        d_arc = "M " + " L ".join(f"{_fmt(x)} {_fmt(y)}" for x, y in pts_2d)
        ref_attr = f' data-ref="{html.escape(ref_s)}"' if ref_s else ""
        pid1, pid2 = P.label, Q.label
        alias_attr = ""
        if pid1 and pid2:
            aliases = [f"/ {pid1} {pid2} /", f"/ {pid2} {pid1} /", f"[ {pid1} {pid2} ]", f"[ {pid2} {pid1} ]"]
            alias_attr = f' data-aliases="{html.escape(" | ".join(aliases))}"'
        graphics_elems.append(f'      <path class="geom-line {role}" d="{d_arc}"{ref_attr}{alias_attr}/>')
        if ref_s:
            highlight_elems.append(
                f'      <path class="geom-line geom-highlight" d="{d_arc}"{ref_attr}{alias_attr}/>'
            )

    point_elems: list[str] = []
    labeled_specs: list[tuple[str, float, float, float]] = []
    for P, role in points:
        sx, sy, _depth = proj3(float(P.x.evalf()), float(P.y.evalf()), float(P.z.evalf()))
        pid = P.label
        rad = 4.6 if ("result" in role or "trace" in role) else 4.0
        tooltip = f"{pid} = ({P.x}, {P.y}, {P.z})"
        point_elems.append(
            f'      <circle class="geom-point {role}" cx="{_fmt(sx)}" cy="{_fmt(sy)}" r="{_fmt(rad)}" '
            f'data-ref="{html.escape(pid)}"><title>{html.escape(tooltip)}</title></circle>'
        )
        if pid:
            labeled_specs.append((pid, sx, sy, rad))

    label_elems = _place_labels_non_overlapping(labeled_specs, segments_px, width, height, label_overrides)

    lines_out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'class="euclid-graphic" data-graphic-id="{html.escape(graphic_id)}">',
        f"  <style>\n{EMBEDDED_SVG_STYLE}\n  </style>",
        SVG_DEFS_TICKS,
        '  <rect class="bg" width="100%" height="100%"/>',
        '  <g id="elements">',
        '    <g id="graphics">',
        *graphics_elems,
        "    </g>",
        '    <g id="highlights" aria-hidden="true">',
        *highlight_elems,
        "    </g>",
        '    <g id="points">',
        *point_elems,
        "    </g>",
        '    <g id="labels">',
        *label_elems,
        "    </g>",
        "  </g>",
        "</svg>",
    ]
    return "\n".join(lines_out) + "\n"


def export_spherical_svg(output_path: Path | str, **kwargs: Any) -> Path:
    """Write a 3D orthographic unit-sphere SVG to ``output_path``."""
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    graphic_id = kwargs.pop("graphic_id", out.stem)
    svg = render_spherical_svg(graphic_id=graphic_id, **kwargs)
    out.write_text(svg, encoding="utf-8")
    return out

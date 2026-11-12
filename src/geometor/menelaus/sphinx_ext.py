"""Runtime Sphinx & photon-platform/publish integration for GEOMETOR Menelaus.

Refines the ``la`` companion-track tab label to ``"Latin (Halley 1758)"`` in
``photon_platform.publish.book`` (without modifying ``photon-platform/publish``)
and binds local ``objects.inv`` inventories for sister GEOMETOR repositories so
offline sandbox builds produce zero warnings.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

__all__ = [
    "configure_local_intersphinx",
    "register_halley_latin_track_label",
    "setup",
]


def register_halley_latin_track_label() -> None:
    """Update the ``la`` track label in ``photon_platform.publish.book`` to ``Latin (Halley 1758)``."""
    try:
        from photon_platform.publish import book
    except ImportError:
        return

    updated_patterns = []
    for pat, key, lbl in book._TRACK_SUFFIX_PATTERNS:
        if key == "la":
            updated_patterns.append((pat, "la", "Latin (Halley 1758)"))
        else:
            updated_patterns.append((pat, key, lbl))
    book._TRACK_SUFFIX_PATTERNS[:] = updated_patterns


def configure_local_intersphinx(intersphinx_mapping: dict[str, Any], project_root: Path) -> None:
    """Bind local ``objects.inv`` files for sister GEOMETOR codices and drop remote-only targets."""
    geometor_dir = project_root.parent
    for sister in ("euclid", "elements", "pappus", "etc", "altshiller-court", "proclus", "hilbert"):
        inv = geometor_dir / sister / "docs" / "objects.inv"
        if inv.is_file():
            intersphinx_mapping[sister] = (
                f"https://geometor.github.io/{sister}",
                str(inv.resolve()),
            )
    for key in list(intersphinx_mapping.keys()):
        _uri, inv_target = intersphinx_mapping[key]
        if inv_target is None:
            intersphinx_mapping.pop(key, None)


def setup(app: Any) -> dict[str, Any]:
    """Sphinx extension entry point."""
    register_halley_latin_track_label()
    return {
        "version": "0.1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

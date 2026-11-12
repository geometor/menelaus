import os
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
_WORKSPACE_ROOT = _REPO_ROOT.parent
for _extra_path in (
    _REPO_ROOT / "src",
    _WORKSPACE_ROOT / "model" / "src",
    _WORKSPACE_ROOT / ".venv" / "lib" / "python3.13" / "site-packages",
):
    if _extra_path.exists() and str(_extra_path) not in sys.path:
        sys.path.insert(0, str(_extra_path))

from photon_platform.publish.global_conf import *  # noqa: E402, F403
import geometor.menelaus as module  # noqa: E402
from geometor.menelaus.sphinx_ext import (  # noqa: E402
    configure_local_intersphinx,
    register_halley_latin_track_label,
)

version = module.__version__

org = "geometor"
org_name = "GEOMETOR"

repo = "menelaus"
repo_name = "menelaus"

setup_globals(org, org_name, repo, repo_name)  # noqa: F405

if "geometor.menelaus.sphinx_ext" not in extensions:  # noqa: F405
    extensions.append("geometor.menelaus.sphinx_ext")  # noqa: F405

register_halley_latin_track_label()
configure_local_intersphinx(
    intersphinx_mapping,  # noqa: F405
    Path(os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))),
)

project = "GEOMETOR • menelaus"
author = "Menelaus of Alexandria"
copyright = "c. 100 CE (Halley 1758 / Heiberg 1898 / Björnbo 1902) • Digital Edition GEOMETOR"
suppress_warnings = ["autoapi.python_import_resolution", "toc.not_included"]

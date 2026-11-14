:navigation: header
:order: 20
:nav_title: Usage

.. _usage:

Using This Edition
==================

.. rubric:: *Reader's Guide to the GEOMETOR Interactive Digital Codex of Menelaus's Sphaerica*

Welcome to the **GEOMETOR Digital Scriptorium** edition of :person:`Menelaus of Alexandria <menelaus>`'s *Sphaerica*. This edition synthesizes public-domain primary witnesses, rigorous modern English translations, and 100% exact symbolic mathematical models.

----

1. Synchronized Reading Tracks
------------------------------

The treatise is organized into four synchronized parallel tracks accessible from the book header bar on any proposition page:

* **English**: Complete modern scholarly translation of Menelaus's spherical definitions, theorems, and proofs.
* **Latin / Greek**: Scan-verified diplomatic Latin text established by :person:`Edmond Halley <halley>` (:cite:`1758 <halley-1758>`) alongside :person:`Claudius Ptolemy <ptolemy>`'s polytonic Greek witness from *Syntaxis Mathematica* I.13 (:cite:`ed. Heiberg 1898 <ptolemy-almagest-i-13>`).
* **Summary**: Executive mathematical condensations of each proposition and unit.
* **Notes & Commentary**: Philological scholia, mathematical analyses, and exact ``geometor.model`` / ``SymPy`` formalizations.

2. Primary-Source Witnesses & Halley/Heiberg Readings
-----------------------------------------------------

Marginal references align the text to historical folio and page markers:

* **Halley (1758)**: Page citations correspond directly to Edmond Halley's posthumous Oxford edition *Menelai Sphaericorum Libri III*.
* **Heiberg (1898)**: Line-level Greek citations match the Teubner edition of Ptolemy's *Almagest*.
* **Björnbo (1902)**: Stemma and proposition concordance numbers correlate the Arabic, Hebrew, and Latin manuscript traditions.

3. Interactive Diagrams & Deductive Links
-----------------------------------------

Every diagram in the edition is generated dynamically from symbolic algebraic coordinates:

* **Geometric References (``:g:``)**: Hovering or clicking any ``:g:`` reference (e.g. vertices, segments, or great-circle arcs) highlights the matching element directly within the interactive SVG graphic.
* **Justification Links (``:just:``)**: Direct cross-references to Euclid's *Elements* (:cite:`Heiberg 1883 <euclid-elements>`) or preceding Menelaus propositions show the deductive dependencies of each step.
* **Algebraic Assertions (``:eq:``)**: Exact mathematical formulas and cross-ratio invariants verified symbolically over :math:`\mathbb{Q}`.

4. Full-Text Search with In-Page Highlighting
---------------------------------------------

The sidebar search engine indexes the full Greek, Latin, and English terminology across all units:

* Executing a query appends ``?highlight=`` parameters to document links.
* Matched terms are highlighted directly in the page text for effortless browsing.

5. Categories, Tags & Collection Views
--------------------------------------

Browse content through structured multi-dimensional taxonomy facets:

* Sidebar facets group material by topic (e.g. spherical triangles, transversal theory, projective duality).
* Collection views support **Cards**, **Banners**, and **List** display modes.

6. Scholarly Hover Cards & Dark Mode
------------------------------------

* **Prosopography (``:person:``)**: Hover over any named person to view biographical dates, historical role, and scholarly contributions.
* **Bibliography (``:cite:``)**: Hover over citation tags to inspect full bibliographic provenance and library loci.
* **Terminology (``:term:``)**: Hover over mathematical terms for multilingual definitions (Greek, Latin, Arabic, Hebrew, English).
* **Theme Support**: Seamlessly toggle between Light and Dark viewing themes.

----

Python API & Command-Line Interface
-----------------------------------

The companion Python package :mod:`geometor.menelaus` provides exact symbolic modeling of Menelaus transversals, spherical trigonometry, and Ceva duality:

.. code-block:: bash

   # Install within the GEOMETOR environment
   uv pip install -e .

.. code-block:: python

   import sympy as sp
   from geometor.menelaus.planar_transversal import construct_menelaus_planar
   from geometor.menelaus.spherical import SphericalTriangle

   # Symbolic planar transversal construction
   model = construct_menelaus_planar()
   print("Planar Menelaus verified over Q:", model is not None)

=================
GEOMETOR menelaus
=================

**Digital Scriptorium 4-Track Book Codex & Exact Symbolic Demonstrations for Menelaus of Alexandria (c. 70–140 CE)**

``geometor-menelaus`` combines a folio-verified, four-track **Book Codex** (``:layout: book``) of **Menelaus of Alexandria's** *Sphaerica* (*Sphaericorum Libri III*) with 100% exact ``SymPy`` and ``geometor.model`` symbolic proofs of the **Planar & Spherical Menelaus Transversal Theorem**, intrinsic spherical geometry, Wildberger Rational Trigonometry invariants, Converse collinearity constructions, and projective Ceva–Menelaus duality.

Public-Domain Primary Sources
=============================

All historical texts, apparatus registries, and original English translations derive strictly from pre-1929 public-domain witnesses inspected page-by-page from archival scans:

- **Edmond Halley (ed.) & George Costard (pref.)**, *Menelai Sphaericorum Libri III* (Oxford, *Sumptibus Academicis*, 1758) — diplomatic Latin witness restored from the Bodleian Huntington Hebrew manuscript (Jacob ben Machir's version of Isḥāq ibn Ḥunayn) collated against Arabic manuscripts.
- **Claudius Ptolemy**, *Syntaxis Mathematica* (*Almagest*) Book I, Chapter 13 (*ed.* J. L. Heiberg, Vol. I Part 1, Teubner, Leipzig, 1898, pp. 68–75) — earliest surviving polytonic Greek witness of both Planar and Spherical Menelaus (*chords of double arcs*).
- **Axel Anthon Björnbo**, *Studien über Menelaos' Sphärik. Beiträge zur Geschichte der Sphärik und Trigonometrie der Griechen* (Teubner, Leipzig, 1902).
- **Francesco Maurolico**, *Menelai Sphaericorum Libri III* (Messina, 1558) and **Pappus of Alexandria**, *Synagoge* Book VI (*ed.* F. Hultsch, Berlin, 1877).

Architecture
============

1. **4-Track Digital Scriptorium Book Codex** (``docsrc/sphaerica/``):

   - **Unit I** (*Book I, Defs. 1–6 & Props. I.1–I.38*): Intrinsic spherical triangles, dihedral angles, spherical angle-sum excess (:math:`A + B + C > 2\text{ right angles}`, Prop. I.11), and Menelaus's intrinsic proof of AAA spherical congruence (Prop. I.17).
   - **Unit II** (*Book II, Props. II.1–II.12*): Parallel circles, polar arcs, Menelaus's programmatic critique of Theodosius (Halley p. 75), and universal declination/right-ascension convexity (Prop. II.10 superseding Theodosius III.5, III.6, III.9).
   - **Unit III** (*Book III, Props. III.1–III.5 & Almagest I.13*): *Theorema Menelai* (*Figura Catha*), Halley's *Scholion* on chords vs. sines, *Lemma I* (Planar Menelaus), Ptolemy's polytonic Greek witness, Spherical Law of Sines (Prop. III.2), and Rule of Tangents (Prop. III.3).
   - **Unit IV** (*Book III, Props. III.6–III.25*): Spherical internal/external angle bisectors (Prop. III.6), spherical harmonic division & cross-ratio pencils (Prop. III.8), spherical incenter (Prop. III.9), and Menelaus's triple-transversal proof of spherical orthocenter concurrency via the orthic axis (Prop. III.10).

2. **100% Exact Symbolic Python Package** (``src/geometor/menelaus/``):

   - ``planar_transversal.py``: Targeted ``Model(..., auto_intersect=False)`` + ``@proposition`` Planar Menelaus with parallel auxiliary ``CH || DF``, universal polynomial converse, four Converse collinearity constructions (External Bisector Axis, Desargues's Axis, Pascal's *Hexagrammum Mysticum*, Monge's Exsimilicenters), and Rational Trigonometry quadrance/spread invariants.
   - ``spherical.py``: Exact 3D unit-sphere (:math:`x^2 + y^2 + z^2 = 1`) ``SphericalPoint``, ``GreatCircle``, ``SphericalTriangle``, rational spherical excess (:math:`\tan(E/2) = 1/17 > 0`), polar triangle AAA duality, Spherical Menelaus in both signed sines (``-1``) and Ptolemaic double-arc chords (``+1``), gnomonic projection equivalence, spherical cross-ratio pencil invariance, and spherical orthocenter concurrency.
   - ``duality_ceva.py``: Homogeneous :math:`\mathbb{P}^2` polarity between Menelaus collinearity (``-1``) and Ceva concurrency (``+1``), complete-quadrangle harmonic conjugation, and trilinear polars of Kimberling centers ``X(1)``, ``X(2)``, ``X(4)``, ``X(7)``.
   - ``render.py``, ``concordance.py``, ``sphinx_ext.py``, ``__main__.py``: Theme-adaptive ``.euclid-graphic`` SVG generator (10 interactive figures in ``docsrc/_static/figures/``), JSON apparatus loaders, and CLI verifier.

Quickstart & Verification
=========================

Using the workspace Python 3.13 environment:

.. code-block:: bash

   # Run full symbolic CLI report
   /home/phi/PROJECTS/geometor/.venv/bin/python -c "import sys; sys.path.insert(0, 'src'); from geometor.menelaus.__main__ import main; main()"

   # Regenerate all 10 interactive .euclid-graphic SVGs
   /home/phi/PROJECTS/geometor/.venv/bin/python scripts/build_figures.py

   # Run executable demos
   /home/phi/PROJECTS/geometor/.venv/bin/python demos/planar_menelaus_demo.py
   /home/phi/PROJECTS/geometor/.venv/bin/python demos/spherical_menelaus_demo.py
   /home/phi/PROJECTS/geometor/.venv/bin/python demos/ceva_menelaus_duality_demo.py

   # Run pytest, ruff, and Sphinx Book Codex build
   /home/phi/PROJECTS/geometor/.venv/bin/python -m pytest
   ruff check src scripts demos tests
   publish build

License
=======

MIT License — Copyright (c) GEOMETOR.

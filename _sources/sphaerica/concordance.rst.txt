:title: Concordantia — Cross-Tradition Proposition & Ecosystem Concordance
:layout: book

.. _concordance:

Concordantia Menelai (Cross-Tradition Concordance)
==================================================

.. rubric:: *Halley (1758) · Maurolico (1558) · Björnbo (1902) · Ptolemy Almagest I.13 (1898) · Euclid · GEOMETOR*

This master concordance aligns the principal definitions, lemmas, and propositions of :person:`Menelaus of Alexandria <menelaus>`'s *Sphaerica* across :person:`Edmond Halley <halley>`'s Oxford Latin edition (:cite:`1758 <halley-1758>`), :person:`Francesco Maurolico <maurolico>`'s Messina *editio princeps* (:cite:`1558 <maurolico-1558>`), :person:`Axel Anthon Björnbo <bjornbo>`'s critical analysis (:cite:`1902 <bjornbo-1902>`), :person:`Claudius Ptolemy <ptolemy>`'s Greek witnesses (:cite:`Heiberg 1898 <ptolemy-almagest-i-13>`), :person:`Euclid <euclid>`'s *Elements*, and sister GEOMETOR repositories.

.. list-table:: Master Concordance of Menelaus's *Sphaerica* & Transversal Legacy
   :header-rows: 1
   :widths: 10 18 14 18 18 22

   * - Codex Unit
     - Halley (1758)
     - Maurolico / Björnbo
     - Greek Witness
     - Euclidean Parallel / Contrast
     - GEOMETOR Constructive & Ecosystem Links
   * - :ref:`Unit I <unit-1-en>`
     - *Praefatio* [pp. i–viii]; Lib. I Def. I–VI [p. 1]
     - Maur. I Def. 1–6; Björnbo §3–§5
     - :person:`Pappus <pappus>` *Synagoge* VI (*τρίπλευρον*)
     - *Elements* I Def. 15–23; XI Def. 6, 18
     - :class:`~geometor.menelaus.spherical.SphericalTriangle`; ``geometor/euclid``
   * - :ref:`Unit I <unit-1-en>`
     - Lib. I Prop. 1 [p. 2]
     - Maur. I.1; Björnbo I.1
     - :person:`Theodosius <theodosius>` *Sphaerica* I–II
     - *Elements* I.23 (copy rectilinear angle)
     - ``elements:G.39``; :class:`~geometor.menelaus.spherical.GreatCircle`
   * - :ref:`Unit I <unit-1-en>`
     - Lib. I Prop. 4, 5, 8 [pp. 5–8]
     - Maur. I.4–5, 8; Björnbo I.4–5, 8
     - :person:`Proclus <proclus>` *In Eucl.* p. 345 (direct I.25)
     - *Elements* I.4 (SAS), I.20 / XI.20, I.8 (SSS), I.24–25
     - ``geometor/proclus``; intrinsic SAS/SSS congruence
   * - :ref:`Unit I <unit-1-en>`
     - **Lib. I Prop. 11** [p. 11]
     - Maur. I.11; Björnbo I.11
     - Antipodal lune *ΑΒΔΓ*
     - **Overturns** *Elements* I.16 & I.32 (:math:`A+B+C > \pi`)
     - :func:`~geometor.menelaus.spherical.spherical_excess_report`; ``geometor/hilbert``
   * - :ref:`Unit I <unit-1-en>`
     - **Lib. I Prop. 17** [pp. 18–19]
     - Maur. I.18; Björnbo I.17
     - Non-existence of non-congruent similar spherical triangles
     - **Contrasts** *Elements* VI.4 (planar AAA similarity)
     - :func:`~geometor.menelaus.spherical.polar_triangle` (AAA congruence)
   * - :ref:`Unit II <unit-2-en>`
     - Lib. II Prop. 1, 6–12 [pp. 48–79]
     - Maur. II.1–19; Björnbo II.1–12
     - :person:`Pappus <pappus>` *Synagoge* VI; *Theodosius* III.5–9
     - Euclid *Phaenomena* (rising-time arcs)
     - ``geometor/pappus`` (Book VI astronomical tradition)
   * - :ref:`Unit III <unit-3-en>`
     - **Lib. III Lemma I** [p. 83]
     - Maur. III Praem.; Björnbo §9
     - :cite:`Almagest I.13 <ptolemy-almagest-i-13>` (Heiberg pp. 68–70)
     - *Elements* I.31, VI.2, VI.4, VI.23
     - :func:`~geometor.menelaus.planar_transversal.construct_menelaus_planar`; ``geometor/altshiller-court`` Ch. VI
   * - :ref:`Unit III <unit-3-en>`
     - **Lib. III Prop. 1 & Scholion** [pp. 80–86]
     - Maur. III.1 (*Figura Catha*); Björnbo III.1
     - :cite:`Almagest I.13 <ptolemy-almagest-i-13>` (Heiberg pp. 74–76)
     - Central projection from sphere center onto planar transversal
     - :func:`~geometor.menelaus.spherical.verify_spherical_menelaus`, :func:`~geometor.menelaus.spherical.gnomonic_projection_menelaus`
   * - :ref:`Unit III <unit-3-en>`
     - Lib. III Prop. 2–5 [pp. 86–90]
     - Maur. III.2–6; Björnbo III.2–5
     - Applied in *Almagest* I.14–16 & II
     - Spherical Rule of Four Quantities & Law of Tangents
     - :func:`~geometor.menelaus.spherical.spherical_excess_report` (`sine_law_common_ratio`)
   * - :ref:`Unit IV <unit-4-en>`
     - **Lib. III Prop. 6–8** [pp. 91–94]
     - Maur. III.7–9; Björnbo III.6–8
     - Anticipates *Pappus* VII.129 cross-ratio invariance on :math:`S^2`!
     - *Elements* VI.3 & external angle-bisector ratio
     - :func:`~geometor.menelaus.planar_transversal.construct_external_bisector_axis`, :func:`~geometor.menelaus.spherical.verify_spherical_cross_ratio_invariance`; ``geometor/pappus``
   * - :ref:`Unit IV <unit-4-en>`
     - **Lib. III Prop. 9–10** [pp. 95–97]
     - Maur. III.10–11; Björnbo III.9–10
     - Complete spherical quadrilateral & altitude concurrency
     - *Elements* IV.4 (incenter) & orthic axis
     - :func:`~geometor.menelaus.spherical.spherical_orthocenter_menelaus`, :func:`~geometor.menelaus.duality_ceva.construct_trilinear_polar`; ``geometor/etc`` `X(1)`, `X(4)`, `X(7)`

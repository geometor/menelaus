:date: 2026-11-12
:type: log
:summary: Initial release of geometor-menelaus v0.1.0 — 4-track synchronized Book Codex of Menelaus's Sphaerica (Halley 1758 Latin & Heiberg 1898 Greek witnesses), 10 interactive .euclid-graphic SVGs, and exact SymPy / geometor.model proofs of Planar, Spherical, and Dual Menelaus theorems.

Initial Release: *Menelai Sphaericorum Libri III* Codex & Exact Symbolic Transversals
=====================================================================================

Established ``geometor/menelaus`` (``v0.1.0``) as a dual Digital Scriptorium Book Codex and exact symbolic geometry package:

- **Multimodal Scan-Verified 4-Track Book Codex**: Inspected the high-resolution archival page scans of :person:`Edmond Halley <halley>`'s *Menelai Sphaericorum Libri III* (:cite:`Oxford, 1758 <halley-1758>`, with :person:`George Costard <costard>`'s *Praefatio*), :person:`Claudius Ptolemy <ptolemy>`'s *Syntaxis Mathematica* I.13 (:cite:`ed. Heiberg, 1898 <ptolemy-almagest-i-13>`), and :person:`Axel Anthon Björnbo <bjornbo>`'s *Studien über Menelaos' Sphärik* (:cite:`Teubner, 1902 <bjornbo-1902>`), authoring a 100% original English translation paired with Latin/Greek diplomatic witnesses, analytical summaries, and mathematical notes across **Units I–IV**.
- **Exact Planar, Spherical & Projective Demonstrations**:

  - Verified Planar Menelaus via Euclidean parallel auxiliary ``CH || DF`` (signed ratio product ``-1``, unsigned ``+1``), universal polynomial converse, External Angle-Bisector Axis, Desargues's Axis, Pascal's *Hexagrammum Mysticum*, Monge's 3-Circle Similicenters, and Wildberger Rational Trigonometry quadrance/spread laws.
  - Built an exact 3D unit-sphere (:math:`x^2 + y^2 + z^2 = 1`) solver verifying positive spherical excess (:math:`\tan(E/2) = 1/17 > 0`, Prop. I.11), polar triangle duality and AAA spherical congruence (Prop. I.17), **Spherical Menelaus's Theorem** (Prop. III.1) in both Ptolemaic double-arc chords and sines, spherical cross-ratio pencil invariance (Prop. III.8), and spherical orthocenter concurrency (Prop. III.10).
  - Formalized projective :math:`\mathbb{P}^2` polarity and complete-quadrangle harmonic conjugation pairing Ceva triples (``+1``) with Menelaus trilinear polars (``-1``) across ``X(1)``, ``X(2)``, ``X(4)``, and ``X(7)``.

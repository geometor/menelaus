:navigation: header
:order: 10
:nav_title: About

.. _about:
.. _about-index:

About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

``geometor.menelaus`` establishes a definitive Digital Scriptorium edition of **Menelaus of Alexandria's** (*c.* 70–140 CE) groundbreaking three-book treatise *Sphaerica* (*Sphaericorum Libri III*). Menelaus marks a pivotal turning point in Hellenistic mathematics: by emancipating spherical geometry from three-dimensional solid stereometry, he was the first to define the intrinsic **spherical triangle** (*triangulum sphaericum*) bounded by great-circle arcs, proving positive **spherical excess** (:math:`A + B + C > \pi`, Prop. I.11) and **AAA spherical triangle congruence** (Prop. I.17) independently of Euclid's Fifth Postulate.

Through this digital edition, the lost architectural core of Menelaus's treatise is recovered and structured into machine-addressable semantic elements. The edition presents scan-verified Latin texts from **Edmond Halley's** critical Oxford edition (*Menelai Sphaericorum Libri III*, 1758, overseen by George Costard) alongside the surviving polytonic Greek text of the Menelaus Transversal Lemma preserved in **Claudius Ptolemy's** *Syntaxis Mathematica* I.13 (ed. J. L. Heiberg, 1898) and the philological stemma established by **Axel Anthon Björnbo** (*Studien über Menelaos' Sphärik*, 1902). Accompanying these primary witnesses is a modern English translation, complete with step-by-step mathematical formalization, interactive ``.euclid-graphic`` SVG diagrams, and dynamic 3D unit-sphere projections.

Within the wider GEOMETOR ecosystem, Menelaus's transversal theorem forms the historical and projective link connecting the planar foundations of Euclid's *Elements* (:external+elements:doc:`index`), the projective cross-ratio pencils of Pappus of Alexandria's *Synagoge* Book VII (:external+pappus:doc:`index`), the modern triangle transversals of the *Encyclopedia of Triangle Centers* (:external+etc:doc:`index`), and the operational complexity measures of Émile Lemoine's *Géométrographie* (``geometor.lemoine``). Every planar, rational-trigonometric, unit-sphere, and projective :math:`\mathbb{P}^2` Ceva–Menelaus duality configuration is formalized symbolically in ``geometor.model`` over exact algebraic number fields.

The GEOMETOR Mission
--------------------

The GEOMETOR project, conceived and directed by **phi ARCHITECT**, is dedicated to a multi-generational synthesis of geometry, computation, and symbolic reasoning. At its core, the project operates across three foundational pillars:

Extracting Historical Semantic Knowledge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Moving beyond passive page scans and superficial OCR, GEOMETOR recovers the living deductive architecture of more than 2,300 years of geometric, axiomatic, and philosophical treatises. From ancient Greek codices and Renaissance folios to nineteenth-century synthetic treatises, our Digital Scriptorium elevates prose, marginal citations, primary-source folios (via ``publish folio``), and calibrated Ink-to-Vector ``.euclid-graphic`` diagrams into structured, machine-addressable semantic knowledge graphs. Every proposition, step, enunciation, and justification is isolated, verified, and interconnected across history.

Exact Symbolic Grounding (``geometor.model``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Geometry in GEOMETOR is never approximated through floating-point fuzz or numerical instability. Constructions are anchored in 100% exact symbolic algebra via `SymPy` and Norman Wildberger's Rational Trigonometry invariants (quadrance, spread, and cross-ratio) over exact algebraic number fields. By eliminating rounding errors entirely, geometric configurations retain absolute fidelity, allowing geometric proofs, collinearities, and concyclicities to be verified symbolically with mathematical certainty.

Repurposing Knowledge Across Mediums
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The extracted semantic graphs and exact algebraic models are re-deployed across a unified computational medium: synchronized multi-track **Book Codices** and EPUB 3 editions published with `photon-platform/publish`; computable deductive canons (such as ``geometor.elements``, ``geometor.etc``, ``geometor.pappus``, and ``geometor.divine``); interactive SVG laboratories powered by ``geometor.explorer``; ultra-high-definition (QHD) visual broadcasts; and neuro-symbolic program synthesis guided by ``geometor.seer`` across `geometor.com <https://geometor.com>`_.

Sources, Provenance & Methodology
---------------------------------

The textual transmission of Menelaus's *Sphaerica* is among the most dramatic survivals in the history of mathematics: the continuous ancient Greek text was lost in late antiquity, surviving only through medieval Arabic and Hebrew translations, Renaissance reconstructions, and eighteenth-century scholarly collation. This edition relies on four public-domain primary witnesses:

* **Edmond Halley**, *Menelai Sphaericorum Libri III* (Oxford: Clarendon Press, 1758; preface by George Costard), established from Hebrew and Arabic manuscripts preserved in the Bodleian Library.
* **Claudius Ptolemy**, *Syntaxis Mathematica* (Almagest) Book I, Chapter 13 (ed. J. L. Heiberg, Leipzig: Teubner, 1898), preserving the oldest extant continuous Greek text of the Menelaus Transversal Theorem.
* **Francesco Maurolico**, *Sphaericorum Menelai Libri III* in *Theodosii Sphaericorum Elementorum Libri III...* (Messina: Petrus Spira, 1558), offering the first Renaissance Latin reconstruction.
* **Axel Anthon Björnbo**, *Studien über Menelaos' Sphärik: Beiträge zur Geschichte der Sphärik und Trigonometrie bei den Griechen* (Leipzig: B. G. Teubner, 1902), providing the comprehensive twentieth-century stemmatic and philological analysis.

Child Essays & Monographic Studies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* :ref:`Menelaus of Alexandria (c. 70–140 CE): Life, Works & Roman Observations <about-menelaus>`
* :ref:`Textual Transmission: Lost Greek, Arabic, Hebrew, Maurolico (1558), Halley (1758) & Björnbo (1902) <about-transmission>`
* :ref:`Intrinsic Spherical Geometry vs. Euclid's Planar Elements <about-intrinsic-spherical>`

.. toctree::
   :maxdepth: 1
   :hidden:

   menelaus-of-alexandria
   transmission-history
   intrinsic-spherical-geometry

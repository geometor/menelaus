:layout: book
:order: 11
:canonical_id: III.10
:breadcrumb_title: Proposition III.10 (Notes)
:folio: halley_1758_menelai_sphaericorum:0111
:tracks: English: index | Latin: la | Summary: summary | Notes: notes

.. _sphaerica-iii-10-notes:

Scholarly & GEOMETOR Notes: Orthocenter Concurrency & Projective Duality
========================================================================

.. rubric:: *Exact Vector Proofs, Collinearities & Trilinear Polarity*

.. folio:: halley_1758_menelai_sphaericorum:0111
   :page: 95

1. Exact Symbolic Proof of Spherical Orthocenter Concurrency
-------------------------------------------------------------

In :func:`~geometor.menelaus.spherical.spherical_orthocenter_menelaus`, Menelaus's three-transversal proof of *Sphaerica* III.10 (`[§4.4]`, Halley pp. 95–97) is verified algebraically on :math:`S^2(\mathbb{Q})` alongside the concise Lagrange vector-triple-product identity for altitude normals :math:`\mathbf{m}_A = (\mathbf{B} \times \mathbf{C}) \times \mathbf{A}`, :math:`\mathbf{m}_B = (\mathbf{C} \times \mathbf{A}) \times \mathbf{B}`, :math:`\mathbf{m}_C = (\mathbf{A} \times \mathbf{B}) \times \mathbf{C}`:

.. math::

   \mathbf{m}_A + \mathbf{m}_B + \mathbf{m}_C \;\equiv\; \mathbf{0}
   \quad\Longleftrightarrow\quad
   \det(\mathbf{m}_A, \mathbf{m}_B, \mathbf{m}_C) \;=\; 0,

and the spherical orthocenter :math:`\mathbf{H} \propto \mathbf{m}_A \times \mathbf{m}_B` satisfies exact dihedral orthogonality :math:`(\mathbf{A}\times\mathbf{H})\cdot(\mathbf{B}\times\mathbf{C}) = (\mathbf{B}\times\mathbf{H})\cdot(\mathbf{C}\times\mathbf{A}) = (\mathbf{C}\times\mathbf{H})\cdot(\mathbf{A}\times\mathbf{B}) = 0` on all three sides simultaneously. Remarkably, Menelaus's auxiliary great circle :math:`E\Delta\Theta` joining altitude feet :math:`\Delta` and :math:`E` is literally the **orthic axis**—the :term:`trilinear polar <polaris-trilinearis>` of the orthocenter :math:`Z`!

2. Converse of Menelaus Collinearity Gallery
--------------------------------------------

.. picture:: /_static/figures/menelaus-pascal-hexagram.svg
   :alt: Pascal's Hexagrammum Mysticum proved via three applications of Planar Menelaus
   :caption: Pascal's Hexagrammum Mysticum: opposite-side intersections L, M, and N of six rational points on a circle align on Pascal's Mystic Line via triple Menelaus on diagonal triangle △UVW.

In :mod:`geometor.menelaus.planar_transversal`:

* **Pascal's Hexagrammum Mysticum** (:func:`~geometor.menelaus.planar_transversal.construct_pascal_hexagram`, cf. ``geometor/pappus``): on circle :g:`( O P1 )` with rational vertices :g:`P1`, :g:`P2`, :g:`P3`, :g:`P4`, :g:`P5`, :g:`P6` and diagonal triangle :g:`U`, :g:`V`, :g:`W`, three applications of Planar Menelaus combined with Euclid III.35/36 chord-power identities cancel to :math:`-1`, aligning opposite-side intersections :g:`L`, :g:`M`, :g:`N` on Pascal's Mystic Line :g:`LM <[ L M ]>`.
* **Desargues's Two-Triangle Theorem** (:func:`~geometor.menelaus.planar_transversal.construct_desargues_axis`): proved via three Menelaus applications on perspective ray-triangles.
* **Monge's Three-Circle Theorem** (:func:`~geometor.menelaus.planar_transversal.construct_monge_exsimilicenters`): proved via :math:`(-r_A/r_B)(-r_B/r_C)(-r_C/r_A) = -1`.

3. Projective Menelaus–Ceva Duality & ETC Trilinear Polars
----------------------------------------------------------

In :func:`~geometor.menelaus.duality_ceva.construct_trilinear_polar`, concurrent cevians through perspector :g:`P` meet the sides of :g:`△ABC << A B C >>` at :g:`Dc`, :g:`Ec`, :g:`Fc` (:math:`\text{Ceva product} = +1`). Intersecting the cevian-triangle sides with the extended sides of :g:`△ABC << A B C >>` produces the harmonic conjugates :g:`Dm`, :g:`Em`, :g:`Fm`, flipping all three signs :math:`(-1)^3(+1) = -1` onto the :term:`trilinear polar <polaris-trilinearis>` :g:`DmEm <[ Dm Em ]>`:

* :func:`~geometor.menelaus.duality_ceva.verify_projective_menelaus_ceva_duality` proves that under homogeneous point-line polarity :math:`[x : y : z] \leftrightarrow xX + yY + zZ = 0` in :math:`\mathbb{P}^2`, :person:`Menelaus <menelaus>`'s **collinearity of three side-cuts** (:math:`-1`) and :person:`Giovanni Ceva <ceva>`'s **concurrency of three vertex-joins** (:math:`+1`) are algebraically dual theorems!
* :func:`~geometor.menelaus.duality_ceva.etc_trilinear_polar_catalogue` connects directly to Kimberling triangle centers:
  - ``X(1)`` (**Incenter**): trilinear polar is the **anti-orthic / external-bisector axis**.
  - ``X(2)`` (**Centroid**): trilinear polar is the **line at infinity** :math:`[0 : 0 : 1]`.
  - ``X(4)`` (**Orthocenter**): trilinear polar is the **orthic axis**—the exact planar counterpart of Menelaus's line :math:`E\Delta\Theta` in *Sphaerica* Prop. III.10!
  - ``X(7)`` (**Gergonne Point**): trilinear polar is the **incircle chordal / Gergonne axis**.

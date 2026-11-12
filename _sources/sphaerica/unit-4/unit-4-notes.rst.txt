:title: Unit IV — GEOMETOR Notes: Converse Gallery, Orthocenter & Ceva–Menelaus Duality
:layout: book

.. _unit-4-notes:

Unit IV — Scholarly & GEOMETOR Symbolic Commentary
==================================================

.. rubric:: *From Menelaus III.6–III.10 to Converse Collinearities & Projective Trilinear Polarity*

1. Exact Symbolic Proof of Spherical Orthocenter Concurrency (*Prop. III.10*)
-----------------------------------------------------------------------------

In :func:`~geometor.menelaus.spherical.spherical_orthocenter_menelaus`, Menelaus's three-transversal proof of *Sphaerica* III.10 (`[§4.4]`, Halley pp. 95–97) is verified algebraically on :math:`S^2(\mathbb{Q})` alongside the concise Lagrange vector-triple-product identity for altitude normals :math:`\mathbf{m}_A = (\mathbf{B} \times \mathbf{C}) \times \mathbf{A}`, :math:`\mathbf{m}_B = (\mathbf{C} \times \mathbf{A}) \times \mathbf{B}`, :math:`\mathbf{m}_C = (\mathbf{A} \times \mathbf{B}) \times \mathbf{C}`:

.. math::

   \mathbf{m}_A + \mathbf{m}_B + \mathbf{m}_C \;\equiv\; \mathbf{0}
   \quad\Longleftrightarrow\quad
   \det(\mathbf{m}_A, \mathbf{m}_B, \mathbf{m}_C) \;=\; 0,

and the spherical orthocenter :math:`\mathbf{H} \propto \mathbf{m}_A \times \mathbf{m}_B` satisfies exact dihedral orthogonality :math:`(\mathbf{A}\times\mathbf{H})\cdot(\mathbf{B}\times\mathbf{C}) = (\mathbf{B}\times\mathbf{H})\cdot(\mathbf{C}\times\mathbf{A}) = (\mathbf{C}\times\mathbf{H})\cdot(\mathbf{A}\times\mathbf{B}) = 0` on all three sides simultaneously. Remarkably, Menelaus's auxiliary great circle ``ΕΔΘ`` joining the altitude feet ``Δ`` and ``Ε`` is literally the **orthic axis**—the :term:`trilinear polar <polaris-trilinearis>` of the orthocenter ``Ζ``!

2. Converse of Menelaus Collinearity Gallery (:mod:`geometor.menelaus.planar_transversal`)
------------------------------------------------------------------------------------------

Menelaus's external bisector theorem (*Prop. III.6*, `[§4.1]`) and harmonic transversal methods blossom into four classic projective collinearity theorems proved in :mod:`geometor.menelaus.planar_transversal` via the **Converse of Menelaus** (:math:`\text{signed product} = -1`):

.. picture:: /_static/figures/menelaus-external-bisectors.svg
   :alt: External Angle-Bisector Axis of a scalene Heronian triangle proved by Converse of Menelaus
   :caption: External Angle-Bisector Axis (planar counterpart of Sphaerica Prop. III.6): external bisector feet De, Ee, and Fe of Heronian △ABC lie on the anti-orthic axis (trilinear polar of incenter I).

* **External Angle-Bisector Axis** (:func:`~geometor.menelaus.planar_transversal.construct_external_bisector_axis`, planar counterpart of *Sphaerica* Prop. III.6): on Heronian :g:`△ABC << A B C >>` (:math:`a=7, b=20, c=15`, incenter :g:`I`), the external bisector feet :g:`De`, :g:`Ee`, :g:`Fe` satisfy :math:`(-c/a)(-b/c)(-a/b) = -1` and lie on the anti-orthic axis :g:`DeEe <[ De Ee ]>` (the trilinear polar of :g:`I`!).

.. picture:: /_static/figures/menelaus-pascal-hexagram.svg
   :alt: Pascal's Hexagrammum Mysticum proved via three applications of Planar Menelaus
   :caption: Pascal's Hexagrammum Mysticum: opposite-side intersections L, M, and N of six rational points on a circle align on Pascal's Mystic Line via triple Menelaus on diagonal triangle △UVW.

* **Pascal's Hexagrammum Mysticum** (:func:`~geometor.menelaus.planar_transversal.construct_pascal_hexagram`, cf. ``geometor/pappus``): on circle :g:`( O P1 )` with rational vertices :g:`P1`, :g:`P2`, :g:`P3`, :g:`P4`, :g:`P5`, :g:`P6` and diagonal triangle :g:`U`, :g:`V`, :g:`W`, three applications of Planar Menelaus combined with Euclid III.35/36 chord-power identities cancel to :math:`-1`, aligning opposite-side intersections :g:`L`, :g:`M`, :g:`N` on Pascal's Mystic Line :g:`LM <[ L M ]>`.

Alongside these two constructions, :func:`~geometor.menelaus.planar_transversal.construct_desargues_axis` proves **Desargues's Two-Triangle Theorem** via three Menelaus applications on perspective ray-triangles, and :func:`~geometor.menelaus.planar_transversal.construct_monge_exsimilicenters` proves **Monge's Three-Circle Theorem** via :math:`(-r_A/r_B)(-r_B/r_C)(-r_C/r_A) = -1` (see :ref:`Symbolic Demonstrations <demos-index>` for all 10 interactive figures).

3. Projective Menelaus–Ceva Duality & ETC Trilinear Polars (:mod:`geometor.menelaus.duality_ceva`)
--------------------------------------------------------------------------------------------------

.. picture:: /_static/figures/menelaus-ceva-trilinear-polar.svg
   :alt: Complete quadrangle harmonic conjugation turning Ceva concurrence (+1) into Menelaus collinearity (-1)
   :caption: Ceva–Menelaus Harmonic Duality: harmonic conjugates Dm, Em, and Fm of concurrent cevian traces Dc, Ec, and Fc align on the trilinear polar of perspector P.

In :func:`~geometor.menelaus.duality_ceva.construct_trilinear_polar`, concurrent cevians through perspector :g:`P` meet the sides of :g:`△ABC << A B C >>` at :g:`Dc`, :g:`Ec`, :g:`Fc` (:math:`\text{Ceva product} = +1`). Intersecting the cevian-triangle sides :g:`EcFc <[ Ec Fc ]>`, :g:`FcDc <[ Fc Dc ]>`, :g:`DcEc <[ Dc Ec ]>` with the extended sides of :g:`△ABC << A B C >>` produces the harmonic conjugates :g:`Dm`, :g:`Em`, :g:`Fm`, flipping all three signs :math:`(-1)^3(+1) = -1` onto the :term:`trilinear polar <polaris-trilinearis>` :g:`DmEm <[ Dm Em ]>`! In :mod:`geometor.menelaus.duality_ceva`:

- :func:`~geometor.menelaus.duality_ceva.verify_projective_menelaus_ceva_duality` proves that under homogeneous point-line polarity :math:`[x : y : z] \leftrightarrow xX + yY + zZ = 0` in :math:`\mathbb{P}^2`, :person:`Menelaus <menelaus>`'s **collinearity of three side-cuts** (:math:`-1`) and :person:`Giovanni Ceva <ceva>`'s **concurrency of three vertex-joins** (:math:`+1`, :cite:`De lineis rectis, 1678 <ceva-1678>`) are algebraically dual theorems!
- :func:`~geometor.menelaus.duality_ceva.etc_trilinear_polar_catalogue` connects directly to ``geometor/etc`` across four canonical Kimberling centers on the integer-incenter Heronian triangle :math:`(15, 7, 20)`:

  * ``X(1)`` (**Incenter**): trilinear polar is the **anti-orthic / external-bisector axis**!
  * ``X(2)`` (**Centroid**): trilinear polar is the **line at infinity** :math:`[0 : 0 : 1]` in :math:`\mathbb{P}^2` (medial sides are parallel to reference sides!).
  * ``X(4)`` (**Orthocenter**): trilinear polar is the **orthic axis**—the exact planar counterpart of Menelaus's line ``ΕΔΘ`` in *Sphaerica* Prop. III.10!
  * ``X(7)`` (**Gergonne Point**): trilinear polar is the **incircle chordal / Gergonne axis**!

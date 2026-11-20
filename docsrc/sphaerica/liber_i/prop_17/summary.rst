:layout: book
:order: 10
:canonical_id: I.17
:breadcrumb_title: Proposition I.17 (Summary)
:folio: halley_1758_menelai_sphaericorum:0034
:tracks: English: index | Latin: la | Summary: summary | Notes: notes

.. _sphaerica-i-17-summary:

Analytical Summary: AAA Congruence & Scale Invariance Failure
=============================================================

.. rubric:: *Deductive Architecture of Proposition I.17*

.. folio:: halley_1758_menelai_sphaericorum:0034
   :page: 18

1. **Failure of Planar Similarity (Contrast Euclid Elements VI.4)**:
   In Euclidean planar geometry, two equiangular triangles are similar (:math:`\triangle ABC \sim \triangle DEF`), but not necessarily congruent: their sides are merely proportional, allowing arbitrary scale magnification or dilation by a continuous parameter :math:`k \in \mathbb{R}_{> 0}`. On the sphere :math:`S^2`, scale invariance fails completely: two equiangular triangles must be strictly congruent!

2. **Menelaus's Primal Sphere Construction**:
   Rather than appealing to polar triangle duality, Menelaus executes a direct intrinsic proof:
   - Reflects :math:`\triangle \Delta EZ` vertically across vertex :math:`B` by setting :math:`BI = \Delta E` and :math:`B\Theta = EZ`.
   - Produces :math:`I\Theta` to meet side :math:`A\Gamma` produced at :math:`K`.
   - By SAS congruence (Proposition I.4), :math:`\triangle BI\Theta \cong \triangle E\Delta Z`, giving :math:`I\Theta = \Delta Z`, :math:`\angle I = \angle A`, and :math:`\angle \Theta = \angle \Gamma`.
   - Applying Proposition I.10 to :math:`\triangle \Theta K\Gamma` forces :math:`K\Theta + K\Gamma = \pi`.
   - Applying Proposition I.10 to :math:`\triangle AIK` forces :math:`AK + KI = \pi`.
   - Equating the two semicircle sums and subtracting common arcs leaves :math:`\Theta I = A\Gamma` identically, forcing :math:`A\Gamma = \Delta Z` and yielding full congruence by ASA (Proposition I.14)!

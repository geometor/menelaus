:layout: book
:order: 1
:canonical_id: III.1
:breadcrumb_title: Proposition III.1 (Summary)
:folio: halley_1758_menelai_sphaericorum:0096
:tracks: English: index | Latin: la | Summary: summary | Notes: notes

.. _sphaerica-iii-1-summary:

Analytical Summary: Gnomonic Reduction & the Transversal Metric
===============================================================

.. rubric:: *Modern Elements-2.0 Decomposition of Proposition III.1*

.. folio:: halley_1758_menelai_sphaericorum:0096
   :page: 80

1. Synthetic Architecture
-------------------------

* **Given**:
  - Unit sphere :math:`S^2` centered at :math:`B`.
  - Two great-circle arcs :math:`NME` and :math:`NA\Lambda` meeting at :math:`N`.
  - Two transversal great-circle arcs :math:`E\Theta A` and :math:`\Lambda\Theta M` meeting at :math:`\Theta`.
* **Demonstrate**:
  The compounded sine ratio:

  .. math::

     \frac{\sin \widehat{AN}}{\sin \widehat{A\Lambda}}
     \;=\;
     \frac{\sin \widehat{NE}}{\sin \widehat{EM}}
     \cdot
     \frac{\sin \widehat{M\Theta}}{\sin \widehat{\Theta\Lambda}}.

2. The Three Deductive Steps
----------------------------

1. **Central Projection to Secant Plane**:
   - Connecting the sphere center :math:`B` with great circles creates plane pencils.
   - The chords :math:`\Lambda N, \Lambda M, MN` form a planar triangle :math:`\triangle N\Lambda M` in 3-space.
   - The radius :math:`AB` meets :math:`N\Lambda` at :math:`\Sigma`.
   - The radius :math:`\Theta B` meets :math:`M\Lambda` at :math:`\Delta`.
   - The transversal chord :math:`\Delta\Sigma` produced meets :math:`MN` produced at :math:`K`.
   - By Euclid *Elements* XI.3, :math:`K` lies in the plane intersection line :math:`KEB`.
2. **Application of Planar Menelaus (*Lemma I*)**:
   - Triangle :math:`\triangle N\Lambda M` is cut by straight transversal line :math:`\Sigma\Delta K`.
   - By Lemma I, :math:`N\Sigma : \Sigma\Lambda = (NK : KM) \cdot (M\Delta : \Delta\Lambda)`.
3. **Translation from Chords to Arc Sines (*Lemma II*)**:
   - Perpendiculars dropped from :math:`N` and :math:`M` onto diameter :math:`KEB` are proportional to the chord segments :math:`NK : KM` and equal to :math:`\sin \widehat{NE} : \sin \widehat{EM}`.
   - Likewise :math:`N\Sigma : \Sigma\Lambda = \sin \widehat{NA} : \sin \widehat{A\Lambda}`, and :math:`M\Delta : \Delta\Lambda = \sin \widehat{M\Theta} : \sin \widehat{\Theta\Lambda}`.
   - Substituting these yields the exact spherical theorem.

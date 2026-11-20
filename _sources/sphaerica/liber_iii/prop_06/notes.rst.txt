:layout: book
:order: 8
:canonical_id: III.6
:breadcrumb_title: Proposition III.6 (Notes)
:folio: halley_1758_menelai_sphaericorum:0107
:tracks: English: index | Latin: la | Summary: summary | Notes: notes

.. _sphaerica-iii-6-notes:

Scholarly & GEOMETOR Notes: External Bisector Axis & Trilinear Polarity
=======================================================================

.. rubric:: *Planar and Spherical Connections in geometor.menelaus*

.. folio:: halley_1758_menelai_sphaericorum:0107
   :page: 91

1. Planar Counterpart: External Angle-Bisector Axis
---------------------------------------------------

The planar version of Proposition III.6 states that the internal and external bisectors of a triangle divide the sides in the ratio of the adjacent sides (Euclid *Elements* VI.3).

In :func:`~geometor.menelaus.planar_transversal.construct_external_bisector_axis`, on Heronian :g:`△ABC << A B C >>` (:math:`a=7, b=20, c=15`, incenter :g:`I`), the external bisector feet :g:`De`, :g:`Ee`, :g:`Fe` satisfy:

.. math::

   \left(-\frac{c}{a}\right) \left(-\frac{a}{b}\right) \left(-\frac{b}{c}\right) \;=\; -1.

By the **Converse of the Menelaus Theorem**, the three external bisector feet are collinear, forming the **anti-orthic axis**—the trilinear polar of the incenter :math:`I = X(1)`.

2. Role in Menelaus's Deductive Progression
-------------------------------------------

Proposition III.6 is the essential engine that drives the second half of Book III:
- **Prop. III.8**: Combines internal and external bisectors at a right angle to establish harmonic division.
- **Prop. III.9**: Applies internal bisectors to prove the concurrence of angle bisectors at the incenter.
- **Prop. III.10**: Uses Prop. III.6 and its converse to prove that the three altitudes concur at the orthocenter.

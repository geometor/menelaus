:layout: book
:order: 9
:canonical_id: III.8
:breadcrumb_title: Proposition III.8 (Notes)
:folio: halley_1758_menelai_sphaericorum:0109
:tracks: English: index | Latin: la | Summary: summary | Notes: notes

.. _sphaerica-iii-8-notes:

Scholarly & GEOMETOR Notes: Pappus's Cross-Ratio Invariance & Modern Projective Geometry
========================================================================================

.. rubric:: *From Menelaus III.8 to Pappus Synagoge VII and Modern S² Cross-Ratios*

.. folio:: halley_1758_menelai_sphaericorum:0109
   :page: 93

1. Pappus of Alexandria's Generalization
----------------------------------------

In Book VII of the *Mathematical Collection* (*Synagoge*, c. 320 CE; :cite:`ed. Hultsch, 1877 <pappus-hultsch-1877>`), :person:`Pappus of Alexandria <pappus>` generalized Menelaus's harmonic division into the universal invariance of the 4-point cross-ratio under central projection.

Where Menelaus proved the harmonic case (cross-ratio :math:`-1`), Pappus proved that any pencil of four lines cut by two transversals produces equal cross-ratios.

2. Exact Verification in geometor.menelaus.spherical
----------------------------------------------------

In :func:`~geometor.menelaus.spherical.verify_spherical_cross_ratio_invariance`:

* Four great circles concurrent at vertex :math:`V` cut two oblique great-circle transversals :math:`\ell_1` and :math:`\ell_2` at points :math:`(X_1, X_2, X_3, X_4)` and :math:`(Y_1, Y_2, Y_3, Y_4)`.
* Computing the spherical sine cross-ratio:

  .. math::

     (X_1, X_2; X_3, X_4)
     \;=\;
     \frac{\sin\widehat{X_1 X_3} \cdot \sin\widehat{X_2 X_4}}{\sin\widehat{X_2 X_3} \cdot \sin\widehat{X_1 X_4}}
     \;=\;
     \frac{\sin\widehat{Y_1 Y_3} \cdot \sin\widehat{Y_2 Y_4}}{\sin\widehat{Y_2 Y_3} \cdot \sin\widehat{Y_1 Y_4}}
     \;=\; -2,

  confirming exact invariance across arbitrary oblique transversals on :math:`S^2`.

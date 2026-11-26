:layout: book
:order: 9
:canonical_id: III.8
:breadcrumb_title: Proposition III.8
:folio: halley_1758_menelai_sphaericorum:0109
:tracks: English: index | Latin: la | Summary: summary | Notes: notes

.. _liber-iii-prop-08:
.. _sphaerica-iii-8:

Proposition III.8 — Spherical Harmonic Division & Pencils
=========================================================

.. rubric:: *Menelai Alexandrini Sphaericorum Lib. III Prop. VIII. Theor. (Halley 1758, pp. 93–95)*

.. folio:: halley_1758_menelai_sphaericorum:0109
   :page: 93

Proposition III.8 — Theorem: Spherical Harmonic Division (pp. 93–94)
--------------------------------------------------------------------

.. admonition:: Enunciation (*Halley 1758, p. 93*)

   *If from the right angle of a right-angled spherical triangle two arcs be drawn to the base containing equal angles with one of its legs: the sine of the arc compounded of the base and the arc adjoined to it shall be to the sine of that adjoined arc itself, as the sine of the segment of the base adjacent to the other leg of the triangle is to the sine of the remaining segment of the base; and conversely.*

.. picture:: /_static/figures/spherical-cross-ratio-pencil.svg
   :alt: Pencil of four great circles concurrent at V cutting two oblique transversals with invariant sine cross-ratio
   :caption: Spherical pencil invariance (generalizing Sphaerica Prop. III.8 & Pappus Synagoge VI/VII): four great circles concurrent at vertex V cut two oblique transversals with identical spherical sine cross-ratio −2.

Four great circles concurrent at vertex :g:`V` cut great circles :g:`X1X4 <[ X1 X4 ]>` and :g:`Y1Y4 <[ Y1 Y4 ]>` in four-tuples (:g:`X1`, :g:`X2`, :g:`X3`, :g:`X4`) and (:g:`Y1`, :g:`Y2`, :g:`Y3`, :g:`Y4`) having identical spherical sine cross-ratio :math:`-2` (and :math:`-1` in the harmonic right-angle bisector case).

**[§4.2 · Proof & Double Converse, Halley pp. 93–95]** Let :math:`\triangle \mathrm{AB\Gamma}` have angle :math:`\angle \mathrm{B}` right (:math:`\mathrm{BA} \perp \mathrm{B\Gamma}`), and from :math:`\mathrm{B}` let two arcs :math:`\mathrm{B\Delta}` (internal) and :math:`\mathrm{BE}` (external) make equal angles :math:`\angle \mathrm{AB\Delta} = \angle \mathrm{ABE}` with :math:`\mathrm{AB}`:

1. **Harmonic Sine Proportion**:
   Because :math:`\angle \mathrm{AB\Gamma}` is right while :math:`\angle \mathrm{AB\Delta} = \angle \mathrm{ABE}`, leg :math:`\mathrm{B\Gamma}` bisects the supplementary angle adjacent to :math:`\angle \mathrm{EB\Delta}`, while :math:`\mathrm{BA}` bisects :math:`\angle \mathrm{EB\Delta}` itself! Applying **Proposition III.6** twice to :math:`\triangle \mathrm{EB\Delta}` (with internal bisector :math:`\mathrm{BA}` and external bisector :math:`\mathrm{B\Gamma}`) yields :math:`\sin \widehat{\mathrm{BE}} : \sin \widehat{\mathrm{B\Delta}} = \sin \widehat{\mathrm{E\Gamma}} : \sin \widehat{\mathrm{\Gamma\Delta}}` and :math:`\sin \widehat{\mathrm{BE}} : \sin \widehat{\mathrm{B\Delta}} = \sin \widehat{\mathrm{EA}} : \sin \widehat{\mathrm{A\Delta}}`. Equating and alternating (*permutando*):

   .. math::

      \frac{\sin \widehat{\mathrm{\Gamma E}}}{\sin \widehat{\mathrm{EA}}}
      \;=\;
      \frac{\sin \widehat{\mathrm{\Gamma\Delta}}}{\sin \widehat{\mathrm{\Delta A}}},

   the exact spherical :term:`harmonic conjugate <sectio-harmonica>` law!
2. **First Converse (p. 94)**:
   If :math:`\sin \widehat{\mathrm{\Gamma E}} : \sin \widehat{\mathrm{EA}} = \sin \widehat{\mathrm{\Gamma\Delta}} : \sin \widehat{\mathrm{\Delta A}}` and :math:`\angle \mathrm{EBA} = \angle \mathrm{AB\Delta}`, then :math:`\mathrm{B\Gamma}` bisects the exterior angle adjacent to :math:`\angle \mathrm{EB\Delta}`, forcing :math:`\angle \mathrm{AB\Gamma}` to be a **right angle**!
3. **Second Converse (pp. 94–95)**:
   Conversely, if :math:`\sin \widehat{\mathrm{\Gamma E}} : \sin \widehat{\mathrm{EA}} = \sin \widehat{\mathrm{\Gamma\Delta}} : \sin \widehat{\mathrm{\Delta A}}` and :math:`\angle \mathrm{AB\Gamma}` is a **right angle**, then :math:`\angle \mathrm{EBA} = \angle \mathrm{AB\Delta}`! (Both converses become the engine of Menelaus's orthocenter proof in Prop. III.10!)

.. picture:: 0110.g1.svg
   :alt: Calibrated vector diagram for folio 0110.g1

.. picture:: 0110.g1.png
   :alt: Archival scan of folio 0110.g1

.. picture:: 0110.g2.svg
   :alt: Calibrated vector diagram for folio 0110.g2

.. picture:: 0110.g2.png
   :alt: Archival scan of folio 0110.g2

.. toctree::
   :hidden:

   la
   summary
   notes

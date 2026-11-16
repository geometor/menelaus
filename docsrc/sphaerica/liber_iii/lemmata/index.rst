:layout: book
:order: 3
:canonical_id: III.lemmata
:breadcrumb_title: Lemmata I & II
:folio: halley_1758_menelai_sphaericorum:0099
:tracks: English: index | Latin: la | Summary: summary | Notes: notes

.. _liber-iii-lemmata:
.. _sphaerica-iii-lemmata:

Lemmata I & II — Planar Transversal & Chord-Sine Projection
===========================================================

.. rubric:: *Menelai Sphaericorum Lib. III Lemmata Duo (Halley 1758, pp. 83–84)*

.. folio:: halley_1758_menelai_sphaericorum:0099
   :page: 83

Lemma I — The Planar Menelaus Transversal Theorem (p. 83)
---------------------------------------------------------

.. admonition:: Enunciation (*Halley 1758, p. 83*)

   *If to two straight lines* :math:`\mathrm{AB}, \mathrm{A\Gamma}` *meeting at* :math:`\mathrm{A}` *there be drawn two other straight lines* :math:`\mathrm{\Gamma\Delta}, \mathrm{BE}` *intersecting one another at point* :math:`\mathrm{Z}`: *I say that straight line* :math:`\mathrm{AE}` *has to* :math:`\mathrm{E\Gamma}` *a ratio compounded of the ratio* :math:`\mathrm{\Delta Z} : \mathrm{Z\Gamma}` *and the ratio* :math:`\mathrm{BA} : \mathrm{B\Delta}`. *And with the same things posited,* :math:`\mathrm{\Gamma A}` *has to* :math:`\mathrm{AE}` *a ratio compounded of* :math:`\mathrm{\Gamma\Delta} : \mathrm{\Delta Z}` *and* :math:`\mathrm{ZB} : \mathrm{BE}`.

.. picture:: /_static/figures/menelaus-planar-parallel.svg
   :alt: Exact Planar Menelaus Theorem with auxiliary parallel CH || DF
   :caption: Exact Planar Menelaus construction (Halley Lemma I): transversal DF cuts the sides of △ABC at D (external on BC), E (on CA), and F (on AB), with auxiliary parallel CH ∥ DF.

In :mod:`geometor.menelaus.planar_transversal`, :term:`transversal <transversalis>` :g:`DF <[ D F ]>` cuts the sides of :g:`△ABC << A B C >>` at :g:`D` (external on :g:`BC <[ B C ]>`), :g:`E` (on :g:`CA <[ C A ]>`), and :g:`F` (on :g:`AB <[ A B ]>`), while auxiliary segment :g:`CH </ C H />` drawn parallel to :g:`DF <[ D F ]>` transfers both ratios onto :g:`AB <[ A B ]>` via Euclid VI.4.

**[§3.4 · Proof of Lemma I, Halley p. 83]**

1. **First Case (Division / Internal Ratio)**:
   Through :math:`\mathrm{A}` draw :math:`\mathrm{AH}` parallel to :math:`\mathrm{BE}`, meeting :math:`\mathrm{\Delta\Gamma}` produced at :math:`\mathrm{H}`. Because :math:`\mathrm{AH} \parallel \mathrm{EZ}`, :math:`\mathrm{AE} : \mathrm{E\Gamma} = \mathrm{HZ} : \mathrm{Z\Gamma}` (Euclid *Elements* VI.4). Interposing :math:`\mathrm{Z\Delta}` as a mean term, :math:`\mathrm{HZ} : \mathrm{Z\Gamma} = (\mathrm{HZ} : \mathrm{Z\Delta}) \cdot (\mathrm{Z\Delta} : \mathrm{Z\Gamma})`. Again by :math:`\mathrm{AH} \parallel \mathrm{BZ}`, :math:`\mathrm{ZH} : \mathrm{Z\Delta} = \mathrm{BA} : \mathrm{B\Delta}`. Hence:

   .. math::

      \frac{\mathrm{AE}}{\mathrm{E\Gamma}}
      \;=\;
      \frac{\mathrm{BA}}{\mathrm{B\Delta}}
      \cdot
      \frac{\mathrm{\Delta Z}}{\mathrm{Z\Gamma}}.

2. **Second Case (Composition / External Ratio)**:
   Draw :math:`\mathrm{E\Theta}` parallel to :math:`\mathrm{\Gamma\Delta}` meeting :math:`\mathrm{AB}` at :math:`\mathrm{\Theta}`. Then :math:`\mathrm{\Gamma A} : \mathrm{AE} = \mathrm{\Gamma\Delta} : \mathrm{E\Theta} = (\mathrm{\Gamma\Delta} : \mathrm{\Delta Z}) \cdot (\mathrm{\Delta Z} : \mathrm{E\Theta}) = (\mathrm{\Gamma\Delta} : \mathrm{\Delta Z}) \cdot (\mathrm{ZB} : \mathrm{BE})`. *Q.E.D.*

----

Lemma II — The Chord-Sine Projection Lemma (pp. 83–84)
------------------------------------------------------

.. folio:: halley_1758_menelai_sphaericorum:0100
   :page: 84

.. admonition:: Enunciation (*Halley 1758, pp. 83–84*)

   *If in a circle any straight line drawn from the center divides an arc and its subtending chord (whether internally or externally), the segments of the chord are proportional to the sines of the segments of the arc.*

Let a radius from center :math:`\mathrm{\Delta}` meet chord :math:`\mathrm{A\Gamma}` at :math:`\mathrm{B}` and the circle at :math:`\mathrm{B}`: dropping perpendiculars from :math:`\mathrm{A}` and :math:`\mathrm{\Gamma}` onto diameter :math:`\mathrm{\Delta B}` produces similar right triangles, so that chord segments :math:`\mathrm{AB} : \mathrm{B\Gamma}` are in the exact ratio of those perpendiculars—that is, the sines :math:`\sin \widehat{\mathrm{AB}} : \sin \widehat{\mathrm{B\Gamma}}`.

.. toctree::
   :hidden:

   la
   summary
   notes

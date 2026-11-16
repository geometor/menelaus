:layout: book
:order: 6
:canonical_id: III.6
:breadcrumb_title: Proposition III.6
:folio: halley_1758_menelai_sphaericorum:0107
:tracks: English: index | Latin: la | Summary: summary | Notes: notes

.. _liber-iii-prop-06:
.. _sphaerica-iii-6:

Proposition III.6 — Spherical Internal & External Angle Bisectors
=================================================================

.. rubric:: *Menelai Alexandrini Sphaericorum Lib. III Prop. VI. Theor. (Halley 1758, pp. 91–92)*

.. folio:: halley_1758_menelai_sphaericorum:0107
   :page: 91

Proposition III.6 — Theorem: Spherical Angle Bisectors (p. 91)
--------------------------------------------------------------

.. admonition:: Enunciation (*Halley 1758, p. 91*)

   *If any angle of a spherical triangle be divided into two equal parts, the sines of the two sides shall be to the sines of the two segments of the base in the same ratio; and conversely, and by alternation* (*ἐναλλάξ*).

**[§4.1 · Internal & External Bisectors, Halley p. 91]** Let :math:`\triangle \mathrm{AB\Gamma}` be a :term:`spherical triangle <triangulum-sphaericum>`, and let arc :math:`\mathrm{B\Delta}` bisect angle :math:`\angle \mathrm{AB\Gamma}`: I say that :math:`\sin \widehat{\mathrm{AB}} : \sin \widehat{\mathrm{A\Delta}} = \sin \widehat{\mathrm{B\Gamma}} : \sin \widehat{\mathrm{\Delta\Gamma}}` (and *alternando*, :math:`\sin \widehat{\mathrm{AB}} : \sin \widehat{\mathrm{B\Gamma}} = \sin \widehat{\mathrm{A\Delta}} : \sin \widehat{\mathrm{\Delta\Gamma}}`).

1. **Direct Proof**:
   In spherical triangles :math:`\triangle \mathrm{AB\Delta}` and :math:`\triangle \mathrm{\Gamma B\Delta}`, angles :math:`\angle \mathrm{AB\Delta} = \angle \mathrm{\Gamma B\Delta}`, while the two adjacent angles at :math:`\mathrm{\Delta}` sum to two right angles. Therefore, by **Proposition III.2** (the Spherical Law of Sines), :math:`\sin \widehat{\mathrm{BA}} : \sin \widehat{\mathrm{A\Delta}} = \sin \widehat{\mathrm{B\Gamma}} : \sin \widehat{\mathrm{\Gamma\Delta}}`.
2. **Converse**:
   Conversely, if :math:`\sin \widehat{\mathrm{AB}} : \sin \widehat{\mathrm{B\Gamma}} = \sin \widehat{\mathrm{A\Delta}} : \sin \widehat{\mathrm{\Delta\Gamma}}`, then since the two angles at :math:`\mathrm{\Delta}` sum to two right angles, by the converse of Proposition III.2 angles :math:`\angle \mathrm{AB\Delta}` and :math:`\angle \mathrm{\Delta B\Gamma}` are either equal or supplementary; they are not supplementary, hence :math:`\mathrm{B\Delta}` bisects :math:`\angle \mathrm{AB\Gamma}`!
3. **External Angle Bisector**:
   Again, let the exterior angle :math:`\angle \mathrm{\Gamma BE}` adjacent to :math:`\angle \mathrm{AB\Gamma}` be bisected by arc :math:`\mathrm{B\delta}` meeting base :math:`\mathrm{A\Gamma}` produced at :math:`\mathrm{\delta}`: by the very same argument on :math:`\triangle \mathrm{AB\delta}` and :math:`\triangle \mathrm{\Gamma B\delta}`, :math:`\sin \widehat{\mathrm{AB}} : \sin \widehat{\mathrm{B\Gamma}} = \sin \widehat{\mathrm{A\delta}} : \sin \widehat{\mathrm{\delta\Gamma}}`! Together with the internal bisector foot :math:`\mathrm{\Delta}`, points :math:`\mathrm{\Delta}` and :math:`\mathrm{\delta}` divide :math:`\mathrm{A\Gamma}` in :term:`harmonic section <sectio-harmonica>` in sines!

.. picture:: /_static/figures/menelaus-external-bisectors.svg
   :alt: External Angle-Bisector Axis of a scalene Heronian triangle proved by Converse of Menelaus
   :caption: External Angle-Bisector Axis (planar counterpart of Sphaerica Prop. III.6): external bisector feet De, Ee, and Fe of Heronian △ABC lie on the anti-orthic axis (trilinear polar of incenter I).

.. toctree::
   :hidden:

   la
   summary
   notes

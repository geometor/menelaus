:layout: book
:order: 9
:canonical_id: III.10
:breadcrumb_title: Proposition III.10
:folio: halley_1758_menelai_sphaericorum:0111
:tracks: English: index | Latin: la | Summary: summary | Notes: notes

.. _liber-iii-prop-10:
.. _sphaerica-iii-10:

Proposition III.10 — Concurrency of Spherical Altitudes
=======================================================

.. rubric:: *Menelai Alexandrini Sphaericorum Lib. III Prop. X. Theor. (Halley 1758, pp. 95–97)*

.. folio:: halley_1758_menelai_sphaericorum:0111
   :page: 95

Proposition III.10 — Theorem: Spherical Orthocenter Concurrency (pp. 95–97)
---------------------------------------------------------------------------

.. admonition:: Enunciation (*Halley 1758, p. 95*)

   *If from any two angles of a spherical triangle two perpendicular arcs be dropped onto the sides opposite to them: the arc drawn from the remaining angle through the point where those first two arcs meet, when produced, shall also be perpendicular to the remaining side.*

.. picture:: /_static/figures/menelaus-ceva-trilinear-polar.svg
   :alt: Complete quadrangle harmonic conjugation turning Ceva concurrence (+1) into Menelaus collinearity (-1)
   :caption: Ceva–Menelaus Harmonic Duality: harmonic conjugates Dm, Em, and Fm of concurrent cevian traces Dc, Ec, and Fc align on the trilinear polar of perspector P.

**[§4.4 · Menelaus's Masterpiece Proof via Triple Menelaus & Orthic Harmonic Polarity, pp. 95–97]** Let :math:`\triangle \mathrm{AB\Gamma}` be a spherical triangle, and from vertices :math:`\mathrm{A}` and :math:`\mathrm{\Gamma}` drop perpendicular arcs :math:`\mathrm{A\Delta} \perp \mathrm{B\Gamma}` and :math:`\mathrm{\Gamma E} \perp \mathrm{AB}` meeting at :math:`\mathrm{Z}`; join :math:`\mathrm{BZ}` and produce it to meet :math:`\mathrm{A\Gamma}` at :math:`\mathrm{H}` (crossing :math:`\mathrm{E\Delta}` at :math:`\mathrm{K}`). Menelaus claims :math:`\mathrm{BH} \perp \mathrm{A\Gamma}`:

1. **Constructing the Orthic Axis (Trilinear Polar)**:
   Draw the great-circle arc :math:`\mathrm{E\Delta}` through the feet :math:`\mathrm{\Delta}, \mathrm{E}` of the two altitudes, produce it to meet :math:`\mathrm{A\Gamma}` produced at :math:`\mathrm{\Theta}`, and join :math:`\mathrm{H\Delta}` and :math:`\mathrm{HE}`.
2. **Triple Application of Proposition III.1 (*Theorema Menelai*)**:
   - In Menelaus figure :math:`\mathrm{A\Theta EZ}`, :math:`\sin \widehat{\mathrm{A\Theta}} : \sin \widehat{\mathrm{\Theta\Gamma}} = (\sin \widehat{\mathrm{A\Delta}} : \sin \widehat{\mathrm{\Delta Z}}) \cdot (\sin \widehat{\mathrm{ZE}} : \sin \widehat{\mathrm{E\Gamma}})`.
   - In Menelaus figure :math:`\mathrm{A\Gamma BZ}`, :math:`\sin \widehat{\mathrm{AH}} : \sin \widehat{\mathrm{H\Gamma}} = (\sin \widehat{\mathrm{AZ}} : \sin \widehat{\mathrm{Z\Delta}}) \cdot (\sin \widehat{\mathrm{\Delta B}} : \sin \widehat{\mathrm{B\Gamma}})`.
   - In Menelaus figure :math:`\mathrm{AB\Gamma Z}`, :math:`\sin \widehat{\mathrm{\Delta B}} : \sin \widehat{\mathrm{B\Gamma}} = (\sin \widehat{\mathrm{\Delta A}} : \sin \widehat{\mathrm{AZ}}) \cdot (\sin \widehat{\mathrm{ZE}} : \sin \widehat{\mathrm{E\Gamma}})`.

   Substituting the third ratio into the second cancels :math:`\sin \widehat{\mathrm{AZ}}`, leaving the **exact same compounded ratio** as the first:

   .. math::

      \frac{\sin \widehat{\mathrm{A\Theta}}}{\sin \widehat{\mathrm{\Theta\Gamma}}}
      \;=\;
      \frac{\sin \widehat{\mathrm{A\Delta}}}{\sin \widehat{\mathrm{Z\Delta}}}
      \cdot
      \frac{\sin \widehat{\mathrm{ZE}}}{\sin \widehat{\mathrm{E\Gamma}}}
      \;=\;
      \frac{\sin \widehat{\mathrm{AH}}}{\sin \widehat{\mathrm{H\Gamma}}}.

   Thus :math:`\mathrm{\Theta}` and :math:`\mathrm{H}` divide base :math:`\mathrm{A\Gamma}` **harmonically** in sines!
3. **Orthic Triangle Bisectors via Prop. III.8 & III.9**:
   Because :math:`\angle \mathrm{A\Delta\Gamma}` is right, the second converse of **Proposition III.8** gives :math:`\angle \mathrm{\Theta\Delta\Gamma} = \angle \mathrm{\Gamma\Delta H}` (hence :math:`\angle \mathrm{A\Delta H} = \angle \mathrm{A\Delta E}`); likewise at right angle :math:`\angle \mathrm{\Gamma EA}`, :math:`\angle \mathrm{\Delta E\Gamma} = \angle \mathrm{\Gamma EH}`. Therefore, in the **orthic spherical triangle** :math:`\triangle \mathrm{\Delta EH}`, the altitudes :math:`\mathrm{\Delta Z}` and :math:`\mathrm{EZ}` bisect angles :math:`\angle \mathrm{\Delta}` and :math:`\angle \mathrm{E}`! By **Proposition III.9**, :math:`\mathrm{HZ}` also bisects :math:`\angle \mathrm{EH\Delta}`!
4. **Right Angle at H via Prop. III.6 & Converse I of Prop. III.8**:
   Applying **Proposition III.6** to :math:`\triangle \mathrm{\Theta\Delta H}` and :math:`\triangle \mathrm{\Theta EH}` (whose angles at :math:`\mathrm{\Delta}` and :math:`\mathrm{E}` are bisected by :math:`\mathrm{\Delta\Gamma}` and :math:`\mathrm{E\Gamma}`) yields :math:`\sin \widehat{\mathrm{\Theta E}} : \sin \widehat{\mathrm{\Theta\Delta}} = \sin \widehat{\mathrm{EH}} : \sin \widehat{\mathrm{H\Delta}} = \sin \widehat{\mathrm{EK}} : \sin \widehat{\mathrm{K\Delta}}` (since :math:`\mathrm{HZK}` bisects :math:`\angle \mathrm{EH\Delta}`). Since :math:`\angle \mathrm{EHK} = \angle \mathrm{\Delta HK}` AND :math:`(\mathrm{\Theta}, \mathrm{K}; \mathrm{E}, \mathrm{\Delta})` is harmonic in sines, the first converse of **Proposition III.8** forces :math:`\angle \mathrm{\Theta HK}` (i.e., :math:`\angle \mathrm{AHB}`) to be a **right angle**! *Q.E.D.*

.. toctree::
   :hidden:

   la
   summary
   notes

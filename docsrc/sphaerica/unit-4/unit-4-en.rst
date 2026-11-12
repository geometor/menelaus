:title: Unit IV — Book III (III.6–25): Harmonic Pencils, Concurrencies & Projective Duality
:layout: book

.. _unit-4-en:

Unit IV — Book III (III.6–25): Harmonic Pencils, Concurrencies & Projective Duality
===================================================================================

.. rubric:: *Original English Translation from Edmond Halley's Oxford Edition (1758, pp. 91–112)*

Proposition III.6 — Theorem: Spherical Internal & External Angle Bisectors (p. 91)
----------------------------------------------------------------------------------

.. admonition:: Enunciation (*Halley 1758, p. 91*)

   *If any angle of a spherical triangle be divided into two equal parts, the sines of the two sides shall be to the sines of the two segments of the base in the same ratio; and conversely, and by alternation* (*ἐναλλάξ*).

**[§4.1 · Internal & External Bisectors, Halley p. 91]** Let :math:`\triangle \mathrm{AB\Gamma}` be a :term:`spherical triangle <triangulum-sphaericum>`, and let arc :math:`\mathrm{B\Delta}` bisect angle :math:`\angle \mathrm{AB\Gamma}`: I say that :math:`\sin \widehat{\mathrm{AB}} : \sin \widehat{\mathrm{A\Delta}} = \sin \widehat{\mathrm{B\Gamma}} : \sin \widehat{\mathrm{\Delta\Gamma}}` (and *alternando*, :math:`\sin \widehat{\mathrm{AB}} : \sin \widehat{\mathrm{B\Gamma}} = \sin \widehat{\mathrm{A\Delta}} : \sin \widehat{\mathrm{\Delta\Gamma}}`).

1. **Direct Proof**: In spherical triangles :math:`\triangle \mathrm{AB\Delta}` and :math:`\triangle \mathrm{\Gamma B\Delta}`, angles :math:`\angle \mathrm{AB\Delta} = \angle \mathrm{\Gamma B\Delta}`, while the two adjacent angles at :math:`\mathrm{\Delta}` sum to two right angles. Therefore, by **Proposition III.2** (the Spherical Law of Sines), :math:`\sin \widehat{\mathrm{BA}} : \sin \widehat{\mathrm{A\Delta}} = \sin \widehat{\mathrm{B\Gamma}} : \sin \widehat{\mathrm{\Gamma\Delta}}`.
2. **Converse**: Conversely, if :math:`\sin \widehat{\mathrm{AB}} : \sin \widehat{\mathrm{B\Gamma}} = \sin \widehat{\mathrm{A\Delta}} : \sin \widehat{\mathrm{\Delta\Gamma}}`, then since the two angles at :math:`\mathrm{\Delta}` sum to two right angles, by the converse of Proposition III.2 angles :math:`\angle \mathrm{AB\Delta}` and :math:`\angle \mathrm{\Delta B\Gamma}` are either equal or supplementary; they are not supplementary, hence :math:`\mathrm{B\Delta}` bisects :math:`\angle \mathrm{AB\Gamma}`!
3. **External Angle Bisector**: Again, let the exterior angle :math:`\angle \mathrm{\Gamma BE}` adjacent to :math:`\angle \mathrm{AB\Gamma}` be bisected by arc :math:`\mathrm{B\delta}` meeting base :math:`\mathrm{A\Gamma}` produced at :math:`\mathrm{\delta}`: by the very same argument on :math:`\triangle \mathrm{AB\delta}` and :math:`\triangle \mathrm{\Gamma B\delta}`, :math:`\sin \widehat{\mathrm{AB}} : \sin \widehat{\mathrm{B\Gamma}} = \sin \widehat{\mathrm{A\delta}} : \sin \widehat{\mathrm{\delta\Gamma}}`! (Together with the internal bisector foot :math:`\mathrm{\Delta}`, points :math:`\mathrm{\Delta}` and :math:`\mathrm{\delta}` divide :math:`\mathrm{A\Gamma}` in :term:`harmonic section <sectio-harmonica>` in sines!)

----

Proposition III.8 — Theorem: Spherical Harmonic Division & Pencils (pp. 93–94)
------------------------------------------------------------------------------

.. admonition:: Enunciation (*Halley 1758, p. 93*)

   *If from the right angle of a right-angled spherical triangle two arcs be drawn to the base containing equal angles with one of its legs: the sine of the arc compounded of the base and the arc adjoined to it shall be to the sine of that adjoined arc itself, as the sine of the segment of the base adjacent to the other leg of the triangle is to the sine of the remaining segment of the base; and conversely.*

.. picture:: /_static/figures/spherical-cross-ratio-pencil.svg
   :alt: Pencil of four great circles concurrent at V cutting two oblique transversals with invariant sine cross-ratio
   :caption: Spherical pencil invariance (generalizing Sphaerica Prop. III.8 & Pappus Synagoge VI/VII): four great circles concurrent at vertex V cut two oblique transversals with identical spherical sine cross-ratio −2.

In :func:`~geometor.menelaus.spherical.verify_spherical_cross_ratio_invariance` (generalizing *Sphaerica* Prop. III.8 and :person:`Pappus <pappus>`'s *Synagoge* VI/VII), four great circles concurrent at vertex :g:`V` cut great circles :g:`X1X4 <[ X1 X4 ]>` and :g:`Y1Y4 <[ Y1 Y4 ]>` in four-tuples (:g:`X1`, :g:`X2`, :g:`X3`, :g:`X4`) and (:g:`Y1`, :g:`Y2`, :g:`Y3`, :g:`Y4`) having identical spherical sine cross-ratio :math:`-2` (and :math:`-1` in the harmonic right-angle bisector case of Prop. III.8).

**[§4.2 · Proof & Double Converse, Halley pp. 93–95]** Let :math:`\triangle \mathrm{AB\Gamma}` have angle :math:`\angle \mathrm{B}` right (:math:`\mathrm{BA} \perp \mathrm{B\Gamma}`), and from :math:`\mathrm{B}` let two arcs :math:`\mathrm{B\Delta}` (internal) and :math:`\mathrm{BE}` (external) make equal angles :math:`\angle \mathrm{AB\Delta} = \angle \mathrm{ABE}` with :math:`\mathrm{AB}`:

1. **Harmonic Sine Proportion**: Because :math:`\angle \mathrm{AB\Gamma}` is right while :math:`\angle \mathrm{AB\Delta} = \angle \mathrm{ABE}`, leg :math:`\mathrm{B\Gamma}` bisects the supplementary angle adjacent to :math:`\angle \mathrm{EB\Delta}`, while :math:`\mathrm{BA}` bisects :math:`\angle \mathrm{EB\Delta}` itself! Applying **Proposition III.6** twice to :math:`\triangle \mathrm{EB\Delta}` (with internal bisector :math:`\mathrm{BA}` and external bisector :math:`\mathrm{B\Gamma}`) yields :math:`\sin \widehat{\mathrm{BE}} : \sin \widehat{\mathrm{B\Delta}} = \sin \widehat{\mathrm{E\Gamma}} : \sin \widehat{\mathrm{\Gamma\Delta}}` and :math:`\sin \widehat{\mathrm{BE}} : \sin \widehat{\mathrm{B\Delta}} = \sin \widehat{\mathrm{EA}} : \sin \widehat{\mathrm{A\Delta}}`. Equating and alternating (*permutando*),

   .. math::

      \frac{\sin \widehat{\mathrm{\Gamma E}}}{\sin \widehat{\mathrm{EA}}}
      \;=\;
      \frac{\sin \widehat{\mathrm{\Gamma\Delta}}}{\sin \widehat{\mathrm{\Delta A}}},

   the exact spherical :term:`harmonic conjugate <sectio-harmonica>` law!
2. **First Converse (p. 94)**: If :math:`\sin \widehat{\mathrm{\Gamma E}} : \sin \widehat{\mathrm{EA}} = \sin \widehat{\mathrm{\Gamma\Delta}} : \sin \widehat{\mathrm{\Delta A}}` and :math:`\angle \mathrm{EBA} = \angle \mathrm{AB\Delta}`, then :math:`\mathrm{B\Gamma}` bisects the exterior angle adjacent to :math:`\angle \mathrm{EB\Delta}`, forcing :math:`\angle \mathrm{AB\Gamma}` to be a **right angle**!
3. **Second Converse (pp. 94–95)**: Conversely, if :math:`\sin \widehat{\mathrm{\Gamma E}} : \sin \widehat{\mathrm{EA}} = \sin \widehat{\mathrm{\Gamma\Delta}} : \sin \widehat{\mathrm{\Delta A}}` and :math:`\angle \mathrm{AB\Gamma}` is a **right angle**, then :math:`\angle \mathrm{EBA} = \angle \mathrm{AB\Delta}`! (Both converses become the engine of Menelaus's orthocenter proof in Prop. III.10!)

----

Proposition III.9 — Theorem: Concurrency of Spherical Angle Bisectors (p. 95)
-----------------------------------------------------------------------------

.. admonition:: Enunciation & Corollary (*Halley 1758, p. 95*)

   *If any two angles of a spherical triangle be bisected by arcs drawn across the triangle, and from the point of concurrence of those two arcs a third arc be drawn to the remaining angle: that arc shall also bisect the remaining angle.*
   **Corollary**: *Therefore a circle can be inscribed in every spherical triangle.*

**[§4.3 · Demonstration, Halley p. 95]** In :math:`\triangle \mathrm{AB\Gamma}`, let the angle bisectors :math:`\mathrm{A\Delta}` and :math:`\mathrm{\Gamma\Delta}` of :math:`\angle \mathrm{A}` and :math:`\angle \mathrm{\Gamma}` meet at :math:`\mathrm{\Delta}`, and join :math:`\mathrm{B\Delta}` produced to meet base :math:`\mathrm{A\Gamma}` at :math:`\mathrm{E}`. Applying **Proposition III.6** first to :math:`\triangle \mathrm{AB\mathrm{E}}` (bisector :math:`\mathrm{A\Delta}`) and then to :math:`\triangle \mathrm{\Gamma BE}` (bisector :math:`\mathrm{\Gamma\Delta}`) gives:

.. math::

   \frac{\sin \widehat{\mathrm{B\Delta}}}{\sin \widehat{\mathrm{\Delta E}}}
   = \frac{\sin \widehat{\mathrm{BA}}}{\sin \widehat{\mathrm{AE}}}
   = \frac{\sin \widehat{\mathrm{B\Gamma}}}{\sin \widehat{\mathrm{\Gamma E}}}
   \quad\Longrightarrow\quad
   \frac{\sin \widehat{\mathrm{B\Gamma}}}{\sin \widehat{\mathrm{AB}}}
   = \frac{\sin \widehat{\mathrm{\Gamma E}}}{\sin \widehat{\mathrm{AE}}}.

By the **converse of Proposition III.6**, :math:`\mathrm{B\Delta E}` bisects :math:`\angle \mathrm{AB\Gamma}`! *Q.E.D.*

----

Proposition III.10 — Theorem: Concurrency of Spherical Altitudes (pp. 95–97)
----------------------------------------------------------------------------

.. admonition:: Enunciation (*Halley 1758, p. 95*)

   *If from any two angles of a spherical triangle two perpendicular arcs be dropped onto the sides opposite to them: the arc drawn from the remaining angle through the point where those first two arcs meet, when produced, shall also be perpendicular to the remaining side.*

**[§4.4 · Menelaus's Masterpiece Proof via Triple Menelaus & Orthic Harmonic Polarity, pp. 95–97]** Let :math:`\triangle \mathrm{AB\Gamma}` be a spherical triangle, and from vertices :math:`\mathrm{A}` and :math:`\mathrm{\Gamma}` drop perpendicular arcs :math:`\mathrm{A\Delta} \perp \mathrm{B\Gamma}` and :math:`\mathrm{\Gamma E} \perp \mathrm{AB}` meeting at :math:`\mathrm{Z}`; join :math:`\mathrm{BZ}` and produce it to meet :math:`\mathrm{A\Gamma}` at :math:`\mathrm{H}` (crossing :math:`\mathrm{E\Delta}` at :math:`\mathrm{K}`). Menelaus claims :math:`\mathrm{BH} \perp \mathrm{A\Gamma}`:

1. **Constructing the Orthic Axis (Trilinear Polar)**: Draw the great-circle arc :math:`\mathrm{E\Delta}` through the feet :math:`\mathrm{\Delta}, \mathrm{E}` of the two altitudes, and produce it to meet :math:`\mathrm{A\Gamma}` produced at :math:`\mathrm{\Theta}`, and join :math:`\mathrm{H\Delta}` and :math:`\mathrm{HE}`.
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
      \frac{\sin \widehat{\mathrm{AH}}}{\sin \widehat{\mathrm{H\Gamma}}}!

   Thus :math:`\mathrm{\Theta}` and :math:`\mathrm{H}` divide :math:`\mathrm{A\Gamma}` **harmonically** in sines!
3. **Orthic Triangle Bisectors via Prop. III.8 & III.9**: Because :math:`\angle \mathrm{A\Delta\Gamma}` is right, the second converse of **Proposition III.8** gives :math:`\angle \mathrm{\Theta\Delta\Gamma} = \angle \mathrm{\Gamma\Delta H}` (hence :math:`\angle \mathrm{A\Delta H} = \angle \mathrm{A\Delta E}`); likewise at right angle :math:`\angle \mathrm{\Gamma EA}`, :math:`\angle \mathrm{\Delta E\Gamma} = \angle \mathrm{\Gamma EH}`. Therefore, in the **orthic spherical triangle** :math:`\triangle \mathrm{\Delta EH}`, the altitudes :math:`\mathrm{\Delta Z}` and :math:`\mathrm{EZ}` bisect angles :math:`\angle \mathrm{\Delta}` and :math:`\angle \mathrm{E}`! By **Proposition III.9** (`[§4.3]`), :math:`\mathrm{HZ}` also bisects :math:`\angle \mathrm{EH\Delta}`!
4. **Right Angle at H via Prop. III.6 & Converse I of Prop. III.8**: Applying **Proposition III.6** to :math:`\triangle \mathrm{\Theta\Delta H}` and :math:`\triangle \mathrm{\Theta EH}` (whose angles at :math:`\mathrm{\Delta}` and :math:`\mathrm{E}` are bisected by :math:`\mathrm{\Delta\Gamma}` and :math:`\mathrm{E\Gamma}`) yields :math:`\sin \widehat{\mathrm{\Theta E}} : \sin \widehat{\mathrm{\Theta\Delta}} = \sin \widehat{\mathrm{EH}} : \sin \widehat{\mathrm{H\Delta}} = \sin \widehat{\mathrm{EK}} : \sin \widehat{\mathrm{K\Delta}}` (since :math:`\mathrm{HZK}` bisects :math:`\angle \mathrm{EH\Delta}`). Since :math:`\angle \mathrm{EHK} = \angle \mathrm{\Delta HK}` AND :math:`(\mathrm{\Theta}, \mathrm{K}; \mathrm{E}, \mathrm{\Delta})` is harmonic in sines, the first converse of **Proposition III.8** forces :math:`\angle \mathrm{\Theta HK}` (i.e., :math:`\angle \mathrm{AHB}`) to be a **right angle**! *Q.E.D.*

----

Closing Horizon of Book III (Propositions III.11–III.25, pp. 97–112)
--------------------------------------------------------------------

The remainder of Book III (*Propositions III.11–III.25*, Halley pp. 97–112) establishes exact spherical difference-ratio bounds and astronomical rising-time proportion laws—culminating in spherical polar/equatorial parameter determinations that served Greek, Arabic, Hebrew, and Latin astronomers from :person:`Ptolemy <ptolemy>` and :person:`Thābit ibn Qurra <thabit-ibn-qurra>` to :person:`Edmond Halley <halley>`.

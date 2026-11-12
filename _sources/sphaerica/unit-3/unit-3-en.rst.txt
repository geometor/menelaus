:title: Unit III — Book III (III.1–5): The Menelaus Transversal Theorem & Law of Sines
:layout: book

.. _unit-3-en:

Unit III — Book III (III.1–5): The Menelaus Transversal Theorem & Law of Sines
==============================================================================

.. rubric:: *Original English Translation from Edmond Halley's Oxford Edition (1758, pp. 80–90) & Claudius Ptolemy's Syntaxis Mathematica I.13 (ed. Heiberg, 1898, pp. 68–75)*

Proposition III.1 — Theorem: *Theorema Menelai* / *Figura Catha* (pp. 80–82)
----------------------------------------------------------------------------

.. admonition:: Enunciation (*Halley 1758, p. 80*)

   *Let there be upon the surface of a sphere two arcs of great circles* :math:`\mathrm{NME}`, :math:`\mathrm{NA\Lambda}`, *between which let two other great-circle arcs* :math:`\mathrm{E\Theta A}`, :math:`\mathrm{\Lambda\Theta M}` *be drawn meeting one another at point* :math:`\mathrm{\Theta}`: *I say that the* :term:`sine <sinus>` *of arc* :math:`\widehat{\mathrm{AN}}` *has to the sine of arc* :math:`\widehat{\mathrm{A\Lambda}}` *a* :term:`ratio compounded <ratio-composita>` *of the ratio which the sine of arc* :math:`\widehat{\mathrm{NE}}` *has to the sine of arc* :math:`\widehat{\mathrm{EM}}`, *and of the ratio which the sine of arc* :math:`\widehat{\mathrm{M\Theta}}` *has to the sine of arc* :math:`\widehat{\mathrm{\Theta\Lambda}}`.

.. picture:: /_static/figures/spherical-menelaus-3d.svg
   :alt: Exact 3D spherical Menelaus configuration on the unit sphere S^2
   :caption: Exact spherical Menelaus configuration on the unit sphere S² (Sphaerica Prop. III.1): great-circle transversal DF cuts the sides of spherical triangle △ABC at D (external on BC), E, and F.

On the unit sphere :g:`S² <( S2 )>`, great-circle :term:`transversal <transversalis>` :g:`DF <[ D F ]>` cuts the sides of spherical triangle :g:`A`, :g:`B`, :g:`C` (:g:`AB </ A B />`, :g:`BC </ B C />`, :g:`CA </ C A />`) at :g:`D` (external on :g:`BC <[ B C ]>`), :g:`E`, and :g:`F`, satisfying :math:`\frac{\sin\widehat{AF}}{\sin\widehat{FB}} \cdot \frac{\sin\widehat{BD}}{\sin\widehat{DC}} \cdot \frac{\sin\widehat{CE}}{\sin\widehat{EA}} = -1`.

**[§3.1 · Menelaus's Gnomonic-Chord Demonstration, Halley pp. 80–82]** Let point :math:`\mathrm{B}` be set as the center of the sphere, and join straight lines (chords and radii) :math:`\mathrm{\Lambda N}`, :math:`\mathrm{\Lambda M}`, :math:`\mathrm{MN}`, :math:`\mathrm{EB}`, and :math:`\mathrm{\Theta B}` meeting chord :math:`\mathrm{M\Lambda}` at :math:`\mathrm{\Delta}`, and radius :math:`\mathrm{AB}` meeting chord :math:`\mathrm{N\Lambda}` at :math:`\mathrm{\Sigma}`; and let straight line :math:`\mathrm{\Delta\Sigma}` be drawn and produced until it meets straight line :math:`\mathrm{MN}` produced at :math:`\mathrm{K}`:

1. Point :math:`\mathrm{K}` lies in the plane of *both* great circles :math:`\mathrm{A\Theta E}` and :math:`\mathrm{NME}`. Since points :math:`\mathrm{E}` and :math:`\mathrm{B}` also lie in both planes, :math:`\mathrm{KEB}` is a single straight line (Euclid *Elements* XI.3).
2. In the planar triangle :math:`\triangle \mathrm{N\Lambda M}`, point :math:`\mathrm{\Sigma}` lies on :math:`\mathrm{N\Lambda}`, point :math:`\mathrm{\Delta}` lies on :math:`\mathrm{M\Lambda}`, and point :math:`\mathrm{K}` lies on :math:`\mathrm{MN}` produced, with :math:`\mathrm{\Sigma}, \mathrm{\Delta}, \mathrm{K}` collinear. Therefore, by the **Planar Menelaus Lemma** (*per sequens Lemma I*), the ratio :math:`\mathrm{N\Sigma} : \mathrm{\Sigma\Lambda}` is compounded of :math:`\mathrm{NK} : \mathrm{KM}` and :math:`\mathrm{M\Delta} : \mathrm{\Delta\Lambda}`.
3. By the **Chord-Sine Lemma** (*per Lemma II*), :math:`\mathrm{NK} : \mathrm{KM}` equals the perpendicular dropped from :math:`\mathrm{N}` onto diameter :math:`\mathrm{KEB}` to the perpendicular from :math:`\mathrm{M}` onto the same diameter—that is, :math:`\sin \widehat{\mathrm{NE}} : \sin \widehat{\mathrm{EM}}`. Likewise :math:`\mathrm{N\Sigma} : \mathrm{\Sigma\Lambda} = \sin \widehat{\mathrm{NA}} : \sin \widehat{\mathrm{A\Lambda}}`, and :math:`\mathrm{M\Delta} : \mathrm{\Delta\Lambda} = \sin \widehat{\mathrm{M\Theta}} : \sin \widehat{\mathrm{\Theta\Lambda}}`.
4. Hence :math:`\sin \widehat{\mathrm{AN}} : \sin \widehat{\mathrm{A\Lambda}}` is compounded of :math:`\sin \widehat{\mathrm{NE}} : \sin \widehat{\mathrm{EM}}` and :math:`\sin \widehat{\mathrm{M\Theta}} : \sin \widehat{\mathrm{\Theta\Lambda}}`. *Q.E.D.*

**[§3.2 · Limiting Parallel Case & Alternation, pp. 81–82]** Menelaus immediately treats the singular case where chord :math:`\mathrm{\Delta\Sigma}` is **parallel** to chord :math:`\mathrm{MN}` (so :math:`\mathrm{K}` recedes to infinity along the common diameter :math:`\mathrm{EBK}` parallel to both, by Euclid *Elements* XI.9): then the perpendiculars from :math:`\mathrm{N}` and :math:`\mathrm{M}` onto :math:`\mathrm{EBK}` are equal (:math:`\sin \widehat{\mathrm{NE}} = \sin \widehat{\mathrm{EM}}`, occurring when :math:`\widehat{\mathrm{EM}} + \widehat{\mathrm{NE}}` equals a semicircle!), and the first factor becomes the ratio of equality (:math:`1 : 1`). Inverting the compounded ratio yields the companion *katà diaíresin* identity :math:`\sin \widehat{\mathrm{A\Lambda}} : \sin \widehat{\mathrm{AN}} = (\sin \widehat{\mathrm{\Lambda\Theta}} : \sin \widehat{\mathrm{\Theta M}}) \cdot (\sin \widehat{\mathrm{ME}} : \sin \widehat{\mathrm{EN}})`.

----

Halley's Historical Scholion on Chords, Sines & *Figura Catha* (p. 82)
----------------------------------------------------------------------

**[§3.3 · Translation of Halley's Scholion, p. 82]**

.. epigraph::

   "The word ``נכחות`` [*nekhōḥōth*], by which the Hebrew translator [:person:`Jacob ben Machir <jacob-ben-machir>`] signifies the :term:`chord of double the arc <subtensa-dupli-arcus>` (or ``τὴν ὑπὸ τὴν διπλῆν τῆς περιφερείας`` in :person:`Ptolemy <ptolemy>`), we have everywhere rendered :term:`Sine <sinus>`, complying with the custom of the mathematicians of our age and following the example of the Arabic translator, who continually employs the word ``جيب`` [*jayb*], that is, Sine. For the ratios of the sines to one another are the very same as those of the chords of the double arcs.

   Moreover, upon this single Theorem almost the entire Trigonometry of the Ancients rests; nor did :person:`Ptolemy <ptolemy>` use any other foundation in his *Syntaxis* [:cite:`Almagest I.13 <ptolemy-almagest-i-13>`]—which indeed it will appear not improbable that he received from :person:`Menelaus <menelaus>`, scarce forty years his senior, when a comparison is made of this chapter with Book I Chapter XII [XIII] of the *Mathematical Syntaxis*. The same theorem was likewise held in the highest esteem by the Arabs, who, seeking the mensuration of spherical triangles from this principle, labored earnestly to adorn and elucidate this Rule, which they called ``القطاع`` [*al-Qaṭṭāʿ*], that is, the :term:`Rule of Intersection <figura-catha>`. Whence European mathematicians several centuries ago borrowed both the name and the subject from the Moors, leaving treatises *On the Figure Catha*—among whom stands out Simon Bredon, Englishman, Fellow of Merton College around the year 1350, whose work on this subject is preserved in more than one volume in the Bodleian Library."

----

Lemma I & II — The Planar Menelaus Transversal Theorem (pp. 83–84)
------------------------------------------------------------------

.. admonition:: Lemma I — Planar Menelaus Theorem (*Halley 1758, p. 83*)

   *If to two straight lines* :math:`\mathrm{AB}, \mathrm{A\Gamma}` *meeting at* :math:`\mathrm{A}` *there be drawn two other straight lines* :math:`\mathrm{\Gamma\Delta}, \mathrm{BE}` *intersecting one another at point* :math:`\mathrm{Z}`: *I say that straight line* :math:`\mathrm{AE}` *has to* :math:`\mathrm{E\Gamma}` *a ratio compounded of the ratio* :math:`\mathrm{\Delta Z} : \mathrm{Z\Gamma}` *and the ratio* :math:`\mathrm{BA} : \mathrm{B\Delta}`. *And with the same things posited,* :math:`\mathrm{\Gamma A}` *has to* :math:`\mathrm{AE}` *a ratio compounded of* :math:`\mathrm{\Gamma\Delta} : \mathrm{\Delta Z}` *and* :math:`\mathrm{ZB} : \mathrm{BE}`.

.. picture:: /_static/figures/menelaus-planar-parallel.svg
   :alt: Exact Planar Menelaus Theorem with auxiliary parallel CH || DF
   :caption: Exact Planar Menelaus construction (Halley Lemma I): transversal DF cuts the sides of △ABC at D (external on BC), E (on CA), and F (on AB), with auxiliary parallel CH ∥ DF.

In :mod:`geometor.menelaus.planar_transversal`, :term:`transversal <transversalis>` :g:`DF <[ D F ]>` cuts the sides of :g:`△ABC << A B C >>` at :g:`D` (external on :g:`BC <[ B C ]>`), :g:`E` (on :g:`CA <[ C A ]>`), and :g:`F` (on :g:`AB <[ A B ]>`), while auxiliary segment :g:`CH </ C H />` drawn parallel to :g:`DF <[ D F ]>` transfers both ratios onto :g:`AB <[ A B ]>` via Euclid VI.4.

**[§3.4 · Proof of Lemma I, Halley p. 83]**

1. **First Case (Division / Internal Ratio)**: Through :math:`\mathrm{A}` draw :math:`\mathrm{AH}` parallel to :math:`\mathrm{BE}`, meeting :math:`\mathrm{\Delta\Gamma}` produced at :math:`\mathrm{H}`. Because :math:`\mathrm{AH} \parallel \mathrm{EZ}`, :math:`\mathrm{AE} : \mathrm{E\Gamma} = \mathrm{HZ} : \mathrm{Z\Gamma}` (Euclid *Elements* VI.4). Interposing :math:`\mathrm{Z\Delta}` as a mean term, :math:`\mathrm{HZ} : \mathrm{Z\Gamma} = (\mathrm{HZ} : \mathrm{Z\Delta}) \cdot (\mathrm{Z\Delta} : \mathrm{Z\Gamma})`. Again by :math:`\mathrm{AH} \parallel \mathrm{BZ}`, :math:`\mathrm{ZH} : \mathrm{Z\Delta} = \mathrm{BA} : \mathrm{B\Delta}`. Hence :math:`\mathrm{AE} : \mathrm{E\Gamma} = (\mathrm{BA} : \mathrm{B\Delta}) \cdot (\mathrm{\Delta Z} : \mathrm{Z\Gamma})`.
2. **Second Case (Composition / External Ratio)**: Draw :math:`\mathrm{E\Theta}` parallel to :math:`\mathrm{\Gamma\Delta}` meeting :math:`\mathrm{AB}` at :math:`\mathrm{\Theta}`. Then :math:`\mathrm{\Gamma A} : \mathrm{AE} = \mathrm{\Gamma\Delta} : \mathrm{E\Theta} = (\mathrm{\Gamma\Delta} : \mathrm{\Delta Z}) \cdot (\mathrm{\Delta Z} : \mathrm{E\Theta}) = (\mathrm{\Gamma\Delta} : \mathrm{\Delta Z}) \cdot (\mathrm{ZB} : \mathrm{BE})`. *Q.E.D.*
3. **Lemma II (pp. 83–84)**: *If in a circle any straight line drawn from the center divides an arc and its subtending chord (internal or external), the segments of the chord are proportional to the sines of the segments of the arc.*

----

Surviving Greek Witness: Claudius Ptolemy, *Almagest* I.13 (Heiberg pp. 68–75)
------------------------------------------------------------------------------

**[§3.5 · Original Translation from Heiberg's Greek Text, pp. 68–69, 74–75]**

* **Planar Lemma (Heiberg pp. 68–69)**: *"Across two straight lines* :math:`\mathrm{AB}` *and* :math:`\mathrm{A\Gamma}`, *let two straight lines* :math:`\mathrm{BE}` *and* :math:`\mathrm{\Gamma\Delta}` *be drawn cutting one another at point* :math:`\mathrm{Z}`. *I say that the ratio of* :math:`\mathrm{\Gamma A}` *to* :math:`\mathrm{AE}` *is compounded of the ratio of* :math:`\mathrm{\Gamma\Delta}` *to* :math:`\mathrm{\Delta Z}` *and the ratio of* :math:`\mathrm{ZB}` *to* :math:`\mathrm{BE}`. *For let* :math:`\mathrm{EH}` *be drawn through* :math:`\mathrm{E}` *parallel to* :math:`\mathrm{\Gamma\Delta}`... *And in the very same way it shall be proved* :term:`by division <compositio-et-divisio-rationis>` (*κατὰ διαίρεσιν*) *that the ratio of* :math:`\mathrm{\Gamma E}` *to* :math:`\mathrm{EA}` *is compounded of the ratio of* :math:`\mathrm{\Gamma Z}` *to* :math:`\mathrm{\Delta Z}` *and the ratio of* :math:`\mathrm{\Delta B}` *to* :math:`\mathrm{BA}`."
* **Spherical Theorem (Heiberg pp. 74–75)**: *"These lemmas having been premised, let arcs of great circles be described upon a spherical surface such that two arcs* :math:`\mathrm{BE}` *and* :math:`\mathrm{\Gamma\Delta}` *drawn across two arcs* :math:`\mathrm{AB}` *and* :math:`\mathrm{A\Gamma}` *cut one another at point* :math:`\mathrm{Z}`; *and let each of them be less than a semicircle. I say then that the ratio of the* :term:`chord subtending double the arc <subtensa-dupli-arcus>` :math:`\mathrm{\Gamma E}` *to the chord subtending double the arc* :math:`\mathrm{EA}` *is compounded of the ratio of the chord of double* :math:`\mathrm{\Gamma Z}` *to the chord of double* :math:`\mathrm{Z\Delta}`, *and the ratio of the chord of double* :math:`\mathrm{\Delta B}` *to the chord of double* :math:`\mathrm{BA}`."

----

Propositions III.2 & III.3 — Spherical Law of Sines & Rule of Tangents (pp. 86–88)
----------------------------------------------------------------------------------

Proposition III.1 Coroll. 2 — Right-Angled Spherical Triangles (p. 86)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When :math:`\mathrm{\Gamma}` is the :term:`pole <polus>` of :math:`\mathrm{AB}` and :math:`\mathrm{B}` is the pole of :math:`\mathrm{A\Gamma}`, angles :math:`\mathrm{A}, \mathrm{E}, \mathrm{\Delta}` are right angles and :math:`\widehat{\mathrm{AB}}, \widehat{\mathrm{A\Gamma}}, \widehat{\mathrm{BE}}, \widehat{\mathrm{\Gamma\Delta}}` are quadrants, immediately yielding the classical right-spherical-triangle canon (:math:`\sin a = \sin c \sin A`, :math:`\tan b = \tan c \cos A`, :math:`\cos c = \cos a \cos b`).

Proposition III.2 — Theorem: The Spherical Law of Sines (pp. 86–87)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Enunciation (*Halley 1758, p. 86*)

   *If of two spherical triangles two angles be equal, and two other angles be either equal to one another or taken together equal to two right angles: I say that the sines of the sides subtending the two equal angles are to the sines of the sides subtending the two other angles (whether equal or supplementary) respectively in the same ratio; and conversely.*

**[§3.6 · Consequence]** Setting :math:`\triangle \mathrm{\Delta EZ}` to be the mirror/perpendicular configuration of :math:`\triangle \mathrm{AB\Gamma}` itself immediately gives the universal **Spherical Law of Sines**:

.. math::

   \frac{\sin a}{\sin A} \;=\; \frac{\sin b}{\sin B} \;=\; \frac{\sin c}{\sin C}.

Proposition III.3 & Corollary — Rule of Four Quantities & Tangents (p. 88)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In two right-angled spherical triangles :math:`\triangle \mathrm{AB\Gamma}` (right at :math:`\mathrm{A}`) and :math:`\triangle \mathrm{\Delta EZ}` (right at :math:`\mathrm{\Delta}`) sharing an equal acute angle :math:`\angle \mathrm{\Gamma} = \angle \mathrm{Z}`, with :math:`\mathrm{H}, \mathrm{\Theta}` the poles of bases :math:`\mathrm{\Gamma A}, \mathrm{Z\Delta}`, Menelaus applies Proposition III.1 to deduce :math:`\sin \widehat{\mathrm{AB}} : \sin \widehat{\mathrm{A\Gamma}} = (\sin \widehat{\mathrm{E\Delta}} : \sin \widehat{\mathrm{\Delta Z}}) \cdot (\sin \widehat{\mathrm{HB}} : \sin \widehat{\mathrm{E\Theta}})`, and states as **Corollary (p. 88)**: *"Hence it is manifest that the tangents of the perpendicular legs* :math:`\mathrm{AB}, \mathrm{\Delta E}` *are proportional to the sines of the bases* :math:`\mathrm{A\Gamma}, \mathrm{\Delta Z}`" (:math:`\tan \widehat{\mathrm{AB}} : \tan \widehat{\mathrm{\Delta E}} = \sin \widehat{\mathrm{A\Gamma}} : \sin \widehat{\mathrm{\Delta Z}}`).

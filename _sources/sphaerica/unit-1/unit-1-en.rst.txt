:title: Unit I — Book I: Intrinsic Spherical Triangles, Congruence & Excess
:layout: book

.. _unit-1-en:

Unit I — Book I: Intrinsic Spherical Triangles, Congruence & Excess
===================================================================

.. rubric:: *Original English Translation from Edmond Halley's Oxford Edition (1758, pp. [i]–[viii], 1–26)*

Preface to the Kind Reader (*Praefatio Costardi*, pp. [i]–[viii])
-----------------------------------------------------------------

**[§1.1 · Halley 1758, pp. i–ii]** :person:`Euclid <euclid>`, who leads the column of mathematicians—edited in 1703 by the most learned David Gregory, Savilian Professor of Astronomy—was followed in 1706 by the books of Apollonius of Perga *On Cutting Off a Ratio and a Space*, translated into Latin and restored from an Arabic manuscript by a man beyond all praise, :person:`Edmond Halley <halley>`, Gregory's closest colleague; and in the very next year (1707) by the *Sphaerica* of :person:`Theodosius <theodosius>`, edited by Joseph Hunt, Master of Balliol College, followed in 1710 by Apollonius's *Conics* with the lemmas of :person:`Pappus of Alexandria <pappus>`. To the same studies and vigils of Halley the Mathematical Republic owes this our :person:`Menelaus <menelaus>`, which—though printed complete at the University Press under Halley's own care—had not yet come forth into the light.

**[§1.2 · Halley 1758, pp. iii–vi]** That Menelaus composed his three books *On Spherical Figures* in Greek is testified by :person:`Pappus <pappus>` and :person:`Proclus <proclus>`, while :person:`Ptolemy <ptolemy>` records astronomical observations made by Menelaus at Rome in the first year of Trajan (*98 CE*, :cite:`Almagest VII.3 <ptolemy-almagest-vii-3>`). With the Greek original lost, Halley collated the Bodleian Huntington Hebrew manuscript (*translated from the version of* :person:`Isḥāq ibn Ḥunayn <ishaq-ibn-hunayn>` *by* :person:`Jacob ben Machir <jacob-ben-machir>`) alongside Arabic witnesses, restoring Menelaus's genuine demonstrations free of the Renaissance interpolations introduced by :person:`Francesco Maurolico <maurolico>` (:cite:`Messina, 1558 <maurolico-1558>`) and abridged by :person:`Marin Mersenne <mersenne>` (:cite:`1644 <mersenne-1644>`).

----

Book I — Definitions (*Definitiones*, p. 1)
-------------------------------------------

- **Definition I.** A :term:`spherical triangle <triangulum-sphaericum>` is the space comprehended under arcs of :term:`great circles <circulus-magnus>` upon the surface of a sphere.
- **Definition II.** And these arcs, which are always **less than a semicircle**, are called the *sides* or *legs* of the triangle.
- **Definition III.** Their :term:`angles <angulus-sphaericus>` are the angles which the great circles contain upon the surface of the sphere.
- **Definition IV.** And these *spherical angles* are called *equal* when the planes of the arcs containing them are inclined to one another with an equal inclination.
- **Definition V.** And if the planes of two arcs be inclined to one another with a greater inclination than the planes of two other arcs, the angle contained by those arcs shall also be greater.
- **Definition VI.** And if the planes of the arcs contain a right dihedral angle, the arcs themselves are likewise said to contain a *right spherical angle*.

.. picture:: /_static/figures/spherical-excess-polar.svg
   :alt: Intrinsic spherical triangle ABC on unit sphere S^2 alongside its polar supplementary triangle A*B*C*
   :caption: Intrinsic spherical triangle △ABC bounded by minor great-circle arcs on S², shown alongside its supplementary polar triangle △A*B*C*.

In the figure above, intrinsic spherical triangle :g:`A`, :g:`B`, :g:`C` is bounded by minor great-circle arcs :g:`AB </ A B />`, :g:`BC </ B C />`, and :g:`CA </ C A />` on :math:`S^2`, paired with its supplementary :term:`polar triangle <triangulum-polare>` :g:`A*`, :g:`B*`, :g:`C*`.

----

Selected Foundational Propositions of Book I (pp. 2–26)
-------------------------------------------------------

Proposition I.1 — Problem (p. 2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*At a given point on a given arc of a great circle, to construct a spherical angle equal to a given spherical angle.*

**[§1.3 · Summary of Halley p. 2]** Taking the given vertex as :term:`pole <polus>`, Menelaus describes great-circle arcs intercepting the dihedral measure of the given angle, transfers the chord/arc opening to the polar circle of the target point, and joins the great-circle arc—establishing the spherical counterpart of :person:`Euclid <euclid>`'s *Elements* I.23 without planar straightedge superposition.

Proposition I.4 & I.5 — SAS Congruence & Spherical Triangle Inequality (pp. 5–6)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Proposition I.4 (p. 5)**: *If two spherical triangles have two sides equal to two sides respectively, and have the angles contained by those equal arcs equal, their bases and remaining angles are equal respectively.*
* **Proposition I.5 (p. 6)**: *In every spherical triangle, any two arcs taken together are greater than the remaining arc* (:math:`\widehat{AB} + \widehat{BC} > \widehat{AC}`, proved via the trihedral solid angle at the sphere's center, cf. Euclid *Elements* XI.20).

Proposition I.8, I.9 & I.10 — SSS Congruence & Semicircle Criterion (pp. 8–10)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Proposition I.8 (p. 8)**: *If two sides equal two sides respectively, the greater angle subtends the greater base; and conversely, if all three sides equal all three sides respectively (SSS), the spherical triangles are equiangular.*
* **Proposition I.9 (p. 9)**: *In every spherical triangle, the greater arc subtends the greater spherical angle.*
* **Proposition I.10 (pp. 9–10)**: *In any spherical triangle* :math:`\triangle \mathrm{AB\Gamma}` *with side* :math:`\mathrm{A\Gamma}` *produced, according as the sum of two sides* :math:`\widehat{\mathrm{AB}} + \widehat{\mathrm{B\Gamma}}` *is less than, equal to, or greater than a semicircle, the exterior angle at* :math:`\mathrm{\Gamma}` *is respectively greater than, equal to, or less than the remote interior angle at* :math:`\mathrm{A}`—and conversely!

Proposition I.11 — Theorem: Spherical Angle-Sum Excess (p. 11)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Enunciation (*Halley 1758, p. 11*)

   *In every spherical triangle, when one side is produced, the exterior angle is less than both remote interior angles taken together; and the three interior angles of the triangle taken together are greater than two right angles.*

**[§1.4 · Demonstration]** Let :math:`\triangle \mathrm{AB\Gamma}` be a spherical triangle with side :math:`\mathrm{A\Gamma}` produced toward :math:`\mathrm{\Delta}` to meet :math:`\mathrm{AB}` produced at the antipode :math:`\mathrm{\Delta}` of :math:`\mathrm{A}` (so :math:`\mathrm{AB\Delta}` and :math:`\mathrm{A\Gamma\Delta}` form a spherical lune of semicircles, and angle :math:`\mathrm{\Delta}` equals angle :math:`\mathrm{A}`). At point :math:`\mathrm{\Gamma}` on arc :math:`\mathrm{\Gamma\Delta}`, construct spherical angle :math:`\angle \mathrm{\Delta\Gamma E} = \angle \mathrm{A} = \angle \mathrm{\Delta}` (:just:`I.1`), meeting arc :math:`\mathrm{AB\Delta}` at :math:`\mathrm{E}`.

Since :math:`\angle \mathrm{\Delta} = \angle \mathrm{\Delta\Gamma E}`, arcs :math:`\widehat{\mathrm{\Delta E}}` and :math:`\widehat{\mathrm{E\Gamma}}` are equal. Therefore :math:`\widehat{\mathrm{BE}} + \widehat{\mathrm{E\Gamma}} = \widehat{\mathrm{BE}} + \widehat{\mathrm{E\Delta}} = \widehat{\mathrm{B\Delta}}`, which is strictly **less than a semicircle** (since :math:`\widehat{\mathrm{AB}} + \widehat{\mathrm{B\Delta}}` is a full semicircle). By Proposition I.10 applied to :math:`\triangle \mathrm{B\Gamma E}`, the exterior angle :math:`\angle \mathrm{\Gamma BA}` (i.e., :math:`\angle \mathrm{B}`) is strictly **greater** than the interior angle :math:`\angle \mathrm{B\Gamma E}`. Adding :math:`\angle \mathrm{E\Gamma\Delta} = \angle \mathrm{A}` to the lesser side, :math:`\angle \mathrm{A} + \angle \mathrm{B} > \angle \mathrm{B\Gamma\Delta}` (the exterior angle of :math:`\triangle \mathrm{AB\Gamma}`!). Finally, add the interior angle :math:`\angle \mathrm{B\Gamma A}` to both: since :math:`\angle \mathrm{B\Gamma\Delta} + \angle \mathrm{B\Gamma A}` equals two right angles, the three interior angles :math:`\angle \mathrm{A} + \angle \mathrm{B} + \angle \mathrm{\Gamma}` **exceed two right angles**. *Q.E.D.*

Proposition I.17 — Theorem: AAA Spherical Congruence (pp. 18–19)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Enunciation (*Halley 1758, p. 18*)

   *If two spherical triangles have the three angles of the one equal to the three angles of the other, each to its corresponding angle, then the arcs containing those triangles are also equal to one another, each to its corresponding side.*

**[§1.5 · Menelaus's Direct Intrinsic Proof]** Let :math:`\triangle \mathrm{AB\Gamma}` and :math:`\triangle \mathrm{\Delta EZ}` have :math:`\angle \mathrm{A} = \angle \mathrm{\Delta}`, :math:`\angle \mathrm{B} = \angle \mathrm{E}`, and :math:`\angle \mathrm{\Gamma} = \angle \mathrm{Z}`. Produce arc :math:`\mathrm{AB}` past :math:`\mathrm{B}` to :math:`\mathrm{I}` so that :math:`\widehat{\mathrm{BI}} = \widehat{\mathrm{\Delta E}}`, and produce :math:`\mathrm{\Gamma B}` past :math:`\mathrm{B}` to :math:`\mathrm{\Theta}` so that :math:`\widehat{\mathrm{B\Theta}} = \widehat{\mathrm{EZ}}`. Join great-circle arc :math:`\mathrm{I\Theta}` and produce it to meet :math:`\mathrm{A\Gamma}` produced at :math:`\mathrm{K}`.

1. Because vertical spherical angles at :math:`\mathrm{B}` are equal, :math:`\angle \mathrm{IB\Theta} = \angle \mathrm{AB\Gamma} = \angle \mathrm{E}`; hence by **SAS congruence** (Prop. I.4), :math:`\triangle \mathrm{BI\Theta} \cong \triangle \mathrm{E\Delta Z}`, giving :math:`\widehat{\mathrm{I\Theta}} = \widehat{\mathrm{\Delta Z}}`, :math:`\angle \mathrm{BI\Theta} = \angle \mathrm{\Delta} = \angle \mathrm{A}`, and :math:`\angle \mathrm{B\Theta I} = \angle \mathrm{Z} = \angle \mathrm{\Gamma}`.
2. In spherical triangle :math:`\triangle \mathrm{\Theta K\Gamma}`, the exterior angle at :math:`\mathrm{\Gamma}` equals the remote interior angle at :math:`\mathrm{\Theta}`; therefore, by **Proposition I.10**, :math:`\widehat{\mathrm{\Theta K}} + \widehat{\mathrm{K\Gamma}} = \text{semicircle}`.
3. Likewise, in :math:`\triangle \mathrm{AIK}`, the exterior angle at :math:`\mathrm{I}` equals the remote interior angle at :math:`\mathrm{A}`; therefore, by **Proposition I.10**, :math:`\widehat{\mathrm{AK}} + \widehat{\mathrm{KI}} = \text{semicircle}`.
4. Consequently :math:`\widehat{\mathrm{K\Theta}} + \widehat{\mathrm{K\Gamma}} = \widehat{\mathrm{IK}} + \widehat{\mathrm{KA}}`. Subtracting the common sum :math:`\widehat{\mathrm{IK}} + \widehat{\mathrm{K\Gamma}}` from both sides leaves :math:`\widehat{\mathrm{\Theta I}} = \widehat{\mathrm{A\Gamma}}`!
5. Since :math:`\widehat{\mathrm{\Theta I}} = \widehat{\mathrm{\Delta Z}}`, we have :math:`\widehat{\mathrm{A\Gamma}} = \widehat{\mathrm{\Delta Z}}`; and because :math:`\angle \mathrm{A} = \angle \mathrm{\Delta}` and :math:`\angle \mathrm{\Gamma} = \angle \mathrm{Z}`, **ASA congruence** (Prop. I.14) yields :math:`\widehat{\mathrm{AB}} = \widehat{\mathrm{\Delta E}}` and :math:`\widehat{\mathrm{B\Gamma}} = \widehat{\mathrm{EZ}}`. *Quod erat demonstrandum.*

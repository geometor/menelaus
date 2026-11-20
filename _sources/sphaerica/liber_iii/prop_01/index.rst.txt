:layout: book
:order: 1
:canonical_id: III.1
:breadcrumb_title: Proposition III.1
:folio: halley_1758_menelai_sphaericorum:0096
:tracks: English: index | Latin: la | Summary: summary | Notes: notes

.. _liber-iii-prop-01:
.. _sphaerica-iii-1:

Proposition III.1 — The Spherical Menelaus Transversal Theorem
==============================================================

.. rubric:: *Menelai Alexandrini Sphaericorum Lib. III Prop. I. Theor. (Halley 1758, pp. 80–82)*

.. folio:: halley_1758_menelai_sphaericorum:0096
   :page: 80

Proposition III.1 — Theorem: *Theorema Menelai* / *Figura Catha* (pp. 80–82)
----------------------------------------------------------------------------

.. admonition:: Enunciation (*Halley 1758, p. 80*)

   *Let there be upon the surface of a sphere two arcs of great circles* :math:`\mathrm{NME}`, :math:`\mathrm{NA\Lambda}`, *between which let two other great-circle arcs* :math:`\mathrm{E\Theta A}`, :math:`\mathrm{\Lambda\Theta M}` *be drawn meeting one another at point* :math:`\mathrm{\Theta}`: *I say that the* :term:`sine <sinus>` *of arc* :math:`\widehat{\mathrm{AN}}` *has to the sine of arc* :math:`\widehat{\mathrm{A\Lambda}}` *a* :term:`ratio compounded <ratio-composita>` *of the ratio which the sine of arc* :math:`\widehat{\mathrm{NE}}` *has to the sine of arc* :math:`\widehat{\mathrm{EM}}`, *and of the ratio which the sine of arc* :math:`\widehat{\mathrm{M\Theta}}` *has to the sine of arc* :math:`\widehat{\mathrm{\Theta\Lambda}}`.

.. picture:: /_static/figures/spherical-menelaus-3d.svg
   :alt: Exact 3D spherical Menelaus configuration on the unit sphere S^2
   :caption: Exact spherical Menelaus configuration on the unit sphere S² (Sphaerica Prop. III.1): great-circle transversal DF cuts the sides of spherical triangle △ABC at D (external on BC), E, and F.

On the unit sphere :g:`S² <( S2 )>`, great-circle :term:`transversal <transversalis>` :g:`DF <[ D F ]>` cuts the sides of spherical triangle :g:`A`, :g:`B`, :g:`C` (:g:`AB </ A B />`, :g:`BC </ B C />`, :g:`CA </ C A />`) at :g:`D` (external on :g:`BC <[ B C ]>`), :g:`E`, and :g:`F`, satisfying:

.. math::

   \frac{\sin\widehat{AF}}{\sin\widehat{FB}} \cdot \frac{\sin\widehat{BD}}{\sin\widehat{DC}} \cdot \frac{\sin\widehat{CE}}{\sin\widehat{EA}} = -1.

**[§3.1 · Menelaus's Gnomonic-Chord Demonstration, Halley pp. 80–82]** Let point :math:`\mathrm{B}` be set as the center of the sphere, and join straight lines (chords and radii) :math:`\mathrm{\Lambda N}`, :math:`\mathrm{\Lambda M}`, :math:`\mathrm{MN}`, :math:`\mathrm{EB}`, and :math:`\mathrm{\Theta B}` meeting chord :math:`\mathrm{M\Lambda}` at :math:`\mathrm{\Delta}`, and radius :math:`\mathrm{AB}` meeting chord :math:`\mathrm{N\Lambda}` at :math:`\mathrm{\Sigma}`; and let straight line :math:`\mathrm{\Delta\Sigma}` be drawn and produced until it meets straight line :math:`\mathrm{MN}` produced at :math:`\mathrm{K}`:

1. Point :math:`\mathrm{K}` lies in the plane of *both* great circles :math:`\mathrm{A\Theta E}` and :math:`\mathrm{NME}`. Since points :math:`\mathrm{E}` and :math:`\mathrm{B}` also lie in both planes, :math:`\mathrm{KEB}` is a single straight line (Euclid *Elements* XI.3).
2. In the planar triangle :math:`\triangle \mathrm{N\Lambda M}`, point :math:`\mathrm{\Sigma}` lies on :math:`\mathrm{N\Lambda}`, point :math:`\mathrm{\Delta}` lies on :math:`\mathrm{M\Lambda}`, and point :math:`\mathrm{K}` lies on :math:`\mathrm{MN}` produced, with :math:`\mathrm{\Sigma}, \mathrm{\Delta}, \mathrm{K}` collinear. Therefore, by the **Planar Menelaus Lemma** (*per sequens Lemma I*), the ratio :math:`\mathrm{N\Sigma} : \mathrm{\Sigma\Lambda}` is compounded of :math:`\mathrm{NK} : \mathrm{KM}` and :math:`\mathrm{M\Delta} : \mathrm{\Delta\Lambda}`.
3. By the **Chord-Sine Lemma** (*per Lemma II*), :math:`\mathrm{NK} : \mathrm{KM}` equals the perpendicular dropped from :math:`\mathrm{N}` onto diameter :math:`\mathrm{KEB}` to the perpendicular from :math:`\mathrm{M}` onto the same diameter—that is, :math:`\sin \widehat{\mathrm{NE}} : \sin \widehat{\mathrm{EM}}`. Likewise :math:`\mathrm{N\Sigma} : \mathrm{\Sigma\Lambda} = \sin \widehat{\mathrm{NA}} : \sin \widehat{\mathrm{A\Lambda}}`, and :math:`\mathrm{M\Delta} : \mathrm{\Delta\Lambda} = \sin \widehat{\mathrm{M\Theta}} : \sin \widehat{\mathrm{\Theta\Lambda}}`.
4. Hence :math:`\sin \widehat{\mathrm{AN}} : \sin \widehat{\mathrm{A\Lambda}}` is compounded of :math:`\sin \widehat{\mathrm{NE}} : \sin \widehat{\mathrm{EM}}` and :math:`\sin \widehat{\mathrm{M\Theta}} : \sin \widehat{\mathrm{\Theta\Lambda}}`. *Q.E.D.*

**[§3.2 · Limiting Parallel Case & Alternation, pp. 81–82]**

.. folio:: halley_1758_menelai_sphaericorum:0097
   :page: 81

Now if straight line :math:`\mathrm{\Delta\Sigma}` be **parallel** to straight line :math:`\mathrm{MN}`: then the common diameter :math:`\mathrm{EB}` will be parallel to both straight lines :math:`\mathrm{\Delta\Sigma}, \mathrm{MN}` (by Euclid *Elements* XI.9); hence the perpendiculars from :math:`\mathrm{N}` and :math:`\mathrm{M}` onto diameter :math:`\mathrm{EB}` are equal (:math:`\sin \widehat{\mathrm{NE}} = \sin \widehat{\mathrm{EM}}`, since :math:`\widehat{\mathrm{EM}} + \widehat{\mathrm{NE}}` equals a semicircle), and :math:`\sin \widehat{\mathrm{NA}} : \sin \widehat{\mathrm{A\Lambda}} = \sin \widehat{\mathrm{M\Theta}} : \sin \widehat{\mathrm{\Theta\Lambda}}`. Inverting the compounded ratio yields the companion *katà diaíresin* identity:

.. math::

   \frac{\sin \widehat{\mathrm{A\Lambda}}}{\sin \widehat{\mathrm{AN}}}
   \;=\;
   \frac{\sin \widehat{\mathrm{\Lambda\Theta}}}{\sin \widehat{\mathrm{\Theta M}}}
   \cdot
   \frac{\sin \widehat{\mathrm{ME}}}{\sin \widehat{\mathrm{EN}}}.

.. toctree::
   :hidden:

   la
   summary
   notes

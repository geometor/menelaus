:navigation: header
:order: 5

.. _demos-index:

Symbolic Demonstrations
=======================

.. rubric:: *100% Exact SymPy & geometor.model Constructions of Planar, Spherical & Dual Menelaus Geometry*

Every construction in :mod:`geometor.menelaus` executes with **zero floating-point approximations** over :math:`\mathbb{Q}` and closed-form quadratic radical extensions, rendering interactive ``.euclid-graphic`` SVGs via ``scripts/build_figures.py``. Hover or click any inline ``:g:`` geometric element reference below to highlight its exact counterpart inside the figure!

----

1. Planar Menelaus & Euclidean Parallel Auxiliary (*Halley Lemma I* / *Almagest I.13*)
--------------------------------------------------------------------------------------

Given reference triangle :g:`ABC << A B C >>` (`A = (3, 6)`, `B = (0, 0)`, `C = (9, 0)`) and transversal :g:`DF <[ D F ]>` cutting extended side :g:`BC <[ B C ]>` externally at :g:`D` (`(12, 0)`), side :g:`CA <[ C A ]>` internally at :g:`E` (`(7, 2)`), and side :g:`AB <[ A B ]>` internally at :g:`F` (`(2, 4)`), drawing auxiliary segment :g:`CH </ C H />` through :g:`C` parallel to :g:`DF <[ D F ]>` (:just:`I.31`) meets :g:`AB <[ A B ]>` at :g:`H` (`(3/2, 3)`):

.. math::

   \frac{\overline{AF}}{\overline{FB}} \cdot \frac{\overline{BD}}{\overline{DC}} \cdot \frac{\overline{CE}}{\overline{EA}}
   = \frac{1}{2} \cdot (-4) \cdot \frac{1}{2} = -1, \qquad
   \left|\frac{AF}{FB} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA}\right| = +1.

.. picture:: /_static/figures/menelaus-planar-parallel.svg
   :alt: Planar Menelaus Theorem with Euclidean parallel auxiliary segment CH || DF
   :caption: Planar Menelaus's Theorem: similar triangles via auxiliary segment CH parallel to transversal DF.

Constructed symbolically via :func:`~geometor.menelaus.planar_transversal.construct_menelaus_planar`.

----

2. Wildberger Rational Trigonometry Formulation (Quadrance & Spread Laws)
-------------------------------------------------------------------------

Using :func:`~geometor.model.quadrance` and :func:`~geometor.model.line_spread` (:func:`~geometor.menelaus.planar_transversal.menelaus_rational_trig_invariants`), Planar Menelaus on :g:`ABC << A B C >>` and transversal :g:`DF <[ D F ]>` holds purely over :math:`\mathbb{Q}` with zero square roots:

.. math::

   \frac{Q(A, F)\,Q(B, D)\,Q(C, E)}{Q(F, B)\,Q(D, C)\,Q(E, A)}
   = \frac{s(t, b)}{s(t, c)} \cdot \frac{s(t, c)}{s(t, a)} \cdot \frac{s(t, a)}{s(t, b)} = 1.

.. picture:: /_static/figures/menelaus-rational-trig.svg
   :alt: Rational Trigonometry quadrance and spread sub-triangle verification of Menelaus's Theorem
   :caption: Rational Trigonometry formulation: spread ratios across sub-triangles △AFE, △BDF, and △CDE telescope identically to 1 over ℚ.

----

3. Converse of Menelaus Gallery (Four Projective Collinearity Theorems)
-----------------------------------------------------------------------

3.1 External Angle-Bisector Axis (Anti-Orthic Axis, cf. *Sphaerica* III.6)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On the scalene Heronian triangle :g:`ABC << A B C >>` (`A = (-9, 12)`, `B = (0, 0)`, `C = (7, 0)`, side lengths `a = 7, b = 20, c = 15`, integer incenter :g:`I` `= (1, 2)`), :func:`~geometor.menelaus.planar_transversal.construct_external_bisector_axis` constructs the three external angle bisectors meeting the opposite sides at :g:`De` `= (-21, 0)`, :g:`Ee` `= (21, -21/2)`, and :g:`Fe` `= (63/13, -84/13)`, whose signed ratio product :math:`(-c/a)(-b/c)(-a/b) = (-15/7)(-20/15)(-7/20) = -1` places :g:`De`, :g:`Ee`, and :g:`Fe` on the anti-orthic axis :g:`DeEe <[ De Ee ]>`!

.. picture:: /_static/figures/menelaus-external-bisectors.svg
   :alt: External Angle-Bisector Axis (anti-orthic axis) proved by Converse of Menelaus
   :caption: External Angle-Bisector Axis (anti-orthic axis De–Ee–Fe) of Heronian △ABC with integer incenter I.

3.2 Desargues's Two-Triangle Perspectivity Axis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In :func:`~geometor.menelaus.planar_transversal.construct_desargues_axis`, applying Planar Menelaus three times to perspective ray-triangles :math:`\triangle OBC`, :math:`\triangle OCA`, and :math:`\triangle OAB` from center :g:`O` cancels the radial ratios along :g:`OA1 <[ O A1 ]>`, :g:`OB1 <[ O B1 ]>`, and :g:`OC1 <[ O C1 ]>`, proving that corresponding side intersections :g:`D`, :g:`E`, and :g:`F` lie on Desargues's axis :g:`DF <[ D F ]>`.

.. picture:: /_static/figures/menelaus-desargues-axis.svg
   :alt: Desargues's Two-Triangle Perspectivity Axis proved via triple Menelaus
   :caption: Desargues's Two-Triangle Perspectivity Theorem proved via three applications of Planar Menelaus from center O.

3.3 Pascal's *Hexagrammum Mysticum*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In :func:`~geometor.menelaus.planar_transversal.construct_pascal_hexagram`, inscribing six rational vertices :g:`P1`, :g:`P2`, :g:`P3`, :g:`P4`, :g:`P5`, :g:`P6` on :math:`x^2 + y^2 = 100` and forming the diagonal triangle :g:`U`, :g:`V`, :g:`W` of alternating sides, three applications of Planar Menelaus combined with Euclid III.35/III.36 power-of-a-point chord products prove that opposite-side intersections :g:`L`, :g:`M`, and :g:`N` are collinear on Pascal's Mystic Line :g:`LM <[ L M ]>`.

.. picture:: /_static/figures/menelaus-pascal-hexagram.svg
   :alt: Pascal's Hexagrammum Mysticum proved via three applications of Menelaus on diagonal triangle UVW
   :caption: Pascal's Hexagrammum Mysticum: opposite-side intersections L, M, and N align on Pascal's Mystic Line via triple Menelaus on △UVW.

3.4 Monge's Three-Circle Similicenter Theorem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In :func:`~geometor.menelaus.planar_transversal.construct_monge_exsimilicenters`, for circles centered at :g:`A`, :g:`B`, :g:`C` with exact radii :math:`r_A = 1, r_B = 2, r_C = 4`, the three external centers of similitude :g:`Sbc`, :g:`Sca`, and :g:`Sab` satisfy :math:`(-r_A/r_B)(-r_B/r_C)(-r_C/r_A) = (-1/2)(-2/4)(-4/1) = -1`, placing them on Monge's external axis :g:`SbcSca <[ Sbc Sca ]>`.

.. picture:: /_static/figures/menelaus-monge-circles.svg
   :alt: Monge's Three-Circle Exsimilicenter Theorem proved via Converse of Menelaus
   :caption: Monge's Three-Circle Theorem: external similicenters Sbc, Sca, and Sab align on Monge's axis via Converse of Menelaus.

----

4. Unit-Sphere Intrinsic Geometry, Spherical Menelaus & Cross-Ratio Pencil
--------------------------------------------------------------------------

4.1 Spherical Excess (:math:`A+B+C > \pi`) & Polar Triangle AAA Congruence (*Sphaerica* I.11 & I.17)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Via :func:`~geometor.menelaus.spherical.polar_triangle`, spherical triangle :g:`A`, :g:`B`, :g:`C` (:g:`AB </ A B />`, :g:`BC </ B C />`, :g:`CA </ C A />`) and its supplementary polar triangle :g:`A*`, :g:`B*`, :g:`C*` satisfy :math:`\cos a^* = -\cos A`, confirming that three dihedral angles uniquely determine all three arc lengths on :math:`S^2` (*Sphaerica* Prop. I.17).

.. picture:: /_static/figures/spherical-excess-polar.svg
   :alt: Spherical triangle ABC and its supplementary polar triangle A*B*C* on unit sphere S^2
   :caption: Intrinsic spherical triangle △ABC and its supplementary polar triangle △A*B*C* on the unit sphere S² (Sphaerica I.11 & I.17).

4.2 Spherical Menelaus Theorem (*Sphaerica* III.1) & Spherical Cross-Ratio Pencil (*Sphaerica* III.8)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On :math:`S^2(\mathbb{Q})` with :g:`A` `= (0, 0, 1)`, :g:`B` `= (3/5, 4/5, 0)`, and :g:`C` `= (2/3, 2/3, 1/3)` cut by transversal normal `(2, -3, 1)`:

.. math::

   \frac{\sin_{\pm}\widehat{AF}}{\sin_{\pm}\widehat{FB}} \cdot
   \frac{\sin_{\pm}\widehat{BD}}{\sin_{\pm}\widehat{DC}} \cdot
   \frac{\sin_{\pm}\widehat{CE}}{\sin_{\pm}\widehat{EA}}
   = \left(\frac{5}{6}\right)\left(-\frac{18}{5}\right)\left(\frac{1}{3}\right) = -1, \qquad
   \tan\!\left(\frac{E}{2}\right) = \frac{1}{17} > 0.

In :func:`~geometor.menelaus.spherical.verify_spherical_cross_ratio_invariance`, four great circles concurrent at pole :g:`V` cut oblique great circles :g:`X1X4 <[ X1 X4 ]>` (:g:`X1`, :g:`X2`, :g:`X3`, :g:`X4`) and :g:`Y1Y4 <[ Y1 Y4 ]>` (:g:`Y1`, :g:`Y2`, :g:`Y3`, :g:`Y4`) with identical spherical sine cross-ratio :math:`-2`:

.. picture:: /_static/figures/spherical-cross-ratio-pencil.svg
   :alt: Spherical 4-great-circle pencil cutting two transversals g1 and g2 with invariant spherical sine cross-ratio
   :caption: Spherical pencil invariance (Sphaerica Prop. III.8): four great circles concurrent at pole V cut two transversals with identical sine cross-ratio −2.

----

5. Projective Point-Line Duality: Ceva (`+1`) vs. Menelaus (`-1`) & Trilinear Polars
------------------------------------------------------------------------------------

Given perspector :g:`P` `= (3, 3)` inside :g:`ABC << A B C >>`, :func:`~geometor.menelaus.duality_ceva.construct_trilinear_polar` constructs its concurrent cevians meeting the sides at :g:`Dc`, :g:`Ec`, :g:`Fc` (`Ceva product = +1`). Intersecting the cevian sides with the extended sides of :g:`ABC << A B C >>` produces the harmonic conjugates :g:`Dm`, :g:`Em`, :g:`Fm`, satisfying :math:`(B, C; D_c, D_m) = (C, A; E_c, E_m) = (A, B; F_c, F_m) = -1`, negating all three ratios :math:`(-1)^3(+1) = -1` and aligning them on the **trilinear polar** :g:`DmEm <[ Dm Em ]>`!

.. picture:: /_static/figures/menelaus-ceva-trilinear-polar.svg
   :alt: Ceva-Menelaus harmonic duality and trilinear polar Dm-Em-Fm of perspector P
   :caption: Ceva–Menelaus Harmonic Duality: harmonic conjugates Dm, Em, and Fm of cevian traces Dc, Ec, and Fc align on the trilinear polar of P.

----

Executable Demo Scripts
-----------------------

Run all three verification demos offline from the repository root:

.. code-block:: bash

   /home/phi/PROJECTS/geometor/.venv/bin/python demos/planar_menelaus_demo.py
   /home/phi/PROJECTS/geometor/.venv/bin/python demos/spherical_menelaus_demo.py
   /home/phi/PROJECTS/geometor/.venv/bin/python demos/ceva_menelaus_duality_demo.py

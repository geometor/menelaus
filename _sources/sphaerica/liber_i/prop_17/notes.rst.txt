:layout: book
:order: 10
:canonical_id: I.17
:breadcrumb_title: Proposition I.17 (Notes)
:folio: halley_1758_menelai_sphaericorum:0034
:tracks: English: index | Latin: la | Summary: summary | Notes: notes

.. _sphaerica-i-17-notes:

Scholarly & GEOMETOR Notes: Absolute Unit of Length
===================================================

.. rubric:: *Polar Triangle Duality vs. Menelaus's Direct Demonstration*

.. folio:: halley_1758_menelai_sphaericorum:0034
   :page: 18

1. Modern Proof via Polar Duality
---------------------------------

Modern textbooks prove AAA spherical congruence by passing to the :term:`polar triangle <triangulum-polare>` :math:`\triangle A^*B^*C^*` (:func:`~geometor.menelaus.spherical.polar_triangle`), where the vertices of the polar triangle are the poles of the sides of the original triangle. By the fundamental polar supplementary relations:

.. math::

   a^* \;=\; \pi - A, \qquad
   b^* \;=\; \pi - B, \qquad
   c^* \;=\; \pi - C.

If two spherical triangles have equal angles (:math:`A = A'`, :math:`B = B'`, :math:`C = C'`), their polar triangles have equal sides (:math:`a^* = a^{*\prime}`, :math:`b^* = b^{*\prime}`, :math:`c^* = c^{*\prime}`). By SSS congruence (Proposition I.8), :math:`\triangle A^*B^*C^* \cong \triangle A^{*\prime}B^{*\prime}C^{*\prime}`, whence their angles are equal, forcing the sides of the original triangles to be equal.

2. Elimination of Homothetic Dilations
--------------------------------------

On any Riemannian 2-manifold with constant Gaussian curvature :math:`K`, the Gauss–Bonnet theorem establishes:

.. math::

   E \;=\; A + B + C - \pi \;=\; K \cdot \text{Area}(\triangle ABC).

Because :math:`K = +1` on the unit sphere, the angular excess :math:`E` directly measures area. If two triangles were similar with sides scaled by :math:`k \neq 1`, their areas would scale by :math:`k^2`, requiring different excesses :math:`E \neq E'`, contradicting the assumption that their angles are identical. Thus positive curvature fixes an absolute unit of length (the quadrant / radius) and eliminates non-congruent scale similarity.

:layout: book
:order: 3
:canonical_id: I.1
:breadcrumb_title: Proposition I.1 (Notes)
:folio: halley_1758_menelai_sphaericorum:0018
:tracks: English: index | Latin: la | Summary: summary | Notes: notes

.. _sphaerica-i-1-notes:

Scholarly & GEOMETOR Notes: Angle Transfer on S^2
=================================================

.. rubric:: *Constructive Mechanics in geometor.model & Relation to Euclid I.23*

1. Elimination of Extrinsic Superposition
-----------------------------------------

In planar geometry, Euclid's proof of SAS (Elements I.4) relied on placing one triangle upon another—an operation critiqued in modern axiomatic geometry from Hilbert to Bertrand Russell. On curved manifolds like :math:`S^2`, rigid bodily superposition from one tangent space to another without parallel transport is geometrically fraught.

Menelaus resolves this difficulty intrinsically in Proposition I.1: by using the sphere's rotational symmetry about the pole normal vector, rotation in the parallel circle preserves the dihedral angle measure rigidly without leaving the surface.

2. Algebraic Realization in geometor.model
------------------------------------------

Given vertex normal :math:`\mathbf{n}_A`, direction vector :math:`\mathbf{v}_1 \perp \mathbf{n}_A`, target vertex :math:`\mathbf{B}`, and initial leg :math:`\mathbf{u}_1 \perp \mathbf{n}_B`, constructing an arc :math:`\mathbf{u}_2` such that :math:`\angle(\mathbf{u}_1, \mathbf{u}_2) = \angle(\mathbf{v}_1, \mathbf{v}_2)` corresponds to rotating :math:`\mathbf{u}_1` in the tangent plane :math:`T_{\mathbf{B}}S^2` by angle :math:`\theta = \arccos(\mathbf{v}_1 \cdot \mathbf{v}_2)` around axis :math:`\mathbf{n}_B` using Rodrigues' rotation formula:

.. math::

   \mathbf{u}_2 \;=\; \mathbf{u}_1 \cos \theta + (\mathbf{n}_B \times \mathbf{u}_1) \sin \theta.

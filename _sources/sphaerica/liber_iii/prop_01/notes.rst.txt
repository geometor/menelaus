:layout: book
:order: 1
:canonical_id: III.1
:breadcrumb_title: Proposition III.1 (Notes)
:folio: halley_1758_menelai_sphaericorum:0096
:tracks: English: index | Latin: la | Summary: summary | Notes: notes

.. _sphaerica-iii-1-notes:

Scholarly & GEOMETOR Notes: Exact 3D S² Verification & Radical Cancellation
===========================================================================

.. rubric:: *Exact SymPy Verification in geometor.menelaus.spherical*

.. folio:: halley_1758_menelai_sphaericorum:0096
   :page: 80

1. Gnomonic Projection and Tangent Plane Mechanics
--------------------------------------------------

Menelaus's chordal proof (`[§3.1]`, Halley p. 80) and Ptolemy's proof (*Syntaxis* I.13, Heiberg pp. 74–75) both operate by intersecting rays from the sphere center :math:`O = (0, 0, 0)` with a secant or tangent plane. In modern differential geometry, this is the **gnomonic projection**:

.. math::

   \Pi_z(x, y, z) \;=\; \left(\frac{x}{z}, \;\frac{y}{z}\right).

Under gnomonic projection, every great circle on :math:`S^2` maps to a straight line on the projection plane, immediately transforming spherical transversals into planar transversals.

2. Pairwise Quadratic Radical Cancellation
------------------------------------------

In :func:`~geometor.menelaus.spherical.spherical_menelaus_default` and :func:`~geometor.menelaus.spherical.gnomonic_projection_menelaus`:

* Canonical rational points on :math:`S^2(\mathbb{Q})`:
  :math:`A = (0, 0, 1)`, :math:`B = (3/5, 4/5, 0)`, :math:`C = (2/3, 2/3, 1/3)`.
* Cutting transversal plane:
  :math:`2x - 3y + z = 0`.
* The intersection points :math:`D, E, F` involve square roots:
  :math:`D \in \mathbb{Q}(\sqrt{181})`, :math:`E = (1/\sqrt{3}, 1/\sqrt{3}, 1/\sqrt{3})`, :math:`F \in \mathbb{Q}(\sqrt{61})`.
* The six individual arc sines:
  :math:`\sin\widehat{AF} = \frac{5}{\sqrt{61}}`, :math:`\sin\widehat{FB} = \frac{6}{\sqrt{61}}`, :math:`\sin\widehat{BD} = \frac{6}{\sqrt{181}}`, :math:`\sin\widehat{DC} = -\frac{5}{3\sqrt{181}}`, :math:`\sin\widehat{CE} = \frac{\sqrt{6}}{9}`, :math:`\sin\widehat{EA} = \frac{\sqrt{6}}{3}`.
* In the signed product, **all square roots cancel identically**:

  .. math::

     \left(\frac{5}{6}\right) \cdot \left(-\frac{18}{5}\right) \cdot \left(\frac{1}{3}\right) \;=\; -1.

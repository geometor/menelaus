:layout: book
:order: 9
:canonical_id: I.11
:breadcrumb_title: Proposition I.11 (Notes)
:folio: halley_1758_menelai_sphaericorum:0027
:tracks: English: index | Latin: la | Summary: summary | Notes: notes

.. _sphaerica-i-11-notes:

Scholarly & GEOMETOR Notes: Exact Rational Excess
=================================================

.. rubric:: *Exact Algebraic Proof via Euler–Eriksson Formula in geometor.model*

.. folio:: halley_1758_menelai_sphaericorum:0027
   :page: 11

1. Exact Rational Spherical Excess
----------------------------------

In :func:`~geometor.menelaus.spherical.spherical_excess_report`, for any three rational vertices :math:`\mathbf{A}, \mathbf{B}, \mathbf{C} \in S^2(\mathbb{Q})` lying in an open hemisphere, the Euler–Eriksson formula expresses the tangent of half the :term:`spherical excess <excessus-sphaericus>` :math:`E = A + B + C - \pi` as an **exact rational number** with zero square roots or inverse trigonometric approximations:

.. math::

   \tan\!\left(\frac{E}{2}\right) \;=\;
   \frac{|\det(\mathbf{A}, \mathbf{B}, \mathbf{C})|}{1 + \mathbf{A}\cdot\mathbf{B} + \mathbf{B}\cdot\mathbf{C} + \mathbf{C}\cdot\mathbf{A}} \;\in\; \mathbb{Q}_{> 0}.

2. Canonical Rational Verification
----------------------------------

For our canonical configuration in :mod:`geometor.menelaus.spherical`:

.. math::

   \mathbf{A} = (0, 0, 1), \quad
   \mathbf{B} = \left(\frac{3}{5}, \frac{4}{5}, 0\right), \quad
   \mathbf{C} = \left(\frac{2}{3}, \frac{2}{3}, \frac{1}{3}\right):

* Determinant volume scalar: :math:`\det(\mathbf{A}, \mathbf{B}, \mathbf{C}) = \frac{3}{5}\cdot\frac{2}{3} - \frac{4}{5}\cdot\frac{2}{3} = \frac{6}{15} - \frac{8}{15} = -\frac{2}{15}`.
* Scalar product sum: :math:`1 + 0 + \left(\frac{6}{15} + \frac{8}{15}\right) + \frac{1}{3} = 1 + \frac{14}{15} + \frac{5}{15} = \frac{34}{15}`.
* Exact half-excess tangent:

.. math::

   \tan\left(\frac{E}{2}\right) \;=\; \frac{2/15}{34/15} \;=\; \frac{1}{17} \;>\; 0.

Since :math:`\tan(E/2) = 1/17 > 0`, it follows with 100% algebraic certitude that :math:`E > 0`, rigorously certifying Menelaus's Proposition I.11 purely within :math:`\mathbb{Q}`!

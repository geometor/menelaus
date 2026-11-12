:title: Unit III — GEOMETOR Notes: Symbolic Proofs, Gnomonic Map & Rational Trigonometry
:layout: book

.. _unit-3-notes:

Unit III — Scholarly & GEOMETOR Symbolic Commentary
===================================================

.. rubric:: *Exact SymPy Verification of Planar Menelaus, Gnomonic Projection & Wildberger Quadrances*

1. Exact Symbolic Verification of Planar Menelaus & Its Universal Converse
--------------------------------------------------------------------------

In :func:`~geometor.menelaus.planar_transversal.construct_menelaus_planar`, triangle :math:`A = (3, 6)`, :math:`B = (0, 0)`, :math:`C = (9, 0)` is cut by :term:`transversal <transversalis>` :math:`DF` through :math:`D = (12, 0)` (external on :math:`BC`) and :math:`F = (2, 4)` (internal on :math:`AB`), meeting :math:`CA` at :math:`E = (7, 2)` with auxiliary parallel :math:`CH \parallel DF` meeting :math:`AB` at :math:`H = (3/2, 3)`:

.. math::

   \frac{\overline{AF}}{\overline{FB}} = \frac{1}{2}, \qquad
   \frac{\overline{BD}}{\overline{DC}} = -4, \qquad
   \frac{\overline{CE}}{\overline{EA}} = \frac{1}{2}
   \quad\Longrightarrow\quad
   \left(\frac{1}{2}\right)(-4)\left(\frac{1}{2}\right) = -1.

Furthermore, :func:`~geometor.menelaus.planar_transversal.verify_planar_menelaus_universal` proves the **universal algebraic identity** over :math:`\mathbb{Q}[x_A, y_A, x_B, y_B, x_C, y_C, u, v, w]`: for :math:`F = (1-u)A + uB`, :math:`D = (1-v)B + vC`, :math:`E = (1-w)C + wA`,

.. math::

   \det\begin{pmatrix} x_D & y_D & 1 \\ x_E & y_E & 1 \\ x_F & y_F & 1 \end{pmatrix}
   \;\equiv\;
   \det\begin{pmatrix} x_A & y_A & 1 \\ x_B & y_B & 1 \\ x_C & y_C & 1 \end{pmatrix}
   \cdot \Bigl(u v w + (1 - u)(1 - v)(1 - w)\Bigr),

making both the **Forward Theorem** and the **Converse Theorem** two halves of a single polynomial factorization!

2. Rational Trigonometry Reformulation (Wildberger Quadrances & Spreads)
------------------------------------------------------------------------

.. picture:: /_static/figures/menelaus-rational-trig.svg
   :alt: Rational Trigonometry quadrance and spread invariants of Planar Menelaus
   :caption: Rational Trigonometry view of Planar Menelaus: polynomial quadrance balance Q(A,F)·Q(B,D)·Q(C,E) = Q(F,B)·Q(D,C)·Q(E,A) and Spread Law telescoping across △ABC and transversal DF.

In Norman J. Wildberger's Rational Trigonometry (:cite:`Divine Proportions, 2005 <wildberger-2005>`, cf. ``geometor/wildberger`` and :func:`~geometor.menelaus.planar_transversal.menelaus_rational_trig_invariants`), replacing Euclidean distance and angle with :term:`quadrance and spread <quadrantia-et-extensio>` :math:`Q(P, R) = (x_R - x_P)^2 + (y_R - y_P)^2` and :math:`s(\ell_1, \ell_2)` eliminates all square roots and transcendental functions across :g:`△ABC << A B C >>` and transversal :g:`DF <[ D F ]>`. On our canonical configuration :math:`A = (3,6), B = (0,0), C = (9,0)` with :math:`D = (12,0), E = (7,2), F = (2,4)`:

- :math:`Q(A,F) = 5`, :math:`Q(F,B) = 20`, :math:`Q(B,D) = 144`, :math:`Q(D,C) = 9`, :math:`Q(C,E) = 8`, :math:`Q(E,A) = 32`,
- :math:`5 \times 144 \times 8 = 5760 = 20 \times 9 \times 32`, and the Spread Law across the three sub-triangles :math:`\triangle AEF`, :math:`\triangle BDF`, :math:`\triangle CDE` telescopes identically to :math:`1`!

3. Exact 3D Unit-Sphere & Gnomonic Verification (:mod:`geometor.menelaus.spherical`)
------------------------------------------------------------------------------------

Notice how Menelaus's chordal proof (`[§3.1]`, Halley p. 80) and Ptolemy's proof (`[§3.5]`, Heiberg pp. 74–75) operate by intersecting rays from the sphere's center :math:`O = (0,0,0)` with an affine plane—which is **central (gnomonic) projection** :math:`\Pi_z(x, y, z) = (x/z, y/z)` onto the tangent plane :math:`z = 1`! In :func:`~geometor.menelaus.spherical.spherical_menelaus_default` and :func:`~geometor.menelaus.spherical.gnomonic_projection_menelaus`:

- Vertices :math:`A = (0,0,1)`, :math:`B = (3/5, 4/5, 0)`, :math:`C = (2/3, 2/3, 1/3) \in S^2(\mathbb{Q})` cut by transversal plane :math:`2x - 3y + z = 0` meet in radical traces :math:`D \in \mathbb{Q}(\sqrt{181})`, :math:`E = (\frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}})`, :math:`F \in \mathbb{Q}(\sqrt{61})`.
- Although the six arc sines lie in quadratic extensions (:math:`\sin\widehat{AF} = \frac{5}{\sqrt{61}}`, :math:`\sin\widehat{FB} = \frac{6}{\sqrt{61}}`, :math:`\sin\widehat{BD} = \frac{6}{\sqrt{181}}`, :math:`\sin\widehat{DC} = -\frac{5}{3\sqrt{181}}`, :math:`\sin\widehat{CE} = \frac{\sqrt{6}}{9}`, :math:`\sin\widehat{EA} = \frac{\sqrt{6}}{3}`), **every quadratic radical cancels pairwise** via :math:`\frac{[\mathbf{P}, \mathbf{Q}, \mathbf{n}_t]}{[\mathbf{Q}, \mathbf{R}, \mathbf{n}_t]}`:

.. math::

   \left(\frac{5}{6}\right) \cdot \left(-\frac{18}{5}\right) \cdot \left(\frac{1}{3}\right) = -1,
   \qquad
   \frac{\operatorname{crd}(2\widehat{AF})}{\operatorname{crd}(2\widehat{FB})}
   \cdot \frac{\operatorname{crd}(2\widehat{BD})}{\operatorname{crd}(2\widehat{DC})}
   \cdot \frac{\operatorname{crd}(2\widehat{CE})}{\operatorname{crd}(2\widehat{EA})} = 1.

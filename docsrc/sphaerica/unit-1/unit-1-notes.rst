:title: Unit I — GEOMETOR Notes: Unit-Sphere Algebra, Excess & Polar AAA
:layout: book

.. _unit-1-notes:

Unit I — Scholarly & GEOMETOR Symbolic Commentary
=================================================

.. rubric:: *Philological Apparatus & Exact SymPy Verification on* :math:`S^2(\mathbb{Q})`

1. Philological Note on Costard's Preface & Direct Proofs
---------------------------------------------------------

In :cite:`Costard's Praefatio (1758, p. iv) <costard-1758>`, the Bodleian Huntington Hebrew witness is traced explicitly to :person:`Isḥāq ibn Ḥunayn <ishaq-ibn-hunayn>`'s ninth-century Baghdad translation and :person:`Jacob ben Machir <jacob-ben-machir>`'s Montpellier version. As :person:`Axel Anthon Björnbo <bjornbo>` (:cite:`1902, §5 <bjornbo-1902>`) and :person:`Thomas Little Heath <euclid>` (:cite:`1921, Vol. II pp. 262–265 <heath-greek-math-1921>`) emphasize, Menelaus systematically avoids *reductio ad absurdum* throughout Book I—matching :person:`Proclus <proclus>`'s testimony (:cite:`Friedlein p. 345 <proclus-friedlein-1873>`) regarding Menelaus's direct proof of Euclid *Elements* I.25.

2. Exact Rational Certification of Spherical Excess (:mod:`geometor.menelaus.spherical`)
----------------------------------------------------------------------------------------

In :func:`~geometor.menelaus.spherical.spherical_excess_report`, for any three rational vertices :math:`\mathbf{A}, \mathbf{B}, \mathbf{C} \in S^2(\mathbb{Q})` lying in an open hemisphere, the Euler–Eriksson formula expresses the tangent of half the :term:`spherical excess <excessus-sphaericus>` :math:`E = A + B + C - \pi` as an **exact rational number** with zero square roots or inverse cosines:

.. math::

   \tan\!\left(\frac{E}{2}\right) =
   \frac{|\det(\mathbf{A}, \mathbf{B}, \mathbf{C})|}{1 + \mathbf{A}\cdot\mathbf{B} + \mathbf{B}\cdot\mathbf{C} + \mathbf{C}\cdot\mathbf{A}} \in \mathbb{Q}_{> 0}.

For our canonical rational triangle :math:`A = (0, 0, 1)`, :math:`B = (3/5, 4/5, 0)`, :math:`C = (2/3, 2/3, 1/3)`:

- :math:`|\det(\mathbf{A}, \mathbf{B}, \mathbf{C})| = \frac{2}{15}`,
- :math:`1 + \mathbf{A}\cdot\mathbf{B} + \mathbf{B}\cdot\mathbf{C} + \mathbf{C}\cdot\mathbf{A} = 1 + 0 + \frac{14}{15} + \frac{1}{3} = \frac{34}{15}`,
- whence :math:`\tan(E/2) = \frac{2/15}{34/15} = \frac{1}{17} > 0`, certifying :math:`A + B + C > \pi` (*Sphaerica* Prop. I.11) purely in :math:`\mathbb{Q}`!

3. Polar Triangle Duality vs. Menelaus's Intrinsic Proof of Prop. I.17
----------------------------------------------------------------------

Modern textbooks prove AAA spherical congruence (*Sphaerica* Prop. I.17) by passing to the :term:`polar triangle <triangulum-polare>` :math:`\triangle A^*B^*C^*` (:func:`~geometor.menelaus.spherical.polar_triangle`), where :math:`\cos a^* = -\cos A` reduces AAA on :math:`\triangle ABC` to SSS (Prop. I.8) on :math:`\triangle A^*B^*C^*`. Remarkably, Menelaus's own proof on pp. 18–19 (`[§1.5]`) achieves the exact same result *within the primal sphere* using only vertical SAS copying and two semicircle applications of Proposition I.10—demonstrating that positive curvature :math:`K = +1` fixes an absolute unit of length (the quadrant / semicircle) and eliminates non-congruent homothetic similarity (contrast ``geometor/hilbert`` on the independence of Euclid's Parallel Postulate).

:title: Unit II — GEOMETOR Notes: Rising-Time Convexity & Spherical Differential Inequalities
:layout: book

.. _unit-2-notes:

Unit II — Scholarly & GEOMETOR Symbolic Commentary
==================================================

.. rubric:: *Historiographical Context (Björnbo 1902) & Exact Convexity Interpretation*

1. Björnbo (1902) & Halley (1758) on Book II Manuscript Numbering
-----------------------------------------------------------------

As :person:`Axel Anthon Björnbo <bjornbo>` (:cite:`1902, §§6–8 <bjornbo-1902>`) documented by comparing :person:`Edmond Halley <halley>`'s Oxford edition (:cite:`1758 <halley-1758>`, 12 propositions in Book II) against :person:`Gerard of Cremona <gerard-of-cremona>`'s Toledo Latin version and :person:`Abū Naṣr Manṣūr <abu-nasr-mansur>`'s 1007 CE redaction, medieval copyists subdivided Menelaus's multi-case cevian theorems differently (producing between 8 and 19 numbered propositions), yet every witness preserves the programmatic Theodosian transition (`[§2.2]`, Halley p. 75) verbatim from the Arabic of :person:`Isḥāq ibn Ḥunayn <ishaq-ibn-hunayn>` / :person:`Thābit ibn Qurra <thabit-ibn-qurra>`. :person:`Francesco Maurolico <maurolico>` (:cite:`1558 <maurolico-1558>`), by contrast, expanded Book II heavily with his own interpolated lemmas, which Halley systematically excised using the Bodleian Huntington Hebrew codex of :person:`Jacob ben Machir <jacob-ben-machir>`.

2. Modern Analytic Meaning of Proposition II.10 (Declination & Right Ascension)
-------------------------------------------------------------------------------

Let the ecliptic ``ΘΜΒ`` meet the celestial equator ``ΒΤΞΡΧ`` at the vernal equinox ``Β`` with obliquity :math:`\varepsilon \in (0, \pi/2)`, and let :math:`\lambda \in [0, \pi/2]` denote ecliptic longitude measured from ``Β`` toward the summer solstice ``Θ`` (:math:`\lambda = \pi/2`). Along the ecliptic, declination :math:`\delta(\lambda)` and right ascension :math:`\alpha(\lambda)` obey the spherical right-triangle laws (derived quantitatively in Book III, Prop. III.1 Coroll. 2):

.. math::

   \sin \delta(\lambda) = \sin \varepsilon \, \sin \lambda,
   \qquad
   \tan \alpha(\lambda) = \cos \varepsilon \, \tan \lambda.

Differentiating twice on :math:`\lambda \in (0, \pi/2)`:

- **Declination concavity** (:math:`\delta''(\lambda) < 0`): equal ecliptic increments :math:`\Delta\lambda` produce **larger** declination changes :math:`\Delta\delta` near the equinox ``Β`` (hence larger polar-complement differences ``ΠΟ > ΣΘ``) than near the solstice ``Θ``.
- **Right-ascension convexity** (:math:`\alpha''(\lambda) > 0` for :math:`\lambda \in (\pi/4, \pi/2)` and monotone comparison from solstice ``Θ``): equal ecliptic arcs near the solstice ``Θ`` project onto **larger** equatorial right-ascension arcs ``ΧΡ > ΞΤ`` than equal arcs nearer the equinox ``Β``.

Menelaus proves both second-difference inequalities purely synthetically—with zero calculus and zero tables—from the intrinsic geometry of spherical triangle ``ΜΓΘ``!

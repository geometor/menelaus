.. _about-intrinsic-spherical:

Intrinsic Spherical Geometry vs. Euclid's Planar *Elements*
===========================================================

Emancipating the Sphere from Stereometry
----------------------------------------

Prior to :person:`Menelaus <menelaus>`, Greek treatises on the sphere—such as Autolycus's *On the Moving Sphere* and :person:`Theodosius <theodosius>`'s :cite:`Sphaerica <theodosius-hunt-1707>`—studied great and parallel circles exclusively as three-dimensional Euclidean sections of a solid ball. Neither Autolycus nor Theodosius ever defined a **spherical triangle**.

In Book I, Definition I of his *Sphaerica* (:cite:`Halley 1758, p. 1 <halley-1758>`), Menelaus performs a quiet axiomatic revolution: he defines the :term:`triangulum sphaericum <triangulum-sphaericum>` intrinsically on the two-dimensional curved surface :math:`S^2` as the region bounded by three minor arcs of :term:`great circles <circulus-magnus>` (*arcus circulorum magnorum... semper minores semicirculo*).

What Survives and What Breaks Without the Parallel Postulate
------------------------------------------------------------

Because two distinct great circles on :math:`S^2` always intersect in two antipodal points, Euclid's Fifth Postulate fails globally on the sphere. Menelaus systematically rebuilds :person:`Euclid <euclid>`'s *Elements* Book I on :math:`S^2`, revealing with razor-sharp precision which theorems belong to neutral/absolute metric geometry and which depend on zero curvature:

.. list-table:: Euclidean Plane (:math:`K = 0`) vs. Menelaus's Sphere (:math:`K = +1`)
   :header-rows: 1
   :widths: 28 36 36

   * - Geometric Principle
     - Euclid's *Elements* (Book I & VI)
     - Menelaus's *Sphaerica* (Book I & III)
   * - Geodesic sides
     - Straight line segments (*I Def. 4*)
     - Minor arcs of great circles (*I Def. 1–2*)
   * - Congruence (SAS, SSS, ASA)
     - *I.4, I.8, I.26*
     - *I.4, I.8, I.14–16* (holds intrinsically!)
   * - Triangle inequality
     - *I.20*: :math:`a + b > c`
     - *I.5*: :math:`\widehat{AB} + \widehat{BC} > \widehat{AC}` (and :math:`a+b+c < 2\pi`)
   * - Exterior & interior angle sum
     - *I.16 & I.32*: :math:`\text{ext} > \text{int}`, :math:`A + B + C = \pi`
     - **I.11**: :math:`\text{ext} < \text{int}_1 + \text{int}_2`, :math:`A + B + C > \pi` (:term:`excess <excessus-sphaericus>`)
   * - Equiangular triangles (AAA)
     - *VI.4*: Similar, arbitrary scale!
     - **I.17**: **Strictly congruent** (scale fixed by sphere radius!)
   * - Transversal compound ratio
     - :math:`\frac{AF}{FB}\frac{BD}{DC}\frac{CE}{EA} = -1` (*Lemma I*)
     - **III.1**: :math:`\frac{\sin AF}{\sin FB}\frac{\sin BD}{\sin DC}\frac{\sin CE}{\sin EA} = -1`

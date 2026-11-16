:layout: book
:order: 4
:canonical_id: Ptolemy I.13
:breadcrumb_title: Ptolemy Almagest I.13 (Summary)
:folio: ptolemy_1898_syntaxis_vol1_pt1:0078
:tracks: English: index | Latin: la | Summary: summary | Notes: notes

.. _sphaerica-iii-ptolemy-i-13-summary:

Analytical Summary: Ptolemy's Chords vs. Menelaus's Sines
=========================================================

.. rubric:: *Modern Elements-2.0 Comparison of Ptolemaic and Menelaean Formulations*

1. Ptolemy's Chord Formulation
------------------------------

In *Almagest* I.13, Ptolemy expresses the transversal theorem in terms of the chord of double the arc:

.. math::

   \frac{\operatorname{crd}(2\widehat{\Gamma E})}{\operatorname{crd}(2\widehat{EA})}
   \;=\;
   \frac{\operatorname{crd}(2\widehat{\Gamma Z})}{\operatorname{crd}(2\widehat{Z\Delta})}
   \cdot
   \frac{\operatorname{crd}(2\widehat{\Delta B})}{\operatorname{crd}(2\widehat{BA})}.

Because Ptolemy's table of chords (:math:`R = 60^p`) was calibrated for astronomical interpolation, this formulation directly fed his calculations of:
- Declination circles and right ascensions (*Syntaxis* I.14–16).
- Rising times in sphaera recta and sphaera obliqua (*Syntaxis* II.7–9).

2. Structural Equivalence
-------------------------

Since :math:`\operatorname{crd}(2\theta) = 2R \sin \theta`, the factor :math:`2R` cancels in each of the three ratios, making Ptolemy's chord identity mathematically identical to Menelaus's sine theorem:

.. math::

   \frac{2R \sin \widehat{\Gamma E}}{2R \sin \widehat{EA}}
   \;=\;
   \frac{2R \sin \widehat{\Gamma Z}}{2R \sin \widehat{Z\Delta}}
   \cdot
   \frac{2R \sin \widehat{\Delta B}}{2R \sin \widehat{BA}}
   \quad\Longleftrightarrow\quad
   \frac{\sin \widehat{\Gamma E}}{\sin \widehat{EA}}
   \;=\;
   \frac{\sin \widehat{\Gamma Z}}{\sin \widehat{Z\Delta}}
   \cdot
   \frac{\sin \widehat{\Delta B}}{\sin \widehat{BA}}.

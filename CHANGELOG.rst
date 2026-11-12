=========
Changelog
=========

0.1.0 (2026-11-12)
------------------

- **4-Track Synchronized Book Codex (`docsrc/sphaerica/`)**:
  - Scan-verified diplomatic Latin edition from Edmond Halley's *Menelai Sphaericorum Libri III* (Oxford, 1758, with George Costard's *Praefatio*) and polytonic Greek primary witness from Claudius Ptolemy's *Syntaxis Mathematica* I.13 (ed. J. L. Heiberg, 1898), paired with a 100% original English translation, analytical summaries, and GEOMETOR mathematical commentary across **Units I–IV**.
  - Full scholarly apparatus (`concordance.rst`, `bibliography.rst`, `persons.rst`, `glossary.rst` and `resources/sphaerica/*.json`) cross-referencing Halley (1758), Maurolico (1558), Björnbo (1902), Euclid's *Elements*, `geometor/elements`, `geometor/pappus`, `geometor/altshiller-court`, `geometor/ceva`, and `geometor/etc`.
- **Exact Symbolic Geometry Engine (`src/geometor/menelaus/`)**:
  - `planar_transversal.py`: `geometor.model` Planar Menelaus proof with Euclidean parallel auxiliary (`CH || DF`), universal polynomial converse, External Angle-Bisector Axis, Desargues's Axis, Pascal's *Hexagrammum Mysticum*, Monge's Three-Circle Similicenters, and Wildberger Rational Trigonometry (`quadrance`, `line_spread`, `vertex_spread`, `cross_ratio`) formulation.
  - `spherical.py`: Exact 3D unit-sphere ($x^2 + y^2 + z^2 = 1$) solver verifying positive spherical excess ($A + B + C > \pi$, Prop. I.11), polar triangle duality and AAA spherical congruence (Prop. I.17), **Spherical Menelaus's Theorem** (Prop. III.1) in both Ptolemaic double-arc chords and sines, central gnomonic projection, spherical cross-ratio pencil invariance (Prop. III.8), and spherical altitude concurrency (Prop. III.10).
  - `duality_ceva.py`: Projective $\mathbb{P}^2$ point-line polarity, complete-quadrangle harmonic conjugation transforming Ceva triples ($+1$) into Menelaus triples ($-1$), and exact ETC trilinear polars (`X(1)`, `X(2)`, `X(4)`, `X(7)`).
  - `render.py` & `scripts/build_figures.py`: 10 interactive dark/light-adaptive `.euclid-graphic` SVGs.

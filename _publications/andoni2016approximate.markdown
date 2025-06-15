---
layout: publication
title: 'Approximate Near Neighbors For General Symmetric Norms'
authors: Alexandr Andoni, Huy L. Nguyen, Aleksandar Nikolov, Ilya Razenshteyn, Erik Waingarten
conference: "Arxiv"
year: 2016
citations: 12
bibkey: andoni2016approximate
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1611.06222'}
tags: ['ANN Search', 'Tools and Libraries', 'Approximate Nearest Neighbor Search']
---
We show that every symmetric normed space admits an efficient nearest
neighbor search data structure with doubly-logarithmic approximation.
Specifically, for every \\(n\\), \\(d = n^\{o(1)\}\\), and every \\(d\\)-dimensional
symmetric norm \\(\|\cdot\|\\), there exists a data structure for
\\(\mathrm\{poly\}(log log n)\\)-approximate nearest neighbor search over
\\(\|\cdot\|\\) for \\(n\\)-point datasets achieving \\(n^\{o(1)\}\\) query time and
\\(n^\{1+o(1)\}\\) space. The main technical ingredient of the algorithm is a
low-distortion embedding of a symmetric norm into a low-dimensional iterated
product of top-\\(k\\) norms.
  We also show that our techniques cannot be extended to general norms.

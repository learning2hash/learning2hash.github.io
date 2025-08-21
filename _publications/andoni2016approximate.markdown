---
layout: publication
title: Approximate Near Neighbors For General Symmetric Norms
authors: Alexandr Andoni, Huy L. Nguyen, Aleksandar Nikolov, Ilya Razenshteyn, Erik
  Waingarten
conference: Proceedings of the 49th Annual ACM SIGACT Symposium on Theory of Computing
year: 2017
bibkey: andoni2016approximate
citations: 24
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1611.06222'}]
tags: ["Datasets", "Efficiency"]
short_authors: Andoni et al.
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
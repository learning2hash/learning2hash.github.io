---
layout: publication
title: Practical And Optimal LSH For Angular Distance
authors: Alexandr Andoni, Piotr Indyk, Thijs Laarhoven, Ilya Razenshteyn, Ludwig Schmidt
conference: Arxiv
year: 2015
citations: 238
bibkey: andoni2015practical
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1509.02897'}]
tags: [Hashing Methods, ANN Search]
---
We show the existence of a Locality-Sensitive Hashing (LSH) family for the
angular distance that yields an approximate Near Neighbor Search algorithm with
the asymptotically optimal running time exponent. Unlike earlier algorithms
with this property (e.g., Spherical LSH [Andoni, Indyk, Nguyen, Razenshteyn
2014], [Andoni, Razenshteyn 2015]), our algorithm is also practical, improving
upon the well-studied hyperplane LSH [Charikar, 2002] in practice. We also
introduce a multiprobe version of this algorithm, and conduct experimental
evaluation on real and synthetic data sets.
  We complement the above positive results with a fine-grained lower bound for
the quality of any LSH family for angular distance. Our lower bound implies
that the above LSH family exhibits a trade-off between evaluation time and
quality that is close to optimal for a natural class of LSH functions.
---
layout: publication
title: Hypercube LSH For Approximate Near Neighbors
authors: Laarhoven Thijs
conference: ""
year: 2017
bibkey: laarhoven2017hypercube
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1702.05760"}
tags: ['Independent', 'LSH']
---
<p>A celebrated technique for finding near neighbors for the angular
distance involves using a set of hyperplanes to partition the space into
hash regions [Charikar, STOC 2002]. Experiments later showed that using
a set of hyperplanes, thereby partitioning the space into the Voronoi
regions induced by a hypercube, leads to even better results [Terasawa
and Tanaka, WADS 2007]. However, no theoretical explanation for this
improvement was ever given, and it remained unclear how the resulting
hypercube hash method scales in high dimensions. In this work, we
provide explicit asymptotics for the collision probabilities when using
hypercubes to partition the space. For instance, two near-orthogonal
vectors are expected to collide with probability <span
class="math inline">\((\frac{1}{\pi})^{d + o(d)}\)</span> in dimension
<span class="math inline">\(d\)</span>, compared to <span
class="math inline">\((\frac{1}{2})^d\)</span> when using random
hyperplanes. Vectors at angle <span
class="math inline">\(\frac{\pi}{3}\)</span> collide with probability
<span class="math inline">\((\frac{\sqrt{3}}{\pi})^{d + o(d)}\)</span>,
compared to <span class="math inline">\((\frac{2}{3})^d\)</span> for
random hyperplanes, and near-parallel vectors collide with similar
asymptotic probabilities in both cases. For <span
class="math inline">\(c\)</span>-approximate nearest neighbor searching,
this translates to a decrease in the exponent <span
class="math inline">\(\rho\)</span> of locality-sensitive hashing (LSH)
methods of a factor up to <span class="math inline">\(\log_2(\pi)
\approx 1.652\)</span> compared to hyperplane LSH. For <span
class="math inline">\(c = 2\)</span>, we obtain <span
class="math inline">\(\rho \approx 0.302 + o(1)\)</span> for hypercube
LSH, improving upon the <span class="math inline">\(\rho
\approx 0.377\)</span> for hyperplane LSH. We further describe how to
use hypercube LSH in practice, and we consider an example application in
the area of lattice algorithms.</p>

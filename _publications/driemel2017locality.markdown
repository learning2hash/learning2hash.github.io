---
layout: publication
title: Locality-sensitive Hashing Of Curves
authors: Driemel Anne, Silvestri Francesco
conference: "Arxiv"
year: 2017
bibkey: driemel2017locality
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1703.04040"}
tags: ['ARXIV']
---
<p>We study data structures for storing a set of polygonal curves in
<span class="math inline">\({\rm R}^d\)</span> such that, given a query
curve, we can efficiently retrieve similar curves from the set, where
similarity is measured using the discrete Fr'echet distance or the
dynamic time warping distance. To this end we devise the first
locality-sensitive hashing schemes for these distance measures. A major
challenge is posed by the fact that these distance measures internally
optimize the alignment between the curves. We give solutions for
different types of alignments including constrained and unconstrained
versions. For unconstrained alignments, we improve over a result by
Indyk from 2002 for short curves. Let <span
class="math inline">\(n\)</span> be the number of input curves and let
<span class="math inline">\(m\)</span> be the maximum complexity of a
curve in the input. In the particular case where <span
class="math inline">\(m \leq \frac{\alpha}{4d} \log
n\)</span>, for some fixed <span
class="math inline">\(\alpha&gt;0\)</span>, our solutions imply an
approximate near-neighbor data structure for the discrete Fr'echet
distance that uses space in <span
class="math inline">\(O(n^{1+\alpha}\log n)\)</span> and achieves query
time in <span class="math inline">\(O(n^{\alpha}\log^2 n)\)</span> and
constant approximation factor. Furthermore, our solutions provide a
trade-off between approximation quality and computational performance:
for any parameter <span class="math inline">\(k \in [m]\)</span>, we can
give a data structure that uses space in <span
class="math inline">\(O(2^{2k}m^{k-1} n
\log n + nm)\)</span>, answers queries in <span class="math inline">\(O(
2^{2k} m^{k}\log n)\)</span> time and achieves approximation factor in
<span class="math inline">\(O(m/k)\)</span>.</p>

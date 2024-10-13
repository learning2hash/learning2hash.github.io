---
layout: publication
title: Graph-based Time-space Trade-offs For Approximate Near Neighbors
authors: Laarhoven Thijs
conference: ""
year: 2017
bibkey: laarhoven2017graph
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1712.03158"}
tags: ['Graph', 'Independent']
---
<p>We take a first step towards a rigorous asymptotic analysis of
graph-based approaches for finding (approximate) nearest neighbors in
high-dimensional spaces, by analyzing the complexity of (randomized)
greedy walks on the approximate near neighbor graph. For random data
sets of size <span class="math inline">\(n = 2^{o(d)}\)</span> on the
<span class="math inline">\(d\)</span>-dimensional Euclidean unit
sphere, using near neighbor graphs we can provably solve the approximate
nearest neighbor problem with approximation factor <span
class="math inline">\(c &gt; 1\)</span> in query time <span
class="math inline">\(n^{\rho_q + o(1)}\)</span> and space <span
class="math inline">\(n^{1 + \rho_s +
o(1)}\)</span>, for arbitrary <span class="math inline">\(\rho_q, \rho_s
\geq 0\)</span> satisfying <span class="math display">\[\begin{align}
(2c^2 -
1) \rho_q + 2 c^2 (c^2 - 1) \sqrt{\rho_s (1 - \rho_s)} \geq c^4.
\end{align}\]</span> Graph-based near neighbor searching is especially
competitive with hash-based methods for small <span
class="math inline">\(c\)</span> and near-linear memory, and in this
regime the asymptotic scaling of a greedy graph-based search matches the
recent optimal hash-based trade-offs of
Andoni-Laarhoven-Razenshteyn-Waingarten [SODA’17]. We further study how
the trade-offs scale when the data set is of size <span
class="math inline">\(n =
2^{\Theta(d)}\)</span>, and analyze asymptotic complexities when
applying these results to lattice sieving.</p>

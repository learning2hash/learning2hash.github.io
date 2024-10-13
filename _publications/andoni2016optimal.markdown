---
layout: publication
title: Optimal Hashing-based Time-space Trade-offs For Approximate Near Neighbors
authors: Andoni Alexandr, Laarhoven Thijs, Razenshteyn Ilya, Waingarten Erik
conference: "Arxiv"
year: 2016
bibkey: andoni2016optimal
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1608.03580"}
tags: ['ARXIV', 'FOCS']
---
<p>[See the paper for the full abstract.] We show tight upper and lower
bounds for time-space trade-offs for the <span
class="math inline">\(c\)</span>-Approximate Near Neighbor Search
problem. For the <span class="math inline">\(d\)</span>-dimensional
Euclidean space and <span class="math inline">\(n\)</span>-point
datasets, we develop a data structure with space <span
class="math inline">\(n^{1 +
\rho_u + o(1)} + O(dn)\)</span> and query time <span
class="math inline">\(n^{\rho_q + o(1)} + d n^{o(1)}\)</span> for every
<span class="math inline">\(\rho_u, \rho_q \geq 0\)</span> such that:
<span class="math display">\[\begin{equation} c^2 \sqrt{\rho_q} +
(c^2 - 1) \sqrt{\rho_u} = \sqrt{2c^2 - 1}. \end{equation}\]</span> This
is the first data structure that achieves sublinear query time and
near-linear space for every approximation factor <span
class="math inline">\(c &gt; 1\)</span>, improving upon [Kapralov, PODS
2015]. The data structure is a culmination of a long line of work on the
problem for all space regimes; it builds on Spherical Locality-Sensitive
Filtering [Becker, Ducas, Gama, Laarhoven, SODA 2016] and data-dependent
hashing [Andoni, Indyk, Nguyen, Razenshteyn, SODA 2014] [Andoni,
Razenshteyn, STOC 2015]. Our matching lower bounds are of two types:
conditional and unconditional. First, we prove tightness of the whole
above trade-off in a restricted model of computation, which captures all
known hashing-based approaches. We then show unconditional cell-probe
lower bounds for one and two probes that match the above trade-off for
<span class="math inline">\(\rho_q = 0\)</span>, improving upon the best
known lower bounds from [Panigrahy, Talwar, Wieder, FOCS 2010]. In
particular, this is the first space lower bound (for any static data
structure) for two probes which is not polynomially smaller than the
one-probe bound. To show the result for two probes, we establish and
exploit a connection to locally-decodable codes.</p>

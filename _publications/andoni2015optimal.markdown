---
layout: publication
title: Optimal Data-dependent Hashing For Approximate Near Neighbors
authors: Andoni Alexandr, Razenshteyn Ilya
conference: "Arxiv"
year: 2015
bibkey: andoni2015optimal
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1501.01062"}
tags: ['ARXIV', 'Independent', 'LSH']
---
<p>We show an optimal data-dependent hashing scheme for the approximate
near neighbor problem. For an <span
class="math inline">\(n\)</span>-point data set in a <span
class="math inline">\(d\)</span>-dimensional space our data structure
achieves query time <span class="math inline">\(O(d
n^{\rho+o(1)})\)</span> and space <span
class="math inline">\(O(n^{1+\rho+o(1)}
+ dn)\)</span>, where <span
class="math inline">\(\rho=\tfrac{1}{2c^2-1}\)</span> for the Euclidean
space and approximation <span class="math inline">\(c&gt;1\)</span>. For
the Hamming space, we obtain an exponent of <span
class="math inline">\(\rho=\tfrac{1}{2c-1}\)</span>. Our result
completes the direction set forth in [AINR14] who gave a
proof-of-concept that data-dependent hashing can outperform classical
Locality Sensitive Hashing (LSH). In contrast to [AINR14], the new bound
is not only optimal, but in fact improves over the best (optimal) LSH
data structures [IM98,AI06] for all approximation factors <span
class="math inline">\(c&gt;1\)</span>. From the technical perspective,
we proceed by decomposing an arbitrary dataset into several subsets that
are, in a certain sense, pseudo-random.</p>

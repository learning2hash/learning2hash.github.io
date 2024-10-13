---
layout: publication
title: Dynamic Enumeration Of Similarity Joins
authors: Agarwal Pankaj K., Hu Xiao, Sintos Stavros, Yang Jun
conference: "Arxiv"
year: 2021
bibkey: agarwal2021dynamic
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2105.01818"}
tags: ['ARXIV', 'Independent', 'LSH']
---
<p>This paper considers enumerating answers to similarity-join queries
under dynamic updates: Given two sets of <span
class="math inline">\(n\)</span> points <span
class="math inline">\(A,B\)</span> in <span
class="math inline">\(\mathbb{R}^d\)</span>, a metric <span
class="math inline">\(\phi(\cdot)\)</span>, and a distance threshold
<span class="math inline">\(r &gt; 0\)</span>, report all pairs of
points <span class="math inline">\((a, b) \in A \times B\)</span> with
<span class="math inline">\(\phi(a,b) \le r\)</span>. Our goal is to
store <span class="math inline">\(A,B\)</span> into a dynamic data
structure that, whenever asked, can enumerate all result pairs with
worst-case delay guarantee, i.e., the time between enumerating two
consecutive pairs is bounded. Furthermore, the data structure can be
efficiently updated when a point is inserted into or deleted from <span
class="math inline">\(A\)</span> or <span
class="math inline">\(B\)</span>. We propose several efficient data
structures for answering similarity-join queries in low dimension. For
exact enumeration of similarity join, we present near-linear-size data
structures for <span class="math inline">\(\ell_1, \ell_\infty\)</span>
metrics with <span class="math inline">\(\log^{O(1)} n\)</span> update
time and delay. We show that such a data structure is not feasible for
the <span class="math inline">\(\ell_2\)</span> metric for <span
class="math inline">\(d \ge 4\)</span>. For approximate enumeration of
similarity join, where the distance threshold is a soft constraint, we
obtain a unified linear-size data structure for <span
class="math inline">\(\ell_p\)</span> metric, with <span
class="math inline">\(\log^{O(1)} n\)</span> delay and update time. In
high dimensions, we present an efficient data structure with worst-case
delay-guarantee using locality sensitive hashing (LSH).</p>

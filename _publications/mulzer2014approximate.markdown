---
layout: publication
title: Approximate K-flat Nearest Neighbor Search
authors: Mulzer Wolfgang, Nguyen Huy L., Seiferth Paul, Stein Yannik
conference: "Arxiv"
year: 2014
bibkey: mulzer2014approximate
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1411.1519"}
tags: ['ARXIV']
---
<p>Let <span class="math inline">\(k\)</span> be a nonnegative integer.
In the approximate <span class="math inline">\(k\)</span>-flat nearest
neighbor (<span class="math inline">\(k\)</span>-ANN) problem, we are
given a set <span class="math inline">\(P \subset \mathbb{R}^d\)</span>
of <span class="math inline">\(n\)</span> points in <span
class="math inline">\(d\)</span>-dimensional space and a fixed
approximation factor <span class="math inline">\(c &gt; 1\)</span>. Our
goal is to preprocess <span class="math inline">\(P\)</span> so that we
can efficiently answer approximate <span
class="math inline">\(k\)</span>-flat nearest neighbor queries: given a
<span class="math inline">\(k\)</span>-flat <span
class="math inline">\(F\)</span>, find a point in <span
class="math inline">\(P\)</span> whose distance to <span
class="math inline">\(F\)</span> is within a factor <span
class="math inline">\(c\)</span> of the distance between <span
class="math inline">\(F\)</span> and the closest point in <span
class="math inline">\(P\)</span>. The case <span class="math inline">\(k
= 0\)</span> corresponds to the well-studied approximate nearest
neighbor problem, for which a plethora of results are known, both in low
and high dimensions. The case <span class="math inline">\(k = 1\)</span>
is called approximate line nearest neighbor. In this case, we are aware
of only one provably efficient data structure, due to Andoni, Indyk,
Krauthgamer, and Nguyen. For <span class="math inline">\(k
\geq 2\)</span>, we know of no previous results. We present the first
efficient data structure that can handle approximate nearest neighbor
queries for arbitrary <span class="math inline">\(k\)</span>. We use a
data structure for <span class="math inline">\(0\)</span>-ANN-queries as
a black box, and the performance depends on the parameters of the <span
class="math inline">\(0\)</span>-ANN solution: suppose we have an <span
class="math inline">\(0\)</span>-ANN structure with query time <span
class="math inline">\(O(n^{\rho})\)</span> and space requirement <span
class="math inline">\(O(n^{1+\sigma})\)</span>, for <span
class="math inline">\(\rho, \sigma &gt; 0\)</span>. Then we can answer
<span class="math inline">\(k\)</span>-ANN queries in time <span
class="math inline">\(O(n^{k/(k + 1 - \rho) + t})\)</span> and space
<span class="math inline">\(O(n^{1+\sigma k/(k + 1 - \rho)} +
n\log^{O(1/t)} n)\)</span>. Here, <span class="math inline">\(t &gt;
0\)</span> is an arbitrary constant and the <span
class="math inline">\(O\)</span>-notation hides exponential factors in
<span class="math inline">\(k\)</span>, <span
class="math inline">\(1/t\)</span>, and <span
class="math inline">\(c\)</span> and polynomials in <span
class="math inline">\(d\)</span>. Our new data structures also give an
improvement in the space requirement over the previous result for <span
class="math inline">\(1\)</span>-ANN: we can achieve near-linear space
and sublinear query time, a further step towards practical applications
where space constitutes the bottleneck.</p>

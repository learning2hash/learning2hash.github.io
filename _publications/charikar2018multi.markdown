---
layout: publication
title: Multi-resolution Hashing For Fast Pairwise Summations
authors: Charikar Moses, Siminelakis Paris
conference: "Arxiv"
year: 2018
bibkey: charikar2018multi
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1807.07635"}
tags: ['ARXIV', 'FOCS', 'Independent']
---
<p>A basic computational primitive in the analysis of massive datasets
is summing simple functions over a large number of objects. Modern
applications pose an additional challenge in that such functions often
depend on a parameter vector <span class="math inline">\(y\)</span>
(query) that is unknown a priori. Given a set of points <span
class="math inline">\(X\subset
\mathbb{R}^{d}\)</span> and a pairwise function <span
class="math inline">\(w:\mathbb{R}^{d}\times
\mathbb{R}^{d}\to [0,1]\)</span>, we study the problem of designing a
data-structure that enables sublinear-time approximation of the
summation <span class="math inline">\(Z_{w}(y)=\frac{1}{|X|}\sum_{x\in
X}w(x,y)\)</span> for any query <span class="math inline">\(y\in
\mathbb{R}^{d}\)</span>. By combining ideas from Harmonic Analysis
(partitions of unity and approximation theory) with
Hashing-Based-Estimators [Charikar, Siminelakis FOCS’17], we provide a
general framework for designing such data structures through hashing
that reaches far beyond what previous techniques allowed. A key design
principle is a collection of <span class="math inline">\(T\geq
1\)</span> hashing schemes with collision probabilities <span
class="math inline">\(p_{1},\ldots, p_{T}\)</span> such that <span
class="math inline">\(\sup_{t\in
[T]}\{p_{t}(x,y)\} = \Theta(\sqrt{w(x,y)})\)</span>. This leads to a
data-structure that approximates <span
class="math inline">\(Z_{w}(y)\)</span> using a sub-linear number of
samples from each hash family. Using this new framework along with
Distance Sensitive Hashing [Aumuller, Christiani, Pagh, Silvestri
PODS’18], we show that such a collection can be constructed and
evaluated efficiently for any log-convex function <span
class="math inline">\(w(x,y)=e^{\phi(\langle x,y\rangle)}\)</span> of
the inner product on the unit sphere <span class="math inline">\(x,y\in
\mathcal{S}^{d-1}\)</span>. Our method leads to data structures with
sub-linear query time that significantly improve upon random sampling
and can be used for Kernel Density or Partition Function Estimation. We
provide extensions of our result from the sphere to <span
class="math inline">\(\mathbb{R}^{d}\)</span> and from scalar functions
to vector functions.</p>

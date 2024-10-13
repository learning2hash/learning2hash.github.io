---
layout: publication
title: Parameter-free Locality Sensitive Hashing For Spherical Range Reporting
authors: Ahle Thomas D., Aumüller Martin, Pagh Rasmus
conference: "Arxiv"
year: 2016
bibkey: ahle2016parameter
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1605.02673"}
tags: ['ARXIV', 'Independent', 'LSH']
---
<p>We present a data structure for <em>spherical range reporting</em> on
a point set <span class="math inline">\(S\)</span>, i.e., reporting all
points in <span class="math inline">\(S\)</span> that lie within radius
<span class="math inline">\(r\)</span> of a given query point <span
class="math inline">\(q\)</span>. Our solution builds upon the
Locality-Sensitive Hashing (LSH) framework of Indyk and Motwani, which
represents the asymptotically best solutions to near neighbor problems
in high dimensions. While traditional LSH data structures have several
parameters whose optimal values depend on the distance distribution from
<span class="math inline">\(q\)</span> to the points of <span
class="math inline">\(S\)</span>, our data structure is parameter-free,
except for the space usage, which is configurable by the user.
Nevertheless, its expected query time basically matches that of an LSH
data structure whose parameters have been <em>optimally chosen for the
data and query</em> in question under the given space constraints. In
particular, our data structure provides a smooth trade-off between hard
queries (typically addressed by standard LSH) and easy queries such as
those where the number of points to report is a constant fraction of
<span class="math inline">\(S\)</span>, or where almost all points in
<span class="math inline">\(S\)</span> are far away from the query
point. In contrast, known data structures fix LSH parameters based on
certain parameters of the input alone. The algorithm has expected query
time bounded by <span class="math inline">\(O(t (n/t)^\rho)\)</span>,
where <span class="math inline">\(t\)</span> is the number of points to
report and <span class="math inline">\(\rho\in (0,1)\)</span> depends on
the data distribution and the strength of the LSH family used. We
further present a parameter-free way of using multi-probing, for LSH
families that support it, and show that for many such families this
approach allows us to get expected query time close to <span
class="math inline">\(O(n^\rho+t)\)</span>, which is the best we can
hope to achieve using LSH. The previously best running time in high
dimensions was <span class="math inline">\(\Omega(t
n^\rho)\)</span>. For many data distributions where the intrinsic
dimensionality of the point set close to <span
class="math inline">\(q\)</span> is low, we can give improved upper
bounds on the expected query time.</p>

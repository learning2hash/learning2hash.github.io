---
layout: publication
title: Entropy Based Nearest Neighbor Search In High Dimensions
authors: Panigrahy Rina
conference: "Arxiv"
year: 2005
bibkey: panigrahy2005entropy
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/cs/0510019"}
tags: ['ARXIV', 'Independent']
---
<p>In this paper we study the problem of finding the approximate nearest
neighbor of a query point in the high dimensional space, focusing on the
Euclidean space. The earlier approaches use locality-preserving hash
functions (that tend to map nearby points to the same value) to
construct several hash tables to ensure that the query point hashes to
the same bucket as its nearest neighbor in at least one table. Our
approach is different – we use one (or a few) hash table and hash
several randomly chosen points in the neighborhood of the query point
showing that at least one of them will hash to the bucket containing its
nearest neighbor. We show that the number of randomly chosen points in
the neighborhood of the query point <span
class="math inline">\(q\)</span> required depends on the entropy of the
hash value <span class="math inline">\(h(p)\)</span> of a random point
<span class="math inline">\(p\)</span> at the same distance from <span
class="math inline">\(q\)</span> at its nearest neighbor, given <span
class="math inline">\(q\)</span> and the locality preserving hash
function <span class="math inline">\(h\)</span> chosen randomly from the
hash family. Precisely, we show that if the entropy <span
class="math inline">\(I(h(p)|q,h) = M\)</span> and <span
class="math inline">\(g\)</span> is a bound on the probability that two
far-off points will hash to the same bucket, then we can find the
approximate nearest neighbor in <span
class="math inline">\(O(n^\rho)\)</span> time and near linear <span
class="math inline">\(\tilde O(n)\)</span> space where <span
class="math inline">\(\rho = M/\log(1/g)\)</span>. Alternatively we can
build a data structure of size <span class="math inline">\(\tilde
O(n^{1/(1-\rho)})\)</span> to answer queries in <span
class="math inline">\(\tilde O(d)\)</span> time. By applying this
analysis to the locality preserving hash functions in and adjusting the
parameters we show that the <span class="math inline">\(c\)</span>
nearest neighbor can be computed in time <span
class="math inline">\(\tilde O(n^\rho)\)</span> and near linear space
where <span class="math inline">\(\rho \approx 2.06/c\)</span> as <span
class="math inline">\(c\)</span> becomes large.</p>

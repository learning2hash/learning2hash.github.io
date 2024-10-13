---
layout: publication
title: Dartminhash Fast Sketching For Weighted Sets
authors: Christiani Tobias
conference: "Arxiv"
year: 2020
bibkey: christiani2020dartminhash
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2005.11547"}
tags: ['ARXIV', 'Independent']
---
<p>Weighted minwise hashing is a standard dimensionality reduction
technique with applications to similarity search and large-scale kernel
machines. We introduce a simple algorithm that takes a weighted set
<span class="math inline">\(x \in \mathbb{R}_{\geq
0}^{d}\)</span> and computes <span class="math inline">\(k\)</span>
independent minhashes in expected time <span class="math inline">\(O(k
\log k +
\Vert x \Vert_{0}\log( \Vert x \Vert_1 + 1/\Vert x \Vert_1))\)</span>,
improving upon the state-of-the-art BagMinHash algorithm (KDD ’18) and
representing the fastest weighted minhash algorithm for sparse data. Our
experiments show running times that scale better with <span
class="math inline">\(k\)</span> and <span class="math inline">\(\Vert x
\Vert_0\)</span> compared to ICWS (ICDM ’10) and BagMinhash, obtaining
<span class="math inline">\(10\)</span>x speedups in common use cases.
Our approach also gives rise to a technique for computing fully
independent locality-sensitive hash values for <span
class="math inline">\((L, K)\)</span>-parameterized approximate near
neighbor search under weighted Jaccard similarity in optimal expected
time <span class="math inline">\(O(LK + \Vert x \Vert_0)\)</span>,
improving on prior work even in the case of unweighted sets.</p>

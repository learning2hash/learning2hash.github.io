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
Weighted minwise hashing is a standard dimensionality reduction technique with applications to similarity search and large-scale kernel machines. We introduce a simple algorithm that takes a weighted set $x \in \mathbb\{R\}\_\{\geq 0\}^\{d\}\( and computes \)k\( independent minhashes in expected time \)O(k \log k + \Vert x \Vert\_\{0\}\log( \Vert x \Vert\_1 + 1/\Vert x \Vert\_1))$, improving upon the state-of-the-art BagMinHash algorithm (KDD '18) and representing the fastest weighted minhash algorithm for sparse data. Our experiments show running times that scale better with \(k\) and \(\Vert x \Vert_0\) compared to ICWS (ICDM '10) and BagMinhash, obtaining \(10\)x speedups in common use cases. Our approach also gives rise to a technique for computing fully independent locality-sensitive hash values for \((L, K)\)-parameterized approximate near neighbor search under weighted Jaccard similarity in optimal expected time \(O(LK + \Vert x \Vert_0)\), improving on prior work even in the case of unweighted sets.

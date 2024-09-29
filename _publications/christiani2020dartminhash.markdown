---
layout: publication
title: Dartminhash Fast Sketching For Weighted Sets
authors: Christiani Tobias
conference: "Arxiv"
year: 2020
bibkey: christiani2020dartminhash
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2005.11547"}
tags: ['ARXIV', 'Independent', 'KDD']
---
Weighted minwise hashing is a standard dimensionality reduction technique with applications to similarity search and large45;scale kernel machines. We introduce a simple algorithm that takes a weighted set x in R95;123;≥ 0125;^123;d125; and computes k independent minhashes in expected time O(k log k + Vert x Vert95;123;0125;log( Vert x Vert95;1 + 1/Vert x Vert95;1)) improving upon the state45;of45;the45;art BagMinHash algorithm (KDD 18) and representing the fastest weighted minhash algorithm for sparse data. Our experiments show running times that scale better with k and Vert x Vert95;0 compared to ICWS (ICDM 10) and BagMinhash obtaining 10x speedups in common use cases. Our approach also gives rise to a technique for computing fully independent locality45;sensitive hash values for (L K)45;parameterized approximate near neighbor search under weighted Jaccard similarity in optimal expected time O(LK + Vert x Vert95;0) improving on prior work even in the case of unweighted sets.

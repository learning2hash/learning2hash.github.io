---
layout: publication
title: Set Similarity Search Beyond Minhash
authors: Christiani Tobias, Pagh Rasmus
conference: "Arxiv"
year: 2016
bibkey: christiani2016set
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1612.07710"}
tags: ['ARXIV', 'Independent', 'LSH']
---
We consider the problem of approximate set similarity search under Braun-Blanquet similarity $B(\mathbf&amp;\#123;x&amp;\#125;, \mathbf&amp;\#123;y&amp;\#125;) = |\mathbf&amp;\#123;x&amp;\#125; \cap \mathbf&amp;\#123;y&amp;\#125;| / \max(|\mathbf&amp;\#123;x&amp;\#125;|, |\mathbf&amp;\#123;y&amp;\#125;|)\(. The \)(b\_2, b\_2)$-approximate Braun-Blanquet similarity search problem is to preprocess a collection of sets \(P\) such that, given a query set \(\mathbf\&amp;\#123;q\&amp;\#125;\), if there exists $\mathbf&amp;\#123;x&amp;\#125; \in P\( with \)B(\mathbf&amp;\#123;q&amp;\#125;, \mathbf&amp;\#123;x&amp;\#125;) \geq b\_1$, then we can efficiently return \(\mathbf\&amp;\#123;x\&amp;\#125;' \in P\) with \(B(\mathbf\&amp;\#123;q\&amp;\#125;, \mathbf\&amp;\#123;x\&amp;\#125;') > b\_2\). We present a simple data structure that solves this problem with space usage \(O(n^\&amp;\#123;1+\rho\&amp;\#125;\log n + \sum\_\&amp;\#123;\mathbf\&amp;\#123;x\&amp;\#125; \in P\&amp;\#125;|\mathbf\&amp;\#123;x\&amp;\#125;|)\) and query time \(O(|\mathbf\&amp;\#123;q\&amp;\#125;|n^\&amp;\#123;\rho\&amp;\#125; \log n)\) where \(n = |P|\) and $\rho = \log(1/b\_1)/\log(1/b\_2)$. Making use of existing lower bounds for locality-sensitive hashing by O'Donnell et al. (TOCT 2014) we show that this value of \(\rho\) is tight across the parameter space, i.e., for every choice of constants \(0 < b\_2 < b\_1 < 1\). In the case where all sets have the same size our solution strictly improves upon the value of \(\rho\) that can be obtained through the use of state-of-the-art data-independent techniques in the Indyk-Motwani locality-sensitive hashing framework (STOC 1998) such as Broder's MinHash (CCS 1997) for Jaccard similarity and Andoni et al.'s cross-polytope LSH (NIPS 2015) for cosine similarity. Surprisingly, even though our solution is data-independent, for a large part of the parameter space we outperform the currently best data-dependent method by Andoni and Razenshteyn (STOC 2015).

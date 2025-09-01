---
layout: publication
title: Set Similarity Search Beyond Minhash
authors: Tobias Christiani, Rasmus Pagh
conference: Proceedings of the 49th Annual ACM SIGACT Symposium on Theory of Computing
year: 2017
bibkey: christiani2016set
citations: 45
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1612.07710'}]
tags: ["Distance Metric Learning", "Efficiency", "Hashing Methods", "Locality-Sensitive-Hashing", "Similarity Search", "Tools & Libraries"]
short_authors: Tobias Christiani, Rasmus Pagh
---
We consider the problem of approximate set similarity search under
Braun-Blanquet similarity \(B(\mathbf\{x\}, \mathbf\{y\}) = |\mathbf\{x\} \cap
\mathbf\{y\}| / \max(|\mathbf\{x\}|, |\mathbf\{y\}|)\). The \((b_2, b_2)\)-approximate
Braun-Blanquet similarity search problem is to preprocess a collection of sets
\(P\) such that, given a query set \(\mathbf\{q\}\), if there exists \(\mathbf\{x\} \in
P\) with \(B(\mathbf\{q\}, \mathbf\{x\}) \geq b_1\), then we can efficiently return
\(\mathbf\{x\}' \in P\) with \(B(\mathbf\{q\}, \mathbf\{x\}') > b_2\).
  We present a simple data structure that solves this problem with space usage
\(O(n^\{1+\rho\}log n + \sum_\{\mathbf\{x\} \in P\}|\mathbf\{x\}|)\) and query time
\(O(|\mathbf\{q\}|n^\{\rho\} log n)\) where \(n = |P|\) and \(\rho =
log(1/b_1)/log(1/b_2)\). Making use of existing lower bounds for
locality-sensitive hashing by O'Donnell et al. (TOCT 2014) we show that this
value of \(\rho\) is tight across the parameter space, i.e., for every choice of
constants \(0 < b_2 < b_1 < 1\).
  In the case where all sets have the same size our solution strictly improves
upon the value of \(\rho\) that can be obtained through the use of
state-of-the-art data-independent techniques in the Indyk-Motwani
locality-sensitive hashing framework (STOC 1998) such as Broder's MinHash (CCS
1997) for Jaccard similarity and Andoni et al.'s cross-polytope LSH (NIPS 2015)
for cosine similarity. Surprisingly, even though our solution is
data-independent, for a large part of the parameter space we outperform the
currently best data-dependent method by Andoni and Razenshteyn (STOC 2015).
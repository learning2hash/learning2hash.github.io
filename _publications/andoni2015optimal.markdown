---
layout: publication
title: "Optimal Data-Dependent Hashing for Approximate Near Neighbors"
authors: Andoni Alexandr, Razenshteyn Ilya
conference: Arxiv
year: 2015
bibkey: andoni2015optimal
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1501.01062"}
tags: ['ARXIV', 'LSH']
---
We show an optimal data-dependent hashing scheme for the approximate near neighbor problem. For an \$n\$-point data set in a \$d\$-dimensional space our data structure achieves query time \$O(d n^\{\rho+o(1)\})\$ and space \$O(n^\{1+\rho+o(1)\} + dn)\$, where \$\rho=\tfrac\{1\}\{2c^2-1\}\$ for the Euclidean space and approximation \$c>1\$. For the Hamming space, we obtain an exponent of \$\rho=\tfrac\{1\}\{2c-1\}\$. Our result completes the direction set forth in [AINR14] who gave a proof-of-concept that data-dependent hashing can outperform classical Locality Sensitive Hashing (LSH). In contrast to [AINR14], the new bound is not only optimal, but in fact improves over the best (optimal) LSH data structures [IM98,AI06] for all approximation factors \$c>1\$. From the technical perspective, we proceed by decomposing an arbitrary dataset into several subsets that are, in a certain sense, pseudo-random.
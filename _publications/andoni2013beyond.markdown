---
layout: publication
title: "Beyond Locality-Sensitive Hashing"
authors: Andoni Alexandr, Indyk Piotr, Nguyen Huy L., Razenshteyn Ilya
conference: "Arxiv"
year: 2013
bibkey: andoni2013beyond
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1306.1547"}
tags: ['ARXIV', 'FOCS']
---
We present a new data structure for the c-approximate near neighbor problem
(ANN) in the Euclidean space. For n points in R^d, our algorithm achieves
O(n^{\rho} + d log n) query time and O(n^{1 + \rho} + d log n) space, where \rho
<= 7/(8c^2) + O(1 / c^3) + o(1). This is the first improvement over the result
by Andoni and Indyk (FOCS 2006) and the first data structure that bypasses a
locality-sensitive hashing lower bound proved by O'Donnell, Wu and Zhou (ICS
2011). By a standard reduction we obtain a data structure for the Hamming space
and \ell_1 norm with \rho <= 7/(8c) + O(1/c^{3/2}) + o(1), which is the first
improvement over the result of Indyk and Motwani (STOC 1998).

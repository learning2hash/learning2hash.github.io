---
layout: publication
title: "Tight Lower Bounds for Data-Dependent Locality-Sensitive Hashing"
authors: Andoni Alexandr, Razenshteyn Ilya
conference: "Arxiv"
year: 2015
bibkey: andoni2015tight
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1507.04299"}
tags: ['ARXIV']
---
We prove a tight lower bound for the exponent \$\rho\$ for data-dependent
Locality-Sensitive Hashing schemes, recently used to design efficient solutions
for the \$c\$-approximate nearest neighbor search. In particular, our lower
bound matches the bound of \$\rho\le \frac\{1\}\{2c-1\}+o(1)\$ for the
\$\ell_1\$ space, obtained via the recent algorithm from [Andoni-Razenshteyn,
STOC'15]. In recent years it emerged that data-dependent hashing is strictly
superior to the classical Locality-Sensitive Hashing, when the hash function is
data-independent. In the latter setting, the best exponent has been already
known: for the \$\ell_1\$ space, the tight bound is \$\rho=1/c\$, with the upper
bound from [Indyk-Motwani, STOC'98] and the matching lower bound from
[O'Donnell-Wu-Zhou, ITCS'11]. We prove that, even if the hashing is data-
dependent, it must hold that \$\rho\ge \frac\{1\}\{2c-1\}-o(1)\$. To prove the
result, we need to formalize the exact notion of data-dependent hashing that
also captures the complexity of the hash functions (in addition to their
collision properties). Without restricting such complexity, we would allow for
obviously infeasible solutions such as the Voronoi diagram of a dataset. To
preclude such solutions, we require our hash functions to be succinct. This
condition is satisfied by all the known algorithmic results.

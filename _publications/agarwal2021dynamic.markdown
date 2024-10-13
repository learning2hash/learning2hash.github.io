---
layout: publication
title: Dynamic Enumeration Of Similarity Joins
authors: Agarwal Pankaj K., Hu Xiao, Sintos Stavros, Yang Jun
conference: "Arxiv"
year: 2021
bibkey: agarwal2021dynamic
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2105.01818"}
tags: ['ARXIV', 'Independent', 'LSH']
---
This paper considers enumerating answers to similarity-join queries under
dynamic updates: Given two sets of \\{n\\} points \\{A,B\\} in \\{\mathbb\{R\}^d\\}, a metric
\\{\phi(\cdot)\\}, and a distance threshold \\{r > 0\\}, report all pairs of points
\\{(a, b) \in A \times B\\} with \\{\phi(a,b) \le r\\}. Our goal is to store \\{A,B\\} into
a dynamic data structure that, whenever asked, can enumerate all result pairs
with worst-case delay guarantee, i.e., the time between enumerating two
consecutive pairs is bounded. Furthermore, the data structure can be
efficiently updated when a point is inserted into or deleted from \\{A\\} or \\{B\\}.
  We propose several efficient data structures for answering similarity-join
queries in low dimension. For exact enumeration of similarity join, we present
near-linear-size data structures for \\{\ell_1, \ell_\infty\\} metrics with
\\{log^\{O(1)\} n\\} update time and delay. We show that such a data structure is
not feasible for the \\{ℓ₂\\} metric for \\{d \ge 4\\}. For approximate enumeration
of similarity join, where the distance threshold is a soft constraint, we
obtain a unified linear-size data structure for \\{\ell_p\\} metric, with
\\{log^\{O(1)\} n\\} delay and update time. In high dimensions, we present an
efficient data structure with worst-case delay-guarantee using locality
sensitive hashing (LSH).

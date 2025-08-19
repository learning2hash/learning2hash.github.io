---
layout: publication
title: 'Lightweight-yet-efficient: Revitalizing Ball-tree For Point-to-hyperplane
  Nearest Neighbor Search'
authors: Qiang Huang, Anthony K. H. Tung
conference: 2023 IEEE 39th International Conference on Data Engineering (ICDE)
year: 2023
bibkey: huang2023lightweight
citations: 4
additional_links: [{name: Code, url: 'https://github.com/HuangQiang/BC-Tree.'}, {
    name: Paper, url: 'https://arxiv.org/abs/2302.10626'}]
tags: [Hashing Methods, Tree-based ANN]
short_authors: Qiang Huang, Anthony K. H. Tung
---
Finding the nearest neighbor to a hyperplane (or Point-to-Hyperplane Nearest
Neighbor Search, simply P2HNNS) is a new and challenging problem with
applications in many research domains. While existing state-of-the-art hashing
schemes (e.g., NH and FH) are able to achieve sublinear time complexity without
the assumption of the data being in a unit hypersphere, they require an
asymmetric transformation, which increases the data dimension from \(d\) to
\(Ω(d^2)\). This leads to considerable overhead for indexing and incurs
significant distortion errors.
  In this paper, we investigate a tree-based approach for solving P2HNNS using
the classical Ball-Tree index. Compared to hashing-based methods, tree-based
methods usually require roughly linear costs for construction, and they provide
different kinds of approximations with excellent flexibility. A simple
branch-and-bound algorithm with a novel lower bound is first developed on
Ball-Tree for performing P2HNNS. Then, a new tree structure named BC-Tree,
which maintains the Ball and Cone structures in the leaf nodes of Ball-Tree, is
described together with two effective strategies, i.e., point-level pruning and
collaborative inner product computing. BC-Tree inherits both the low
construction cost and lightweight property of Ball-Tree while providing a
similar or more efficient search. Experimental results over 16 real-world data
sets show that Ball-Tree and BC-Tree are around 1.1\(\sim\)10\(\times\) faster than
NH and FH, and they can reduce the index size and indexing time by about
1\(\sim\)3 orders of magnitudes on average. The code is available at
https://github.com/HuangQiang/BC-Tree.
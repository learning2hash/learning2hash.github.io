---
layout: publication
title: Simple And Efficient Four-cycle Counting On Sparse Graphs
authors: Burkhardt Paul, Harris David G.
conference: "Arxiv"
year: 2023
bibkey: burkhardt2023simple
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2303.06090"}
tags: ['ARXIV', 'Graph']
---
We consider the problem of counting 4-cycles (\(C_4\)) in an undirected graph \(G\) of \(n\) vertices and \(m\) edges (in bipartite graphs, 4-cycles are also often referred to as \(\textit{butterflies}\)). Most recently, Wang et al. (2019, 2022) developed algorithms for this problem based on hash tables and sorting the graph by degree. Their algorithm takes \(O(m\bar\delta)\) expected time and \(O(m)\) space, where \(\bar \delta \leq O(\sqrt{m})\) is the $\textit\{average degeneracy\}$ parameter introduced by Burkhardt, Faber \&amp; Harris (2020). We develop a streamlined version of this algorithm requiring \(O(m\bar\delta)\) time and precisely \(n\) words of space. It has several practical improvements and optimizations; for example, it is fully deterministic, does not require any auxiliary storage or sorting of the input graph, and uses only addition and array access in its inner loops. Our algorithm is very simple and easily adapted to count 4-cycles incident to each vertex and edge. Empirical tests demonstrate that our array-based approach is \(4\times\) -- \(7\times\) faster on average compared to popular hash table implementations.

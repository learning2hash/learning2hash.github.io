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
We consider the problem of counting 4-cycles (\{&#37; raw &#37;\}\\(C\_4\\)\{&#37; endraw &#37;\}) in an undirected graph \{&#37; raw &#37;\}\\(G\\)\{&#37; endraw &#37;\} of \{&#37; raw &#37;\}\\(n\\)\{&#37; endraw &#37;\} vertices and \{&#37; raw &#37;\}\\(m\\)\{&#37; endraw &#37;\} edges (in bipartite graphs, 4-cycles are also often referred to as \{&#37; raw &#37;\}\\(\textit\{butterflies\}\\)\{&#37; endraw &#37;\}). Most recently, Wang et al. (2019, 2022) developed algorithms for this problem based on hash tables and sorting the graph by degree. Their algorithm takes \{&#37; raw &#37;\}\\(O(m\bar\delta)\\)\{&#37; endraw &#37;\} expected time and \{&#37; raw &#37;\}\\(O(m)\\)\{&#37; endraw &#37;\} space, where \{&#37; raw &#37;\}\\(\bar \delta \leq O(\sqrt\{m\})\\)\{&#37; endraw &#37;\} is the $\textit\{average degeneracy\}$ parameter introduced by Burkhardt, Faber \&amp; Harris (2020). We develop a streamlined version of this algorithm requiring \{&#37; raw &#37;\}\\(O(m\bar\delta)\\)\{&#37; endraw &#37;\} time and precisely \{&#37; raw &#37;\}\\(n\\)\{&#37; endraw &#37;\} words of space. It has several practical improvements and optimizations; for example, it is fully deterministic, does not require any auxiliary storage or sorting of the input graph, and uses only addition and array access in its inner loops. Our algorithm is very simple and easily adapted to count 4-cycles incident to each vertex and edge. Empirical tests demonstrate that our array-based approach is \{&#37; raw &#37;\}\\(4\times\\)\{&#37; endraw &#37;\} -- \{&#37; raw &#37;\}\\(7\times\\)\{&#37; endraw &#37;\} faster on average compared to popular hash table implementations.

---
layout: publication
title: Relative Nn-descent A Fast Index Construction For Graph-based Approximate Nearest Neighbor Search
authors: Ono Naoki, Matsui Yusuke
conference: "Arxiv"
year: 2023
bibkey: ono2023relative
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2310.20419"}
tags: ['ARXIV', 'Graph']
---
Approximate Nearest Neighbor Search (ANNS) is the task of finding the
database vector that is closest to a given query vector. Graph-based ANNS is
the family of methods with the best balance of accuracy and speed for
million-scale datasets. However, graph-based methods have the disadvantage of
long index construction time. Recently, many researchers have improved the
tradeoff between accuracy and speed during a search. However, there is little
research on accelerating index construction. We propose a fast graph
construction algorithm, Relative NN-Descent (RNN-Descent). RNN-Descent combines
NN-Descent, an algorithm for constructing approximate K-nearest neighbor graphs
(K-NN graphs), and RNG Strategy, an algorithm for selecting edges effective for
search. This algorithm allows the direct construction of graph-based indexes
without ANNS. Experimental results demonstrated that the proposed method had
the fastest index construction speed, while its search performance is
comparable to existing state-of-the-art methods such as NSG. For example, in
experiments on the GIST1M dataset, the construction of the proposed method is
2x faster than NSG. Additionally, it was even faster than the construction
speed of NN-Descent.

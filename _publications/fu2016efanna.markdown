---
layout: publication
title: EFANNA An Extremely Fast Approximate Nearest Neighbor Search Algorithm Based On Knn Graph
authors: Fu Cong, Cai Deng
conference: "Arxiv"
year: 2016
bibkey: fu2016efanna
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1609.07228"}
tags: ['ARXIV', 'Graph', 'Independent']
---
Approximate nearest neighbor (ANN) search is a fundamental problem in many areas of data mining, machine learning and computer vision. The performance of traditional hierarchical structure (tree) based methods decreases as the dimensionality of data grows, while hashing based methods usually lack efficiency in practice. Recently, the graph based methods have drawn considerable attention. The main idea is that \emph&amp;\#123;a neighbor of a neighbor is also likely to be a neighbor&amp;\#125;, which we refer as \emph&amp;\#123;NN-expansion&amp;\#125;. These methods construct a \(k\)-nearest neighbor (\(k\)NN) graph offline. And at online search stage, these methods find candidate neighbors of a query point in some way (\eg, random selection), and then check the neighbors of these candidate neighbors for closer ones iteratively. Despite some promising results, there are mainly two problems with these approaches: 1) These approaches tend to converge to local optima. 2) Constructing a \(k\)NN graph is time consuming. We find that these two problems can be nicely solved when we provide a good initialization for NN-expansion. In this paper, we propose EFANNA, an extremely fast approximate nearest neighbor search algorithm based on \(k\)NN Graph. Efanna nicely combines the advantages of hierarchical structure based methods and nearest-neighbor-graph based methods. Extensive experiments have shown that EFANNA outperforms the state-of-art algorithms both on approximate nearest neighbor search and approximate nearest neighbor graph construction. To the best of our knowledge, EFANNA is the fastest algorithm so far both on approximate nearest neighbor graph construction and approximate nearest neighbor search. A library EFANNA based on this research is released on Github.

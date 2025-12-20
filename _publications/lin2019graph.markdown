---
layout: publication
title: 'Graph Based Nearest Neighbor Search: Promises And Failures'
authors: Peng-Cheng Lin, Wan-Lei Zhao
conference: Arxiv
year: 2019
bibkey: lin2019graph
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.02077'}]
tags: ["Efficiency", "Evaluation", "Graph Based ANN", "Scalability"]
short_authors: Peng-Cheng Lin, Wan-Lei Zhao
---
Recently, graph based nearest neighbor search gets more and more popular on
large-scale retrieval tasks. The attractiveness of this type of approaches lies
in its superior performance over most of the known nearest neighbor search
approaches as well as its genericness to various metrics. In this paper, the
role of two strategies, namely hierarchical structure and graph diversification
that are adopted as the key steps in the graph based approaches, is
investigated. We find the hierarchical structure could not achieve "much better
logarithmic complexity scaling" as it was claimed in the original paper,
particularly on high dimensional cases. Moreover, we find that similar high
search speed efficiency as the one with hierarchical structure could be
achieved with the support of flat k-NN graph after graph diversification.
Finally, we point out the difficulty, that is faced by most of the graph based
search approaches, is directly linked to "curse of dimensionality".
---
layout: publication
title: Proximity Graph Maintenance For Fast Online Nearest Neighbor Search
authors: Zhaozhuo Xu, Weijie Zhao, Shulong Tan, Zhixin Zhou, Ping Li
conference: Arxiv
year: 2022
bibkey: xu2022proximity
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.10839'}]
tags: ["Graph Based ANN", "Quantization", "Recommender Systems", "Similarity Search", "Tree Based ANN"]
short_authors: Xu et al.
---
Approximate Nearest Neighbor (ANN) search is a fundamental technique for
(e.g.,) the deployment of recommender systems. Recent studies bring proximity
graph-based methods into practitioners' attention -- proximity graph-based
methods outperform other solutions such as quantization, hashing, and
tree-based ANN algorithm families. In current recommendation systems, data
point insertions, deletions, and queries are streamed into the system in an
online fashion as users and items change dynamically. As proximity graphs are
constructed incrementally by inserting data points as new vertices into the
graph, online insertions and queries are well-supported in proximity graph.
However, a data point deletion incurs removing a vertex from the proximity
graph index, while no proper graph index updating mechanisms are discussed in
previous studies. To tackle the challenge, we propose an incremental proximity
graph maintenance (IPGM) algorithm for online ANN. IPGM supports both vertex
deletion and insertion on proximity graphs. Given a vertex deletion request, we
thoroughly investigate solutions to update the connections of the vertex. The
proposed updating scheme eliminates the performance drop in online ANN methods
on proximity graphs, making the algorithm suitable for practical systems.
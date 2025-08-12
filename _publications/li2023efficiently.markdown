---
layout: publication
title: Efficiently Visualizing Large Graphs
authors: Xinyu Li, Yao Xiao, Yuchen Zhou
conference: Arxiv
year: 2023
bibkey: li2023efficiently
citations: 0
additional_links: [{name: Code, url: 'https://github.com/Charlie-XIAO/embedding-visualization-test'},
  {name: Paper, url: 'https://arxiv.org/abs/2310.11186'}]
tags: ["Scalability"]
short_authors: Xinyu Li, Yao Xiao, Yuchen Zhou
---
Most existing graph visualization methods based on dimension reduction are
limited to relatively small graphs due to performance issues. In this work, we
propose a novel dimension reduction method for graph visualization, called
t-Distributed Stochastic Graph Neighbor Embedding (t-SGNE). t-SGNE is
specifically designed to visualize cluster structures in the graph. As a
variant of the standard t-SNE method, t-SGNE avoids the time-consuming
computations of pairwise similarity. Instead, it uses the neighbor structures
of the graph to reduce the time complexity from quadratic to linear, thus
supporting larger graphs. In addition, to suit t-SGNE, we combined Laplacian
Eigenmaps with the shortest path algorithm in graphs to form the graph
embedding algorithm ShortestPath Laplacian Eigenmaps Embedding (SPLEE).
Performing SPLEE to obtain a high-dimensional embedding of the large-scale
graph and then using t-SGNE to reduce its dimension for visualization, we are
able to visualize graphs with up to 300K nodes and 1M edges within 5 minutes
and achieve approximately 10% improvement in visualization quality. Codes and
data are available at
https://github.com/Charlie-XIAO/embedding-visualization-test.
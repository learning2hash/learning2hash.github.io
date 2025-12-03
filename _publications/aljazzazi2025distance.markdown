---
layout: publication
title: Distance Adaptive Beam Search For Provably Accurate Graph-based Nearest Neighbor
  Search
authors: Yousef Al-Jazzazi, Haya Diwan, Jinrui Gou, Cameron Musco, Christopher Musco,
  Torsten Suel
conference: Arxiv
year: 2025
bibkey: aljazzazi2025distance
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2505.15636'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Graph Based ANN"]
short_authors: Al-Jazzazi et al.
---
Nearest neighbor search is central in machine learning, information retrieval, and databases. For high-dimensional datasets, graph-based methods such as HNSW, DiskANN, and NSG have become popular thanks to their empirical accuracy and efficiency. These methods construct a directed graph over the dataset and perform beam search on the graph to find nodes close to a given query. While significant work has focused on practical refinements and theoretical understanding of graph-based methods, many questions remain. We propose a new distance-based termination condition for beam search to replace the commonly used condition based on beam width. We prove that, as long as the search graph is navigable, our resulting Adaptive Beam Search method is guaranteed to approximately solve the nearest-neighbor problem, establishing a connection between navigability and the performance of graph-based search. We also provide extensive experiments on our new termination condition for both navigable graphs and approximately navigable graphs used in practice, such as HNSW and Vamana graphs. We find that Adaptive Beam Search outperforms standard beam search over a range of recall values, data sets, graph constructions, and target number of nearest neighbors. It thus provides a simple and practical way to improve the performance of popular methods.
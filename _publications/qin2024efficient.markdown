---
layout: publication
title: "Efficient Graph Encoder Embedding for Large Sparse Graphs in Python"
authors: Qin Xihan, Shen Cencheng
conference: Arxiv
year: 2024
bibkey: qin2024efficient
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2406.03726"}
tags: ['ARXIV', 'Graph']
---
Graph is a ubiquitous representation of data in various research fields, and graph embedding is a prevalent machine learning technique for capturing key features and generating fixed-sized attributes. However, most state-of-the-art graph embedding methods are computationally and spatially expensive. Recently, the Graph Encoder Embedding (GEE) has been shown as the fastest graph embedding technique and is suitable for a variety of network data applications. As real-world data often involves large and sparse graphs, the huge sparsity usually results in redundant computations and storage. To address this issue, we propose an improved version of GEE, sparse GEE, which optimizes the calculation and storage of zero entries in sparse matrices to enhance the running time further. Our experiments demonstrate that the sparse version achieves significant speedup compared to the original GEE with Python implementation for large sparse graphs, and sparse GEE is capable of processing millions of edges within minutes on a standard laptop.
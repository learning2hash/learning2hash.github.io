---
layout: publication
title: 'LANNS: A Web-scale Approximate Nearest Neighbor Lookup System'
authors: Ishita Doshi et al.
conference: "Arxiv"
year: 2020
citations: 0
bibkey: doshi2020web
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2010.09426'}
tags: ['Tools and Libraries', 'ANN Search', 'Applications', 'Approximate Nearest Neighbor Search']
---
Nearest neighbor search (NNS) has a wide range of applications in information
retrieval, computer vision, machine learning, databases, and other areas.
Existing state-of-the-art algorithm for nearest neighbor search, Hierarchical
Navigable Small World Networks(HNSW), is unable to scale to large datasets of
100M records in high dimensions. In this paper, we propose LANNS, an end-to-end
platform for Approximate Nearest Neighbor Search, which scales for web-scale
datasets. Library for Large Scale Approximate Nearest Neighbor Search (LANNS)
is deployed in multiple production systems for identifying topK (\\(100 \leq topK
\leq 200\\)) approximate nearest neighbors with a latency of a few milliseconds
per query, high throughput of 2.5k Queries Per Second (QPS) on a single node,
on large (\\(\sim\\)180M data points) high dimensional (50-2048 dimensional)
datasets.

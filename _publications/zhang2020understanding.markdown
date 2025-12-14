---
layout: publication
title: 'Understanding Image Retrieval Re-ranking: A Graph Neural Network Perspective'
authors: Xuanmeng Zhang, Minyue Jiang, Zhedong Zheng, Xiao Tan, Errui Ding, Yi Yang
conference: Arxiv
year: 2020
bibkey: zhang2020understanding
citations: 25
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.07620'}]
tags: [Evaluation, Image Retrieval, Re-ranking, Efficiency, Datasets, Hybrid ANN Methods]
short_authors: Zhang et al.
---
The re-ranking approach leverages high-confidence retrieved samples to refine
retrieval results, which have been widely adopted as a post-processing tool for
image retrieval tasks. However, we notice one main flaw of re-ranking, i.e.,
high computational complexity, which leads to an unaffordable time cost for
real-world applications. In this paper, we revisit re-ranking and demonstrate
that re-ranking can be reformulated as a high-parallelism Graph Neural Network
(GNN) function. In particular, we divide the conventional re-ranking process
into two phases, i.e., retrieving high-quality gallery samples and updating
features. We argue that the first phase equals building the k-nearest neighbor
graph, while the second phase can be viewed as spreading the message within the
graph. In practice, GNN only needs to concern vertices with the connected
edges. Since the graph is sparse, we can efficiently update the vertex
features. On the Market-1501 dataset, we accelerate the re-ranking processing
from 89.2s to 9.4ms with one K40m GPU, facilitating the real-time
post-processing. Similarly, we observe that our method achieves comparable or
even better retrieval results on the other four image retrieval benchmarks,
i.e., VeRi-776, Oxford-5k, Paris-6k and University-1652, with limited time
cost. Our code is publicly available.
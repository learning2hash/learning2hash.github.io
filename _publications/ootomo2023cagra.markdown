---
layout: publication
title: 'CAGRA: Highly Parallel Graph Construction And Approximate Nearest Neighbor
  Search For Gpus'
authors: Hiroyuki Ootomo, Akira Naruse, Corey Nolet, Ray Wang, Tamas Feher, Yong Wang
conference: 2024 IEEE 40th International Conference on Data Engineering (ICDE)
year: 2024
bibkey: ootomo2023cagra
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.15136'}]
tags: ["Efficiency", "Evaluation", "Recommender Systems"]
short_authors: Ootomo et al.
---
Approximate Nearest Neighbor Search (ANNS) plays a critical role in various
disciplines spanning data mining and artificial intelligence, from information
retrieval and computer vision to natural language processing and recommender
systems. Data volumes have soared in recent years and the computational cost of
an exhaustive exact nearest neighbor search is often prohibitive, necessitating
the adoption of approximate techniques. The balanced performance and recall of
graph-based approaches have more recently garnered significant attention in
ANNS algorithms, however, only a few studies have explored harnessing the power
of GPUs and multi-core processors despite the widespread use of massively
parallel and general-purpose computing. To bridge this gap, we introduce a
novel parallel computing hardware-based proximity graph and search algorithm.
By leveraging the high-performance capabilities of modern hardware, our
approach achieves remarkable efficiency gains. In particular, our method
surpasses existing CPU and GPU-based methods in constructing the proximity
graph, demonstrating higher throughput in both large- and small-batch searches
while maintaining compatible accuracy. In graph construction time, our method,
CAGRA, is 2.2~27x faster than HNSW, which is one of the CPU SOTA
implementations. In large-batch query throughput in the 90% to 95% recall
range, our method is 33~77x faster than HNSW, and is 3.8~8.8x faster than the
SOTA implementations for GPU. For a single query, our method is 3.4~53x faster
than HNSW at 95% recall.
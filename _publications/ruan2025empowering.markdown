---
layout: publication
title: Empowering Graph-based Approximate Nearest Neighbor Search With Adaptive Awareness
  Capabilities
authors: Jiancheng Ruan, Tingyang Chen, Renchi Yang, Xiangyu Ke, Yunjun Gao
conference: Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and
  Data Mining V.2
year: 2025
bibkey: ruan2025empowering
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2506.15986'}]
tags: [Evaluation, Self-Supervised, Graph-based ANN, KDD, Recommender Systems]
short_authors: Ruan et al.
---
Approximate Nearest Neighbor Search (ANNS) in high-dimensional spaces finds extensive applications in databases, information retrieval, recommender systems, etc. While graph-based methods have emerged as the leading solution for ANNS due to their superior query performance, they still face several challenges, such as struggling with local optima and redundant computations. These issues arise because existing methods (i) fail to fully exploit the topological information underlying the proximity graph G, and (ii) suffer from severe distribution mismatches between the base data and queries in practice.
  To this end, this paper proposes GATE, high-tier proximity Graph with Adaptive Topology and Query AwarEness, as a lightweight and adaptive module atop the graph-based indexes to accelerate ANNS. Specifically, GATE formulates the critical problem to identify an optimal entry point in the proximity graph for a given query, facilitating faster online search. By leveraging the inherent clusterability of high-dimensional data, GATE first extracts a small set of hub nodes V as candidate entry points. Then, resorting to a contrastive learning-based two-tower model, GATE encodes both the structural semantics underlying G and the query-relevant features into the latent representations of these hub nodes V. A navigation graph index on V is further constructed to minimize the model inference overhead. Extensive experiments demonstrate that GATE achieves a 1.2-2.0X speed-up in query performance compared to state-of-the-art graph-based indexes.
---
layout: publication
title: Scalable Overload-aware Graph-based Index Construction For 10-billion-scale
  Vector Similarity Search
authors: Yang Shi, Yiping Sun, Jiaolong Du, Xiaocheng Zhong, Zhiyong Wang, Yao Hu
conference: Companion Proceedings of the ACM on Web Conference 2025
year: 2025
bibkey: shi2025scalable
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.20695'}]
tags: ["Datasets", "Evaluation", "Graph Based ANN", "Large Scale Search", "Scalability", "Similarity Search", "Tools & Libraries"]
short_authors: Shi et al.
---
Approximate Nearest Neighbor Search (ANNS) is essential for modern
data-driven applications that require efficient retrieval of top-k results from
massive vector databases. Although existing graph-based ANNS algorithms achieve
a high recall rate on billion-scale datasets, their slow construction speed and
limited scalability hinder their applicability to large-scale industrial
scenarios. In this paper, we introduce SOGAIC, the first Scalable
Overload-Aware Graph-Based ANNS Index Construction system tailored for
ultra-large-scale vector databases: 1) We propose a dynamic data partitioning
algorithm with overload constraints that adaptively introduces overlaps among
subsets; 2) To enable efficient distributed subgraph construction, we employ a
load-balancing task scheduling framework combined with an agglomerative merging
strategy; 3) Extensive experiments on various datasets demonstrate a reduction
of 47.3% in average construction time compared to existing methods. The
proposed method has also been successfully deployed in a real-world industrial
search engine, managing over 10 billion daily updated vectors and serving
hundreds of millions of users.
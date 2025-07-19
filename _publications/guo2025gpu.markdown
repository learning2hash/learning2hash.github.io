---
layout: publication
title: GPU-accelerated Multi-relational Parallel Graph Retrieval for Web-scale Recommendations
authors: Guo et al.
conference: Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and
  Data Mining
year: 2025
bibkey: guo2025gpu
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.11490'}]
tags: [SCALABILITY, KDD, Large Scale Search, Recommender Systems]
---
Web recommendations provide personalized items from massive catalogs for
users, which rely heavily on retrieval stages to trade off the effectiveness
and efficiency of selecting a small relevant set from billion-scale candidates
in online digital platforms. As one of the largest Chinese search engine and
news feed providers, Baidu resorts to Deep Neural Network (DNN) and graph-based
Approximate Nearest Neighbor Search (ANNS) algorithms for accurate relevance
estimation and efficient search for relevant items. However, current retrieval
at Baidu fails in comprehensive user-item relational understanding due to
dissected interaction modeling, and performs inefficiently in large-scale
graph-based ANNS because of suboptimal traversal navigation and the GPU
computational bottleneck under high concurrency. To this end, we propose a
GPU-accelerated Multi-relational Parallel Graph Retrieval (GMP-GR) framework to
achieve effective yet efficient retrieval in web-scale recommendations. First,
we propose a multi-relational user-item relevance metric learning method that
unifies diverse user behaviors through multi-objective optimization and employs
a self-covariant loss to enhance pathfinding performance. Second, we develop a
hierarchical parallel graph-based ANNS to boost graph retrieval throughput,
which conducts breadth-depth-balanced searches on a large-scale item graph and
cost-effectively handles irregular neural computation via adaptive aggregation
on GPUs. In addition, we integrate system optimization strategies in the
deployment of GMP-GR in Baidu. Extensive experiments demonstrate the
superiority of GMP-GR in retrieval accuracy and efficiency. Deployed across
more than twenty applications at Baidu, GMP-GR serves hundreds of millions of
users with a throughput exceeding one hundred million requests per second.
---
layout: publication
title: Constructing Tree-based Index for Efficient and Effective Dense Retrieval
authors: Li et al.
conference: Proceedings of the 46th International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2023
bibkey: li2023constructing
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.11943'}]
tags: ["SIGIR"]
---
Recent studies have shown that Dense Retrieval (DR) techniques can
significantly improve the performance of first-stage retrieval in IR systems.
Despite its empirical effectiveness, the application of DR is still limited. In
contrast to statistic retrieval models that rely on highly efficient inverted
index solutions, DR models build dense embeddings that are difficult to be
pre-processed with most existing search indexing systems. To avoid the
expensive cost of brute-force search, the Approximate Nearest Neighbor (ANN)
algorithm and corresponding indexes are widely applied to speed up the
inference process of DR models. Unfortunately, while ANN can improve the
efficiency of DR models, it usually comes with a significant price on retrieval
performance.
  To solve this issue, we propose JTR, which stands for Joint optimization of
TRee-based index and query encoding. Specifically, we design a new unified
contrastive learning loss to train tree-based index and query encoder in an
end-to-end manner. The tree-based negative sampling strategy is applied to make
the tree have the maximum heap property, which supports the effectiveness of
beam search well. Moreover, we treat the cluster assignment as an optimization
problem to update the tree-based index that allows overlapped clustering. We
evaluate JTR on numerous popular retrieval benchmarks. Experimental results
show that JTR achieves better retrieval performance while retaining high system
efficiency compared with widely-adopted baselines. It provides a potential
solution to balance efficiency and effectiveness in neural retrieval system
designs.
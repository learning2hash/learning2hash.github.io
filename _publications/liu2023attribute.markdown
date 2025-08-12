---
layout: publication
title: Attribute Simulation For Item Embedding Enhancement In Multi-interest Recommendation
authors: Yaokun Liu, Xiaowang Zhang, Minghui Zou, Zhiyong Feng
conference: Proceedings of the 17th ACM International Conference on Web Search and
  Data Mining
year: 2024
bibkey: liu2023attribute
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.17374'}]
tags: ["Recommender Systems"]
short_authors: Liu et al.
---
Although multi-interest recommenders have achieved significant progress in
the matching stage, our research reveals that existing models tend to exhibit
an under-clustered item embedding space, which leads to a low discernibility
between items and hampers item retrieval. This highlights the necessity for
item embedding enhancement. However, item attributes, which serve as effective
and straightforward side information for enhancement, are either unavailable or
incomplete in many public datasets due to the labor-intensive nature of manual
annotation tasks. This dilemma raises two meaningful questions: 1. Can we
bypass manual annotation and directly simulate complete attribute information
from the interaction data? And 2. If feasible, how to simulate attributes with
high accuracy and low complexity in the matching stage?
  In this paper, we first establish an inspiring theoretical feasibility that
the item-attribute correlation matrix can be approximated through elementary
transformations on the item co-occurrence matrix. Then based on formula
derivation, we propose a simple yet effective module, SimEmb (Item Embedding
Enhancement via Simulated Attribute), in the multi-interest recommendation of
the matching stage to implement our findings. By simulating attributes with the
co-occurrence matrix, SimEmb discards the item ID-based embedding and employs
the attribute-weighted summation for item embedding enhancement. Comprehensive
experiments on four benchmark datasets demonstrate that our approach notably
enhances the clustering of item embedding and significantly outperforms SOTA
models with an average improvement of 25.59% on Recall@20.
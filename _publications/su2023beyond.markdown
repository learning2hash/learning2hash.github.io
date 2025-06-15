---
layout: publication
title: 'Beyond Two-tower Matching: Learning Sparse Retrievable Cross-interactions For Recommendation'
authors: Liangcai Su et al.
conference: "Arxiv"
year: 2023
citations: 1
bibkey: su2023beyond
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2311.18213'}
tags: ['Applications', 'Evaluation Metrics', 'Indexing', 'Tools and Libraries', 'ANN Search', 'Benchmarks and Datasets']
---
Two-tower models are a prevalent matching framework for recommendation, which
have been widely deployed in industrial applications. The success of two-tower
matching attributes to its efficiency in retrieval among a large number of
items, since the item tower can be precomputed and used for fast Approximate
Nearest Neighbor (ANN) search. However, it suffers two main challenges,
including limited feature interaction capability and reduced accuracy in online
serving. Existing approaches attempt to design novel late interactions instead
of dot products, but they still fail to support complex feature interactions or
lose retrieval efficiency. To address these challenges, we propose a new
matching paradigm named SparCode, which supports not only sophisticated feature
interactions but also efficient retrieval. Specifically, SparCode introduces an
all-to-all interaction module to model fine-grained query-item interactions.
Besides, we design a discrete code-based sparse inverted index jointly trained
with the model to achieve effective and efficient model inference. Extensive
experiments have been conducted on open benchmark datasets to demonstrate the
superiority of our framework. The results show that SparCode significantly
improves the accuracy of candidate item matching while retaining the same level
of retrieval efficiency with two-tower models. Our source code will be
available at MindSpore/models.

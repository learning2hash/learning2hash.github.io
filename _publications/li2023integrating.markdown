---
layout: publication
title: Integrating Listwise Ranking Into Pairwise-based Image-text Retrieval
authors: Zheng Li, Caili Guo, Xin Wang, Zerun Feng, Yanjun Wang
conference: Arxiv
year: 2023
bibkey: li2023integrating
citations: 1
additional_links: [{name: Code, url: 'https://github.com/AAA-Zheng/Listwise_ITR'},
  {name: Paper, url: 'https://arxiv.org/abs/2305.16566'}]
tags: ["Evaluation", "Image Retrieval", "Re-Ranking", "Text Retrieval"]
short_authors: Li et al.
---
Image-Text Retrieval (ITR) is essentially a ranking problem. Given a query
caption, the goal is to rank candidate images by relevance, from large to
small. The current ITR datasets are constructed in a pairwise manner.
Image-text pairs are annotated as positive or negative. Correspondingly, ITR
models mainly use pairwise losses, such as triplet loss, to learn to rank.
Pairwise-based ITR increases positive pair similarity while decreasing negative
pair similarity indiscriminately. However, the relevance between dissimilar
negative pairs is different. Pairwise annotations cannot reflect this
difference in relevance. In the current datasets, pairwise annotations miss
many correlations. There are many potential positive pairs among the pairs
labeled as negative. Pairwise-based ITR can only rank positive samples before
negative samples, but cannot rank negative samples by relevance. In this paper,
we integrate listwise ranking into conventional pairwise-based ITR. Listwise
ranking optimizes the entire ranking list based on relevance scores.
Specifically, we first propose a Relevance Score Calculation (RSC) module to
calculate the relevance score of the entire ranked list. Then we choose the
ranking metric, Normalized Discounted Cumulative Gain (NDCG), as the
optimization objective. We transform the non-differentiable NDCG into a
differentiable listwise loss, named Smooth-NDCG (S-NDCG). Our listwise ranking
approach can be plug-and-play integrated into current pairwise-based ITR
models. Experiments on ITR benchmarks show that integrating listwise ranking
can improve the performance of current ITR models and provide more
user-friendly retrieval results. The code is available at
https://github.com/AAA-Zheng/Listwise_ITR.
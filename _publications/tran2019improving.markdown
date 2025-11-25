---
layout: publication
title: Improving Collaborative Metric Learning With Efficient Negative Sampling
authors: Viet-Anh Tran, Romain Hennequin, Jimena Royo-Letelier, Manuel Moussallam
conference: Proceedings of the 42nd International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2019
bibkey: tran2019improving
citations: 21
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.10912'}]
tags: ["Distance Metric Learning", "Image Retrieval", "Recommender Systems", "SIGIR"]
short_authors: Tran et al.
---
Distance metric learning based on triplet loss has been applied with success
in a wide range of applications such as face recognition, image retrieval,
speaker change detection and recently recommendation with the CML model.
However, as we show in this article, CML requires large batches to work
reasonably well because of a too simplistic uniform negative sampling strategy
for selecting triplets. Due to memory limitations, this makes it difficult to
scale in high-dimensional scenarios. To alleviate this problem, we propose here
a 2-stage negative sampling strategy which finds triplets that are highly
informative for learning. Our strategy allows CML to work effectively in terms
of accuracy and popularity bias, even when the batch size is an order of
magnitude smaller than what would be needed with the default uniform sampling.
We demonstrate the suitability of the proposed strategy for recommendation and
exhibit consistent positive results across various datasets.
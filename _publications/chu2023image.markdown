---
layout: publication
title: Image Clustering Via The Principle Of Rate Reduction In The Age Of Pretrained
  Models
authors: "Tianzhe Chu, Shengbang Tong, Tianjiao Ding, Xili Dai, Benjamin David Haeffele,\
  \ Ren\xE9 Vidal, Yi Ma"
conference: Arxiv
year: 2023
bibkey: chu2023image
citations: 0
additional_links: [{name: Code, url: 'https://github.com/LeslieTrue/CPP'}, {name: Paper,
    url: 'https://arxiv.org/abs/2306.05272'}]
tags: []
short_authors: Chu et al.
---
The advent of large pre-trained models has brought about a paradigm shift in
both visual representation learning and natural language processing. However,
clustering unlabeled images, as a fundamental and classic machine learning
problem, still lacks an effective solution, particularly for large-scale
datasets. In this paper, we propose a novel image clustering pipeline that
leverages the powerful feature representation of large pre-trained models such
as CLIP and cluster images effectively and efficiently at scale. We first
developed a novel algorithm to estimate the number of clusters in a given
dataset. We then show that the pre-trained features are significantly more
structured by further optimizing the rate reduction objective. The resulting
features may significantly improve the clustering accuracy, e.g., from 57% to
66% on ImageNet-1k. Furthermore, by leveraging CLIP's multimodality bridge
between image and text, we develop a simple yet effective self-labeling
algorithm that produces meaningful captions for the clusters. Through extensive
experiments, we show that our pipeline works well on standard datasets such as
CIFAR-10, CIFAR-100, and ImageNet-1k. It also extends to datasets that are not
curated for clustering, such as LAION-Aesthetics and WikiArts. We released the
code in https://github.com/LeslieTrue/CPP.
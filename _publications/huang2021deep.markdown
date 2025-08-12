---
layout: publication
title: Deep Clustering By Semantic Contrastive Learning
authors: Jiabo Huang, Shaogang Gong
conference: Arxiv
year: 2021
bibkey: huang2021deep
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.02662'}]
tags: ["Self-Supervised", "Unsupervised"]
short_authors: Jiabo Huang, Shaogang Gong
---
Whilst contrastive learning has recently brought notable benefits to deep
clustering of unlabelled images by learning sample-specific discriminative
visual features, its potential for explicitly inferring class decision
boundaries is less well understood. This is because its instance discrimination
strategy is not class sensitive, therefore, the clusters derived on the
resulting sample-specific feature space are not optimised for corresponding to
meaningful class decision boundaries. In this work, we solve this problem by
introducing Semantic Contrastive Learning (SCL). SCL imposes explicitly
distance-based cluster structures on unlabelled training data by formulating a
semantic (cluster-aware) contrastive learning objective. Moreover, we introduce
a clustering consistency condition to be satisfied jointly by both instance
visual similarities and cluster decision boundaries, and concurrently
optimising both to reason about the hypotheses of semantic ground-truth classes
(unknown/unlabelled) on-the-fly by their consensus. This semantic contrastive
learning approach to discovering unknown class decision boundaries has
considerable advantages to unsupervised learning of object recognition tasks.
Extensive experiments show that SCL outperforms state-of-the-art contrastive
learning and deep clustering methods on six object recognition benchmarks,
especially on the more challenging finer-grained and larger datasets.
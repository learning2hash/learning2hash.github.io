---
layout: publication
title: Bag Of Image Patch Embedding Behind The Success Of Self-supervised Learning
authors: Yubei Chen, Adrien Bardes, Zengyi Li, Yann Lecun
conference: Arxiv
year: 2022
bibkey: chen2022bag
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.08954'}]
tags: ["Self-Supervised"]
short_authors: Chen et al.
---
Self-supervised learning (SSL) has recently achieved tremendous empirical
advancements in learning image representation. However, our understanding of
the principle behind learning such a representation is still limited. This work
shows that joint-embedding SSL approaches primarily learn a representation of
image patches, which reflects their co-occurrence. Such a connection to
co-occurrence modeling can be established formally, and it supplements the
prevailing invariance perspective. We empirically show that learning a
representation for fixed-scale patches and aggregating local patch
representations as the image representation achieves similar or even better
results than the baseline methods. We denote this process as BagSSL. Even with
32x32 patch representation, BagSSL achieves 62% top-1 linear probing accuracy
on ImageNet. On the other hand, with a multi-scale pretrained model, we show
that the whole image embedding is approximately the average of local patch
embeddings. While the SSL representation is relatively invariant at the global
scale, we show that locality is preserved when we zoom into local patch-level
representation. Further, we show that patch representation aggregation can
improve various SOTA baseline methods by a large margin. The patch
representation is considerably easier to understand, and this work makes a step
to demystify self-supervised representation learning.
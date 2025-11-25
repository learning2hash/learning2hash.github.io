---
layout: publication
title: Self-supervised Representation Learning With Multi-segmental Informational
  Coding (MUSIC)
authors: Chuang Niu, Ge Wang
conference: Arxiv
year: 2022
bibkey: niu2022self
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.06461'}]
tags: ["Distance Metric Learning", "Self-Supervised"]
short_authors: Chuang Niu, Ge Wang
---
Self-supervised representation learning maps high-dimensional data into a
meaningful embedding space, where samples of similar semantic contents are
close to each other. Most of the recent representation learning methods
maximize cosine similarity or minimize the distance between the embedding
features of different views from the same sample usually on the \(l2\) normalized
unit hypersphere. To prevent the trivial solutions that all samples have the
same embedding feature, various techniques have been developed, such as
contrastive learning, stop gradient, variance and covariance regularization,
etc. In this study, we propose MUlti-Segmental Informational Coding (MUSIC) for
self-supervised representation learning. MUSIC divides the embedding feature
into multiple segments that discriminatively partition samples into different
semantic clusters and different segments focus on different partition
principles. Information theory measurements are directly used to optimize MUSIC
and theoretically guarantee trivial solutions are avoided. MUSIC does not
depend on commonly used techniques, such as memory bank or large batches,
asymmetry networks, gradient stopping, momentum weight updating, etc, making
the training framework flexible. Our experiments demonstrate that MUSIC
achieves better results than most related Barlow Twins and VICReg methods on
ImageNet classification with linear probing, and requires neither deep
projectors nor large feature dimensions. Code will be made available.
---
layout: publication
title: Digging Into Self-supervised Learning Of Feature Descriptors
authors: Iaroslav Melekhov, Zakaria Laskar, Xiaotian Li, Shuzhe Wang, Juho Kannala
conference: 2021 International Conference on 3D Vision (3DV)
year: 2021
bibkey: melekhov2021digging
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.04773'}]
tags: ["Image Retrieval", "Self-Supervised", "Supervised"]
short_authors: Melekhov et al.
---
Fully-supervised CNN-based approaches for learning local image descriptors
have shown remarkable results in a wide range of geometric tasks. However, most
of them require per-pixel ground-truth keypoint correspondence data which is
difficult to acquire at scale. To address this challenge, recent weakly- and
self-supervised methods can learn feature descriptors from relative camera
poses or using only synthetic rigid transformations such as homographies. In
this work, we focus on understanding the limitations of existing
self-supervised approaches and propose a set of improvements that combined lead
to powerful feature descriptors. We show that increasing the search space from
in-pair to in-batch for hard negative mining brings consistent improvement. To
enhance the discriminativeness of feature descriptors, we propose a
coarse-to-fine method for mining local hard negatives from a wider search space
by using global visual image descriptors. We demonstrate that a combination of
synthetic homography transformation, color augmentation, and photorealistic
image stylization produces useful representations that are viewpoint and
illumination invariant. The feature descriptors learned by the proposed
approach perform competitively and surpass their fully- and weakly-supervised
counterparts on various geometric benchmarks such as image-based localization,
sparse feature matching, and image retrieval.
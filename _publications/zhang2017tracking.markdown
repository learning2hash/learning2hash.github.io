---
layout: publication
title: Tracking Persons-of-interest Via Unsupervised Representation Adaptation
authors: Shun Zhang, Jia-bin Huang, Jongwoo Lim, Yihong Gong, Jinjun Wang, Narendra
  Ahuja, Ming-hsuan Yang
conference: International Journal of Computer Vision
year: 2019
bibkey: zhang2017tracking
citations: 29
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1710.02139'}]
tags: ["Unsupervised"]
short_authors: Zhang et al.
---
Multi-face tracking in unconstrained videos is a challenging problem as faces
of one person often appear drastically different in multiple shots due to
significant variations in scale, pose, expression, illumination, and make-up.
Existing multi-target tracking methods often use low-level features which are
not sufficiently discriminative for identifying faces with such large
appearance variations. In this paper, we tackle this problem by learning
discriminative, video-specific face representations using convolutional neural
networks (CNNs). Unlike existing CNN-based approaches which are only trained on
large-scale face image datasets offline, we use the contextual constraints to
generate a large number of training samples for a given video, and further
adapt the pre-trained face CNN to specific videos using discovered training
samples. Using these training samples, we optimize the embedding space so that
the Euclidean distances correspond to a measure of semantic face similarity via
minimizing a triplet loss function. With the learned discriminative features,
we apply the hierarchical clustering algorithm to link tracklets across
multiple shots to generate trajectories. We extensively evaluate the proposed
algorithm on two sets of TV sitcoms and YouTube music videos, analyze the
contribution of each component, and demonstrate significant performance
improvement over existing techniques.
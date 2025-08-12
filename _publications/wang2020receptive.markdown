---
layout: publication
title: Receptive Multi-granularity Representation For Person Re-identification
authors: Guanshuo Wang, Yufeng Yuan, Jiwei Li, Shiming Ge, Xi Zhou
conference: IEEE Transactions on Image Processing
year: 2020
bibkey: wang2020receptive
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.13450'}]
tags: []
short_authors: Wang et al.
---
A key for person re-identification is achieving consistent local details for
discriminative representation across variable environments. Current
stripe-based feature learning approaches have delivered impressive accuracy,
but do not make a proper trade-off between diversity, locality, and robustness,
which easily suffers from part semantic inconsistency for the conflict between
rigid partition and misalignment. This paper proposes a receptive
multi-granularity learning approach to facilitate stripe-based feature
learning. This approach performs local partition on the intermediate
representations to operate receptive region ranges, rather than current
approaches on input images or output features, thus can enhance the
representation of locality while remaining proper local association. Toward
this end, the local partitions are adaptively pooled by using
significance-balanced activations for uniform stripes. Random shifting
augmentation is further introduced for a higher variance of person appearing
regions within bounding boxes to ease misalignment. By two-branch network
architecture, different scales of discriminative identity representation can be
learned. In this way, our model can provide a more comprehensive and efficient
feature representation without larger model storage costs. Extensive
experiments on intra-dataset and cross-dataset evaluations demonstrate the
effectiveness of the proposed approach. Especially, our approach achieves a
state-of-the-art accuracy of 96.2%@Rank-1 or 90.0%@mAP on the challenging
Market-1501 benchmark.
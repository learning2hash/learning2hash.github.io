---
layout: publication
title: Locality-aware Inter-and Intra-video Reconstruction For Self-supervised Correspondence
  Learning
authors: Liulei Li, Tianfei Zhou, Wenguan Wang, Lu Yang, Jianwu Li, Yi Yang
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: li2022locality
citations: 36
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.14333'}]
tags: ["CVPR", "Self-Supervised"]
short_authors: Li et al.
---
Our target is to learn visual correspondence from unlabeled videos. We
develop LIIR, a locality-aware inter-and intra-video reconstruction framework
that fills in three missing pieces, i.e., instance discrimination, location
awareness, and spatial compactness, of self-supervised correspondence learning
puzzle. First, instead of most existing efforts focusing on intra-video
self-supervision only, we exploit cross video affinities as extra negative
samples within a unified, inter-and intra-video reconstruction scheme. This
enables instance discriminative representation learning by contrasting desired
intra-video pixel association against negative inter-video correspondence.
Second, we merge position information into correspondence matching, and design
a position shifting strategy to remove the side-effect of position encoding
during inter-video affinity computation, making our LIIR location-sensitive.
Third, to make full use of the spatial continuity nature of video data, we
impose a compactness-based constraint on correspondence matching, yielding more
sparse and reliable solutions. The learned representation surpasses
self-supervised state-of-the-arts on label propagation tasks including objects,
semantic parts, and keypoints.
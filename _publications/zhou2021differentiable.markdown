---
layout: publication
title: Differentiable Multi-granularity Human Representation Learning For Instance-aware
  Human Semantic Parsing
authors: Tianfei Zhou, Wenguan Wang, Si Liu, Yi Yang, Luc van Gool
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: zhou2021differentiable
citations: 73
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.04570'}]
tags: ["CVPR"]
short_authors: Zhou et al.
---
To address the challenging task of instance-aware human part parsing, a new
bottom-up regime is proposed to learn category-level human semantic
segmentation as well as multi-person pose estimation in a joint and end-to-end
manner. It is a compact, efficient and powerful framework that exploits
structural information over different human granularities and eases the
difficulty of person partitioning. Specifically, a dense-to-sparse projection
field, which allows explicitly associating dense human semantics with sparse
keypoints, is learnt and progressively improved over the network feature
pyramid for robustness. Then, the difficult pixel grouping problem is cast as
an easier, multi-person joint assembling task. By formulating joint association
as maximum-weight bipartite matching, a differentiable solution is developed to
exploit projected gradient descent and Dykstra's cyclic projection algorithm.
This makes our method end-to-end trainable and allows back-propagating the
grouping error to directly supervise multi-granularity human representation
learning. This is distinguished from current bottom-up human parsers or pose
estimators which require sophisticated post-processing or heuristic greedy
algorithms. Experiments on three instance-aware human parsing datasets show
that our model outperforms other bottom-up alternatives with much more
efficient inference.
---
layout: publication
title: 'Descriptor Ensemble: An Unsupervised Approach To Descriptor Fusion In The
  Homography Space'
authors: Yuan-Ting Hu, Yen-Yu Lin, Hsin-Yi Chen, Kuang-Jui Hsu, Bing-Yu Chen
conference: Arxiv
year: 2014
bibkey: hu2014descriptor
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1412.4196'}]
tags: ["Unsupervised"]
short_authors: Hu et al.
---
With the aim to improve the performance of feature matching, we present an
unsupervised approach to fuse various local descriptors in the space of
homographies. Inspired by the observation that the homographies of correct
feature correspondences vary smoothly along the spatial domain, our approach
stands on the unsupervised nature of feature matching, and can select a good
descriptor for matching each feature point. Specifically, the homography space
serves as the common domain, in which a correspondence obtained by any
descriptor is considered as a point, for integrating various heterogeneous
descriptors. Both geometric coherence and spatial continuity among
correspondences are considered via computing their geodesic distances in the
space. In this way, mutual verification across different descriptors is
allowed, and correct correspondences will be highlighted with a high degree of
consistency (i.e., short geodesic distances here). It follows that one-class
SVM can be applied to identifying these correct correspondences, and boosts the
performance of feature matching. The proposed approach is comprehensively
compared with the state-of-the-art approaches, and evaluated on four benchmarks
of image matching. The promising results manifest its effectiveness.
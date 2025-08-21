---
layout: publication
title: Differential Geometric Retrieval Of Deep Features
authors: Y Qian, E Vazquez, B Sengupta
conference: Arxiv
year: 2017
bibkey: qian2017differential
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1702.06383'}]
tags: ["Distance Metric Learning", "Evaluation", "Image Retrieval", "Scalability"]
short_authors: Y Qian, E Vazquez, B Sengupta
---
Comparing images to recommend items from an image-inventory is a subject of
continued interest. Added with the scalability of deep-learning architectures
the once `manual' job of hand-crafting features have been largely alleviated,
and images can be compared according to features generated from a deep
convolutional neural network. In this paper, we compare distance metrics (and
divergences) to rank features generated from a neural network, for
content-based image retrieval. Specifically, after modelling individual images
using approximations of mixture models or sparse covariance estimators, we
resort to their information-theoretic and Riemann geometric comparisons. We
show that using approximations of mixture models enable us to compute a
distance measure based on the Wasserstein metric that requires less effort than
other computationally intensive optimal transport plans; finally, an affine
invariant metric is used to compare the optimal transport metric to its Riemann
geometric counterpart -- we conclude that although expensive, retrieval metric
based on Wasserstein geometry is more suitable than information theoretic
comparison of images. In short, we combine GPU scalability in learning deep
feature vectors with statistically efficient metrics that we foresee being
utilised in a commercial setting.
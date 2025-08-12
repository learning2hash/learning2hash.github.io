---
layout: publication
title: Unsupervised Feature Learning By Deep Sparse Coding
authors: Yunlong He, Koray Kavukcuoglu, Yun Wang, Arthur Szlam, Yanjun Qi
conference: Proceedings of the 2014 SIAM International Conference on Data Mining
year: 2014
bibkey: he2013unsupervised
citations: 61
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1312.5783'}]
tags: ["Unsupervised"]
short_authors: He et al.
---
In this paper, we propose a new unsupervised feature learning framework,
namely Deep Sparse Coding (DeepSC), that extends sparse coding to a multi-layer
architecture for visual object recognition tasks. The main innovation of the
framework is that it connects the sparse-encoders from different layers by a
sparse-to-dense module. The sparse-to-dense module is a composition of a local
spatial pooling step and a low-dimensional embedding process, which takes
advantage of the spatial smoothness information in the image. As a result, the
new method is able to learn several levels of sparse representation of the
image which capture features at a variety of abstraction levels and
simultaneously preserve the spatial smoothness between the neighboring image
patches. Combining the feature representations from multiple layers, DeepSC
achieves the state-of-the-art performance on multiple object recognition tasks.
---
layout: publication
title: Multiple Instance Dense Connected Convolution Neural Network For Aerial Image
  Scene Classification
authors: Qi Bi, Kun Qin, Zhili Li, Han Zhang, Kai Xu
conference: 2019 IEEE International Conference on Image Processing (ICIP)
year: 2019
bibkey: bi2019multiple
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.08156'}]
tags: []
short_authors: Bi et al.
---
With the development of deep learning, many state-of-the-art natural image
scene classification methods have demonstrated impressive performance. While
the current convolution neural network tends to extract global features and
global semantic information in a scene, the geo-spatial objects can be located
at anywhere in an aerial image scene and their spatial arrangement tends to be
more complicated. One possible solution is to preserve more local semantic
information and enhance feature propagation. In this paper, an end to end
multiple instance dense connected convolution neural network (MIDCCNN) is
proposed for aerial image scene classification. First, a 23 layer dense
connected convolution neural network (DCCNN) is built and served as a backbone
to extract convolution features. It is capable of preserving middle and low
level convolution features. Then, an attention based multiple instance pooling
is proposed to highlight the local semantics in an aerial image scene. Finally,
we minimize the loss between the bag-level predictions and the ground truth
labels so that the whole framework can be trained directly. Experiments on
three aerial image datasets demonstrate that our proposed methods can
outperform current baselines by a large margin.
---
layout: publication
title: 'Xsepconv: Extremely Separated Convolution'
authors: Jiarong Chen, Zongqing Lu, Jing-Hao Xue, Qingmin Liao
conference: Arxiv
year: 2020
bibkey: chen2020xsepconv
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.12046'}]
tags: []
short_authors: Chen et al.
---
Depthwise convolution has gradually become an indispensable operation for
modern efficient neural networks and larger kernel sizes (\(\ge5\)) have been
applied to it recently. In this paper, we propose a novel extremely separated
convolutional block (XSepConv), which fuses spatially separable convolutions
into depthwise convolution to further reduce both the computational cost and
parameter size of large kernels. Furthermore, an extra \(2\times2\) depthwise
convolution coupled with improved symmetric padding strategy is employed to
compensate for the side effect brought by spatially separable convolutions.
XSepConv is designed to be an efficient alternative to vanilla depthwise
convolution with large kernel sizes. To verify this, we use XSepConv for the
state-of-the-art architecture MobileNetV3-Small and carry out extensive
experiments on four highly competitive benchmark datasets (CIFAR-10, CIFAR-100,
SVHN and Tiny-ImageNet) to demonstrate that XSepConv can indeed strike a better
trade-off between accuracy and efficiency.
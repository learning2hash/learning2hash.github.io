---
layout: publication
title: Deep Isometric Learning For Visual Recognition
authors: Haozhi Qi, Chong You, Xiaolong Wang, Yi Ma, Jitendra Malik
conference: Arxiv
year: 2020
bibkey: qi2020deep
citations: 25
additional_links: [{name: Code, url: 'https://github.com/HaozhiQi/ISONet'}, {name: Paper,
    url: 'https://arxiv.org/abs/2006.16992'}]
tags: ["Distance Metric Learning"]
short_authors: Qi et al.
---
Initialization, normalization, and skip connections are believed to be three
indispensable techniques for training very deep convolutional neural networks
and obtaining state-of-the-art performance. This paper shows that deep vanilla
ConvNets without normalization nor skip connections can also be trained to
achieve surprisingly good performance on standard image recognition benchmarks.
This is achieved by enforcing the convolution kernels to be near isometric
during initialization and training, as well as by using a variant of ReLU that
is shifted towards being isometric. Further experiments show that if combined
with skip connections, such near isometric networks can achieve performances on
par with (for ImageNet) and better than (for COCO) the standard ResNet, even
without normalization at all. Our code is available at
https://github.com/HaozhiQi/ISONet.
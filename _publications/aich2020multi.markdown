---
layout: publication
title: Multi-scale Weight Sharing Network For Image Recognition
authors: Shubhra Aich, Ian Stavness, Yasuhiro Taniguchi, Masaki Yamazaki
conference: Pattern Recognition Letters
year: 2020
bibkey: aich2020multi
citations: 21
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2001.02816'}]
tags: []
short_authors: Aich et al.
---
In this paper, we explore the idea of weight sharing over multiple scales in
convolutional networks. Inspired by traditional computer vision approaches, we
share the weights of convolution kernels over different scales in the same
layers of the network. Although multi-scale feature aggregation and sharing
inside convolutional networks are common in practice, none of the previous
works address the issue of convolutional weight sharing. We evaluate our weight
sharing scheme on two heterogeneous image recognition datasets - ImageNet
(object recognition) and Places365-Standard (scene classification). With
approximately 25% fewer parameters, our shared-weight ResNet model provides
similar performance compared to baseline ResNets. Shared-weight models are
further validated via transfer learning experiments on four additional image
recognition datasets - Caltech256 and Stanford 40 Actions (object-centric) and
SUN397 and MIT Inddor67 (scene-centric). Experimental results demonstrate
significant redundancy in the vanilla implementations of the deeper networks,
and also indicate that a shift towards increasing the receptive field per
parameter may improve future convolutional network architectures.
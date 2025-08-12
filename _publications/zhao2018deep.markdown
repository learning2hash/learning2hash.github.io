---
layout: publication
title: Deep Multiple Description Coding By Learning Scalar Quantization
authors: Lijun Zhao, Huihui Bai, Anhong Wang, Yao Zhao
conference: 2019 Data Compression Conference (DCC)
year: 2019
bibkey: zhao2018deep
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.01504'}]
tags: ["Quantization"]
short_authors: Zhao et al.
---
In this paper, we propose a deep multiple description coding framework, whose
quantizers are adaptively learned via the minimization of multiple description
compressive loss. Firstly, our framework is built upon auto-encoder networks,
which have multiple description multi-scale dilated encoder network and
multiple description decoder networks. Secondly, two entropy estimation
networks are learned to estimate the informative amounts of the quantized
tensors, which can further supervise the learning of multiple description
encoder network to represent the input image delicately. Thirdly, a pair of
scalar quantizers accompanied by two importance-indicator maps is automatically
learned in an end-to-end self-supervised way. Finally, multiple description
structural dissimilarity distance loss is imposed on multiple description
decoded images in pixel domain for diversified multiple description generations
rather than on feature tensors in feature domain, in addition to multiple
description reconstruction loss. Through testing on two commonly used datasets,
it is verified that our method is beyond several state-of-the-art multiple
description coding approaches in terms of coding efficiency.
---
layout: publication
title: Self-supervising Fine-grained Region Similarities For Large-scale Image Localization
authors: Yixiao Ge, Haibo Wang, Feng Zhu, Rui Zhao, Hongsheng Li
conference: Lecture Notes in Computer Science
year: 2020
bibkey: ge2020self
citations: 107
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.03926'}]
tags: ["Image Retrieval", "Scalability"]
short_authors: Ge et al.
---
The task of large-scale retrieval-based image localization is to estimate the
geographical location of a query image by recognizing its nearest reference
images from a city-scale dataset. However, the general public benchmarks only
provide noisy GPS labels associated with the training images, which act as weak
supervisions for learning image-to-image similarities. Such label noise
prevents deep neural networks from learning discriminative features for
accurate localization. To tackle this challenge, we propose to self-supervise
image-to-region similarities in order to fully explore the potential of
difficult positive images alongside their sub-regions. The estimated
image-to-region similarities can serve as extra training supervision for
improving the network in generations, which could in turn gradually refine the
fine-grained similarities to achieve optimal performance. Our proposed
self-enhanced image-to-region similarity labels effectively deal with the
training bottleneck in the state-of-the-art pipelines without any additional
parameters or manual annotations in both training and inference. Our method
outperforms state-of-the-arts on the standard localization benchmarks by
noticeable margins and shows excellent generalization capability on multiple
image retrieval datasets.
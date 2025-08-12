---
layout: publication
title: Sorted Convolutional Network For Achieving Continuous Rotational Invariance
authors: Hanlin Mo, Guoying Zhao
conference: Arxiv
year: 2023
bibkey: mo2023sorted
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.14462'}]
tags: []
short_authors: Hanlin Mo, Guoying Zhao
---
The topic of achieving rotational invariance in convolutional neural networks
(CNNs) has gained considerable attention recently, as this invariance is
crucial for many computer vision tasks such as image classification and
matching. In this letter, we propose a Sorting Convolution (SC) inspired by
some hand-crafted features of texture images, which achieves continuous
rotational invariance without requiring additional learnable parameters or data
augmentation. Further, SC can directly replace the conventional convolution
operations in a classic CNN model to achieve its rotational invariance. Based
on MNIST-rot dataset, we first analyze the impact of convolutional kernel
sizes, different sampling and sorting strategies on SC's rotational invariance,
and compare our method with previous rotation-invariant CNN models. Then, we
combine SC with VGG, ResNet and DenseNet, and conduct classification
experiments on popular texture and remote sensing image datasets. Our results
demonstrate that SC achieves the best performance in the aforementioned tasks.
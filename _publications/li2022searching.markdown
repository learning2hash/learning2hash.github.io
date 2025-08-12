---
layout: publication
title: Searching Similarity Measure For Binarized Neural Networks
authors: Yanfei Li, Ang Li, Huimin Yu
conference: Arxiv
year: 2022
bibkey: li2022searching
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.03325'}]
tags: []
short_authors: Yanfei Li, Ang Li, Huimin Yu
---
Being a promising model to be deployed in resource-limited devices, Binarized
Neural Networks (BNNs) have drawn extensive attention from both academic and
industry. However, comparing to the full-precision deep neural networks (DNNs),
BNNs suffer from non-trivial accuracy degradation, limiting its applicability
in various domains. This is partially because existing network components, such
as the similarity measure, are specially designed for DNNs, and might be
sub-optimal for BNNs.
  In this work, we focus on the key component of BNNs -- the similarity
measure, which quantifies the distance between input feature maps and filters,
and propose an automatic searching method, based on genetic algorithm, for
BNN-tailored similarity measure. Evaluation results on Cifar10 and Cifar100
using ResNet, NIN and VGG show that most of the identified similarty measure
can achieve considerable accuracy improvement (up to 3.39%) over the
commonly-used cross-correlation approach.
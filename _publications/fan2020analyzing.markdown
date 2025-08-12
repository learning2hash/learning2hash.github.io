---
layout: publication
title: Analyzing The Dependency Of Convnets On Spatial Information
authors: Yue Fan, Yongqin Xian, Max Maria Losch, Bernt Schiele
conference: Lecture Notes in Computer Science
year: 2021
bibkey: fan2020analyzing
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.01827'}]
tags: []
short_authors: Fan et al.
---
Intuitively, image classification should profit from using spatial
information. Recent work, however, suggests that this might be overrated in
standard CNNs. In this paper, we are pushing the envelope and aim to further
investigate the reliance on spatial information. We propose spatial shuffling
and GAP+FC to destroy spatial information during both training and testing
phases. Interestingly, we observe that spatial information can be deleted from
later layers with small performance drops, which indicates spatial information
at later layers is not necessary for good performance. For example, test
accuracy of VGG-16 only drops by 0.03% and 2.66% with spatial information
completely removed from the last 30% and 53% layers on CIFAR100, respectively.
Evaluation on several object recognition datasets (CIFAR100, Small-ImageNet,
ImageNet) with a wide range of CNN architectures (VGG16, ResNet50, ResNet152)
shows an overall consistent pattern.
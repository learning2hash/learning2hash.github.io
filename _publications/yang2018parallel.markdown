---
layout: publication
title: Parallel Convolutional Networks For Image Recognition Via A Discriminator
authors: Shiqi Yang, Gang Peng
conference: Lecture Notes in Computer Science
year: 2019
bibkey: yang2018parallel
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.02265'}]
tags: []
short_authors: Shiqi Yang, Gang Peng
---
In this paper, we introduce a simple but quite effective recognition
framework dubbed D-PCN, aiming at enhancing feature extracting ability of CNN.
The framework consists of two parallel CNNs, a discriminator and an extra
classifier which takes integrated features from parallel networks and gives
final prediction. The discriminator is core which drives parallel networks to
focus on different regions and learn different representations. The
corresponding training strategy is introduced to ensures utilization of
discriminator. We validate D-PCN with several CNN models on benchmark datasets:
CIFAR-100, and ImageNet, D-PCN enhances all models. In particular it yields
state of the art performance on CIFAR-100 compared with related works. We also
conduct visualization experiment on fine-grained Stanford Dogs dataset to
verify our motivation. Additionally, we apply D-PCN for segmentation on PASCAL
VOC 2012 and also find promotion.
---
layout: publication
title: Data-free Dynamic Compression Of Cnns For Tractable Efficiency
authors: Lukas Meiner, Jens Mehnert, Alexandru Paul Condurache
conference: Proceedings of the 20th International Joint Conference on Computer Vision,
  Imaging and Computer Graphics Theory and Applications
year: 2025
bibkey: meiner2023data
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.17211'}]
tags: ["Efficiency", "Hashing Methods", "Locality Sensitive Hashing"]
short_authors: Lukas Meiner, Jens Mehnert, Alexandru Paul Condurache
---
To reduce the computational cost of convolutional neural networks (CNNs) on
resource-constrained devices, structured pruning approaches have shown promise
in lowering floating-point operations (FLOPs) without substantial drops in
accuracy. However, most methods require fine-tuning or specific training
procedures to achieve a reasonable trade-off between retained accuracy and
reduction in FLOPs, adding computational overhead and requiring training data
to be available. To this end, we propose HASTE (Hashing for Tractable
Efficiency), a data-free, plug-and-play convolution module that instantly
reduces a network's test-time inference cost without training or fine-tuning.
Our approach utilizes locality-sensitive hashing (LSH) to detect redundancies
in the channel dimension of latent feature maps, compressing similar channels
to reduce input and filter depth simultaneously, resulting in cheaper
convolutions. We demonstrate our approach on the popular vision benchmarks
CIFAR-10 and ImageNet, where we achieve a 46.72% reduction in FLOPs with only a
1.25% loss in accuracy by swapping the convolution modules in a ResNet34 on
CIFAR-10 for our HASTE module.
---
layout: publication
title: 'Tresnet: High Performance Gpu-dedicated Architecture'
authors: Tal Ridnik, Hussam Lawen, Asaf Noy, Emanuel Ben Baruch, Gilad Sharir, Itamar
  Friedman
conference: 2021 IEEE Winter Conference on Applications of Computer Vision (WACV)
year: 2021
bibkey: ridnik2020tresnet
citations: 187
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2003.13630'}]
tags: ["Efficiency"]
short_authors: Ridnik et al.
---
Many deep learning models, developed in recent years, reach higher ImageNet
accuracy than ResNet50, with fewer or comparable FLOPS count. While FLOPs are
often seen as a proxy for network efficiency, when measuring actual GPU
training and inference throughput, vanilla ResNet50 is usually significantly
faster than its recent competitors, offering better throughput-accuracy
trade-off.
  In this work, we introduce a series of architecture modifications that aim to
boost neural networks' accuracy, while retaining their GPU training and
inference efficiency. We first demonstrate and discuss the bottlenecks induced
by FLOPs-optimizations. We then suggest alternative designs that better utilize
GPU structure and assets. Finally, we introduce a new family of GPU-dedicated
models, called TResNet, which achieve better accuracy and efficiency than
previous ConvNets.
  Using a TResNet model, with similar GPU throughput to ResNet50, we reach 80.8
top-1 accuracy on ImageNet. Our TResNet models also transfer well and achieve
state-of-the-art accuracy on competitive single-label classification datasets
such as Stanford cars (96.0%), CIFAR-10 (99.0%), CIFAR-100 (91.5%) and
Oxford-Flowers (99.1%). They also perform well on multi-label classification
and object detection tasks. Implementation is available at:
https://github.com/mrT23/TResNet.
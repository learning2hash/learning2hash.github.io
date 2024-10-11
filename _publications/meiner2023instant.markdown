---
layout: publication
title: Instant Complexity Reduction In Cnns Using Locality-sensitive Hashing
authors: Meiner Lukas, Mehnert Jens, Condurache Alexandru Paul
conference: "Arxiv"
year: 2023
bibkey: meiner2023instant
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2309.17211"}
tags: ['ARXIV', 'LSH', 'Supervised']
---
To reduce the computational cost of convolutional neural networks (CNNs) for usage on resource-constrained devices, structured pruning approaches have shown promising results, drastically reducing floating-point operations (FLOPs) without substantial drops in accuracy. However, most recent methods require fine-tuning or specific training procedures to achieve a reasonable trade-off between retained accuracy and reduction in FLOPs. This introduces additional cost in the form of computational overhead and requires training data to be available. To this end, we propose HASTE (Hashing for Tractable Efficiency), a parameter-free and data-free module that acts as a plug-and-play replacement for any regular convolution module. It instantly reduces the network's test-time inference cost without requiring any training or fine-tuning. We are able to drastically compress latent feature maps without sacrificing much accuracy by using locality-sensitive hashing (LSH) to detect redundancies in the channel dimension. Similar channels are aggregated to reduce the input and filter depth simultaneously, allowing for cheaper convolutions. We demonstrate our approach on the popular vision benchmarks CIFAR-10 and ImageNet. In particular, we are able to instantly drop 46.72&#37; of FLOPs while only losing 1.25&#37; accuracy by just swapping the convolution modules in a ResNet34 on CIFAR-10 for our HASTE module.

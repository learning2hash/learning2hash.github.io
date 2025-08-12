---
layout: publication
title: 'CAT: Compression-aware Training For Bandwidth Reduction'
authors: Chaim Baskin, Brian Chmiel, Evgenii Zheltonozhskii, Ron Banner, Alex M. Bronstein,
  Avi Mendelson
conference: Arxiv
year: 2019
bibkey: baskin2019cat
citations: 10
additional_links: [{name: Code, url: 'https://github.com/CAT-teams/CAT'}, {name: Paper,
    url: 'https://arxiv.org/abs/1909.11481'}]
tags: ["Quantization"]
short_authors: Baskin et al.
---
Convolutional neural networks (CNNs) have become the dominant neural network
architecture for solving visual processing tasks. One of the major obstacles
hindering the ubiquitous use of CNNs for inference is their relatively high
memory bandwidth requirements, which can be a main energy consumer and
throughput bottleneck in hardware accelerators. Accordingly, an efficient
feature map compression method can result in substantial performance gains.
Inspired by quantization-aware training approaches, we propose a
compression-aware training (CAT) method that involves training the model in a
way that allows better compression of feature maps during inference. Our method
trains the model to achieve low-entropy feature maps, which enables efficient
compression at inference time using classical transform coding methods. CAT
significantly improves the state-of-the-art results reported for quantization.
For example, on ResNet-34 we achieve 73.1% accuracy (0.2% degradation from the
baseline) with an average representation of only 1.79 bits per value. Reference
implementation accompanies the paper at https://github.com/CAT-teams/CAT
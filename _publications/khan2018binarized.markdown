---
layout: publication
title: Binarized Convolutional Neural Networks For Efficient Inference On Gpus
authors: Mir Khan, Heikki Huttunen, Jani Boutellier
conference: 2018 26th European Signal Processing Conference (EUSIPCO)
year: 2018
bibkey: khan2018binarized
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1808.00209'}]
tags: ["Efficiency", "Memory Efficiency"]
short_authors: Mir Khan, Heikki Huttunen, Jani Boutellier
---
Convolutional neural networks have recently achieved significant
breakthroughs in various image classification tasks. However, they are
computationally expensive,which can make their feasible mplementation on
embedded and low-power devices difficult. In this paper convolutional neural
network binarization is implemented on GPU-based platforms for real-time
inference on resource constrained devices. In binarized networks, all weights
and intermediate computations between layers are quantized to +1 and -1,
allowing multiplications and additions to be replaced with bit-wise operations
between 32-bit words. This representation completely eliminates the need for
floating point multiplications and additions and decreases both the
computational load and the memory footprint compared to a full-precision
network implemented in floating point, making it well-suited for
resource-constrained environments. We compare the performance of our
implementation with an equivalent floating point implementation on one desktop
and two embedded GPU platforms. Our implementation achieves a maximum speed up
of 7. 4X with only 4.4% loss in accuracy compared to a reference
implementation.
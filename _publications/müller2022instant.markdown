---
layout: publication
title: Instant Neural Graphics Primitives With A Multiresolution Hash Encoding
authors: Müller Thomas, Evans Alex, Schied Christoph, Keller Alexander
conference: "ACM Trans. Graph."
year: 2022
bibkey: müller2022instant
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2201.05989"}
tags: ['Graph', 'Supervised']
---
Neural graphics primitives, parameterized by fully connected neural networks, can be costly to train and evaluate. We reduce this cost with a versatile new input encoding that permits the use of a smaller network without sacrificing quality, thus significantly reducing the number of floating point and memory access operations: a small neural network is augmented by a multiresolution hash table of trainable feature vectors whose values are optimized through stochastic gradient descent. The multiresolution structure allows the network to disambiguate hash collisions, making for a simple architecture that is trivial to parallelize on modern GPUs. We leverage this parallelism by implementing the whole system using fully-fused CUDA kernels with a focus on minimizing wasted bandwidth and compute operations. We achieve a combined speedup of several orders of magnitude, enabling training of high-quality neural graphics primitives in a matter of seconds, and rendering in tens of milliseconds at a resolution of \(\{1920\!\times\!1080\}\).

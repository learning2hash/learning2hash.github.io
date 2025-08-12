---
layout: publication
title: Parallel Discrete Convolutions On Adaptive Particle Representations Of Images
authors: Joel Jonsson, Bevan L. Cheeseman, Suryanarayana Maddu, Krzysztof Gonciarz,
  Ivo F. Sbalzarini
conference: IEEE Transactions on Image Processing
year: 2022
bibkey: jonsson2021parallel
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.03592'}]
tags: []
short_authors: Jonsson et al.
---
We present data structures and algorithms for native implementations of
discrete convolution operators over Adaptive Particle Representations (APR) of
images on parallel computer architectures. The APR is a content-adaptive image
representation that locally adapts the sampling resolution to the image signal.
It has been developed as an alternative to pixel representations for large,
sparse images as they typically occur in fluorescence microscopy. It has been
shown to reduce the memory and runtime costs of storing, visualizing, and
processing such images. This, however, requires that image processing natively
operates on APRs, without intermediately reverting to pixels. Designing
efficient and scalable APR-native image processing primitives, however, is
complicated by the APR's irregular memory structure. Here, we provide the
algorithmic building blocks required to efficiently and natively process APR
images using a wide range of algorithms that can be formulated in terms of
discrete convolutions. We show that APR convolution naturally leads to
scale-adaptive algorithms that efficiently parallelize on multi-core CPU and
GPU architectures. We quantify the speedups in comparison to pixel-based
algorithms and convolutions on evenly sampled data. We achieve pixel-equivalent
throughputs of up to 1 TB/s on a single Nvidia GeForce RTX 2080 gaming GPU,
requiring up to two orders of magnitude less memory than a pixel-based
implementation.
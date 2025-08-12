---
layout: publication
title: Parallel Multi Channel Convolution Using General Matrix Multiplication
authors: Aravind Vasudevan, Andrew Anderson, David Gregg
conference: 2017 IEEE 28th International Conference on Application-specific Systems,
  Architectures and Processors (ASAP)
year: 2017
bibkey: vasudevan2017parallel
citations: 131
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1704.04428'}]
tags: []
short_authors: Aravind Vasudevan, Andrew Anderson, David Gregg
---
Convolutional neural networks (CNNs) have emerged as one of the most
successful machine learning technologies for image and video processing. The
most computationally intensive parts of CNNs are the convolutional layers,
which convolve multi-channel images with multiple kernels. A common approach to
implementing convolutional layers is to expand the image into a column matrix
(im2col) and perform Multiple Channel Multiple Kernel (MCMK) convolution using
an existing parallel General Matrix Multiplication (GEMM) library. This im2col
conversion greatly increases the memory footprint of the input matrix and
reduces data locality.
  In this paper we propose a new approach to MCMK convolution that is based on
General Matrix Multiplication (GEMM), but not on im2col. Our algorithm
eliminates the need for data replication on the input thereby enabling us to
apply the convolution kernels on the input images directly. We have implemented
several variants of our algorithm on a CPU processor and an embedded ARM
processor. On the CPU, our algorithm is faster than im2col in most cases.
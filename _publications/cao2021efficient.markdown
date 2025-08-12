---
layout: publication
title: Efficient Tensor Contraction Via Fast Count Sketch
authors: Xingyu Cao, Jiani Liu
conference: Arxiv
year: 2021
bibkey: cao2021efficient
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.13062'}]
tags: ["Efficiency", "Hashing Methods"]
short_authors: Xingyu Cao, Jiani Liu
---
Sketching uses randomized Hash functions for dimensionality reduction and
acceleration. The existing sketching methods, such as count sketch (CS), tensor
sketch (TS), and higher-order count sketch (HCS), either suffer from low
accuracy or slow speed in some tensor based applications. In this paper, the
proposed fast count sketch (FCS) applies multiple shorter Hash functions based
CS to the vector form of the input tensor, which is more accurate than TS since
the spatial information of the input tensor can be preserved more sufficiently.
When the input tensor admits CANDECOMP/PARAFAC decomposition (CPD), FCS can
accelerate CS and HCS by using fast Fourier transform, which exhibits a
computational complexity asymptotically identical to TS for low-order tensors.
The effectiveness of FCS is validated by CPD, tensor regression network
compression, and Kronecker product compression. Experimental results show its
superior performance in terms of approximation accuracy and computational
efficiency.
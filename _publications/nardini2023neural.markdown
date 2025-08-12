---
layout: publication
title: Neural Network Compression Using Binarization And Few Full-precision Weights
authors: Franco Maria Nardini, Cosimo Rulli, Salvatore Trani, Rossano Venturini
conference: Information Sciences
year: 2025
bibkey: nardini2023neural
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.08960'}]
tags: ["Efficiency", "Quantization"]
short_authors: Nardini et al.
---
Quantization and pruning are two effective Deep Neural Networks model
compression methods. In this paper, we propose Automatic Prune Binarization
(APB), a novel compression technique combining quantization with pruning. APB
enhances the representational capability of binary networks using a few
full-precision weights. Our technique jointly maximizes the accuracy of the
network while minimizing its memory impact by deciding whether each weight
should be binarized or kept in full precision. We show how to efficiently
perform a forward pass through layers compressed using APB by decomposing it
into a binary and a sparse-dense matrix multiplication. Moreover, we design two
novel efficient algorithms for extremely quantized matrix multiplication on
CPU, leveraging highly efficient bitwise operations. The proposed algorithms
are 6.9x and 1.5x faster than available state-of-the-art solutions. We
extensively evaluate APB on two widely adopted model compression datasets,
namely CIFAR10 and ImageNet. APB delivers better accuracy/memory trade-off
compared to state-of-the-art methods based on i) quantization, ii) pruning, and
iii) combination of pruning and quantization. APB outperforms quantization in
the accuracy/efficiency trade-off, being up to 2x faster than the 2-bit
quantized model with no loss in accuracy.
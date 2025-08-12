---
layout: publication
title: 'PCNN: Pattern-based Fine-grained Regular Pruning Towards Optimizing CNN Accelerators'
authors: Zhanhong Tan, Jiebo Song, Xiaolong Ma, Sia-Huat Tan, Hongyang Chen, Yuanqing
  Miao, Yifu Wu, Shaokai Ye, Yanzhi Wang, Dehui Li, Kaisheng Ma
conference: 2020 57th ACM/IEEE Design Automation Conference (DAC)
year: 2020
bibkey: tan2020pcnn
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.04997'}]
tags: ["Efficiency"]
short_authors: Tan et al.
---
Weight pruning is a powerful technique to realize model compression. We
propose PCNN, a fine-grained regular 1D pruning method. A novel index format
called Sparsity Pattern Mask (SPM) is presented to encode the sparsity in PCNN.
Leveraging SPM with limited pruning patterns and non-zero sequences with equal
length, PCNN can be efficiently employed in hardware. Evaluated on VGG-16 and
ResNet-18, our PCNN achieves the compression rate up to 8.4X with only 0.2%
accuracy loss. We also implement a pattern-aware architecture in 55nm process,
achieving up to 9.0X speedup and 28.39 TOPS/W efficiency with only 3.1% on-chip
memory overhead of indices.
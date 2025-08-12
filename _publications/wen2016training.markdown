---
layout: publication
title: Training Bit Fully Convolutional Network For Fast Semantic Segmentation
authors: He Wen, Shuchang Zhou, Zhe Liang, Yuxiang Zhang, Dieqiao Feng, Xinyu Zhou,
  Cong Yao
conference: Arxiv
year: 2016
bibkey: wen2016training
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1612.00212'}]
tags: ["Evaluation"]
short_authors: Wen et al.
---
Fully convolutional neural networks give accurate, per-pixel prediction for
input images and have applications like semantic segmentation. However, a
typical FCN usually requires lots of floating point computation and large
run-time memory, which effectively limits its usability. We propose a method to
train Bit Fully Convolution Network (BFCN), a fully convolutional neural
network that has low bit-width weights and activations. Because most of its
computation-intensive convolutions are accomplished between low bit-width
numbers, a BFCN can be accelerated by an efficient bit-convolution
implementation. On CPU, the dot product operation between two bit vectors can
be reduced to bitwise operations and popcounts, which can offer much higher
throughput than 32-bit multiplications and additions.
  To validate the effectiveness of BFCN, we conduct experiments on the PASCAL
VOC 2012 semantic segmentation task and Cityscapes. Our BFCN with 1-bit weights
and 2-bit activations, which runs 7.8x faster on CPU or requires less than 1%
resources on FPGA, can achieve comparable performance as the 32-bit
counterpart.
---
layout: publication
title: A Binary Convolutional Encoder-decoder Network For Real-time Natural Scene
  Text Processing
authors: Zichuan Liu, Yixing Li, Fengbo Ren, Hao Yu
conference: Arxiv
year: 2016
bibkey: liu2016binary
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1612.03630'}]
tags: ["Efficiency"]
short_authors: Liu et al.
---
In this paper, we develop a binary convolutional encoder-decoder network
(B-CEDNet) for natural scene text processing (NSTP). It converts a text image
to a class-distinguished salience map that reveals the categorical, spatial and
morphological information of characters. The existing solutions are either
memory consuming or run-time consuming that cannot be applied to real-time
applications on resource-constrained devices such as advanced driver assistance
systems. The developed network can process multiple regions containing
characters by one-off forward operation, and is trained to have binary weights
and binary feature maps, which lead to both remarkable inference run-time
speedup and memory usage reduction. By training with over 200, 000 synthesis
scene text images (size of \(32\times128\)), it can achieve \(90%\) and \(91%\)
pixel-wise accuracy on ICDAR-03 and ICDAR-13 datasets. It only consumes \(4.59\
ms\) inference run-time realized on GPU with a small network size of 2.14 MB,
which is up to \(8\times\) faster and \(96%\) smaller than it full-precision
version.
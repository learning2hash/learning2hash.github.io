---
layout: publication
title: 'A Computing Kernel For Network Binarization On Pytorch'
authors: Xianda Xu, Marco Pedersoli
conference: "Arxiv"
year: 2019
citations: 1
bibkey: xu2019computing
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1911.04477'}
tags: ['Quantization and Compression']
---
Deep Neural Networks have now achieved state-of-the-art results in a wide
range of tasks including image classification, object detection and so on.
However, they are both computation consuming and memory intensive, making them
difficult to deploy on low-power devices. Network binarization is one of the
existing effective techniques for model compression and acceleration, but there
is no computing kernel yet to support it on PyTorch. In this paper we developed
a computing kernel supporting 1-bit xnor and bitcount computation on PyTorch.
Experimental results show that our kernel could accelerate the inference of the
binarized neural network by 3 times in GPU and by 4.5 times in CPU compared
with the control group.

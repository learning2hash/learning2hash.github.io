---
layout: publication
title: 'Binary Neural Networks: A Survey'
authors: Haotong Qin, Ruihao Gong, Xianglong Liu, Xiao Bai, Jingkuan Song, Nicu Sebe
conference: Pattern Recognition
year: 2020
bibkey: qin2020binary
citations: 446
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.03333'}]
tags: ["Survey Paper"]
short_authors: Qin et al.
---
The binary neural network, largely saving the storage and computation, serves
as a promising technique for deploying deep models on resource-limited devices.
However, the binarization inevitably causes severe information loss, and even
worse, its discontinuity brings difficulty to the optimization of the deep
network. To address these issues, a variety of algorithms have been proposed,
and achieved satisfying progress in recent years. In this paper, we present a
comprehensive survey of these algorithms, mainly categorized into the native
solutions directly conducting binarization, and the optimized ones using
techniques like minimizing the quantization error, improving the network loss
function, and reducing the gradient error. We also investigate other practical
aspects of binary neural networks such as the hardware-friendly design and the
training tricks. Then, we give the evaluation and discussions on different
tasks, including image classification, object detection and semantic
segmentation. Finally, the challenges that may be faced in future research are
prospected.
---
layout: publication
title: JPEG Inspired Deep Learning
authors: Ahmed H. Salamah, Kaixiang Zheng, Yiwen Liu, En-Hui Yang
conference: The Thirteenth International Conference on Learning Representations 2025
  (ICLR 2025)
year: 2024
bibkey: salamah2024jpeg
citations: 0
additional_links: [{name: Code, url: 'https://github.com/AhmedHussKhalifa/JPEG-Inspired-DL.git'},
  {name: Paper, url: 'https://arxiv.org/abs/2410.07081'}]
tags: []
short_authors: Salamah et al.
---
Although it is traditionally believed that lossy image compression, such as
JPEG compression, has a negative impact on the performance of deep neural
networks (DNNs), it is shown by recent works that well-crafted JPEG compression
can actually improve the performance of deep learning (DL). Inspired by this,
we propose JPEG-DL, a novel DL framework that prepends any underlying DNN
architecture with a trainable JPEG compression layer. To make the quantization
operation in JPEG compression trainable, a new differentiable soft quantizer is
employed at the JPEG layer, and then the quantization operation and underlying
DNN are jointly trained. Extensive experiments show that in comparison with the
standard DL, JPEG-DL delivers significant accuracy improvements across various
datasets and model architectures while enhancing robustness against adversarial
attacks. Particularly, on some fine-grained image classification datasets,
JPEG-DL can increase prediction accuracy by as much as 20.9%. Our code is
available on https://github.com/AhmedHussKhalifa/JPEG-Inspired-DL.git.
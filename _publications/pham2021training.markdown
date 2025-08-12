---
layout: publication
title: Training Multi-bit Quantized And Binarized Networks With A Learnable Symmetric
  Quantizer
authors: Phuoc Pham, Jacob Abraham, Jaeyong Chung
conference: IEEE Access
year: 2021
bibkey: pham2021training
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.00210'}]
tags: ["Quantization"]
short_authors: Phuoc Pham, Jacob Abraham, Jaeyong Chung
---
Quantizing weights and activations of deep neural networks is essential for
deploying them in resource-constrained devices, or cloud platforms for at-scale
services. While binarization is a special case of quantization, this extreme
case often leads to several training difficulties, and necessitates specialized
models and training methods. As a result, recent quantization methods do not
provide binarization, thus losing the most resource-efficient option, and
quantized and binarized networks have been distinct research areas. We examine
binarization difficulties in a quantization framework and find that all we need
to enable the binary training are a symmetric quantizer, good initialization,
and careful hyperparameter selection. These techniques also lead to substantial
improvements in multi-bit quantization. We demonstrate our unified quantization
framework, denoted as UniQ, on the ImageNet dataset with various architectures
such as ResNet-18,-34 and MobileNetV2. For multi-bit quantization, UniQ
outperforms existing methods to achieve the state-of-the-art accuracy. In
binarization, the achieved accuracy is comparable to existing state-of-the-art
methods even without modifying the original architectures.
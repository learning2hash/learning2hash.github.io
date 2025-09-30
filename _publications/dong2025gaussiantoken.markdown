---
layout: publication
title: 'Gaussiantoken: An Effective Image Tokenizer With 2D Gaussian Splatting'
authors: Jiajun Dong, Chengkun Wang, Wenzhao Zheng, Lei Chen, Jiwen Lu, Yansong Tang
conference: Arxiv
year: 2025
bibkey: dong2025gaussiantoken
citations: 0
additional_links: [{name: Code, url: 'https://github.com/ChrisDong-THU/GaussianToken'},
  {name: Paper, url: 'https://arxiv.org/abs/2501.15619'}]
tags: ["Quantization", "Tools & Libraries"]
short_authors: Dong et al.
---
Effective image tokenization is crucial for both multi-modal understanding
and generation tasks due to the necessity of the alignment with discrete text
data. To this end, existing approaches utilize vector quantization (VQ) to
project pixels onto a discrete codebook and reconstruct images from the
discrete representation. However, compared with the continuous latent space,
the limited discrete codebook space significantly restrict the representational
ability of these image tokenizers. In this paper, we propose GaussianToken: An
Effective Image Tokenizer with 2D Gaussian Splatting as a solution. We first
represent the encoded samples as multiple flexible featured 2D Gaussians
characterized by positions, rotation angles, scaling factors, and feature
coefficients. We adopt the standard quantization for the Gaussian features and
then concatenate the quantization results with the other intrinsic Gaussian
parameters before the corresponding splatting operation and the subsequent
decoding module. In general, GaussianToken integrates the local influence of 2D
Gaussian distribution into the discrete space and thus enhances the
representation capability of the image tokenizer. Competitive reconstruction
performances on CIFAR, Mini-ImageNet, and ImageNet-1K demonstrate the
effectiveness of our framework. Our code is available at:
https://github.com/ChrisDong-THU/GaussianToken.
---
layout: publication
title: Factorized Visual Tokenization And Generation
authors: Zechen Bai, Jianxiong Gao, Ziteng Gao, Pichao Wang, Zheng Zhang, Tong He,
  Mike Zheng Shou
conference: Arxiv
year: 2024
bibkey: bai2024factorized
citations: 0
additional_links: [{name: Code, url: 'https://showlab.github.io/FQGAN'}, {name: Paper,
    url: 'https://arxiv.org/abs/2411.16681'}]
tags: []
short_authors: Bai et al.
---
Visual tokenizers are fundamental to image generation. They convert visual
data into discrete tokens, enabling transformer-based models to excel at image
generation. Despite their success, VQ-based tokenizers like VQGAN face
significant limitations due to constrained vocabulary sizes. Simply expanding
the codebook often leads to training instability and diminishing performance
gains, making scalability a critical challenge. In this work, we introduce
Factorized Quantization (FQ), a novel approach that revitalizes VQ-based
tokenizers by decomposing a large codebook into multiple independent
sub-codebooks. This factorization reduces the lookup complexity of large
codebooks, enabling more efficient and scalable visual tokenization. To ensure
each sub-codebook captures distinct and complementary information, we propose a
disentanglement regularization that explicitly reduces redundancy, promoting
diversity across the sub-codebooks. Furthermore, we integrate representation
learning into the training process, leveraging pretrained vision models like
CLIP and DINO to infuse semantic richness into the learned representations.
This design ensures our tokenizer captures diverse semantic levels, leading to
more expressive and disentangled representations. Experiments show that the
proposed FQGAN model substantially improves the reconstruction quality of
visual tokenizers, achieving state-of-the-art performance. We further
demonstrate that this tokenizer can be effectively adapted into auto-regressive
image generation. https://showlab.github.io/FQGAN
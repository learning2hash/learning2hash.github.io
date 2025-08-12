---
layout: publication
title: 'Fast Sign Retrieval Via Sub-band Convolution: An Elementary Extension Of Binary
  Classification'
authors: Fuma Ito, Chihiro Tsutake, Keita Takahashi, Toshiaki Fujii
conference: ITE Transactions on Media Technology and Applications 13 (2025) 242-249
year: 2025
bibkey: ito2025fast
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2504.21632'}]
tags: []
short_authors: Ito et al.
---
To efficiently compress the sign information of images, we address a sign retrieval problem for the block-wise discrete cosine transformation (DCT): reconstruction of the signs of DCT coefficients from their amplitudes. To this end, we propose a fast sign retrieval method on the basis of binary classification machine learning. We first introduce 3D representations of the amplitudes and signs, where we pack amplitudes/signs belonging to the same frequency band into a 2D slice, referred to as the sub-band block. We then retrieve the signs from the 3D amplitudes via binary classification, where each sign is regarded as a binary label. We implement a binary classification algorithm using convolutional neural networks, which are advantageous for efficiently extracting features in the 3D amplitudes. Experimental results demonstrate that our method achieves accurate sign retrieval with an overwhelmingly low computation cost.
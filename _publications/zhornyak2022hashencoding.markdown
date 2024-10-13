---
layout: publication
title: Hashencoding Autoencoding With Multiscale Coordinate Hashing
authors: Zhornyak Lukas, Xu Zhengjie, Tang Haoran, Shi Jianbo
conference: "Arxiv"
year: 2022
bibkey: zhornyak2022hashencoding
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2211.15894"}
tags: ['ARXIV', 'Unsupervised']
---
<p>We present HashEncoding, a novel autoencoding architecture that
leverages a non-parametric multiscale coordinate hash function to
facilitate a per-pixel decoder without convolutions. By leveraging the
space-folding behaviour of hashing functions, HashEncoding allows for an
inherently multiscale embedding space that remains much smaller than the
original image. As a result, the decoder requires very few parameters
compared with decoders in traditional autoencoders, approaching a
non-parametric reconstruction of the original image and allowing for
greater generalizability. Finally, by allowing backpropagation directly
to the coordinate space, we show that HashEncoding can be exploited for
geometric tasks such as optical flow.</p>

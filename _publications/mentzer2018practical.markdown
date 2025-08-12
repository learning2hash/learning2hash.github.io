---
layout: publication
title: Practical Full Resolution Learned Lossless Image Compression
authors: Fabian Mentzer, Eirikur Agustsson, Michael Tschannen, Radu Timofte, Luc van
  Gool
conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: mentzer2018practical
citations: 184
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.12817'}]
tags: ["CVPR"]
short_authors: Mentzer et al.
---
We propose the first practical learned lossless image compression system,
L3C, and show that it outperforms the popular engineered codecs, PNG, WebP and
JPEG 2000. At the core of our method is a fully parallelizable hierarchical
probabilistic model for adaptive entropy coding which is optimized end-to-end
for the compression task. In contrast to recent autoregressive discrete
probabilistic models such as PixelCNN, our method i) models the image
distribution jointly with learned auxiliary representations instead of
exclusively modeling the image distribution in RGB space, and ii) only requires
three forward-passes to predict all pixel probabilities instead of one for each
pixel. As a result, L3C obtains over two orders of magnitude speedups when
sampling compared to the fastest PixelCNN variant (Multiscale-PixelCNN).
Furthermore, we find that learning the auxiliary representation is crucial and
outperforms predefined auxiliary representations such as an RGB pyramid
significantly.
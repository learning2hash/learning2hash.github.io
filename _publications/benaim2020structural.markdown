---
layout: publication
title: Structural-analogy From A Single Image Pair
authors: Sagie Benaim, Ron Mokady, Amit Bermano, Daniel Cohen-Or, Lior Wolf
conference: Computer Graphics Forum
year: 2020
bibkey: benaim2020structural
citations: 18
additional_links: [{name: Code, url: 'https://github.com/rmokady/structural-analogy/'},
  {name: Paper, url: 'https://arxiv.org/abs/2004.02222'}]
tags: []
short_authors: Benaim et al.
---
The task of unsupervised image-to-image translation has seen substantial
advancements in recent years through the use of deep neural networks.
Typically, the proposed solutions learn the characterizing distribution of two
large, unpaired collections of images, and are able to alter the appearance of
a given image, while keeping its geometry intact. In this paper, we explore the
capabilities of neural networks to understand image structure given only a
single pair of images, A and B. We seek to generate images that are
structurally aligned: that is, to generate an image that keeps the appearance
and style of B, but has a structural arrangement that corresponds to A. The key
idea is to map between image patches at different scales. This enables
controlling the granularity at which analogies are produced, which determines
the conceptual distinction between style and content. In addition to structural
alignment, our method can be used to generate high quality imagery in other
conditional generation tasks utilizing images A and B only: guided image
synthesis, style and texture transfer, text translation as well as video
translation. Our code and additional results are available in
https://github.com/rmokady/structural-analogy/.
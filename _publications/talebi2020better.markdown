---
layout: publication
title: Better Compression With Deep Pre-editing
authors: Hossein Talebi, Damien Kelly, Xiyang Luo, Ignacio Garcia Dorado, Feng Yang,
  Peyman Milanfar, Michael Elad
conference: IEEE Transactions on Image Processing
year: 2021
bibkey: talebi2020better
citations: 28
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.00113'}]
tags: []
short_authors: Talebi et al.
---
Could we compress images via standard codecs while avoiding visible
artifacts? The answer is obvious -- this is doable as long as the bit budget is
generous enough. What if the allocated bit-rate for compression is
insufficient? Then unfortunately, artifacts are a fact of life. Many attempts
were made over the years to fight this phenomenon, with various degrees of
success. In this work we aim to break the unholy connection between bit-rate
and image quality, and propose a way to circumvent compression artifacts by
pre-editing the incoming image and modifying its content to fit the given bits.
We design this editing operation as a learned convolutional neural network, and
formulate an optimization problem for its training. Our loss takes into account
a proximity between the original image and the edited one, a bit-budget penalty
over the proposed image, and a no-reference image quality measure for forcing
the outcome to be visually pleasing. The proposed approach is demonstrated on
the popular JPEG compression, showing savings in bits and/or improvements in
visual quality, obtained with intricate editing effects.
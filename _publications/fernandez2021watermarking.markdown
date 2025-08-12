---
layout: publication
title: Watermarking Images In Self-supervised Latent Spaces
authors: "Pierre Fernandez, Alexandre Sablayrolles, Teddy Furon, Herv\xE9 J\xE9gou,\
  \ Matthijs Douze"
conference: ICASSP 2022 - 2022 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2022
bibkey: fernandez2021watermarking
citations: 30
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.09581'}]
tags: ["ICASSP", "Self-Supervised"]
short_authors: Fernandez et al.
---
We revisit watermarking techniques based on pre-trained deep networks, in the
light of self-supervised approaches. We present a way to embed both marks and
binary messages into their latent spaces, leveraging data augmentation at
marking time. Our method can operate at any resolution and creates watermarks
robust to a broad range of transformations (rotations, crops, JPEG, contrast,
etc). It significantly outperforms the previous zero-bit methods, and its
performance on multi-bit watermarking is on par with state-of-the-art
encoder-decoder architectures trained end-to-end for watermarking. The code is
available at github.com/facebookresearch/ssl_watermarking
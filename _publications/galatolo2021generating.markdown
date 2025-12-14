---
layout: publication
title: Generating Images From Caption And Vice Versa Via Clip-guided Generative Latent
  Space Search
authors: Federico A. Galatolo, Mario G. C. A. Cimino, Gigliola Vaglini
conference: Proceedings of the International Conference on Image Processing and Vision
  Engineering
year: 2021
bibkey: galatolo2021generating
citations: 41
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.01645'}]
tags: [Tools & Libraries, Few-shot & Zero-shot]
short_authors: Federico A. Galatolo, Mario G. C. A. Cimino, Gigliola Vaglini
---
In this research work we present CLIP-GLaSS, a novel zero-shot framework to
generate an image (or a caption) corresponding to a given caption (or image).
CLIP-GLaSS is based on the CLIP neural network, which, given an image and a
descriptive caption, provides similar embeddings. Differently, CLIP-GLaSS takes
a caption (or an image) as an input, and generates the image (or the caption)
whose CLIP embedding is the most similar to the input one. This optimal image
(or caption) is produced via a generative network, after an exploration by a
genetic algorithm. Promising results are shown, based on the experimentation of
the image Generators BigGAN and StyleGAN2, and of the text Generator GPT2
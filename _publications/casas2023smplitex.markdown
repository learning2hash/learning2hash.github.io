---
layout: publication
title: 'Smplitex: A Generative Model And Dataset For 3D Human Texture Estimation From
  Single Image'
authors: Dan Casas, Marc Comino-Trinidad
conference: Arxiv
year: 2023
bibkey: casas2023smplitex
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.01855'}]
tags: ["Datasets"]
short_authors: Dan Casas, Marc Comino-Trinidad
---
We propose SMPLitex, a method for estimating and manipulating the complete 3D
appearance of humans captured from a single image. SMPLitex builds upon the
recently proposed generative models for 2D images, and extends their use to the
3D domain through pixel-to-surface correspondences computed on the input image.
To this end, we first train a generative model for complete 3D human
appearance, and then fit it into the input image by conditioning the generative
model to the visible parts of the subject. Furthermore, we propose a new
dataset of high-quality human textures built by sampling SMPLitex conditioned
on subject descriptions and images. We quantitatively and qualitatively
evaluate our method in 3 publicly available datasets, demonstrating that
SMPLitex significantly outperforms existing methods for human texture
estimation while allowing for a wider variety of tasks such as editing,
synthesis, and manipulation
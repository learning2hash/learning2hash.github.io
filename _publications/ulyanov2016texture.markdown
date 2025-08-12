---
layout: publication
title: 'Texture Networks: Feed-forward Synthesis Of Textures And Stylized Images'
authors: Dmitry Ulyanov, Vadim Lebedev, Andrea Vedaldi, Victor Lempitsky
conference: Arxiv
year: 2016
bibkey: ulyanov2016texture
citations: 558
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1603.03417'}]
tags: ["Efficiency", "Image Retrieval"]
short_authors: Ulyanov et al.
---
Gatys et al. recently demonstrated that deep networks can generate beautiful
textures and stylized images from a single texture example. However, their
methods requires a slow and memory-consuming optimization process. We propose
here an alternative approach that moves the computational burden to a learning
stage. Given a single example of a texture, our approach trains compact
feed-forward convolutional networks to generate multiple samples of the same
texture of arbitrary size and to transfer artistic style from a given image to
any other image. The resulting networks are remarkably light-weight and can
generate textures of quality comparable to Gatys~et~al., but hundreds of times
faster. More generally, our approach highlights the power and flexibility of
generative feed-forward models trained with complex and expressive loss
functions.
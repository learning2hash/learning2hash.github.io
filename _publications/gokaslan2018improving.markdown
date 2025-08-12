---
layout: publication
title: Improving Shape Deformation In Unsupervised Image-to-image Translation
authors: Aaron Gokaslan, Vivek Ramanujan, Daniel Ritchie, Kwang In Kim, James Tompkin
conference: Lecture Notes in Computer Science
year: 2018
bibkey: gokaslan2018improving
citations: 79
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1808.04325'}]
tags: ["Unsupervised"]
short_authors: Gokaslan et al.
---
Unsupervised image-to-image translation techniques are able to map local
texture between two domains, but they are typically unsuccessful when the
domains require larger shape change. Inspired by semantic segmentation, we
introduce a discriminator with dilated convolutions that is able to use
information from across the entire image to train a more context-aware
generator. This is coupled with a multi-scale perceptual loss that is better
able to represent error in the underlying shape of objects. We demonstrate that
this design is more capable of representing shape deformation in a challenging
toy dataset, plus in complex mappings with significant dataset variation
between humans, dolls, and anime faces, and between cats and dogs.
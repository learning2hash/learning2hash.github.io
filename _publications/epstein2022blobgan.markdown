---
layout: publication
title: 'Blobgan: Spatially Disentangled Scene Representations'
authors: Dave Epstein, Taesung Park, Richard Zhang, Eli Shechtman, Alexei A. Efros
conference: Lecture Notes in Computer Science
year: 2022
bibkey: epstein2022blobgan
citations: 26
additional_links: [{name: Code, url: 'https://www.dave.ml/blobgan'}, {name: Paper,
    url: 'https://arxiv.org/abs/2205.02837'}]
tags: []
short_authors: Epstein et al.
---
We propose an unsupervised, mid-level representation for a generative model
of scenes. The representation is mid-level in that it is neither per-pixel nor
per-image; rather, scenes are modeled as a collection of spatial, depth-ordered
"blobs" of features. Blobs are differentiably placed onto a feature grid that
is decoded into an image by a generative adversarial network. Due to the
spatial uniformity of blobs and the locality inherent to convolution, our
network learns to associate different blobs with different entities in a scene
and to arrange these blobs to capture scene layout. We demonstrate this
emergent behavior by showing that, despite training without any supervision,
our method enables applications such as easy manipulation of objects within a
scene (e.g., moving, removing, and restyling furniture), creation of feasible
scenes given constraints (e.g., plausible rooms with drawers at a particular
location), and parsing of real-world images into constituent parts. On a
challenging multi-category dataset of indoor scenes, BlobGAN outperforms
StyleGAN2 in image quality as measured by FID. See our project page for video
results and interactive demo: https://www.dave.ml/blobgan
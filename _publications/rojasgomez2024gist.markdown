---
layout: publication
title: 'GIST: Towards Photorealistic Style Transfer Via Multiscale Geometric Representations'
authors: Renan A. Rojas-Gomez, Minh N. Do
conference: Arxiv
year: 2024
bibkey: rojasgomez2024gist
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.02214'}]
tags: []
short_authors: Renan A. Rojas-Gomez, Minh N. Do
---
State-of-the-art Style Transfer methods often leverage pre-trained encoders
optimized for discriminative tasks, which may not be ideal for image synthesis.
This can result in significant artifacts and loss of photorealism. Motivated by
the ability of multiscale geometric image representations to capture
fine-grained details and global structure, we propose GIST: Geometric-based
Image Style Transfer, a novel Style Transfer technique that exploits the
geometric properties of content and style images. GIST replaces the standard
Neural Style Transfer autoencoding framework with a multiscale image expansion,
preserving scene details without the need for post-processing or training. Our
method matches multiresolution and multidirectional representations such as
Wavelets and Contourlets by solving an optimal transport problem, leading to an
efficient texture transferring. Experiments show that GIST is on-par or
outperforms recent photorealistic Style Transfer approaches while significantly
reducing the processing time with no model training.
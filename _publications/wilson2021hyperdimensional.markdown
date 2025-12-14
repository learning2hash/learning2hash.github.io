---
layout: publication
title: Hyperdimensional Feature Fusion For Out-of-distribution Detection
authors: "Samuel Wilson, Tobias Fischer, Niko S\xFCnderhauf, Feras Dayoub"
conference: 2023 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2021
bibkey: wilson2021hyperdimensional
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.05341'}]
tags: [Distance Metric Learning, Evaluation]
short_authors: Wilson et al.
---
We introduce powerful ideas from Hyperdimensional Computing into the
challenging field of Out-of-Distribution (OOD) detection. In contrast to most
existing work that performs OOD detection based on only a single layer of a
neural network, we use similarity-preserving semi-orthogonal projection
matrices to project the feature maps from multiple layers into a common vector
space. By repeatedly applying the bundling operation \(\oplus\), we create
expressive class-specific descriptor vectors for all in-distribution classes.
At test time, a simple and efficient cosine similarity calculation between
descriptor vectors consistently identifies OOD samples with better performance
than the current state-of-the-art. We show that the hyperdimensional fusion of
multiple network layers is critical to achieve best general performance.
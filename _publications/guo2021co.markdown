---
layout: publication
title: 'CO-SNE: Dimensionality Reduction And Visualization For Hyperbolic Data'
authors: Yunhui Guo, Haoran Guo, Stella Yu
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: guo2021co
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.15037'}]
tags: ["CVPR"]
short_authors: Yunhui Guo, Haoran Guo, Stella Yu
---
Hyperbolic space can naturally embed hierarchies that often exist in
real-world data and semantics. While high-dimensional hyperbolic embeddings
lead to better representations, most hyperbolic models utilize low-dimensional
embeddings, due to non-trivial optimization and visualization of
high-dimensional hyperbolic data.
  We propose CO-SNE, which extends the Euclidean space visualization tool,
t-SNE, to hyperbolic space. Like t-SNE, it converts distances between data
points to joint probabilities and tries to minimize the Kullback-Leibler
divergence between the joint probabilities of high-dimensional data \\(X\\) and
low-dimensional embedding \\(Y\\). However, unlike Euclidean space, hyperbolic
space is inhomogeneous: A volume could contain a lot more points at a location
far from the origin. CO-SNE thus uses hyperbolic normal distributions for \\(X\\)
and hyperbolic \underline\{C\}auchy instead of t-SNE's Student's t-distribution
for \\(Y\\), and it additionally seeks to preserve \\(X\\)'s individual distances to
the \underline\{O\}rigin in \\(Y\\).
  We apply CO-SNE to naturally hyperbolic data and supervisedly learned
hyperbolic features. Our results demonstrate that CO-SNE deflates
high-dimensional hyperbolic data into a low-dimensional space without losing
their hyperbolic characteristics, significantly outperforming popular
visualization tools such as PCA, t-SNE, UMAP, and HoroPCA which is also
designed for hyperbolic data.
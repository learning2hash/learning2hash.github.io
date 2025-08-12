---
layout: publication
title: Learning Canonical Embeddings For Unsupervised Shape Correspondence With Locally
  Linear Transformations
authors: Pan He, Patrick Emami, Sanjay Ranka, Anand Rangarajan
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2023
bibkey: he2022learning
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.02152'}]
tags: ["Unsupervised"]
short_authors: He et al.
---
We present a new approach to unsupervised shape correspondence learning
between pairs of point clouds. We make the first attempt to adapt the classical
locally linear embedding algorithm (LLE) -- originally designed for nonlinear
dimensionality reduction -- for shape correspondence. The key idea is to find
dense correspondences between shapes by first obtaining high-dimensional
neighborhood-preserving embeddings of low-dimensional point clouds and
subsequently aligning the source and target embeddings using locally linear
transformations. We demonstrate that learning the embedding using a new
LLE-inspired point cloud reconstruction objective results in accurate shape
correspondences. More specifically, the approach comprises an end-to-end
learnable framework of extracting high-dimensional neighborhood-preserving
embeddings, estimating locally linear transformations in the embedding space,
and reconstructing shapes via divergence measure-based alignment of
probabilistic density functions built over reconstructed and target shapes. Our
approach enforces embeddings of shapes in correspondence to lie in the same
universal/canonical embedding space, which eventually helps regularize the
learning process and leads to a simple nearest neighbors approach between shape
embeddings for finding reliable correspondences. Comprehensive experiments show
that the new method makes noticeable improvements over state-of-the-art
approaches on standard shape correspondence benchmark datasets covering both
human and nonhuman shapes.
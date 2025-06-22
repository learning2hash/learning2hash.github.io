---
layout: publication
title: Givens Coordinate Descent Methods For Rotation Matrix Learning In Trainable
  Embedding Indexes
authors: Yunjiang Jiang et al.
conference: The Tenth International Conference on Learning Representations (ICLR 2022)
year: 2022
citations: 1
bibkey: jiang2022givens
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.05082'}]
tags: [ANN Search, Quantization]
---
Product quantization (PQ) coupled with a space rotation, is widely used in
modern approximate nearest neighbor (ANN) search systems to significantly
compress the disk storage for embeddings and speed up the inner product
computation. Existing rotation learning methods, however, minimize quantization
distortion for fixed embeddings, which are not applicable to an end-to-end
training scenario where embeddings are updated constantly. In this paper, based
on geometric intuitions from Lie group theory, in particular the special
orthogonal group \\(SO(n)\\), we propose a family of block Givens coordinate
descent algorithms to learn rotation matrix that are provably convergent on any
convex objectives. Compared to the state-of-the-art SVD method, the Givens
algorithms are much more parallelizable, reducing runtime by orders of
magnitude on modern GPUs, and converge more stably according to experimental
studies. They further improve upon vanilla product quantization significantly
in an end-to-end training scenario.
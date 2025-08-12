---
layout: publication
title: Layered Image Vectorization Via Semantic Simplification
authors: Zhenyu Wang, Jianxi Huang, Zhida Sun, Yuanhao Gong, Daniel Cohen-Or, Min
  Lu
conference: Arxiv
year: 2024
bibkey: wang2024layered
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.05404'}]
tags: []
short_authors: Wang et al.
---
This work presents a progressive image vectorization technique that
reconstructs the raster image as layer-wise vectors from semantic-aligned macro
structures to finer details. Our approach introduces a new image simplification
method leveraging the feature-average effect in the Score Distillation Sampling
mechanism, achieving effective visual abstraction from the detailed to coarse.
Guided by the sequence of progressive simplified images, we propose a two-stage
vectorization process of structural buildup and visual refinement, constructing
the vectors in an organized and manageable manner. The resulting vectors are
layered and well-aligned with the target image's explicit and implicit semantic
structures. Our method demonstrates high performance across a wide range of
images. Comparative analysis with existing vectorization methods highlights our
technique's superiority in creating vectors with high visual fidelity, and more
importantly, achieving higher semantic alignment and more compact layered
representation. The project homepage is
https://szuviz.github.io/layered_vectorization/.
---
layout: publication
title: 'Robust Hashing For Multi-view Data: Jointly Learning Low-rank Kernelized Similarity
  Consensus And Hash Functions'
authors: Lin Wu, Yang Wang
conference: Image and Vision Computing
year: 2016
bibkey: wu2016robust
citations: 49
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1611.05521'}]
tags: ["Hashing Methods", "Robustness", "Similarity Search"]
short_authors: Lin Wu, Yang Wang
---
Learning hash functions/codes for similarity search over multi-view data is
attracting increasing attention, where similar hash codes are assigned to the
data objects characterizing consistently neighborhood relationship across
views. Traditional methods in this category inherently suffer three
limitations: 1) they commonly adopt a two-stage scheme where similarity matrix
is first constructed, followed by a subsequent hash function learning; 2) these
methods are commonly developed on the assumption that data samples with
multiple representations are noise-free,which is not practical in real-life
applications; 3) they often incur cumbersome training model caused by the
neighborhood graph construction using all \\(N\\) points in the database (\\(O(N)\\)).
In this paper, we motivate the problem of jointly and efficiently training the
robust hash functions over data objects with multi-feature representations
which may be noise corrupted. To achieve both the robustness and training
efficiency, we propose an approach to effectively and efficiently learning
low-rank kernelized \footnote\{We use kernelized similarity rather than kernel,
as it is not a squared symmetric matrix for data-landmark affinity matrix.\}
hash functions shared across views. Specifically, we utilize landmark graphs to
construct tractable similarity matrices in multi-views to automatically
discover neighborhood structure in the data. To learn robust hash functions, a
latent low-rank kernel function is used to construct hash functions in order to
accommodate linearly inseparable data. In particular, a latent kernelized
similarity matrix is recovered by rank minimization on multiple kernel-based
similarity matrices. Extensive experiments on real-world multi-view datasets
validate the efficacy of our method in the presence of error corruptions.
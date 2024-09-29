---
layout: publication
title: Robust Hashing For Multi45;view Data Jointly Learning Low45;rank Kernelized Similarity Consensus And Hash Functions
authors: Wu Lin, Wang Yang
conference: "Arxiv"
year: 2016
bibkey: wu2016robust
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1611.05521"}
tags: ['ARXIV', 'Graph', 'Independent']
---
Learning hash functions/codes for similarity search over multi45;view data is attracting increasing attention where similar hash codes are assigned to the data objects characterizing consistently neighborhood relationship across views. Traditional methods in this category inherently suffer three limitations 1) they commonly adopt a two45;stage scheme where similarity matrix is first constructed followed by a subsequent hash function learning; 2) these methods are commonly developed on the assumption that data samples with multiple representations are noise45;freewhich is not practical in real45;life applications; 3) they often incur cumbersome training model caused by the neighborhood graph construction using all N points in the database (O(N)). In this paper we motivate the problem of jointly and efficiently training the robust hash functions over data objects with multi45;feature representations which may be noise corrupted. To achieve both the robustness and training efficiency we propose an approach to effectively and efficiently learning low45;rank kernelized footnote123;We use kernelized similarity rather than kernel as it is not a squared symmetric matrix for data45;landmark affinity matrix.125; hash functions shared across views. Specifically we utilize landmark graphs to construct tractable similarity matrices in multi45;views to automatically discover neighborhood structure in the data. To learn robust hash functions a latent low45;rank kernel function is used to construct hash functions in order to accommodate linearly inseparable data. In particular a latent kernelized similarity matrix is recovered by rank minimization on multiple kernel45;based similarity matrices. Extensive experiments on real45;world multi45;view datasets validate the efficacy of our method in the presence of error corruptions.

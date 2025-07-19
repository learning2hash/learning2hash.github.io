---
layout: publication
title: Cluster-wise Unsupervised Hashing for Cross-Modal Similarity Search
authors: Wang Lu, Yang Jie
conference: Pattern Recognition
year: 2020
bibkey: wang2020cluster
citations: 25
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.07923'}]
tags: [Supervised, CVPR, Neural Hashing, Unsupervised, Similarity Search, Hashing
    Methods]
---
Large-scale cross-modal hashing similarity retrieval has attracted more and
more attention in modern search applications such as search engines and
autopilot, showing great superiority in computation and storage. However,
current unsupervised cross-modal hashing methods still have some limitations:
(1)many methods relax the discrete constraints to solve the optimization
objective which may significantly degrade the retrieval performance;(2)most
existing hashing model project heterogenous data into a common latent space,
which may always lose sight of diversity in heterogenous data;(3)transforming
real-valued data point to binary codes always results in abundant loss of
information, producing the suboptimal continuous latent space. To overcome
above problems, in this paper, a novel Cluster-wise Unsupervised Hashing (CUH)
method is proposed. Specifically, CUH jointly performs the multi-view
clustering that projects the original data points from different modalities
into its own low-dimensional latent semantic space and finds the cluster
centroid points and the common clustering indicators in its own low-dimensional
space, and learns the compact hash codes and the corresponding linear hash
functions. An discrete optimization framework is developed to learn the unified
binary codes across modalities under the guidance cluster-wise code-prototypes.
The reasonableness and effectiveness of CUH is well demonstrated by
comprehensive experiments on diverse benchmark datasets.
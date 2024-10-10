---
layout: publication
title: Minimizing Flops To Learn Efficient Sparse Representations
authors: Paria Biswajit, Yeh Chih-kuan, Yen Ian E. H., Xu Ning, Ravikumar Pradeep, Póczos Barnabás
conference: "Arxiv"
year: 2020
bibkey: paria2020minimizing
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2004.05665"}
tags: ['ARXIV', 'Quantisation', 'Unsupervised']
---
Deep representation learning has become one of the most widely adopted approaches for visual search recommendation and identification. Retrieval of such representations from a large database is however computationally challenging. Approximate methods based on learning compact representations have been widely explored for this problem such as locality sensitive hashing product quantization and PCA. In this work in contrast to learning compact representations we propose to learn high dimensional and sparse representations that have similar representational capacity as dense embeddings while being more efficient due to sparse matrix multiplication operations which can be much faster than dense multiplication. Following the key insight that the number of operations decreases quadratically with the sparsity of embeddings provided the non-zero entries are distributed uniformly across dimensions we propose a novel approach to learn such distributed sparse embeddings via the use of a carefully constructed regularization function that directly minimizes a continuous relaxation of the number of floating-point operations (FLOPs) incurred during retrieval. Our experiments show that our approach is competitive to the other baselines and yields a similar or better speed-vs-accuracy tradeoff on practical datasets.

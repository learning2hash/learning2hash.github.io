---
layout: publication
title: Semantically Constrained Memory Allocation (SCMA) For Embedding In Efficient Recommendation Systems
authors: Desai Aditya, Pan Yanzhou, Sun Kuangyuan, Chou Li, Shrivastava Anshumali
conference: "Arxiv"
year: 2021
bibkey: desai2021semantically
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2103.06124"}
tags: ['ARXIV', 'Deep Learning', 'Independent']
---
Deep learning-based models are utilized to achieve state-of-the-art performance for recommendation systems. A key challenge for these models is to work with millions of categorical classes or tokens. The standard approach is to learn end-to-end, dense latent representations or embeddings for each token. The resulting embeddings require large amounts of memory that blow up with the number of tokens. Training and inference with these models create storage, and memory bandwidth bottlenecks leading to significant computing and energy consumption when deployed in practice. To this end, we present the problem of \textit\{Memory Allocation\} under budget for embeddings and propose a novel formulation of memory shared embedding, where memory is shared in proportion to the overlap in semantic information. Our formulation admits a practical and efficient randomized solution with Locality sensitive hashing based Memory Allocation (LMA). We demonstrate a significant reduction in the memory footprint while maintaining performance. In particular, our LMA embeddings achieve the same performance compared to standard embeddings with a 16\{\{ '\{\{' \}\}\times\{\{ '\}\}' \}\} reduction in memory footprint. Moreover, LMA achieves an average improvement of over 0.003 AUC across different memory regimes than standard DLRM models on Criteo and Avazu datasets

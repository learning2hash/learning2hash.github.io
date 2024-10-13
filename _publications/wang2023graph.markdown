---
layout: publication
title: Graph-collaborated Auto-encoder Hashing For Multi-view Binary Clustering
authors: Wang Huibing, Yao Mingze, Jiang Guangqi, Mi Zetian, Fu Xianping
conference: "Arxiv"
year: 2023
bibkey: wang2023graph
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2301.02484"}
tags: ['ARXIV', 'Cross Modal', 'Graph', 'Quantisation', 'Unsupervised']
---
Unsupervised hashing methods have attracted widespread attention with the
explosive growth of large-scale data, which can greatly reduce storage and
computation by learning compact binary codes. Existing unsupervised hashing
methods attempt to exploit the valuable information from samples, which fails
to take the local geometric structure of unlabeled samples into consideration.
Moreover, hashing based on auto-encoders aims to minimize the reconstruction
loss between the input data and binary codes, which ignores the potential
consistency and complementarity of multiple sources data. To address the above
issues, we propose a hashing algorithm based on auto-encoders for multi-view
binary clustering, which dynamically learns affinity graphs with low-rank
constraints and adopts collaboratively learning between auto-encoders and
affinity graphs to learn a unified binary code, called Graph-Collaborated
Auto-Encoder Hashing for Multi-view Binary Clustering (GCAE). Specifically, we
propose a multi-view affinity graphs learning model with low-rank constraint,
which can mine the underlying geometric information from multi-view data. Then,
we design an encoder-decoder paradigm to collaborate the multiple affinity
graphs, which can learn a unified binary code effectively. Notably, we impose
the decorrelation and code balance constraints on binary codes to reduce the
quantization errors. Finally, we utilize an alternating iterative optimization
scheme to obtain the multi-view clustering results. Extensive experimental
results on \\{5\\} public datasets are provided to reveal the effectiveness of the
algorithm and its superior performance over other state-of-the-art
alternatives.

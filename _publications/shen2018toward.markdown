---
layout: publication
title: 'NASH: Toward End-to-end Neural Architecture For Generative Semantic Hashing'
authors: Dinghan Shen et al.
conference: "Arxiv"
year: 2018
citations: 19
bibkey: shen2018toward
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1805.05361'}
tags: ['Cross-Modal', 'Independent', 'Retrieval Models', 'Shallow', 'Hashing', 'Datasets', 'Training Strategy', 'Supervised Hashing']
---
Semantic hashing has become a powerful paradigm for fast similarity search in
many information retrieval systems. While fairly successful, previous
techniques generally require two-stage training, and the binary constraints are
handled ad-hoc. In this paper, we present an end-to-end Neural Architecture for
Semantic Hashing (NASH), where the binary hashing codes are treated as
Bernoulli latent variables. A neural variational inference framework is
proposed for training, where gradients are directly back-propagated through the
discrete latent variable to optimize the hash function. We also draw
connections between proposed method and rate-distortion theory, which provides
a theoretical foundation for the effectiveness of the proposed framework.
Experimental results on three public datasets demonstrate that our method
significantly outperforms several state-of-the-art models on both unsupervised
and supervised scenarios.

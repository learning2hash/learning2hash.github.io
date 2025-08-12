---
layout: publication
title: Discriminative Embedding Autoencoder With A Regressor Feedback For Zero-shot
  Learning
authors: Ying Shi, Wei Wei, Zhiming Zheng
conference: IEEE Access
year: 2020
bibkey: shi2019discriminative
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1907.08070'}]
tags: []
short_authors: Ying Shi, Wei Wei, Zhiming Zheng
---
Zero-shot learning (ZSL) aims to recognize the novel object categories using
the semantic representation of categories, and the key idea is to explore the
knowledge of how the novel class is semantically related to the familiar
classes. Some typical models are to learn the proper embedding between the
image feature space and the semantic space, whilst it is important to learn
discriminative features and comprise the coarse-to-fine image feature and
semantic information. In this paper, we propose a discriminative embedding
autoencoder with a regressor feedback model for ZSL. The encoder learns a
mapping from the image feature space to the discriminative embedding space,
which regulates both inter-class and intra-class distances between the learned
features by a margin, making the learned features be discriminative for object
recognition. The regressor feedback learns to map the reconstructed samples
back to the the discriminative embedding and the semantic embedding, assisting
the decoder to improve the quality of the samples and provide a generalization
to the unseen classes. The proposed model is validated extensively on four
benchmark datasets: SUN, CUB, AWA1, AWA2, the experiment results show that our
proposed model outperforms the state-of-the-art models, and especially in the
generalized zero-shot learning (GZSL), significant improvements are achieved.
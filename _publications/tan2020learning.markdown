---
layout: publication
title: Learning To Hash With Graph Neural Networks For Recommender Systems
authors: Qiaoyu Tan et al.
conference: Arxiv
year: 2020
citations: 64
bibkey: tan2020learning
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2003.01917'}]
tags: [Deep Hashing, RecSys, Graph and Transformer Models, Loss Functions, Hashing
    Methods]
---
Graph representation learning has attracted much attention in supporting high
quality candidate search at scale. Despite its effectiveness in learning
embedding vectors for objects in the user-item interaction network, the
computational costs to infer users' preferences in continuous embedding space
are tremendous. In this work, we investigate the problem of hashing with graph
neural networks (GNNs) for high quality retrieval, and propose a simple yet
effective discrete representation learning framework to jointly learn
continuous and discrete codes. Specifically, a deep hashing with GNNs (HashGNN)
is presented, which consists of two components, a GNN encoder for learning node
representations, and a hash layer for encoding representations to hash codes.
The whole architecture is trained end-to-end by jointly optimizing two losses,
i.e., reconstruction loss from reconstructing observed links, and ranking loss
from preserving the relative ordering of hash codes. A novel discrete
optimization strategy based on straight through estimator (STE) with guidance
is proposed. The principal idea is to avoid gradient magnification in
back-propagation of STE with continuous embedding guidance, in which we begin
from learning an easier network that mimic the continuous embedding and let it
evolve during the training until it finally goes back to STE. Comprehensive
experiments over three publicly available and one real-world Alibaba company
datasets demonstrate that our model not only can achieve comparable performance
compared with its continuous counterpart but also runs multiple times faster
during inference.
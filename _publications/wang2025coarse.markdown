---
layout: publication
title: Coarse-to-fine Lightweight Meta-embedding For Id-based Recommendation
authors: Yang Wang, Haipeng Liu, Zeqian Yi, Biao Qian, Meng Wang
conference: Arxiv
year: 2025
bibkey: wang2025coarse
citations: 0
additional_links: [{name: Code, url: 'https://github.com/htyjers/C2F-MetaEmbed'},
  {name: Paper, url: 'https://arxiv.org/abs/2501.11870'}]
tags: [Recommender Systems, Robustness]
short_authors: Wang et al.
---
The state-of-the-art recommendation systems have shifted the attention to
efficient recommendation, e.g., on-device recommendation, under memory
constraints. To this end, the existing methods either focused on the
lightweight embeddings for both users and items, or involved on-device systems
enjoying the compact embeddings to enhance reusability and reduces space
complexity. However, they focus solely on the coarse granularity of embedding,
while overlook the fine-grained semantic nuances, to adversarially downgrade
the efficacy of meta-embeddings in capturing the intricate relationship over
both user and item, consequently resulting into the suboptimal recommendations.
In this paper, we aim to study how the meta-embedding can efficiently learn
varied grained semantics, together with how the fine-grained meta-embedding can
strengthen the representation of coarse-grained meta-embedding. To answer these
questions, we develop a novel graph neural networks (GNNs) based recommender
where each user and item serves as the node, linked directly to coarse-grained
virtual nodes and indirectly to fine-grained virtual nodes, ensuring different
grained semantic learning, while disclosing: 1) In contrast to coarse-grained
semantics, fine-grained semantics are well captured through sparse
meta-embeddings, which adaptively 2) balance the embedding uniqueness and
memory constraint. Additionally, the initialization method come up upon
SparsePCA, along with a soft thresholding activation function to render the
sparseness of the meta-embeddings. We propose a weight bridging update strategy
that focuses on matching each coarse-grained meta-embedding with several
fine-grained meta-embeddings based on the users/items' semantics. Extensive
experiments substantiate our method's superiority over existing baselines. Our
code is available at https://github.com/htyjers/C2F-MetaEmbed.
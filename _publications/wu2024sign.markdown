---
layout: publication
title: Sign-guided Bipartite Graph Hashing For Hamming Space Search
authors: Xueyi Wu
conference: Arxiv
year: 2024
citations: 0
bibkey: wu2024sign
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.02716'}]
tags: [Hashing Methods, Graph and Transformer Models, Deep Hashing]
---
Bipartite graph hashing (BGH) is extensively used for Top-K search in Hamming
space at low storage and inference costs. Recent research adopts graph
convolutional hashing for BGH and has achieved the state-of-the-art
performance. However, the contributions of its various influencing factors to
hashing performance have not been explored in-depth, including the
same/different sign count between two binary embeddings during Hamming space
search (sign property), the contribution of sub-embeddings at each layer (model
property), the contribution of different node types in the bipartite graph
(node property), and the combination of augmentation methods. In this work, we
build a lightweight graph convolutional hashing model named LightGCH by mainly
removing the augmentation methods of the state-of-the-art model BGCH. By
analyzing the contributions of each layer and node type to performance, as well
as analyzing the Hamming similarity statistics at each layer, we find that the
actual neighbors in the bipartite graph tend to have low Hamming similarity at
the shallow layer, and all nodes tend to have high Hamming similarity at the
deep layers in LightGCH. To tackle these problems, we propose a novel
sign-guided framework SGBGH to make improvement, which uses sign-guided
negative sampling to improve the Hamming similarity of neighbors, and uses
sign-aware contrastive learning to help nodes learn more uniform
representations. Experimental results show that SGBGH outperforms BGCH and
LightGCH significantly in embedding quality.
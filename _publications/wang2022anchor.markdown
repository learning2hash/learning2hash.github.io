---
layout: publication
title: Anchor Graph Structure Fusion Hashing For Cross-modal Similarity Search
authors: Lu Wang, Jie Yang, Masoumeh Zareapoor, Zhonglong Zheng
conference: Arxiv
year: 2022
citations: 2
bibkey: wang2022anchor
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2202.04327'}]
tags: [Multi-Modal Hashing, Hashing Methods, Efficient Learning]
---
Cross-modal hashing still has some challenges needed to address: (1) most
existing CMH methods take graphs as input to model data distribution. These
methods omit to consider the correlation of graph structure among multiple
modalities; (2) most existing CMH methods ignores considering the fusion
affinity among multi-modalities data; (3) most existing CMH methods relax the
discrete constraints to solve the optimization objective, significantly
degrading the retrieval performance. To solve the above limitations, we propose
a novel Anchor Graph Structure Fusion Hashing (AGSFH). AGSFH constructs the
anchor graph structure fusion matrix from different anchor graphs of multiple
modalities with the Hadamard product, which can fully exploit the geometric
property of underlying data structure. Based on the anchor graph structure
fusion matrix, AGSFH attempts to directly learn an intrinsic anchor graph,
where the structure of the intrinsic anchor graph is adaptively tuned so that
the number of components of the intrinsic graph is exactly equal to the number
of clusters. Besides, AGSFH preserves the anchor fusion affinity into the
common binary Hamming space. Furthermore, a discrete optimization framework is
designed to learn the unified binary codes. Extensive experimental results on
three public social datasets demonstrate the superiority of AGSFH.
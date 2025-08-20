---
layout: publication
title: 'GGNN: Graph-based GPU Nearest Neighbor Search'
authors: Fabian Groh, Lukas Ruppert, Patrick Wieschollek, Hendrik P. A. Lensch
conference: IEEE Transactions on Big Data
year: 2022
bibkey: groh2019ggnn
citations: 34
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.01059'}]
tags: [Vector Indexing, Graph-based ANN, Tools & Libraries, Evaluation]
short_authors: Groh et al.
---
Approximate nearest neighbor (ANN) search in high dimensions is an integral
part of several computer vision systems and gains importance in deep learning
with explicit memory representations. Since PQT, FAISS, and SONG started to
leverage the massive parallelism offered by GPUs, GPU-based implementations are
a crucial resource for today's state-of-the-art ANN methods. While most of
these methods allow for faster queries, less emphasis is devoted to
accelerating the construction of the underlying index structures. In this
paper, we propose a novel GPU-friendly search structure based on nearest
neighbor graphs and information propagation on graphs. Our method is designed
to take advantage of GPU architectures to accelerate the hierarchical
construction of the index structure and for performing the query. Empirical
evaluation shows that GGNN significantly surpasses the state-of-the-art CPU-
and GPU-based systems in terms of build-time, accuracy and search speed.
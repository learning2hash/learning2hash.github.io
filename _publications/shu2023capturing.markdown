---
layout: publication
title: Capturing Fine-grained Semantics In Contrastive Graph Representation Learning
authors: Lin Shu, Chuan Chen, Zibin Zheng
conference: Arxiv
year: 2023
bibkey: shu2023capturing
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.11658'}]
tags: ["Datasets", "Self-Supervised"]
short_authors: Lin Shu, Chuan Chen, Zibin Zheng
---
Graph contrastive learning defines a contrastive task to pull similar
instances close and push dissimilar instances away. It learns discriminative
node embeddings without supervised labels, which has aroused increasing
attention in the past few years. Nevertheless, existing methods of graph
contrastive learning ignore the differences between diverse semantics existed
in graphs, which learn coarse-grained node embeddings and lead to sub-optimal
performances on downstream tasks. To bridge this gap, we propose a novel
Fine-grained Semantics enhanced Graph Contrastive Learning (FSGCL) in this
paper. Concretely, FSGCL first introduces a motif-based graph construction,
which employs graph motifs to extract diverse semantics existed in graphs from
the perspective of input data. Then, the semantic-level contrastive task is
explored to further enhance the utilization of fine-grained semantics from the
perspective of model training. Experiments on five real-world datasets
demonstrate the superiority of our proposed FSGCL over state-of-the-art
methods. To make the results reproducible, we will make our codes public on
GitHub after this paper is accepted.
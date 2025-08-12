---
layout: publication
title: Graph Pooling With Node Proximity For Hierarchical Representation Learning
authors: Xing Gao, Wenrui Dai, Chenglin Li, Hongkai Xiong, Pascal Frossard
conference: Arxiv
year: 2020
bibkey: gao2020graph
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.11118'}]
tags: []
short_authors: Gao et al.
---
Graph neural networks have attracted wide attentions to enable representation
learning of graph data in recent works. In complement to graph convolution
operators, graph pooling is crucial for extracting hierarchical representation
of graph data. However, most recent graph pooling methods still fail to
efficiently exploit the geometry of graph data. In this paper, we propose a
novel graph pooling strategy that leverages node proximity to improve the
hierarchical representation learning of graph data with their multi-hop
topology. Node proximity is obtained by harmonizing the kernel representation
of topology information and node features. Implicit structure-aware kernel
representation of topology information allows efficient graph pooling without
explicit eigendecomposition of the graph Laplacian. Similarities of node
signals are adaptively evaluated with the combination of the affine
transformation and kernel trick using the Gaussian RBF function. Experimental
results demonstrate that the proposed graph pooling strategy is able to achieve
state-of-the-art performance on a collection of public graph classification
benchmark datasets.
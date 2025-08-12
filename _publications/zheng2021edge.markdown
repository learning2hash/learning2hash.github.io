---
layout: publication
title: Edge-labeling Based Directed Gated Graph Network For Few-shot Learning
authors: Peixiao Zheng, Xin Guo, Lin Qi
conference: Arxiv
year: 2021
bibkey: zheng2021edge
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.11299'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Peixiao Zheng, Xin Guo, Lin Qi
---
Existing graph-network-based few-shot learning methods obtain similarity
between nodes through a convolution neural network (CNN). However, the CNN is
designed for image data with spatial information rather than vector form node
feature. In this paper, we proposed an edge-labeling-based directed gated graph
network (DGGN) for few-shot learning, which utilizes gated recurrent units to
implicitly update the similarity between nodes. DGGN is composed of a gated
node aggregation module and an improved gated recurrent unit (GRU) based edge
update module. Specifically, the node update module adopts a gate mechanism
using activation of edge feature, making a learnable node aggregation process.
Besides, improved GRU cells are employed in the edge update procedure to
compute the similarity between nodes. Further, this mechanism is beneficial to
gradient backpropagation through the GRU sequence across layers. Experiment
results conducted on two benchmark datasets show that our DGGN achieves a
comparable performance to the-state-of-art methods.
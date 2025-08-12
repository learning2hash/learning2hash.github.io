---
layout: publication
title: Hierarchical Vector Quantized Graph Autoencoder With Annealing-based Code Selection
authors: Long Zeng, Jianxiang Yu, Jiapeng Zhu, Qingsong Zhong, Xiang Li
conference: Proceedings of the ACM on Web Conference 2025
year: 2025
bibkey: zeng2025hierarchical
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2504.12715'}]
tags: ["Quantization"]
short_authors: Zeng et al.
---
Graph self-supervised learning has gained significant attention recently.
However, many existing approaches heavily depend on perturbations, and
inappropriate perturbations may corrupt the graph's inherent information. The
Vector Quantized Variational Autoencoder (VQ-VAE) is a powerful autoencoder
extensively used in fields such as computer vision; however, its application to
graph data remains underexplored. In this paper, we provide an empirical
analysis of vector quantization in the context of graph autoencoders,
demonstrating its significant enhancement of the model's capacity to capture
graph topology. Furthermore, we identify two key challenges associated with
vector quantization when applying in graph data: codebook underutilization and
codebook space sparsity. For the first challenge, we propose an annealing-based
encoding strategy that promotes broad code utilization in the early stages of
training, gradually shifting focus toward the most effective codes as training
progresses. For the second challenge, we introduce a hierarchical two-layer
codebook that captures relationships between embeddings through clustering. The
second layer codebook links similar codes, encouraging the model to learn
closer embeddings for nodes with similar features and structural topology in
the graph. Our proposed model outperforms 16 representative baseline methods in
self-supervised link prediction and node classification tasks across multiple
datasets.
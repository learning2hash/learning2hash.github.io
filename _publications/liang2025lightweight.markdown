---
layout: publication
title: Lightweight Embeddings With Graph Rewiring For Collaborative Filtering
authors: Xurong Liang, Tong Chen, Wei Yuan, Hongzhi Yin
conference: ACM Transactions on Information Systems
year: 2025
bibkey: liang2025lightweight
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2505.18999'}]
tags: ["Memory Efficiency", "Quantization", "Recommender Systems"]
short_authors: Liang et al.
---
As recommendation services scale rapidly and their deployment now commonly involves resource-constrained edge devices, GNN-based recommender systems face significant challenges, including high embedding storage costs and runtime latency from graph propagations. Our previous work, LEGCF, effectively reduced embedding storage costs but struggled to maintain recommendation performance under stricter storage limits. Additionally, LEGCF did not address the extensive runtime computation costs associated with graph propagation, which involves heavy multiplication and accumulation operations (MACs). These challenges consequently hinder effective training and inference on resource-constrained edge devices. To address these limitations, we propose Lightweight Embeddings with Rewired Graph for Graph Collaborative Filtering (LERG), an improved extension of LEGCF. LERG retains LEGCFs compositional codebook structure but introduces quantization techniques to reduce the storage cost, enabling the inclusion of more meta-embeddings within the same storage. To optimize graph propagation, we pretrain the quantized compositional embedding table using the full interaction graph on resource-rich servers, after which a fine-tuning stage is engaged to identify and prune low-contribution entities via a gradient-free binary integer programming approach, constructing a rewired graph that excludes these entities (i.e., user/item nodes) from propagating signals. The quantized compositional embedding table with selective embedding participation and sparse rewired graph are transferred to edge devices which significantly reduce computation memory and inference time. Experiments on three public benchmark datasets, including an industry-scale dataset, demonstrate that LERG achieves superior recommendation performance while dramatically reducing storage and computation costs for graph-based recommendation services.
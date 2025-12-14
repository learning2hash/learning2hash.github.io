---
layout: publication
title: 'Bang For The Buck: Vector Search On Cloud Cpus'
authors: Leonardo Kuffo, Peter Boncz
conference: Proceedings of the 21st International Workshop on Data Management on New
  Hardware
year: 2025
bibkey: kuffo2025bang
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2505.07621'}]
tags: [Evaluation, Vector Indexing, Graph-based ANN, Quantization]
short_authors: Leonardo Kuffo, Peter Boncz
---
Vector databases have emerged as a new type of systems that support efficient querying of high-dimensional vectors. Many of these offer their database as a service in the cloud. However, the variety of available CPUs and the lack of vector search benchmarks across CPUs make it difficult for users to choose one. In this study, we show that CPU microarchitectures available in the cloud perform significantly differently across vector search scenarios. For instance, in an IVF index on float32 vectors, AMD's Zen4 gives almost 3x more queries per second (QPS) compared to Intel's Sapphire Rapids, but for HNSW indexes, the tables turn. However, when looking at the number of queries per dollar (QP$), Graviton3 is the best option for most indexes and quantization settings, even over Graviton4 (Table 1). With this work, we hope to guide users in getting the best "bang for the buck" when deploying vector search systems.
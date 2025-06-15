---
layout: publication
title: 'VIBE: Vector Index Benchmark For Embeddings'
authors: Elias Jääsaari, Ville Hyvönen, Matteo Ceccarello, Teemu Roos, Martin Aumüller
conference: "Arxiv"
year: 2025
citations: 0
bibkey: jääsaari2025vector
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2505.17810'}
tags: ['Model Design', 'Unsupervised', 'Retrieval Models', 'Unimodal', 'Evaluation', 'Shallow', 'Datasets', 'Vector Indexing', 'Applications']
---
Approximate nearest neighbor (ANN) search is a performance-critical component of many machine learning pipelines. Rigorous benchmarking is essential for evaluating the performance of vector indexes for ANN search. However, the datasets of the existing benchmarks are no longer representative of the current applications of ANN search. Hence, there is an urgent need for an up-to-date set of benchmarks. To this end, we introduce Vector Index Benchmark for Embeddings (VIBE), an open source project for benchmarking ANN algorithms. VIBE contains a pipeline for creating benchmark datasets using dense embedding models characteristic of modern applications, such as retrieval-augmented generation (RAG). To replicate real-world workloads, we also include out-of-distribution (OOD) datasets where the queries and the corpus are drawn from different distributions. We use VIBE to conduct a comprehensive evaluation of SOTA vector indexes, benchmarking 21 implementations on 12 in-distribution and 6 out-of-distribution datasets.

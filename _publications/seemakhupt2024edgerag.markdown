---
layout: publication
title: 'Edgerag: Online-indexed RAG For Edge Devices'
authors: Seemakhupt Korakit, Liu Sihang, Khan Samira
conference: Arxiv
year: 2024
bibkey: seemakhupt2024edgerag
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.21023'}]
tags: ["Efficiency", "Scalability", "Vector Indexing"]
short_authors: Seemakhupt Korakit, Liu Sihang, Khan Samira
---
Deploying Retrieval Augmented Generation (RAG) on resource-constrained edge
devices is challenging due to limited memory and processing power. In this
work, we propose EdgeRAG which addresses the memory constraint by pruning
embeddings within clusters and generating embeddings on-demand during
retrieval. To avoid the latency of generating embeddings for large tail
clusters, EdgeRAG pre-computes and stores embeddings for these clusters, while
adaptively caching remaining embeddings to minimize redundant computations and
further optimize latency. The result from BEIR suite shows that EdgeRAG offers
significant latency reduction over the baseline IVF index, but with similar
generation quality while allowing all of our evaluated datasets to fit into the
memory.
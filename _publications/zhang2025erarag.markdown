---
layout: publication
title: 'Erarag: Efficient And Incremental Retrieval Augmented Generation For Growing
  Corpora'
authors: Fangyuan Zhang, Zhengjun Huang, Yingli Zhou, Qintian Guo, Zhixun Li, Wensheng
  Luo, di Jiang, Yixiang Fang, Xiaofang Zhou
conference: Arxiv
year: 2025
bibkey: zhang2025erarag
citations: 0
additional_links: [{name: Code, url: 'https://github.com/EverM0re/EraRAG-Official'},
  {name: Paper, url: 'https://arxiv.org/abs/2506.20963'}]
tags: ["Efficiency", "Graph Based ANN", "Hashing Methods", "Locality-Sensitive-Hashing", "Scalability"]
short_authors: Zhang et al.
---
Graph-based Retrieval-Augmented Generation (Graph-RAG) enhances large language models (LLMs) by structuring retrieval over an external corpus. However, existing approaches typically assume a static corpus, requiring expensive full-graph reconstruction whenever new documents arrive, limiting their scalability in dynamic, evolving environments. To address these limitations, we introduce EraRAG, a novel multi-layered Graph-RAG framework that supports efficient and scalable dynamic updates. Our method leverages hyperplane-based Locality-Sensitive Hashing (LSH) to partition and organize the original corpus into hierarchical graph structures, enabling efficient and localized insertions of new data without disrupting the existing topology. The design eliminates the need for retraining or costly recomputation while preserving high retrieval accuracy and low latency. Experiments on large-scale benchmarks demonstrate that EraRag achieves up to an order of magnitude reduction in update time and token consumption compared to existing Graph-RAG systems, while providing superior accuracy performance. This work offers a practical path forward for RAG systems that must operate over continually growing corpora, bridging the gap between retrieval efficiency and adaptability. Our code and data are available at https://github.com/EverM0re/EraRAG-Official.
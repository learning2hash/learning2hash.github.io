---
layout: publication
title: 'ESPN: Memory-efficient Multi-vector Information Retrieval'
authors: Susav Shrestha, Narasimha Reddy, Zongwang Li
conference: Proceedings of the 2024 ACM SIGPLAN International Symposium on Memory
  Management
year: 2024
bibkey: shrestha2023espn
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.05417'}]
tags: [Similarity Search, Scalability, Hybrid ANN Methods, Re-ranking]
short_authors: Susav Shrestha, Narasimha Reddy, Zongwang Li
---
Recent advances in large language models have demonstrated remarkable
effectiveness in information retrieval (IR) tasks. While many neural IR systems
encode queries and documents into single-vector representations, multi-vector
models elevate the retrieval quality by producing multi-vector representations
and facilitating similarity searches at the granularity of individual tokens.
However, these models significantly amplify memory and storage requirements for
retrieval indices by an order of magnitude. This escalation in index size
renders the scalability of multi-vector IR models progressively challenging due
to their substantial memory demands. We introduce Embedding from Storage
Pipelined Network (ESPN) where we offload the entire re-ranking embedding
tables to SSDs and reduce the memory requirements by 5-16x. We design a
software prefetcher with hit rates exceeding 90%, improving SSD based retrieval
up to 6.4x, and demonstrate that we can maintain near memory levels of query
latency even for large query batch sizes.
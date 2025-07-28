---
layout: publication
title: 'Hashevict: A Pre-attention KV Cache Eviction Strategy Using Locality-sensitive
  Hashing'
authors: "Minghui Liu, Tahseen Rabbani, Tony O'halloran, Ananth Sankaralingam, Mary-anne\
  \ Hartley, Furong Huang, Cornelia Ferm\xFCller, Yiannis Aloimonos"
conference: Arxiv
year: 2024
bibkey: liu2024hashevict
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.16187'}]
tags: ["Hashing Methods", "Locality Sensitive Hashing"]
short_authors: Liu et al.
---
Transformer-based large language models (LLMs) use the key-value (KV) cache to significantly accelerate inference by storing the key and value embeddings of past tokens. However, this cache consumes significant GPU memory. In this work, we introduce HashEvict, an algorithm that uses locality-sensitive hashing (LSH) to compress the KV cache. HashEvict quickly locates tokens in the cache that are cosine dissimilar to the current query token. This is achieved by computing the Hamming distance between binarized Gaussian projections of the current token query and cached token keys, with a projection length much smaller than the embedding dimension. We maintain a lightweight binary structure in GPU memory to facilitate these calculations. Unlike existing compression strategies that compute attention to determine token retention, HashEvict makes these decisions pre-attention, thereby reducing computational costs. Additionally, HashEvict is dynamic - at every decoding step, the key and value of the current token replace the embeddings of a token expected to produce the lowest attention score. We demonstrate that HashEvict can compress the KV cache by 30%-70% while maintaining high performance across reasoning, multiple-choice, long-context retrieval and summarization tasks.
---
layout: publication
title: 'Dresd: Dense Retrieval For Speculative Decoding'
authors: Milan Gritta, Huiyin Xue, Gerasimos Lampouras
conference: 'Findings of the Association for Computational Linguistics: ACL 2025'
year: 2025
bibkey: gritta2025dresd
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.15572'}]
tags: ["Scalability", "Similarity Search", "Tools & Libraries"]
short_authors: Milan Gritta, Huiyin Xue, Gerasimos Lampouras
---
Speculative decoding (SD) accelerates Large Language Model (LLM) generation by using an efficient draft model to propose the next few tokens, which are verified by the LLM in a single forward call, reducing latency while preserving its outputs. We focus on retrieval-based SD where the draft model retrieves the next tokens from a non-parametric datastore. Sparse retrieval (REST), which operates on the surface form of strings, is currently the dominant paradigm due to its simplicity and scalability. However, its effectiveness is limited due to the usage of short contexts and exact string matching. Instead, we introduce Dense Retrieval for Speculative Decoding (DReSD), a novel framework that uses approximate nearest neighbour search with contextualised token embeddings to retrieve the most semantically relevant token sequences for SD. Extensive experiments show that DReSD achieves (on average) 87% higher acceptance rates, 65% longer accepted tokens and 19% faster generation speeds compared to sparse retrieval (REST).
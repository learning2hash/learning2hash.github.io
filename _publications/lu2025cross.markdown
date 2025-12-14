---
layout: publication
title: Cross-encoder Rediscovers A Semantic Variant Of BM25
authors: Meng Lu, Catherine Chen, Carsten Eickhoff
conference: Arxiv
year: 2025
bibkey: lu2025cross
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.04645'}]
tags: [Scalability, Evaluation]
short_authors: Meng Lu, Catherine Chen, Carsten Eickhoff
---
Neural Ranking Models (NRMs) have rapidly advanced state-of-the-art
performance on information retrieval tasks. In this work, we investigate a
Cross-Encoder variant of MiniLM to determine which relevance features it
computes and where they are stored. We find that it employs a semantic variant
of the traditional BM25 in an interpretable manner, featuring localized
components: (1) Transformer attention heads that compute soft term frequency
while controlling for term saturation and document length effects, and (2) a
low-rank component of its embedding matrix that encodes inverse document
frequency information for the vocabulary. This suggests that the Cross-Encoder
uses the same fundamental mechanisms as BM25, but further leverages their
capacity to capture semantics for improved retrieval performance. The granular
understanding lays the groundwork for model editing to enhance model
transparency, addressing safety concerns, and improving scalability in training
and real-world applications.
---
layout: publication
title: An Ensemble Embedding Approach For Improving Semantic Caching Performance In
  Llm-based Systems
authors: Shervin Ghaffari, Zohre Bahranifard, Mohammad Akbari
conference: Arxiv
year: 2025
bibkey: ghaffari2025an
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2507.07061'}]
tags: [Evaluation, Efficiency, Datasets]
short_authors: Shervin Ghaffari, Zohre Bahranifard, Mohammad Akbari
---
Semantic caching enhances the efficiency of large language model (LLM) systems by identifying semantically similar queries, storing responses once, and serving them for subsequent equivalent requests. However, existing semantic caching frameworks rely on single embedding models for query representation, which limits their ability to capture the diverse semantic relationships present in real-world query distributions. This paper presents an ensemble embedding approach that combines multiple embedding models through a trained meta-encoder to improve semantic similarity detection in LLM caching systems. We evaluate our method using the Quora Question Pairs (QQP) dataset, measuring cache hit ratios, cache miss ratios, token savings, and response times. Our ensemble approach achieves a 92% cache hit ratio for semantically equivalent queries while maintaining an 85% accuracy in correctly rejecting non-equivalent queries as cache misses. These results demonstrate that ensemble embedding methods significantly outperform single-model approaches in distinguishing between semantically similar and dissimilar queries, leading to more effective caching performance and reduced computational overhead in LLM-based systems.
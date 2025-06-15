---
layout: publication
title: 'Lshbloom: Memory-efficient, Extreme-scale Document Deduplication'
authors: Arham Khan et al.
conference: "Arxiv"
year: 2024
citations: 0
bibkey: khan2024memory
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2411.04257'}
tags: ['Efficient Learning', 'Tools and Libraries']
---
Deduplication is a major focus for assembling and curating training datasets for large language models (LLM) -- detecting and eliminating additional instances of the same content -- in large collections of technical documents. Unrestrained, duplicates in the training dataset increase training costs and lead to undesirable properties such as memorization in trained models or cheating on evaluation. Contemporary approaches to document-level deduplication are often extremely expensive in both runtime and memory. We propose LSHBloom, an extension to MinhashLSH, which replaces the expensive LSHIndex with lightweight Bloom filters. LSHBloom demonstrates the same deduplication performance as MinhashLSH with only a marginal increase in false positives (as low as 1e-5 in our experiments); demonstrates competitive runtime (270% faster than MinhashLSH on peS2o); and, crucially, uses just 0.6% of the disk space required by MinhashLSH to deduplicate peS2o. We demonstrate that this space advantage scales with increased dataset size -- at the extreme scale of several billion documents, LSHBloom promises a 250% speedup and a 54\\(\times\\) space advantage over traditional MinHashLSH scaling deduplication of text datasets to many billions of documents.

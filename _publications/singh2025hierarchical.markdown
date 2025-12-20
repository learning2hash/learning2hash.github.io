---
layout: publication
title: Hierarchical Re-ranker Retriever (HRR)
authors: Ashish Singh, Priti Mohapatra
conference: Arxiv
year: 2025
bibkey: singh2025hierarchical
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2503.02401'}]
tags: ["Re-Ranking", "Text Retrieval", "Tools & Libraries"]
short_authors: Ashish Singh, Priti Mohapatra
---
Retrieving the right level of context for a given query is a perennial
challenge in information retrieval - too large a chunk dilutes semantic
specificity, while chunks that are too small lack broader context. This paper
introduces the Hierarchical Re-ranker Retriever (HRR), a framework designed to
achieve both fine-grained and high-level context retrieval for large language
model (LLM) applications. In HRR, documents are split into sentence-level and
intermediate-level (512 tokens) chunks to maximize vector-search quality for
both short and broad queries. We then employ a reranker that operates on these
512-token chunks, ensuring an optimal balance neither too coarse nor too fine
for robust relevance scoring. Finally, top-ranked intermediate chunks are
mapped to parent chunks (2048 tokens) to provide an LLM with sufficiently large
context.
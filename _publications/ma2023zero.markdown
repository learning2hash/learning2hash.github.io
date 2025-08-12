---
layout: publication
title: Zero-shot Listwise Document Reranking With A Large Language Model
authors: Xueguang Ma, Xinyu Zhang, Ronak Pradeep, Jimmy Lin
conference: Arxiv
year: 2023
bibkey: ma2023zero
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.02156'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Ma et al.
---
Supervised ranking methods based on bi-encoder or cross-encoder architectures
have shown success in multi-stage text ranking tasks, but they require large
amounts of relevance judgments as training data. In this work, we propose
Listwise Reranker with a Large Language Model (LRL), which achieves strong
reranking effectiveness without using any task-specific training data.
Different from the existing pointwise ranking methods, where documents are
scored independently and ranked according to the scores, LRL directly generates
a reordered list of document identifiers given the candidate documents.
Experiments on three TREC web search datasets demonstrate that LRL not only
outperforms zero-shot pointwise methods when reranking first-stage retrieval
results, but can also act as a final-stage reranker to improve the top-ranked
results of a pointwise method for improved efficiency. Additionally, we apply
our approach to subsets of MIRACL, a recent multilingual retrieval dataset,
with results showing its potential to generalize across different languages.
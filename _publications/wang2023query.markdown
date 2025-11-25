---
layout: publication
title: Query Encoder Distillation Via Embedding Alignment Is A Strong Baseline Method
  To Boost Dense Retriever Online Efficiency
authors: Yuxuan Wang, Hong Lyu
conference: Proceedings of The Fourth Workshop on Simple and Efficient Natural Language
  Processing (SustaiNLP)
year: 2023
bibkey: wang2023query
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.11550'}]
tags: ["Efficiency", "Evaluation", "Unsupervised"]
short_authors: Yuxuan Wang, Hong Lyu
---
The information retrieval community has made significant progress in
improving the efficiency of Dual Encoder (DE) dense passage retrieval systems,
making them suitable for latency-sensitive settings. However, many proposed
procedures are often too complex or resource-intensive, which makes it
difficult for practitioners to adopt them or identify sources of empirical
gains. Therefore, in this work, we propose a trivially simple recipe to serve
as a baseline method for boosting the efficiency of DE retrievers leveraging an
asymmetric architecture. Our results demonstrate that even a 2-layer,
BERT-based query encoder can still retain 92.5% of the full DE performance on
the BEIR benchmark via unsupervised distillation and proper student
initialization. We hope that our findings will encourage the community to
re-evaluate the trade-offs between method complexity and performance
improvements.
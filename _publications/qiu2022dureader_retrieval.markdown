---
layout: publication
title: 'Dureader_retrieval: A Large-scale Chinese Benchmark For Passage Retrieval
  From Web Search Engine'
authors: Yifu Qiu, Hongyu Li, Yingqi Qu, Ying Chen, Qiaoqiao She, Jing Liu, Hua Wu,
  Haifeng Wang
conference: Arxiv
year: 2022
bibkey: qiu2022dureader_retrieval
citations: 0
additional_links: [{name: Code, url: 'https://github.com/baidu/DuReader/tree/master/DuReader-Retrieval'},
  {name: Paper, url: 'https://arxiv.org/abs/2203.10232'}]
tags: [Scalability, Evaluation, Datasets]
short_authors: Qiu et al.
---
In this paper, we present DuReader_retrieval, a large-scale Chinese dataset
for passage retrieval. DuReader_retrieval contains more than 90K queries and
over 8M unique passages from a commercial search engine. To alleviate the
shortcomings of other datasets and ensure the quality of our benchmark, we (1)
reduce the false negatives in development and test sets by manually annotating
results pooled from multiple retrievers, and (2) remove the training queries
that are semantically similar to the development and testing queries.
Additionally, we provide two out-of-domain testing sets for cross-domain
evaluation, as well as a set of human translated queries for for cross-lingual
retrieval evaluation. The experiments demonstrate that DuReader_retrieval is
challenging and a number of problems remain unsolved, such as the salient
phrase mismatch and the syntactic mismatch between queries and paragraphs.
These experiments also show that dense retrievers do not generalize well across
domains, and cross-lingual retrieval is essentially challenging.
DuReader_retrieval is publicly available at
https://github.com/baidu/DuReader/tree/master/DuReader-Retrieval.
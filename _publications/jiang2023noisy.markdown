---
layout: publication
title: Noisy Self-training With Synthetic Queries For Dense Retrieval
authors: Fan Jiang, Tom Drummond, Trevor Cohn
conference: Arxiv
year: 2023
bibkey: jiang2023noisy
citations: 0
additional_links: [{name: Code, url: 'https://github.com/Fantabulous-J/Self-Training-DPR\'},
  {name: Paper, url: 'https://arxiv.org/abs/2311.15563'}]
tags: ["Evaluation", "Re-Ranking", "Tools & Libraries"]
short_authors: Fan Jiang, Tom Drummond, Trevor Cohn
---
Although existing neural retrieval models reveal promising results when
training data is abundant and the performance keeps improving as training data
increases, collecting high-quality annotated data is prohibitively costly. To
this end, we introduce a novel noisy self-training framework combined with
synthetic queries, showing that neural retrievers can be improved in a
self-evolution manner with no reliance on any external models. Experimental
results show that our method improves consistently over existing methods on
both general-domain (e.g., MS-MARCO) and out-of-domain (i.e., BEIR) retrieval
benchmarks. Extra analysis on low-resource settings reveals that our method is
data efficient and outperforms competitive baselines, with as little as 30% of
labelled training data. Further extending the framework for reranker training
demonstrates that the proposed method is general and yields additional gains on
tasks of diverse domains.\footnote\{Source code is available at
https://github.com/Fantabulous-J/Self-Training-DPR\}
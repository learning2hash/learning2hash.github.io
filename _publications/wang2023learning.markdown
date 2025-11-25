---
layout: publication
title: Learning Multi-stage Multi-grained Semantic Embeddings For E-commerce Search
authors: Binbin Wang, Mingming Li, Zhixiong Zeng, Jingwei Zhuo, Songlin Wang, Sulong
  Xu, Bo Long, Weipeng Yan
conference: Companion Proceedings of the ACM Web Conference 2023
year: 2023
bibkey: wang2023learning
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.11009'}]
tags: ["Efficiency", "Large Scale Search", "Scalability", "Similarity Search"]
short_authors: Wang et al.
---
Retrieving relevant items that match users' queries from billion-scale corpus
forms the core of industrial e-commerce search systems, in which
embedding-based retrieval (EBR) methods are prevailing. These methods adopt a
two-tower framework to learn embedding vectors for query and item separately
and thus leverage efficient approximate nearest neighbor (ANN) search to
retrieve relevant items. However, existing EBR methods usually ignore
inconsistent user behaviors in industrial multi-stage search systems, resulting
in insufficient retrieval efficiency with a low commercial return. To tackle
this challenge, we propose to improve EBR methods by learning Multi-level
Multi-Grained Semantic Embeddings(MMSE). We propose the multi-stage information
mining to exploit the ordered, clicked, unclicked and random sampled items in
practical user behavior data, and then capture query-item similarity via a
post-fusion strategy. We then propose multi-grained learning objectives that
integrate the retrieval loss with global comparison ability and the ranking
loss with local comparison ability to generate semantic embeddings. Both
experiments on a real-world billion-scale dataset and online A/B tests verify
the effectiveness of MMSE in achieving significant performance improvements on
metrics such as offline recall and online conversion rate (CVR).
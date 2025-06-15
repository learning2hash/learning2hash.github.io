---
layout: publication
title: 'Early Exit Strategies For Approximate K-nn Search In Dense Retrieval'
authors: Francesco Busolin et al.
conference: "Arxiv"
year: 2024
citations: 2
bibkey: busolin2024early
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2408.04981'}
  - {name: "Code", url: 'https://github.com/francescobusolin/faiss_pEE'}
tags: ['Efficiency', 'Benchmarks and Tools', 'Unimodal', 'Shallow', 'Retrieval Models', 'Vector Indexing', 'Has Code', 'Supervised']
---
Learned dense representations are a popular family of techniques for encoding
queries and documents using high-dimensional embeddings, which enable retrieval
by performing approximate k nearest-neighbors search (A-kNN). A popular
technique for making A-kNN search efficient is based on a two-level index,
where the embeddings of documents are clustered offline and, at query
processing, a fixed number N of clusters closest to the query is visited
exhaustively to compute the result set. In this paper, we build upon
state-of-the-art for early exit A-kNN and propose an unsupervised method based
on the notion of patience, which can reach competitive effectiveness with large
efficiency gains. Moreover, we discuss a cascade approach where we first
identify queries that find their nearest neighbor within the closest t << N
clusters, and then we decide how many more to visit based on our patience
approach or other state-of-the-art strategies. Reproducible experiments
employing state-of-the-art dense retrieval models and publicly available
resources show that our techniques improve the A-kNN efficiency with up to 5x
speedups while achieving negligible effectiveness losses. All the code used is
available at https://github.com/francescobusolin/faiss_pEE

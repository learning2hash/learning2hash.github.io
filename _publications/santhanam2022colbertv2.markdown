---
layout: publication
title: 'Colbertv2: Effective And Efficient Retrieval Via Lightweight Late Interaction'
authors: Santhanam et al.
conference: 'Proceedings of the 2022 Conference of the North American Chapter of the
  Association for Computational Linguistics: Human Language Technologies'
year: 2022
bibkey: santhanam2022colbertv2
citations: 163
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.01488'}]
tags: ["Similarity-Search", "Eacl", "NAACL"]
---
Neural information retrieval (IR) has greatly advanced search and other
knowledge-intensive language tasks. While many neural IR methods encode queries
and documents into single-vector representations, late interaction models
produce multi-vector representations at the granularity of each token and
decompose relevance modeling into scalable token-level computations. This
decomposition has been shown to make late interaction more effective, but it
inflates the space footprint of these models by an order of magnitude. In this
work, we introduce ColBERTv2, a retriever that couples an aggressive residual
compression mechanism with a denoised supervision strategy to simultaneously
improve the quality and space footprint of late interaction. We evaluate
ColBERTv2 across a wide range of benchmarks, establishing state-of-the-art
quality within and outside the training domain while reducing the space
footprint of late interaction models by 6--10\\(\times\\).
---
layout: publication
title: Contextual Dictionary Lookup For Knowledge Graph Completion
authors: Jining Wang, Delai Qiu, Youming Liu, Yining Wang, Chuan Chen, Zibin Zheng,
  Yuren Zhou
conference: Arxiv
year: 2023
bibkey: wang2023contextual
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.07719'}]
tags: []
short_authors: Wang et al.
---
Knowledge graph completion (KGC) aims to solve the incompleteness of
knowledge graphs (KGs) by predicting missing links from known triples, numbers
of knowledge graph embedding (KGE) models have been proposed to perform KGC by
learning embeddings. Nevertheless, most existing embedding models map each
relation into a unique vector, overlooking the specific fine-grained semantics
of them under different entities. Additionally, the few available fine-grained
semantic models rely on clustering algorithms, resulting in limited performance
and applicability due to the cumbersome two-stage training process. In this
paper, we present a novel method utilizing contextual dictionary lookup,
enabling conventional embedding models to learn fine-grained semantics of
relations in an end-to-end manner. More specifically, we represent each
relation using a dictionary that contains multiple latent semantics. The
composition of a given entity and the dictionary's central semantics serves as
the context for generating a lookup, thus determining the fine-grained
semantics of the relation adaptively. The proposed loss function optimizes both
the central and fine-grained semantics simultaneously to ensure their semantic
consistency. Besides, we introduce two metrics to assess the validity and
accuracy of the dictionary lookup operation. We extend several KGE models with
the method, resulting in substantial performance improvements on widely-used
benchmark datasets.
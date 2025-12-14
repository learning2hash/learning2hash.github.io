---
layout: publication
title: Universal Knowledge Graph Embeddings
authors: N'Dah Jean Kouagou, Caglar Demir, Hamada M. Zahera, Adrian Wilke, Stefan
  Heindorf, Jiayi Li, Axel-Cyrille Ngonga Ngomo
conference: Companion Proceedings of the ACM Web Conference 2024 (WWW 24 Companion)
  May 13--17 2024 Singapore Singapore
year: 2023
bibkey: kouagou2023universal
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.14899'}]
tags: [Scalability, Tools & Libraries, Datasets]
short_authors: Kouagou et al.
---
A variety of knowledge graph embedding approaches have been developed. Most
of them obtain embeddings by learning the structure of the knowledge graph
within a link prediction setting. As a result, the embeddings reflect only the
structure of a single knowledge graph, and embeddings for different knowledge
graphs are not aligned, e.g., they cannot be used to find similar entities
across knowledge graphs via nearest neighbor search. However, knowledge graph
embedding applications such as entity disambiguation require a more global
representation, i.e., a representation that is valid across multiple sources.
We propose to learn universal knowledge graph embeddings from large-scale
interlinked knowledge sources. To this end, we fuse large knowledge graphs
based on the owl:sameAs relation such that every entity is represented by a
unique identity. We instantiate our idea by computing universal embeddings
based on DBpedia and Wikidata yielding embeddings for about 180 million
entities, 15 thousand relations, and 1.2 billion triples. We believe our
computed embeddings will support the emerging field of graph foundation models.
Moreover, we develop a convenient API to provide embeddings as a service.
Experiments on link prediction suggest that universal knowledge graph
embeddings encode better semantics compared to embeddings computed on a single
knowledge graph. For reproducibility purposes, we provide our source code and
datasets open access.
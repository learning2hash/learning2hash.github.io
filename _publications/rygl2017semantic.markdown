---
layout: publication
title: Semantic Vector Encoding And Similarity Search Using Fulltext Search Engines
authors: "Jan Rygl, Jan Pomik\xE1lek, Radim \u0158eh\u016F\u0159ek, Michal R\u016F\
  \u017Ei\u010Dka, V\xEDt Novotn\xFD, Petr Sojka"
conference: Proceedings of the 2nd Workshop on Representation Learning for NLP
year: 2017
bibkey: rygl2017semantic
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1706.00957'}]
tags: ["Efficiency", "Robustness", "Scalability", "Similarity Search", "Text Retrieval"]
short_authors: Rygl et al.
---
Vector representations and vector space modeling (VSM) play a central role in
modern machine learning. We propose a novel approach to `vector similarity
searching' over dense semantic representations of words and documents that can
be deployed on top of traditional inverted-index-based fulltext engines, taking
advantage of their robustness, stability, scalability and ubiquity.
  We show that this approach allows the indexing and querying of dense vectors
in text domains. This opens up exciting avenues for major efficiency gains,
along with simpler deployment, scaling and monitoring.
  The end result is a fast and scalable vector database with a tunable
trade-off between vector search performance and quality, backed by a standard
fulltext engine such as Elasticsearch.
  We empirically demonstrate its querying performance and quality by applying
this solution to the task of semantic searching over a dense vector
representation of the entire English Wikipedia.
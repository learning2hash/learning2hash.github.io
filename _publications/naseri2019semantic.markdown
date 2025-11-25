---
layout: publication
title: Semantic Driven Fielded Entity Retrieval
authors: Shahrzad Naseri, Sheikh Muhammad Sarwar, James Allan
conference: Arxiv
year: 2019
bibkey: naseri2019semantic
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1907.01457'}]
tags: ["Datasets", "Re-Ranking"]
short_authors: Shahrzad Naseri, Sheikh Muhammad Sarwar, James Allan
---
A common approach for knowledge-base entity search is to consider an entity
as a document with multiple fields. Models that focus on matching query terms
in different fields are popular choices for searching such entity
representations. An instance of such a model is FSDM (Fielded Sequential
Dependence Model). We propose to integrate field-level semantic features into
FSDM. We use FSDM to retrieve a pool of documents, and then to use semantic
field-level features to re-rank those documents. We propose to represent
queries as bags of terms as well as bags of entities, and eventually, use their
dense vector representation to compute semantic features based on query
document similarity. Our proposed re-ranking approach achieves significant
improvement in entity retrieval on the DBpedia-Entity (v2) dataset over
existing FSDM model. Specifically, for all queries we achieve 2.5% and 1.2%
significant improvement in NDCG@10 and NDCG@100, respectively.
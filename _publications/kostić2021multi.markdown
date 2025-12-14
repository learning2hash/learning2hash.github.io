---
layout: publication
title: Multi-modal Retrieval Of Tables And Texts Using Tri-encoder Models
authors: "Bogdan Kosti\u0107, Julian Risch, Timo M\xF6ller"
conference: Proceedings of the 3rd Workshop on Machine Reading for Question Answering
year: 2021
bibkey: "kosti\u01072021multi"
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.04049'}]
tags: [Datasets, Graph-based ANN, Evaluation]
short_authors: "Bogdan Kosti\u0107, Julian Risch, Timo M\xF6ller"
---
Open-domain extractive question answering works well on textual data by first
retrieving candidate texts and then extracting the answer from those
candidates. However, some questions cannot be answered by text alone but
require information stored in tables. In this paper, we present an approach for
retrieving both texts and tables relevant to a question by jointly encoding
texts, tables and questions into a single vector space. To this end, we create
a new multi-modal dataset based on text and table datasets from related work
and compare the retrieval performance of different encoding schemata. We find
that dense vector embeddings of transformer models outperform sparse embeddings
on four out of six evaluation datasets. Comparing different dense embedding
models, tri-encoders with one encoder for each question, text and table,
increase retrieval performance compared to bi-encoders with one encoder for the
question and one for both text and tables. We release the newly created
multi-modal dataset to the community so that it can be used for training and
evaluation.
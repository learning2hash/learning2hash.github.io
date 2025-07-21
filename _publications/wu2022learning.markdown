---
layout: publication
title: Learning Deep Semantic Model for Code Search using CodeSearchNet Corpus
authors: Wu Chen, Yan Ming
conference: Arxiv
year: 2022
bibkey: wu2022learning
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.11313'}]
tags: []
---
Semantic code search is the task of retrieving relevant code snippet given a
natural language query. Different from typical information retrieval tasks,
code search requires to bridge the semantic gap between the programming
language and natural language, for better describing intrinsic concepts and
semantics. Recently, deep neural network for code search has been a hot
research topic. Typical methods for neural code search first represent the code
snippet and query text as separate embeddings, and then use vector distance
(e.g. dot-product or cosine) to calculate the semantic similarity between them.
There exist many different ways for aggregating the variable length of code or
query tokens into a learnable embedding, including bi-encoder, cross-encoder,
and poly-encoder. The goal of the query encoder and code encoder is to produce
embeddings that are close with each other for a related pair of query and the
corresponding desired code snippet, in which the choice and design of encoder
is very significant.
  In this paper, we propose a novel deep semantic model which makes use of the
utilities of not only the multi-modal sources, but also feature extractors such
as self-attention, the aggregated vectors, combination of the intermediate
representations. We apply the proposed model to tackle the CodeSearchNet
challenge about semantic code search. We align cross-lingual embedding for
multi-modality learning with large batches and hard example mining, and combine
different learned representations for better enhancing the representation
learning. Our model is trained on CodeSearchNet corpus and evaluated on the
held-out data, the final model achieves 0.384 NDCG and won the first place in
this benchmark. Models and code are available at
https://github.com/overwindows/SemanticCodeSearch.git.
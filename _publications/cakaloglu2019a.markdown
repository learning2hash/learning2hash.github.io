---
layout: publication
title: A Multi-resolution Word Embedding For Document Retrieval From Large Unstructured
  Knowledge Bases
authors: Tolgahan Cakaloglu, Xiaowei Xu
conference: Arxiv
year: 2019
bibkey: cakaloglu2019a
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1902.00663'}]
tags: [Text Retrieval, Evaluation, Datasets]
short_authors: Tolgahan Cakaloglu, Xiaowei Xu
---
Deep language models learning a hierarchical representation proved to be a
powerful tool for natural language processing, text mining and information
retrieval. However, representations that perform well for retrieval must
capture semantic meaning at different levels of abstraction or context-scopes.
In this paper, we propose a new method to generate multi-resolution word
embeddings that represent documents at multiple resolutions in terms of
context-scopes. In order to investigate its performance,we use the Stanford
Question Answering Dataset (SQuAD) and the Question Answering by Search And
Reading (QUASAR) in an open-domain question-answering setting, where the first
task is to find documents useful for answering a given question. To this end,
we first compare the quality of various text-embedding methods for retrieval
performance and give an extensive empirical comparison with the performance of
various non-augmented base embeddings with and without multi-resolution
representation. We argue that multi-resolution word embeddings are consistently
superior to the original counterparts and deep residual neural models
specifically trained for retrieval purposes can yield further significant gains
when they are used for augmenting those embeddings.
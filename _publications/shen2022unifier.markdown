---
layout: publication
title: 'Unifier: A Unified Retriever For Large-scale Retrieval'
authors: Tao Shen, Xiubo Geng, Chongyang Tao, Can Xu, Guodong Long, Kai Zhang, Daxin
  Jiang
conference: Arxiv
year: 2022
bibkey: shen2022unifier
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.11194'}]
tags: ["Evaluation", "Scalability", "Text Retrieval"]
short_authors: Shen et al.
---
Large-scale retrieval is to recall relevant documents from a huge collection
given a query. It relies on representation learning to embed documents and
queries into a common semantic encoding space. According to the encoding space,
recent retrieval methods based on pre-trained language models (PLM) can be
coarsely categorized into either dense-vector or lexicon-based paradigms. These
two paradigms unveil the PLMs' representation capability in different
granularities, i.e., global sequence-level compression and local word-level
contexts, respectively. Inspired by their complementary global-local
contextualization and distinct representing views, we propose a new learning
framework, UnifieR which unifies dense-vector and lexicon-based retrieval in
one model with a dual-representing capability. Experiments on passage retrieval
benchmarks verify its effectiveness in both paradigms. A uni-retrieval scheme
is further presented with even better retrieval quality. We lastly evaluate the
model on BEIR benchmark to verify its transferability.
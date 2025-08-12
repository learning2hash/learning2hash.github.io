---
layout: publication
title: 'Few-shot Prompting For Pairwise Ranking: An Effective Non-parametric Retrieval
  Model'
authors: Nilanjan Sinhababu, Andrew Parry, Debasis Ganguly, Debasis Samanta, Pabitra
  Mitra
conference: 'Findings of the Association for Computational Linguistics: EMNLP 2024'
year: 2024
bibkey: sinhababu2024few
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.17745'}]
tags: ["EMNLP", "Few Shot & Zero Shot"]
short_authors: Sinhababu et al.
---
A supervised ranking model, despite its advantage of being effective, usually
involves complex processing - typically multiple stages of task-specific
pre-training and fine-tuning. This has motivated researchers to explore simpler
pipelines leveraging large language models (LLMs) that are capable of working
in a zero-shot manner. However, since zero-shot inference does not make use of
a training set of pairs of queries and their relevant documents, its
performance is mostly worse than that of supervised models, which are trained
on such example pairs. Motivated by the existing findings that training
examples generally improve zero-shot performance, in our work, we explore if
this also applies to ranking models. More specifically, given a query and a
pair of documents, the preference prediction task is improved by augmenting
examples of preferences for similar queries from a training set. Our proposed
pairwise few-shot ranker demonstrates consistent improvements over the
zero-shot baseline on both in-domain (TREC DL) and out-domain (BEIR subset)
retrieval benchmarks. Our method also achieves a close performance to that of a
supervised model without requiring any complex training pipeline.
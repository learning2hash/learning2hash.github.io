---
layout: publication
title: Label Semantics For Few Shot Named Entity Recognition
authors: Jie Ma, Miguel Ballesteros, Srikanth Doss, Rishita Anubhai, Sunil Mallya,
  Yaser Al-Onaizan, Dan Roth
conference: 'Findings of the Association for Computational Linguistics: ACL 2022'
year: 2022
bibkey: ma2022label
citations: 66
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.08985'}]
tags: []
short_authors: Ma et al.
---
We study the problem of few shot learning for named entity recognition.
Specifically, we leverage the semantic information in the names of the labels
as a way of giving the model additional signal and enriched priors. We propose
a neural architecture that consists of two BERT encoders, one to encode the
document and its tokens and another one to encode each of the labels in natural
language format. Our model learns to match the representations of named
entities computed by the first encoder with label representations computed by
the second encoder. The label semantics signal is shown to support improved
state-of-the-art results in multiple few shot NER benchmarks and on-par
performance in standard benchmarks. Our model is especially effective in low
resource settings.
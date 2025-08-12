---
layout: publication
title: Hierarchical Meta-embeddings For Code-switching Named Entity Recognition
authors: Genta Indra Winata, Zhaojiang Lin, Jamin Shin, Zihan Liu, Pascale Fung
conference: Proceedings of the 2019 Conference on Empirical Methods in Natural Language
  Processing and the 9th International Joint Conference on Natural Language Processing
  (EMNLP-IJCNLP)
year: 2019
bibkey: winata2019hierarchical
citations: 21
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.08504'}]
tags: ["EMNLP"]
short_authors: Winata et al.
---
In countries that speak multiple main languages, mixing up different
languages within a conversation is commonly called code-switching. Previous
works addressing this challenge mainly focused on word-level aspects such as
word embeddings. However, in many cases, languages share common subwords,
especially for closely related languages, but also for languages that are
seemingly irrelevant. Therefore, we propose Hierarchical Meta-Embeddings (HME)
that learn to combine multiple monolingual word-level and subword-level
embeddings to create language-agnostic lexical representations. On the task of
Named Entity Recognition for English-Spanish code-switching data, our model
achieves the state-of-the-art performance in the multilingual settings. We also
show that, in cross-lingual settings, our model not only leverages closely
related languages, but also learns from languages with different roots.
Finally, we show that combining different subunits are crucial for capturing
code-switching entities.
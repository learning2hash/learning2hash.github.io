---
layout: publication
title: A Robust Self-learning Method For Fully Unsupervised Cross-lingual Mappings
  Of Word Embeddings
authors: Mikel Artetxe, Gorka Labaka, Eneko Agirre
conference: 'Proceedings of the 56th Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)'
year: 2018
bibkey: artetxe2018robust
citations: 565
additional_links: [{name: Code, url: 'https://github.com/artetxem/vecmap'}, {name: Paper,
    url: 'https://arxiv.org/abs/1805.06297'}]
tags: ["Robustness", "Unsupervised"]
short_authors: Mikel Artetxe, Gorka Labaka, Eneko Agirre
---
Recent work has managed to learn cross-lingual word embeddings without
parallel data by mapping monolingual embeddings to a shared space through
adversarial training. However, their evaluation has focused on favorable
conditions, using comparable corpora or closely-related languages, and we show
that they often fail in more realistic scenarios. This work proposes an
alternative approach based on a fully unsupervised initialization that
explicitly exploits the structural similarity of the embeddings, and a robust
self-learning algorithm that iteratively improves this solution. Our method
succeeds in all tested scenarios and obtains the best published results in
standard datasets, even surpassing previous supervised systems. Our
implementation is released as an open source project at
https://github.com/artetxem/vecmap
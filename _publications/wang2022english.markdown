---
layout: publication
title: English Contrastive Learning Can Learn Universal Cross-lingual Sentence Embeddings
authors: Yau-Shian Wang, Ashley Wu, Graham Neubig
conference: Proceedings of the 2022 Conference on Empirical Methods in Natural Language
  Processing
year: 2022
bibkey: wang2022english
citations: 12
additional_links: [{name: Code, url: 'https://github.com/yaushian/mSimCSE.'}, {name: Paper,
    url: 'https://arxiv.org/abs/2211.06127'}]
tags: ["EMNLP", "Evaluation", "Self-Supervised", "Supervised", "Unsupervised"]
short_authors: Yau-Shian Wang, Ashley Wu, Graham Neubig
---
Universal cross-lingual sentence embeddings map semantically similar
cross-lingual sentences into a shared embedding space. Aligning cross-lingual
sentence embeddings usually requires supervised cross-lingual parallel
sentences. In this work, we propose mSimCSE, which extends SimCSE to
multilingual settings and reveal that contrastive learning on English data can
surprisingly learn high-quality universal cross-lingual sentence embeddings
without any parallel data. In unsupervised and weakly supervised settings,
mSimCSE significantly improves previous sentence embedding methods on
cross-lingual retrieval and multilingual STS tasks. The performance of
unsupervised mSimCSE is comparable to fully supervised methods in retrieving
low-resource languages and multilingual STS. The performance can be further
enhanced when cross-lingual NLI data is available. Our code is publicly
available at https://github.com/yaushian/mSimCSE.
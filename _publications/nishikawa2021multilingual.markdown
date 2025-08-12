---
layout: publication
title: A Multilingual Bag-of-entities Model For Zero-shot Cross-lingual Text Classification
authors: Sosuke Nishikawa, Ikuya Yamada, Yoshimasa Tsuruoka, Isao Echizen
conference: Proceedings of the 26th Conference on Computational Natural Language Learning
  (CoNLL)
year: 2022
bibkey: nishikawa2021multilingual
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.07792'}]
tags: []
short_authors: Nishikawa et al.
---
We present a multilingual bag-of-entities model that effectively boosts the
performance of zero-shot cross-lingual text classification by extending a
multilingual pre-trained language model (e.g., M-BERT). It leverages the
multilingual nature of Wikidata: entities in multiple languages representing
the same concept are defined with a unique identifier. This enables entities
described in multiple languages to be represented using shared embeddings. A
model trained on entity features in a resource-rich language can thus be
directly applied to other languages. Our experimental results on cross-lingual
topic classification (using the MLDoc and TED-CLDC datasets) and entity typing
(using the SHINRA2020-ML dataset) show that the proposed model consistently
outperforms state-of-the-art models.
---
layout: publication
title: Contrastive Representation Learning For Cross-document Coreference Resolution
  Of Events And Entities
authors: Benjamin Hsu, Graham Horwood
conference: 'Proceedings of the 2022 Conference of the North American Chapter of the
  Association for Computational Linguistics: Human Language Technologies'
year: 2022
bibkey: hsu2022contrastive
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.11438'}]
tags: ["NAACL", "Self-Supervised"]
short_authors: Benjamin Hsu, Graham Horwood
---
Identifying related entities and events within and across documents is
fundamental to natural language understanding. We present an approach to entity
and event coreference resolution utilizing contrastive representation learning.
Earlier state-of-the-art methods have formulated this problem as a binary
classification problem and leveraged large transformers in a cross-encoder
architecture to achieve their results. For large collections of documents and
corresponding set of \(n\) mentions, the necessity of performing \(n^\{2\}\)
transformer computations in these earlier approaches can be computationally
intensive. We show that it is possible to reduce this burden by applying
contrastive learning techniques that only require \(n\) transformer computations
at inference time. Our method achieves state-of-the-art results on a number of
key metrics on the ECB+ corpus and is competitive on others.
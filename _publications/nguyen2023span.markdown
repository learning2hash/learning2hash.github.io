---
layout: publication
title: Span-based Named Entity Recognition By Generating And Compressing Information
authors: Nhung T. H. Nguyen, Makoto Miwa, Sophia Ananiadou
conference: Proceedings of the 17th Conference of the European Chapter of the Association
  for Computational Linguistics
year: 2023
bibkey: nguyen2023span
citations: 5
additional_links: [{name: Code, url: 'https://github.com/nguyennth/joint-ib-models'},
  {name: Paper, url: 'https://arxiv.org/abs/2302.05392'}]
tags: ["Eacl"]
short_authors: Nhung T. H. Nguyen, Makoto Miwa, Sophia Ananiadou
---
The information bottleneck (IB) principle has been proven effective in
various NLP applications. The existing work, however, only used either
generative or information compression models to improve the performance of the
target task. In this paper, we propose to combine the two types of IB models
into one system to enhance Named Entity Recognition (NER). For one type of IB
model, we incorporate two unsupervised generative components, span
reconstruction and synonym generation, into a span-based NER system. The span
reconstruction ensures that the contextualised span representation keeps the
span information, while the synonym generation makes synonyms have similar
representations even in different contexts. For the other type of IB model, we
add a supervised IB layer that performs information compression into the system
to preserve useful features for NER in the resulting span representations.
Experiments on five different corpora indicate that jointly training both
generative and information compression models can enhance the performance of
the baseline span-based NER system. Our source code is publicly available at
https://github.com/nguyennth/joint-ib-models.
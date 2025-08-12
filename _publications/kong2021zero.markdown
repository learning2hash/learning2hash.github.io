---
layout: publication
title: 'Zero-shot Medical Entity Retrieval Without Annotation: Learning From Rich
  Knowledge Graph Semantics'
authors: Luyang Kong, Christopher Winestock, Parminder Bhatia
conference: 'Findings of the Association for Computational Linguistics: ACL-IJCNLP
  2021'
year: 2021
bibkey: kong2021zero
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.12682'}]
tags: []
short_authors: Luyang Kong, Christopher Winestock, Parminder Bhatia
---
Medical entity retrieval is an integral component for understanding and
communicating information across various health systems. Current approaches
tend to work well on specific medical domains but generalize poorly to unseen
sub-specialties. This is of increasing concern under a public health crisis as
new medical conditions and drug treatments come to light frequently. Zero-shot
retrieval is challenging due to the high degree of ambiguity and variability in
medical corpora, making it difficult to build an accurate similarity measure
between mentions and concepts. Medical knowledge graphs (KG), however, contain
rich semantics including large numbers of synonyms as well as its curated
graphical structures. To take advantage of this valuable information, we
propose a suite of learning tasks designed for training efficient zero-shot
entity retrieval models. Without requiring any human annotation, our knowledge
graph enriched architecture significantly outperforms common zero-shot
benchmarks including BM25 and Clinical BERT with 7% to 30% higher recall across
multiple major medical ontologies, such as UMLS, SNOMED, and ICD-10.
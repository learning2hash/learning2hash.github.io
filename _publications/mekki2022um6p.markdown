---
layout: publication
title: 'UM6P-CS At Semeval-2022 Task 11: Enhancing Multilingual And Code-mixed Complex
  Named Entity Recognition Via Pseudo Labels Using Multilingual Transformer'
authors: Abdellah El Mekki, Abdelkader El Mahdaouy, Mohammed Akallouch, Ismail Berrada,
  Ahmed Khoumsi
conference: Proceedings of the 16th International Workshop on Semantic Evaluation
  (SemEval-2022)
year: 2022
bibkey: mekki2022um6p
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.13515'}]
tags: ["Datasets"]
short_authors: Mekki et al.
---
Building real-world complex Named Entity Recognition (NER) systems is a
challenging task. This is due to the complexity and ambiguity of named entities
that appear in various contexts such as short input sentences, emerging
entities, and complex entities. Besides, real-world queries are mostly
malformed, as they can be code-mixed or multilingual, among other scenarios. In
this paper, we introduce our submitted system to the Multilingual Complex Named
Entity Recognition (MultiCoNER) shared task. We approach the complex NER for
multilingual and code-mixed queries, by relying on the contextualized
representation provided by the multilingual Transformer XLM-RoBERTa. In
addition to the CRF-based token classification layer, we incorporate a span
classification loss to recognize named entities spans. Furthermore, we use a
self-training mechanism to generate weakly-annotated data from a large
unlabeled dataset. Our proposed system is ranked 6th and 8th in the
multilingual and code-mixed MultiCoNER's tracks respectively.
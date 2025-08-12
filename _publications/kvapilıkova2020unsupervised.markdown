---
layout: publication
title: Unsupervised Multilingual Sentence Embeddings For Parallel Corpus Mining
authors: "Ivana Kvapil\u0131kova, Mikel Artetxe, Gorka Labaka, Eneko Agirre, Ond\u0159\
  ej Bojar"
conference: 'Proceedings of the 58th Annual Meeting of the Association for Computational
  Linguistics: Student Research Workshop'
year: 2020
bibkey: "kvapil\u0131kova2020unsupervised"
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.10419'}]
tags: ["Unsupervised"]
short_authors: "Kvapil\u0131kova et al."
---
Existing models of multilingual sentence embeddings require large parallel
data resources which are not available for low-resource languages. We propose a
novel unsupervised method to derive multilingual sentence embeddings relying
only on monolingual data. We first produce a synthetic parallel corpus using
unsupervised machine translation, and use it to fine-tune a pretrained
cross-lingual masked language model (XLM) to derive the multilingual sentence
representations. The quality of the representations is evaluated on two
parallel corpus mining tasks with improvements of up to 22 F1 points over
vanilla XLM. In addition, we observe that a single synthetic bilingual corpus
is able to improve results for other language pairs.
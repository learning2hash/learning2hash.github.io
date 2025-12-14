---
layout: publication
title: Massively Multilingual Sentence Embeddings For Zero-shot Cross-lingual Transfer
  And Beyond
authors: Mikel Artetxe, Holger Schwenk
conference: Transactions of the Association for Computational Linguistics
year: 2018
bibkey: artetxe2018massively
citations: 723
additional_links: [{name: Code, url: 'https://github.com/facebookresearch/LASER'},
  {name: Paper, url: 'https://arxiv.org/abs/1812.10464'}]
tags: [Few-shot & Zero-shot, Similarity Search, Datasets, TACL, ACL]
short_authors: Mikel Artetxe, Holger Schwenk
---
We introduce an architecture to learn joint multilingual sentence
representations for 93 languages, belonging to more than 30 different families
and written in 28 different scripts. Our system uses a single BiLSTM encoder
with a shared BPE vocabulary for all languages, which is coupled with an
auxiliary decoder and trained on publicly available parallel corpora. This
enables us to learn a classifier on top of the resulting embeddings using
English annotated data only, and transfer it to any of the 93 languages without
any modification. Our experiments in cross-lingual natural language inference
(XNLI dataset), cross-lingual document classification (MLDoc dataset) and
parallel corpus mining (BUCC dataset) show the effectiveness of our approach.
We also introduce a new test set of aligned sentences in 112 languages, and
show that our sentence embeddings obtain strong results in multilingual
similarity search even for low-resource languages. Our implementation, the
pre-trained encoder and the multilingual test set are available at
https://github.com/facebookresearch/LASER
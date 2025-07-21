---
layout: publication
title: Massively Multilingual Sentence Embeddings for Zero-Shot Cross-Lingual Transfer
  and Beyond
authors: Artetxe Mikel, Schwenk Holger
conference: Transactions of the Association for Computational Linguistics
year: 2019
bibkey: artetxe2019massively
citations: 747
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1812.10464'}]
tags: ["Few-Shot-&-Zero-Shot"]
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
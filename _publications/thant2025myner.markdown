---
layout: publication
title: 'Myner: Contextualized Burmese Named Entity Recognition With Bidirectional
  LSTM And Fasttext Embeddings Via Joint Training With POS Tagging'
authors: Kaung Lwin Thant, Kwankamol Nongpong, Ye Kyaw Thu, Thura Aung, Khaing Hsu
  Wai, Thazin Myint Oo
conference: 2025 IEEE International Conference on Cybernetics and Innovations (ICCI)
year: 2025
bibkey: thant2025myner
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2504.04038'}]
tags: []
short_authors: Thant et al.
---
Named Entity Recognition (NER) involves identifying and categorizing named
entities within textual data. Despite its significance, NER research has often
overlooked low-resource languages like Myanmar (Burmese), primarily due to the
lack of publicly available annotated datasets. To address this, we introduce
myNER, a novel word-level NER corpus featuring a 7-tag annotation scheme,
enriched with Part-of-Speech (POS) tagging to provide additional syntactic
information. Alongside the corpus, we conduct a comprehensive evaluation of NER
models, including Conditional Random Fields (CRF), Bidirectional LSTM
(BiLSTM)-CRF, and their combinations with fastText embeddings in different
settings. Our experiments reveal the effectiveness of contextualized word
embeddings and the impact of joint training with POS tagging, demonstrating
significant performance improvements across models. The traditional CRF
joint-task model with fastText embeddings as a feature achieved the best
result, with a 0.9818 accuracy and 0.9811 weighted F1 score with 0.7429 macro
F1 score. BiLSTM-CRF with fine-tuned fastText embeddings gets the best result
of 0.9791 accuracy and 0.9776 weighted F1 score with 0.7395 macro F1 score.
---
layout: publication
title: Learning Bilingual Sentence Embeddings Via Autoencoding And Computing Similarities
  With A Multilayer Perceptron
authors: Yunsu Kim, Hendrik Rosendahl, Nick Rossenbach, Jan Rosendahl, Shahram Khadivi,
  Hermann Ney
conference: Proceedings of the 4th Workshop on Representation Learning for NLP (RepL4NLP-2019)
year: 2019
bibkey: kim2019learning
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.01942'}]
tags: ["Evaluation"]
short_authors: Kim et al.
---
We propose a novel model architecture and training algorithm to learn
bilingual sentence embeddings from a combination of parallel and monolingual
data. Our method connects autoencoding and neural machine translation to force
the source and target sentence embeddings to share the same space without the
help of a pivot language or an additional transformation. We train a multilayer
perceptron on top of the sentence embeddings to extract good bilingual sentence
pairs from nonparallel or noisy parallel data. Our approach shows promising
performance on sentence alignment recovery and the WMT 2018 parallel corpus
filtering tasks with only a single model.
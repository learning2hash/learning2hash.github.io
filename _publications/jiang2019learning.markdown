---
layout: publication
title: Learning Numeral Embeddings
authors: Chengyue Jiang, Zhonglin Nian, Kaihao Guo, Shanbo Chu, Yinggong Zhao, Libin
  Shen, Kewei Tu
conference: 'Findings of the Association for Computational Linguistics: EMNLP 2020'
year: 2020
bibkey: jiang2019learning
citations: 25
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2001.00003'}]
tags: ["EMNLP"]
short_authors: Jiang et al.
---
Word embedding is an essential building block for deep learning methods for
natural language processing. Although word embedding has been extensively
studied over the years, the problem of how to effectively embed numerals, a
special subset of words, is still underexplored. Existing word embedding
methods do not learn numeral embeddings well because there are an infinite
number of numerals and their individual appearances in training corpora are
highly scarce. In this paper, we propose two novel numeral embedding methods
that can handle the out-of-vocabulary (OOV) problem for numerals. We first
induce a finite set of prototype numerals using either a self-organizing map or
a Gaussian mixture model. We then represent the embedding of a numeral as a
weighted average of the prototype number embeddings. Numeral embeddings
represented in this manner can be plugged into existing word embedding learning
approaches such as skip-gram for training. We evaluated our methods and showed
its effectiveness on four intrinsic and extrinsic tasks: word similarity,
embedding numeracy, numeral prediction, and sequence labeling.
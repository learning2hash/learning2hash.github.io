---
layout: publication
title: 'Whiteningbert: An Easy Unsupervised Sentence Embedding Approach'
authors: Junjie Huang, Duyu Tang, Wanjun Zhong, Shuai Lu, Linjun Shou, Ming Gong,
  Daxin Jiang, Nan Duan
conference: 'Findings of the Association for Computational Linguistics: EMNLP 2021'
year: 2021
bibkey: huang2021whiteningbert
citations: 70
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.01767'}]
tags: ["Datasets", "EMNLP", "Evaluation", "Supervised", "Unsupervised"]
short_authors: Huang et al.
---
Producing the embedding of a sentence in an unsupervised way is valuable to
natural language matching and retrieval problems in practice. In this work, we
conduct a thorough examination of pretrained model based unsupervised sentence
embeddings. We study on four pretrained models and conduct massive experiments
on seven datasets regarding sentence semantics. We have there main findings.
First, averaging all tokens is better than only using [CLS] vector. Second,
combining both top andbottom layers is better than only using top layers.
Lastly, an easy whitening-based vector normalization strategy with less than 10
lines of code consistently boosts the performance.
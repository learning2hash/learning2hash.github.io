---
layout: publication
title: Evaluating Word Embeddings In Multi-label Classification Using Fine-grained
  Name Typing
authors: "Yadollah Yaghoobzadeh, Katharina Kann, Hinrich Sch\xFCtze"
conference: Proceedings of The Third Workshop on Representation Learning for NLP
year: 2018
bibkey: yaghoobzadeh2018evaluating
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.07186'}]
tags: ["Datasets", "Evaluation"]
short_authors: "Yadollah Yaghoobzadeh, Katharina Kann, Hinrich Sch\xFCtze"
---
Embedding models typically associate each word with a single real-valued
vector, representing its different properties. Evaluation methods, therefore,
need to analyze the accuracy and completeness of these properties in
embeddings. This requires fine-grained analysis of embedding subspaces.
Multi-label classification is an appropriate way to do so. We propose a new
evaluation method for word embeddings based on multi-label classification given
a word embedding. The task we use is fine-grained name typing: given a large
corpus, find all types that a name can refer to based on the name embedding.
Given the scale of entities in knowledge bases, we can build datasets for this
task that are complementary to the current embedding evaluation datasets in:
they are very large, contain fine-grained classes, and allow the direct
evaluation of embeddings without confounding factors like sentence context
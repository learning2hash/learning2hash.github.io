---
layout: publication
title: Distributional Inclusion Vector Embedding For Unsupervised Hypernymy Detection
authors: Haw-shiuan Chang, Ziyun Wang, Luke Vilnis, Andrew Mccallum
conference: 'Proceedings of the 2018 Conference of the North American Chapter of the
  Association for Computational Linguistics: Human Language Technologies, Volume 1
  (Long Papers)'
year: 2018
bibkey: chang2017distributional
citations: 44
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1710.00880'}]
tags: ["Unsupervised"]
short_authors: Chang et al.
---
Modeling hypernymy, such as poodle is-a dog, is an important generalization
aid to many NLP tasks, such as entailment, coreference, relation extraction,
and question answering. Supervised learning from labeled hypernym sources, such
as WordNet, limits the coverage of these models, which can be addressed by
learning hypernyms from unlabeled text. Existing unsupervised methods either do
not scale to large vocabularies or yield unacceptably poor accuracy. This paper
introduces distributional inclusion vector embedding (DIVE), a
simple-to-implement unsupervised method of hypernym discovery via per-word
non-negative vector embeddings which preserve the inclusion property of word
contexts in a low-dimensional and interpretable space. In experimental
evaluations more comprehensive than any previous literature of which we are
aware-evaluating on 11 datasets using multiple existing as well as newly
proposed scoring functions-we find that our method provides up to double the
precision of previous unsupervised embeddings, and the highest average
performance, using a much more compact word representation, and yielding many
new state-of-the-art results.
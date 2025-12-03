---
layout: publication
title: 'Item2vec: Neural Item Embedding For Collaborative Filtering'
authors: Oren Barkan, Noam Koenigstein
conference: 2016 IEEE 26th International Workshop on Machine Learning for Signal Processing
  (MLSP)
year: 2016
bibkey: barkan2016item2vec
citations: 73
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1603.04259'}]
tags: ["Recommender Systems", "Tools & Libraries"]
short_authors: Oren Barkan, Noam Koenigstein
---
Many Collaborative Filtering (CF) algorithms are item-based in the sense that
they analyze item-item relations in order to produce item similarities.
Recently, several works in the field of Natural Language Processing (NLP)
suggested to learn a latent representation of words using neural embedding
algorithms. Among them, the Skip-gram with Negative Sampling (SGNS), also known
as word2vec, was shown to provide state-of-the-art results on various
linguistics tasks. In this paper, we show that item-based CF can be cast in the
same framework of neural word embedding. Inspired by SGNS, we describe a method
we name item2vec for item-based CF that produces embedding for items in a
latent space. The method is capable of inferring item-item relations even when
user information is not available. We present experimental results that
demonstrate the effectiveness of the item2vec method and show it is competitive
with SVD.
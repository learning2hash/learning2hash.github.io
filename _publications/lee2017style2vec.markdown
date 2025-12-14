---
layout: publication
title: 'Style2vec: Representation Learning For Fashion Items From Style Sets'
authors: Hanbit Lee, Jinseok Seol, Sang-Goo Lee
conference: Arxiv
year: 2017
bibkey: lee2017style2vec
citations: 29
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1708.04014'}]
tags: [Evaluation, Recommender Systems]
short_authors: Hanbit Lee, Jinseok Seol, Sang-Goo Lee
---
With the rapid growth of online fashion market, demand for effective fashion
recommendation systems has never been greater. In fashion recommendation, the
ability to find items that goes well with a few other items based on style is
more important than picking a single item based on the user's entire purchase
history. Since the same user may have purchased dress suits in one month and
casual denims in another, it is impossible to learn the latent style features
of those items using only the user ratings. If we were able to represent the
style features of fashion items in a reasonable way, we will be able to
recommend new items that conform to some small subset of pre-purchased items
that make up a coherent style set. We propose Style2Vec, a vector
representation model for fashion items. Based on the intuition of
distributional semantics used in word embeddings, Style2Vec learns the
representation of a fashion item using other items in matching outfits as
context. Two different convolutional neural networks are trained to maximize
the probability of item co-occurrences. For evaluation, a fashion analogy test
is conducted to show that the resulting representation connotes diverse fashion
related semantics like shapes, colors, patterns and even latent styles. We also
perform style classification using Style2Vec features and show that our method
outperforms other baselines.
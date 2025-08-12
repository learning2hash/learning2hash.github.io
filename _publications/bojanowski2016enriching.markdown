---
layout: publication
title: Enriching Word Vectors With Subword Information
authors: Piotr Bojanowski, Edouard Grave, Armand Joulin, Tomas Mikolov
conference: Transactions of the Association for Computational Linguistics
year: 2017
bibkey: bojanowski2016enriching
citations: 9435
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1607.04606'}]
tags: ["TACL"]
short_authors: Bojanowski et al.
---
Continuous word representations, trained on large unlabeled corpora are
useful for many natural language processing tasks. Popular models that learn
such representations ignore the morphology of words, by assigning a distinct
vector to each word. This is a limitation, especially for languages with large
vocabularies and many rare words. In this paper, we propose a new approach
based on the skipgram model, where each word is represented as a bag of
character \\(n\\)-grams. A vector representation is associated to each character
\\(n\\)-gram; words being represented as the sum of these representations. Our
method is fast, allowing to train models on large corpora quickly and allows us
to compute word representations for words that did not appear in the training
data. We evaluate our word representations on nine different languages, both on
word similarity and analogy tasks. By comparing to recently proposed
morphological word representations, we show that our vectors achieve
state-of-the-art performance on these tasks.
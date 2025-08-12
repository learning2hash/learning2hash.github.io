---
layout: publication
title: Improve Lexicon-based Word Embeddings By Word Sense Disambiguation
authors: Yuanzhi Ke, Masafumi Hagiwara
conference: Arxiv
year: 2017
bibkey: ke2017improve
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.07628'}]
tags: []
short_authors: Yuanzhi Ke, Masafumi Hagiwara
---
There have been some works that learn a lexicon together with the corpus to
improve the word embeddings. However, they either model the lexicon separately
but update the neural networks for both the corpus and the lexicon by the same
likelihood, or minimize the distance between all of the synonym pairs in the
lexicon. Such methods do not consider the relatedness and difference of the
corpus and the lexicon, and may not be the best optimized. In this paper, we
propose a novel method that considers the relatedness and difference of the
corpus and the lexicon. It trains word embeddings by learning the corpus to
predicate a word and its corresponding synonym under the context at the same
time. For polysemous words, we use a word sense disambiguation filter to
eliminate the synonyms that have different meanings for the context. To
evaluate the proposed method, we compare the performance of the word embeddings
trained by our proposed model, the control groups without the filter or the
lexicon, and the prior works in the word similarity tasks and text
classification task. The experimental results show that the proposed model
provides better embeddings for polysemous words and improves the performance
for text classification.
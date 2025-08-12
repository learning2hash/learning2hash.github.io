---
layout: publication
title: Unsupervised Lemmatization As Embeddings-based Word Clustering
authors: "Rudolf Rosa, Zden\u011Bk \u017Dabokrtsk\xFD"
conference: Arxiv
year: 2019
bibkey: rosa2019unsupervised
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.08528'}]
tags: ["Unsupervised"]
short_authors: "Rudolf Rosa, Zden\u011Bk \u017Dabokrtsk\xFD"
---
We focus on the task of unsupervised lemmatization, i.e. grouping together
inflected forms of one word under one label (a lemma) without the use of
annotated training data. We propose to perform agglomerative clustering of word
forms with a novel distance measure. Our distance measure is based on the
observation that inflections of the same word tend to be similar both
string-wise and in meaning. We therefore combine word embedding cosine
similarity, serving as a proxy to the meaning similarity, with Jaro-Winkler
edit distance. Our experiments on 23 languages show our approach to be
promising, surpassing the baseline on 23 of the 28 evaluation datasets.
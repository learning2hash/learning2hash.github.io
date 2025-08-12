---
layout: publication
title: Contextual Salience For Fast And Accurate Sentence Vectors
authors: Eric Zelikman, Richard Socher
conference: Arxiv
year: 2018
bibkey: zelikman2018contextual
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.08493'}]
tags: ["Unsupervised"]
short_authors: Eric Zelikman, Richard Socher
---
Unsupervised vector representations of sentences or documents are a major
building block for many language tasks such as sentiment classification.
However, current methods are uninterpretable and slow or require large training
datasets. Recent word vector-based proposals implicitly assume that distances
in a word embedding space are equally important, regardless of context. We
introduce contextual salience (CoSal), a measure of word importance that uses
the distribution of context vectors to normalize distances and weights. CoSal
relies on the insight that unusual word vectors disproportionately affect
phrase vectors. A bag-of-words model with CoSal-based weights produces accurate
unsupervised sentence or document representations for classification, requiring
little computation to evaluate and only a single covariance calculation to
``train." CoSal supports small contexts, out-of context words and outperforms
SkipThought on most benchmarks, beats tf-idf on all benchmarks, and is
competitive with the unsupervised state-of-the-art.
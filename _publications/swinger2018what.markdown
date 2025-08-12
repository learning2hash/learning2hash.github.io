---
layout: publication
title: What Are The Biases In My Word Embedding?
authors: Nathaniel Swinger, Maria De-arteaga, Neil Thomas Heffernan Iv, Mark Dm Leiserson,
  Adam Tauman Kalai
conference: Proceedings of the 2019 AAAI/ACM Conference on AI, Ethics, and Society
year: 2019
bibkey: swinger2018what
citations: 82
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1812.08769'}]
tags: ["AAAI"]
short_authors: Swinger et al.
---
This paper presents an algorithm for enumerating biases in word embeddings.
The algorithm exposes a large number of offensive associations related to
sensitive features such as race and gender on publicly available embeddings,
including a supposedly "debiased" embedding. These biases are concerning in
light of the widespread use of word embeddings. The associations are identified
by geometric patterns in word embeddings that run parallel between people's
names and common lower-case tokens. The algorithm is highly unsupervised: it
does not even require the sensitive features to be pre-specified. This is
desirable because: (a) many forms of discrimination--such as racial
discrimination--are linked to social constructs that may vary depending on the
context, rather than to categories with fixed definitions; and (b) it makes it
easier to identify biases against intersectional groups, which depend on
combinations of sensitive features. The inputs to our algorithm are a list of
target tokens, e.g. names, and a word embedding. It outputs a number of Word
Embedding Association Tests (WEATs) that capture various biases present in the
data. We illustrate the utility of our approach on publicly available word
embeddings and lists of names, and evaluate its output using crowdsourcing. We
also show how removing names may not remove potential proxy bias.
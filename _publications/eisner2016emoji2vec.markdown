---
layout: publication
title: 'Emoji2vec: Learning Emoji Representations From Their Description'
authors: "Ben Eisner, Tim Rockt\xE4schel, Isabelle Augenstein, Matko Bo\u0161njak,\
  \ Sebastian Riedel"
conference: Proceedings of The Fourth International Workshop on Natural Language Processing
  for Social Media
year: 2016
bibkey: eisner2016emoji2vec
citations: 250
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1609.08359'}]
tags: []
short_authors: Eisner et al.
---
Many current natural language processing applications for social media rely
on representation learning and utilize pre-trained word embeddings. There
currently exist several publicly-available, pre-trained sets of word
embeddings, but they contain few or no emoji representations even as emoji
usage in social media has increased. In this paper we release emoji2vec,
pre-trained embeddings for all Unicode emoji which are learned from their
description in the Unicode emoji standard. The resulting emoji embeddings can
be readily used in downstream social natural language processing applications
alongside word2vec. We demonstrate, for the downstream task of sentiment
analysis, that emoji embeddings learned from short descriptions outperforms a
skip-gram model trained on a large collection of tweets, while avoiding the
need for contexts in which emoji need to appear frequently in order to estimate
a representation.
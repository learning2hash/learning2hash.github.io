---
layout: publication
title: Frustratingly Easy Meta-embedding -- Computing Meta-embeddings By Averaging
  Source Word Embeddings
authors: Joshua Coates, Danushka Bollegala
conference: 'Proceedings of the 2018 Conference of the North American Chapter of the
  Association for Computational Linguistics: Human Language Technologies, Volume 2
  (Short Papers)'
year: 2018
bibkey: coates2018frustratingly
citations: 96
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.05262'}]
tags: []
short_authors: Joshua Coates, Danushka Bollegala
---
Creating accurate meta-embeddings from pre-trained source embeddings has
received attention lately. Methods based on global and locally-linear
transformation and concatenation have shown to produce accurate
meta-embeddings. In this paper, we show that the arithmetic mean of two
distinct word embedding sets yields a performant meta-embedding that is
comparable or better than more complex meta-embedding learning methods. The
result seems counter-intuitive given that vector spaces in different source
embeddings are not comparable and cannot be simply averaged. We give insight
into why averaging can still produce accurate meta-embedding despite the
incomparability of the source vector spaces.
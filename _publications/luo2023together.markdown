---
layout: publication
title: Together We Make Sense -- Learning Meta-sense Embeddings From Pretrained Static
  Sense Embeddings
authors: Haochen Luo, Yi Zhou, Danushka Bollegala
conference: Arxiv
year: 2023
bibkey: luo2023together
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.19092'}]
tags: []
short_authors: Haochen Luo, Yi Zhou, Danushka Bollegala
---
Sense embedding learning methods learn multiple vectors for a given ambiguous
word, corresponding to its different word senses. For this purpose, different
methods have been proposed in prior work on sense embedding learning that use
different sense inventories, sense-tagged corpora and learning methods.
However, not all existing sense embeddings cover all senses of ambiguous words
equally well due to the discrepancies in their training resources. To address
this problem, we propose the first-ever meta-sense embedding method --
Neighbour Preserving Meta-Sense Embeddings, which learns meta-sense embeddings
by combining multiple independently trained source sense embeddings such that
the sense neighbourhoods computed from the source embeddings are preserved in
the meta-embedding space. Our proposed method can combine source sense
embeddings that cover different sets of word senses. Experimental results on
Word Sense Disambiguation (WSD) and Word-in-Context (WiC) tasks show that the
proposed meta-sense embedding method consistently outperforms several
competitive baselines.
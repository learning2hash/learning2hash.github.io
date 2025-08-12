---
layout: publication
title: Robust Cross-lingual Embeddings From Parallel Sentences
authors: Ali Sabet, Prakhar Gupta, Jean-Baptiste Cordonnier, Robert West, Martin Jaggi
conference: Arxiv
year: 2019
bibkey: sabet2019robust
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.12481'}]
tags: ["Evaluation"]
short_authors: Sabet et al.
---
Recent advances in cross-lingual word embeddings have primarily relied on
mapping-based methods, which project pretrained word embeddings from different
languages into a shared space through a linear transformation. However, these
approaches assume word embedding spaces are isomorphic between different
languages, which has been shown not to hold in practice (S\{\o\}gaard et al.,
2018), and fundamentally limits their performance. This motivates investigating
joint learning methods which can overcome this impediment, by simultaneously
learning embeddings across languages via a cross-lingual term in the training
objective. We propose a bilingual extension of the CBOW method which leverages
sentence-aligned corpora to obtain robust cross-lingual word and sentence
representations. Our approach significantly improves cross-lingual sentence
retrieval performance over all other approaches while maintaining parity with
the current state-of-the-art methods on word-translation. It also achieves
parity with a deep RNN method on a zero-shot cross-lingual document
classification task, requiring far fewer computational resources for training
and inference. As an additional advantage, our bilingual method leads to a much
more pronounced improvement in the the quality of monolingual word vectors
compared to other competing methods.
---
layout: publication
title: Ontology-aware Token Embeddings For Prepositional Phrase Attachment
authors: Pradeep Dasigi, Waleed Ammar, Chris Dyer, Eduard Hovy
conference: 'Proceedings of the 55th Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)'
year: 2017
bibkey: dasigi2017ontology
citations: 25
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.02925'}]
tags: ["COLING", "EMNLP", "Eacl", "LREC", "NAACL", "TACL", "Text Retrieval"]
short_authors: Dasigi et al.
---
Type-level word embeddings use the same set of parameters to represent all
instances of a word regardless of its context, ignoring the inherent lexical
ambiguity in language. Instead, we embed semantic concepts (or synsets) as
defined in WordNet and represent a word token in a particular context by
estimating a distribution over relevant semantic concepts. We use the new,
context-sensitive embeddings in a model for predicting prepositional phrase(PP)
attachments and jointly learn the concept embeddings and model parameters. We
show that using context-sensitive embeddings improves the accuracy of the PP
attachment model by 5.4% absolute points, which amounts to a 34.4% relative
reduction in errors.
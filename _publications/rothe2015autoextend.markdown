---
layout: publication
title: 'Autoextend: Extending Word Embeddings To Embeddings For Synsets And Lexemes'
authors: "Sascha Rothe, Hinrich Sch\xFCtze"
conference: 'Proceedings of the 53rd Annual Meeting of the Association for Computational
  Linguistics and the 7th International Joint Conference on Natural Language Processing
  (Volume 1: Long Papers)'
year: 2015
bibkey: rothe2015autoextend
citations: 225
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1507.01127'}]
tags: []
short_authors: "Sascha Rothe, Hinrich Sch\xFCtze"
---
We present \textit\{AutoExtend\}, a system to learn embeddings for synsets and
lexemes. It is flexible in that it can take any word embeddings as input and
does not need an additional training corpus. The synset/lexeme embeddings
obtained live in the same vector space as the word embeddings. A sparse tensor
formalization guarantees efficiency and parallelizability. We use WordNet as a
lexical resource, but AutoExtend can be easily applied to other resources like
Freebase. AutoExtend achieves state-of-the-art performance on word similarity
and word sense disambiguation tasks.
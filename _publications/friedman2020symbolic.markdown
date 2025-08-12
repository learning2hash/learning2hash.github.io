---
layout: publication
title: 'Symbolic Querying Of Vector Spaces: Probabilistic Databases Meets Relational
  Embeddings'
authors: Tal Friedman, Guy van Den Broeck
conference: Arxiv
year: 2020
bibkey: friedman2020symbolic
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.10029'}]
tags: []
short_authors: Tal Friedman, Guy van Den Broeck
---
We propose unifying techniques from probabilistic databases and relational
embedding models with the goal of performing complex queries on incomplete and
uncertain data. We formalize a probabilistic database model with respect to
which all queries are done. This allows us to leverage the rich literature of
theory and algorithms from probabilistic databases for solving problems. While
this formalization can be used with any relational embedding model, the lack of
a well-defined joint probability distribution causes simple query problems to
become provably hard. With this in mind, we introduce \TO, a relational
embedding model designed to be a tractable probabilistic database, by
exploiting typical embedding assumptions within the probabilistic framework.
Using a principled, efficient inference algorithm that can be derived from its
definition, we empirically demonstrate that \TOs is an effective and general
model for these querying tasks.
---
layout: publication
title: Putting Rdf2vec In Order
authors: Jan Portisch, Heiko Paulheim
conference: Arxiv
year: 2021
bibkey: portisch2021putting
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.05280'}]
tags: ["Evaluation"]
short_authors: Jan Portisch, Heiko Paulheim
---
The RDF2vec method for creating node embeddings on knowledge graphs is based
on word2vec, which, in turn, is agnostic towards the position of context words.
In this paper, we argue that this might be a shortcoming when training RDF2vec,
and show that using a word2vec variant which respects order yields considerable
performance gains especially on tasks where entities of different classes are
involved.
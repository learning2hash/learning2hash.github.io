---
layout: publication
title: Compressed Indexes For Fast Search Of Semantic Data
authors: Raffaele Perego, Giulio Ermanno Pibiri, Rossano Venturini
conference: IEEE Transactions on Knowledge and Data Engineering
year: 2020
bibkey: perego2019compressed
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.07619'}]
tags: []
short_authors: Raffaele Perego, Giulio Ermanno Pibiri, Rossano Venturini
---
The sheer increase in volume of RDF data demands efficient solutions for the
triple indexing problem, that is devising a compressed data structure to
compactly represent RDF triples by guaranteeing, at the same time, fast pattern
matching operations. This problem lies at the heart of delivering good
practical performance for the resolution of complex SPARQL queries on large RDF
datasets. In this work, we propose a trie-based index layout to solve the
problem and introduce two novel techniques to reduce its space of
representation for improved effectiveness. The extensive experimental analysis
conducted over a wide range of publicly available real-world datasets, reveals
that our best space/time trade-off configuration substantially outperforms
existing solutions at the state-of-the-art, by taking 30-60% less space and
speeding up query execution by a factor of 2-81x.
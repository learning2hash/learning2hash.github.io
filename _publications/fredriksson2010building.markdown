---
layout: publication
title: On Building Minimal Automaton For Subset Matching Queries
authors: Kimmo Fredriksson
conference: Information Processing Letters
year: 2010
bibkey: fredriksson2010building
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1004.0902'}]
tags: []
short_authors: Kimmo Fredriksson
---
We address the problem of building an index for a set \(D\) of \(n\) strings,
where each string location is a subset of some finite integer alphabet of size
\(\sigma\), so that we can answer efficiently if a given simple query string
(where each string location is a single symbol) \(p\) occurs in the set. That is,
we need to efficiently find a string \(d \in D\) such that \(p[i] \in d[i]\) for
every \(i\). We show how to build such index in
\(O(n^\{log_\{\sigma/\Delta\}(\sigma)\}log(n))\) average time, where \(\Delta\) is
the average size of the subsets. Our methods have applications e.g.\ in
computational biology (haplotype inference) and music information retrieval.
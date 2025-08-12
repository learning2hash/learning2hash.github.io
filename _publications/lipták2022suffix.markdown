---
layout: publication
title: Suffix Sorting Via Matching Statistics
authors: "Zsuzsanna Lipt\xE1k, Francesco Masillo, Simon J. Puglisi"
conference: Algorithms for Molecular Biology
year: 2024
bibkey: "lipt\xE1k2022suffix"
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.00972'}]
tags: []
short_authors: "Zsuzsanna Lipt\xE1k, Francesco Masillo, Simon J. Puglisi"
---
We introduce a new algorithm for constructing the generalized suffix array of
a collection of highly similar strings. As a first step, we construct a
compressed representation of the matching statistics of the collection with
respect to a reference string. We then use this data structure to distribute
suffixes into a partial order, and subsequently to speed up suffix comparisons
to complete the generalized suffix array. Our experimental evidence with a
prototype implementation (a tool we call sacamats) shows that on string
collections with highly similar strings we can construct the suffix array in
time competitive with or faster than the fastest available methods. Along the
way, we describe a heuristic for fast computation of the matching statistics of
two strings, which may be of independent interest.
---
layout: publication
title: Faster Wavelet Tree Queries
authors: Matteo Ceregini, Florian Kurpicz, Rossano Venturini
conference: 2024 Data Compression Conference (DCC)
year: 2024
bibkey: ceregini2023faster
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.09239'}]
tags: []
short_authors: Matteo Ceregini, Florian Kurpicz, Rossano Venturini
---
Given a text, rank and select queries return the number of occurrences of a
character up to a position (rank) or the position of a character with a given
rank (select). These queries have applications in, e.g., compression,
computational geometry, and most notably pattern matching in the form of the
backward search -- the backbone of many compressed full-text indices.
Currently, in practice, for text over non-binary alphabets, the wavelet tree is
probably the most used data structure for rank and select queries.
  In this paper, we present techniques to speed up queries by a factor of two
(access and select) up to three (rank), compared to the wavelet tree
implementation contained in the widely used Succinct Data Structure Library
(SDSL). To this end, we change the underlying tree structure from a binary tree
to a 4-ary tree and reduce cache misses by approximating rank queries using a
predictive model to prefetch all data required for the actual rank query.
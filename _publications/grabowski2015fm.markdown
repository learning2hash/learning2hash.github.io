---
layout: publication
title: Fm-index For Dummies
authors: Szymon Grabowski, Marcin Raniszewski, Sebastian Deorowicz
conference: Communications in Computer and Information Science
year: 2017
bibkey: grabowski2015fm
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1506.04896'}]
tags: []
short_authors: Szymon Grabowski, Marcin Raniszewski, Sebastian Deorowicz
---
The FM-index is a celebrated compressed data structure for full-text pattern
searching. After the first wave of interest in its theoretical developments, we
can observe a surge of interest in practical FM-index variants in the last few
years. These enhancements are often related to a bit-vector representation,
augmented with an efficient rank-handling data structure. In this work, we
propose a new, cache-friendly, implementation of the rank primitive and
advocate for a very simple architecture of the FM-index, which trades
compression ratio for speed. Experimental results show that our variants are
2--3 times faster than the fastest known ones, for the price of using typically
1.5--5 times more space.
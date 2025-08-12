---
layout: publication
title: 'Rank And Select: Another Lesson Learned'
authors: Szymon Grabowski, Marcin Raniszewski
conference: Information Systems
year: 2017
bibkey: grabowski2016rank
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1605.01539'}]
tags: []
short_authors: Szymon Grabowski, Marcin Raniszewski
---
Rank and select queries on bitmaps are essential building bricks of many
compressed data structures, including text indexes, membership and range
supporting spatial data structures, compressed graphs, and more. Theoretically
considered yet in 1980s, these primitives have also been a subject of vivid
research concerning their practical incarnations in the last decade. We present
a few novel rank/select variants, focusing mostly on speed, obtaining
competitive space-time results in the compressed setting. Our findings can be
summarized as follows: \\((i)\\) no single rank/select solution works best on any
kind of data (ours are optimized for concatenated bit arrays obtained from
wavelet trees for real text datasets), \\((ii)\\) it pays to efficiently handle
blocks consisting of all 0 or all 1 bits, \\((iii)\\) compressed select does not
have to be significantly slower than compressed rank at a comparable memory
use.
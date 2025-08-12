---
layout: publication
title: Sampling The Suffix Array With Minimizers
authors: Szymon Grabowski, Marcin Raniszewski
conference: Lecture Notes in Computer Science
year: 2015
bibkey: grabowski2014sampling
citations: 21
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1406.2348'}]
tags: []
short_authors: Szymon Grabowski, Marcin Raniszewski
---
Sampling (evenly) the suffixes from the suffix array is an old idea trading
the pattern search time for reduced index space. A few years ago Claude et al.
showed an alphabet sampling scheme allowing for more efficient pattern searches
compared to the sparse suffix array, for long enough patterns. A drawback of
their approach is the requirement that sought patterns need to contain at least
one character from the chosen subalphabet. In this work we propose an
alternative suffix sampling approach with only a minimum pattern length as a
requirement, which seems more convenient in practice. Experiments show that our
algorithm achieves competitive time-space tradeoffs on most standard benchmark
data.
---
layout: publication
title: Most Recent Match Queries In On-line Suffix Trees (with Appendix)
authors: N. Jesper Larsson
conference: Arxiv
year: 2014
bibkey: larsson2014most
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1403.0800'}]
tags: []
short_authors: N. Jesper Larsson
---
A suffix tree is able to efficiently locate a pattern in an indexed string,
but not in general the most recent copy of the pattern in an online stream,
which is desirable in some applications. We study the most general version of
the problem of locating a most recent match: supporting queries for arbitrary
patterns, at each step of processing an online stream. We present augmentations
to Ukkonen's suffix tree construction algorithm for optimal-time queries,
maintaining indexing time within a logarithmic factor in the size of the
indexed string. We show that the algorithm is applicable to sliding-window
indexing, and sketch a possible optimization for use in the special case of
Lempel-Ziv compression.
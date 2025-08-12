---
layout: publication
title: On Slicing Sorted Integer Sequences
authors: Giulio Ermanno Pibiri
conference: Arxiv
year: 2019
bibkey: pibiri2019slicing
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1907.01032'}]
tags: []
short_authors: Giulio Ermanno Pibiri
---
Representing sorted integer sequences in small space is a central problem for
large-scale retrieval systems such as Web search engines. Efficient query
resolution, e.g., intersection or random access, is achieved by carefully
partitioning the sequences. In this work we describe and compare two different
partitioning paradigms: partitioning by cardinality and partitioning by
universe. Although the ideas behind such paradigms have been known in the
coding and algorithmic community since many years, inverted index compression
has extensively adopted the former paradigm, whereas the latter has received
only little attention. As a result, an experimental comparison between these
two is missing for the setting of inverted index compression. We also propose
and implement a solution that recursively slices the universe of representation
of a sequence to achieve compact storage and attain to fast query execution.
Albeit larger than some state-of-the-art representations, this slicing approach
substantially improves the performance of list intersections and unions while
operating in compressed space, thus offering an excellent space/time trade-off
for the problem.
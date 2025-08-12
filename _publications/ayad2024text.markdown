---
layout: publication
title: Text Indexing For Long Patterns Using Locally Consistent Anchors
authors: Lorraine A. K. Ayad, Grigorios Loukides, Solon P. Pissis
conference: The VLDB Journal
year: 2025
bibkey: ayad2024text
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.11819'}]
tags: []
short_authors: Lorraine A. K. Ayad, Grigorios Loukides, Solon P. Pissis
---
In many real-world database systems, a large fraction of the data is
represented by strings: sequences of letters over some alphabet. This is
because strings can easily encode data arising from different sources. It is
often crucial to represent such string datasets in a compact form but also to
simultaneously enable fast pattern matching queries. This is the classic text
indexing problem. The four absolute measures anyone should pay attention to
when designing or implementing a text index are: (i) index space; (ii) query
time; (iii) construction space; and (iv) construction time. Unfortunately,
however, most (if not all) widely-used indexes (e.g., suffix tree, suffix
array, or their compressed counterparts) are not optimized for all four
measures simultaneously, as it is difficult to have the best of all four
worlds. Here, we take an important step in this direction by showing that text
indexing with sampling based on locally consistent anchors (lc-anchors) offers
remarkably good performance in all four measures, when we have at hand a lower
bound \\(\ell\\) on the length of the queried patterns -- which is arguably a quite
reasonable assumption in practical applications. Our index offers average-case
guarantees. In our experiments using real benchmark datasets, we show that it
compares favorably based on the four measures to all classic indexes:
(compressed) suffix tree; (compressed) suffix array; and the FM-index. Notably,
we also present a counterpart of our index with worst-case guarantees based on
the lc-anchors notion of partitioning sets. To the best of our knowledge, this
is the first index achieving the best of all worlds in the regime where we have
at hand a lower bound \\(\ell\\) on the length of the queried patterns.
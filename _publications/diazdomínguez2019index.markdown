---
layout: publication
title: An Index For Sequencing Reads Based On The Colored De Bruijn Graph
authors: "Diego Diaz-Dom\xEDnguez"
conference: Lecture Notes in Computer Science
year: 2019
bibkey: "diazdom\xEDnguez2019index"
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.02211'}]
tags: []
short_authors: "Diego Diaz-Dom\xEDnguez"
---
In this article, we show how to transform a colored de Bruijn graph (dBG)
into a practical index for processing massive sets of sequencing reads. Similar
to previous works, we encode an instance of a colored dBG of the set using BOSS
and a color matrix C. To reduce the space requirements, we devise an algorithm
that produces a smaller and more sparse version of C. The novelties in this
algorithm are (i) an incomplete coloring of the graph and (ii) a greedy
coloring approach that tries to reuse the same colors for different strings
when possible. We also propose two algorithms that work on top of the index;
one is for reconstructing reads, and the other is for contig assembly.
Experimental results show that our data structure uses about half the space of
the plain representation of the set (1 Byte per DNA symbol) and that more than
99% of the reads can be reconstructed just from the index.
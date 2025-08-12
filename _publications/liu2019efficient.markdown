---
layout: publication
title: An Efficient Skyline Computation Framework
authors: Rui Liu, Dominique Li
conference: Arxiv
year: 2019
bibkey: liu2019efficient
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.04083'}]
tags: ["Tools & Libraries"]
short_authors: Rui Liu, Dominique Li
---
Skyline computation aims at looking for the set of tuples that are not worse
than any other tuples in all dimensions from a multidimensional database. In
this paper, we present SDI (Skyline on Dimension Index), a dimension indexing
conducted general framework to skyline computation. We prove that to determine
whether a tuple belongs to the skyline, it is enough to compare this tuple with
a bounded subset of skyline tuples in an arbitrary dimensional index, but not
with all existing skyline tuples. Base on SDI, we also show that any skyline
tuple can be used to stop the whole skyline computation process with outputting
the complete set of all skyline tuples. We develop an efficient algorithm
SDI-RS that significantly reduces the skyline computation time, of which the
space and time complexity can be guaranteed. Our experimental evaluation shows
that SDI-RS outperforms the baseline algorithms in general and is especially
very efficient on high-dimensional data.
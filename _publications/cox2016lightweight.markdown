---
layout: publication
title: Lightweight LCP Construction For Very Large Collections Of Strings
authors: Anthony J. Cox, Fabio Garofalo, Giovanna Rosone, Marinella Sciortino
conference: Journal of Discrete Algorithms
year: 2016
bibkey: cox2016lightweight
citations: 25
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1605.04098'}]
tags: []
short_authors: Cox et al.
---
The longest common prefix array is a very advantageous data structure that,
combined with the suffix array and the Burrows-Wheeler transform, allows to
efficiently compute some combinatorial properties of a string useful in several
applications, especially in biological contexts. Nowadays, the input data for
many problems are big collections of strings, for instance the data coming from
"next-generation" DNA sequencing (NGS) technologies. In this paper we present
the first lightweight algorithm (called extLCP) for the simultaneous
computation of the longest common prefix array and the Burrows-Wheeler
transform of a very large collection of strings having any length. The
computation is realized by performing disk data accesses only via sequential
scans, and the total disk space usage never needs more than twice the output
size, excluding the disk space required for the input. Moreover, extLCP allows
to compute also the suffix array of the strings of the collection, without any
other further data structure is needed. Finally, we test our algorithm on real
data and compare our results with another tool capable to work in external
memory on large collections of strings.
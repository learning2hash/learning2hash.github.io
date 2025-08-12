---
layout: publication
title: Lightweight LCP Construction For Next-generation Sequencing Datasets
authors: Markus J. Bauer, Anthony J. Cox, Giovanna Rosone, Marinella Sciortino
conference: Lecture Notes in Computer Science
year: 2012
bibkey: bauer2012lightweight
citations: 29
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1305.0160'}]
tags: ["Datasets"]
short_authors: Bauer et al.
---
The advent of "next-generation" DNA sequencing (NGS) technologies has meant
that collections of hundreds of millions of DNA sequences are now commonplace
in bioinformatics. Knowing the longest common prefix array (LCP) of such a
collection would facilitate the rapid computation of maximal exact matches,
shortest unique substrings and shortest absent words. CPU-efficient algorithms
for computing the LCP of a string have been described in the literature, but
require the presence in RAM of large data structures. This prevents such
methods from being feasible for NGS datasets.
  In this paper we propose the first lightweight method that simultaneously
computes, via sequential scans, the LCP and BWT of very large collections of
sequences. Computational results on collections as large as 800 million
100-mers demonstrate that our algorithm scales to the vast sequence collections
encountered in human whole genome sequencing experiments.
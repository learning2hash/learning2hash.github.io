---
layout: publication
title: 'IBB: Fast Burrows-wheeler Transform Construction For Length-diverse DNA Data'
authors: "Enno Adler, Stefan B\xF6ttcher, Rita Hartel, Cederic Alexander Steininger"
conference: Arxiv
year: 2025
bibkey: adler2025ibb
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.01327'}]
tags: ["Memory Efficiency"]
short_authors: Adler et al.
---
The Burrows-Wheeler transform (BWT) is integral to the FM-index, which is
used extensively in text compression, indexing, pattern search, and
bioinformatic problems as de novo assembly and read alignment. Thus, efficient
construction of the BWT in terms of time and memory usage is key to these
applications. We present a novel external algorithm called Improved-Bucket
Burrows-Wheeler transform (IBB) for constructing the BWT of DNA datasets with
highly diverse sequence lengths. IBB uses a right-aligned approach to
efficiently handle sequences of varying lengths, a tree-based data structure to
manage relative insert positions and ranks, and fine buckets to reduce the
necessary amount of input and output to external memory. Our experiments
demonstrate that IBB is 10% to 40% faster than the best existing
state-of-the-art BWT construction algorithms on most datasets while maintaining
competitive memory consumption.
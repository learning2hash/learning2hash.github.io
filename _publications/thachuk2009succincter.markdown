---
layout: publication
title: Succincter Text Indexing With Wildcards
authors: Chris Thachuk
conference: Lecture Notes in Computer Science
year: 2009
bibkey: thachuk2009succincter
citations: 30
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1101.5376'}]
tags: ["Text Retrieval"]
short_authors: Chris Thachuk
---
We study the problem of indexing text with wildcard positions, motivated by
the challenge of aligning sequencing data to large genomes that contain
millions of single nucleotide polymorphisms (SNPs)---positions known to differ
between individuals. SNPs modeled as wildcards can lead to more informed and
biologically relevant alignments. We improve the space complexity of previous
approaches by giving a succinct index requiring \((2 + o(1))n log \sigma + O(n)
+ O(d log n) + O(k log k)\) bits for a text of length \(n\) over an alphabet of
size \(\sigma\) containing \(d\) groups of \(k\) wildcards. A key to the space
reduction is a result we give showing how any compressed suffix array can be
supplemented with auxiliary data structures occupying \(O(n) + O(d log
\frac\{n\}\{d\})\) bits to also support efficient dictionary matching queries. The
query algorithm for our wildcard index is faster than previous approaches using
reasonable working space. More importantly our new algorithm greatly reduces
the query working space to \(O(d m + m log n)\) bits. We note that compared to
previous results this reduces the working space by two orders of magnitude when
aligning short read data to the Human genome.
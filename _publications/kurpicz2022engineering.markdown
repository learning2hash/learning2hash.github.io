---
layout: publication
title: Engineering Compact Data Structures For Rank And Select Queries On Bit Vectors
authors: Florian Kurpicz
conference: Lecture Notes in Computer Science
year: 2022
bibkey: kurpicz2022engineering
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.01149'}]
tags: ["Efficiency", "Memory Efficiency", "Scalability"]
short_authors: Florian Kurpicz
---
Bit vectors are fundamental building blocks of many succinct data structures.
They can be used to represent graphs, are an important part of many text
indices in the form of the wavelet tree, and can be used to encode ordered
sequences of integers as Elias-Fano codes. To do so, two queries have to be
answered: namely rank and select queries. Given a position in the bit vector, a
rank query returns the number of 1-bits before that position. A select query,
given a parameter \(j\), returns the position of the \(j\)-th 1-bit. On a length-n
bit vector, both queries can be answered in \(O(1)\) time and require \(o(n)\) bits
of additional space. In practice, the smallest (uncompressed) rank and select
data structure cs-poppy has a space overhead of \(\approx\) 3.51% [Zhou et al.,
SEA 13]. In this paper, we present an improved rank and select data structure
that has the same space overhead but can answer queries up to 8% (rank) and
16.5% (select) faster compared with cs-poppy.
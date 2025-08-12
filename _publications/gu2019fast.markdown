---
layout: publication
title: Fast Multiple Pattern Cartesian Tree Matching
authors: Geonmo Gu, Siwoo Song, Simone Faro, Thierry Lecroq, Kunsoo Park
conference: Lecture Notes in Computer Science
year: 2020
bibkey: gu2019fast
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.01644'}]
tags: []
short_authors: Gu et al.
---
Cartesian tree matching is the problem of finding all substrings in a given
text which have the same Cartesian trees as that of a given pattern. In this
paper, we deal with Cartesian tree matching for the case of multiple patterns.
We present two fingerprinting methods, i.e., the parent-distance encoding and
the binary encoding. By combining an efficient fingerprinting method and a
conventional multiple string matching algorithm, we can efficiently solve
multiple pattern Cartesian tree matching. We propose three practical algorithms
for multiple pattern Cartesian tree matching based on the Wu-Manber algorithm,
the Rabin-Karp algorithm, and the Alpha Skip Search algorithm, respectively. In
the experiments we compare our solutions against the previous algorithm [18].
Our solutions run faster than the previous algorithm as the pattern lengths
increase. Especially, our algorithm based on Wu-Manber runs up to 33 times
faster.
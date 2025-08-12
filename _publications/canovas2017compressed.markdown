---
layout: publication
title: The Compressed Overlap Index
authors: Rodrigo Canovas, Bastien Cazaux, Eric Rivals
conference: Arxiv
year: 2017
bibkey: canovas2017compressed
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.05613'}]
tags: []
short_authors: Rodrigo Canovas, Bastien Cazaux, Eric Rivals
---
For analysing text algorithms, for computing superstrings, or for testing
random number generators, one needs to compute all overlaps between any pairs
of words in a given set. The positions of overlaps of a word onto itself, or of
two words, are needed to compute the absence probability of a word in a random
text, or the numbers of common words shared by two random texts. In all these
contexts, one needs to compute or to query overlaps between pairs of words in a
given set. For this sake, we designed COvI, a compressed overlap index that
supports multiple queries on overlaps: like computing the correlation of two
words, or listing pairs of words whose longest overlap is maximal among all
possible pairs. COvI stores overlaps in a hierarchical and non-redundant
manner. We propose an implementation that can handle datasets of millions of
words and still answer queries efficiently. Comparison with a baseline solution
- called FullAC - relying on the Aho-Corasick automaton shows that COvI
provides significant advantages. For similar construction times, COvI requires
half the memory FullAC, and still solves complex queries much faster.
---
layout: publication
title: Practical Combinations Of Repetition-aware Data Structures
authors: Djamal Belazzougui, Fabio Cunial, Travis Gagie, Nicola Prezza, Mathieu Raffinot
conference: Arxiv
year: 2016
bibkey: belazzougui2016practical
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1604.06002'}]
tags: []
short_authors: Belazzougui et al.
---
Highly-repetitive collections of strings are increasingly being amassed by
genome sequencing and genetic variation experiments, as well as by storing all
versions of human-generated files, like webpages and source code. Existing
indexes for locating all the exact occurrences of a pattern in a
highly-repetitive string take advantage of a single measure of repetition.
However, multiple, distinct measures of repetition all grow sublinearly in the
length of a highly-repetitive string. In this paper we explore the practical
advantages of combining data structures whose size depends on distinct measures
of repetition. The main ingredient of our structures is the run-length encoded
BWT (RLBWT), which takes space proportional to the number of runs in the
Burrows-Wheeler transform of a string. We describe a range of practical
variants that combine RLBWT with the set of boundaries of the Lempel-Ziv 77
factors of a string, which take space proportional to the number of factors.
Such variants use, respectively, the RLBWT of a string and the RLBWT of its
reverse, or just one RLBWT inside a bidirectional index, or just one RLBWT with
support for unidirectional extraction. We also study the practical advantages
of combining RLBWT with the compact directed acyclic word graph of a string, a
data structure that takes space proportional to the number of one-character
extensions of maximal repeats. Our approaches are easy to implement, and
provide competitive tradeoffs on significant datasets.
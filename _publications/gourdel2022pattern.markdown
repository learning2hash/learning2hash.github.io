---
layout: publication
title: Pattern Matching Under DTW Distance
authors: Garance Gourdel, Anne Driemel, Pierre Peterlongo, Tatiana Starikovskaya
conference: SPIRE String Processing and Information Retrieval Nov 2022 Concepcion
  Chile
year: 2022
bibkey: gourdel2022pattern
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.14669'}]
tags: ["Distance Metric Learning", "Similarity Search"]
short_authors: Gourdel et al.
---
In this work, we consider the problem of pattern matching under the dynamic
time warping (DTW) distance motivated by potential applications in the analysis
of biological data produced by the third generation sequencing. To measure the
DTW distance between two strings, one must "warp" them, that is, double some
letters in the strings to obtain two equal-lengths strings, and then sum the
distances between the letters in the corresponding positions. When the
distances between letters are integers, we show that for a pattern P with m
runs and a text T with n runs: 1. There is an O(m + n)-time algorithm that
computes all locations where the DTW distance from P to T is at most 1; 2.
There is an O(kmn)-time algorithm that computes all locations where the DTW
distance from P to T is at most k. As a corollary of the second result, we also
derive an approximation algorithm for general metrics on the alphabet.
---
layout: publication
title: Finding Motif Sets In Time Series
authors: Anthony Bagnall, Jon Hills, Jason Lines
conference: Arxiv
year: 2014
bibkey: bagnall2014finding
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1407.3685'}]
tags: []
short_authors: Anthony Bagnall, Jon Hills, Jason Lines
---
Time-series motifs are representative subsequences that occur frequently in a
time series; a motif set is the set of subsequences deemed to be instances of a
given motif. We focus on finding motif sets. Our motivation is to detect motif
sets in household electricity-usage profiles, representing repeated patterns of
household usage.
  We propose three algorithms for finding motif sets. Two are greedy algorithms
based on pairwise comparison, and the third uses a heuristic measure of set
quality to find the motif set directly. We compare these algorithms on
simulated datasets and on electricity-usage data. We show that Scan MK, the
simplest way of using the best-matching pair to find motif sets, is less
accurate on our synthetic data than Set Finder and Cluster MK, although the
latter is very sensitive to parameter settings. We qualitatively analyse the
outputs for the electricity-usage data and demonstrate that both Scan MK and
Set Finder can discover useful motif sets in such data.
---
layout: publication
title: Faster Binary Mean Computation Under Dynamic Time Warping
authors: Nathan Schaar, Vincent Froese, Rolf Niedermeier
conference: Arxiv
year: 2020
bibkey: schaar2020faster
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.01178'}]
tags: ["Efficiency"]
short_authors: Nathan Schaar, Vincent Froese, Rolf Niedermeier
---
Many consensus string problems are based on Hamming distance. We replace
Hamming distance by the more flexible (e.g., easily coping with different input
string lengths) dynamic time warping distance, best known from applications in
time series mining. Doing so, we study the problem of finding a mean string
that minimizes the sum of (squared) dynamic time warping distances to a given
set of input strings. While this problem is known to be NP-hard (even for
strings over a three-element alphabet), we address the binary alphabet case
which is known to be polynomial-time solvable. We significantly improve on a
previously known algorithm in terms of worst-case running time. Moreover, we
also show the practical usefulness of one of our algorithms in experiments with
real-world and synthetic data. Finally, we identify special cases solvable in
linear time (e.g., finding a mean of only two binary input strings) and report
some empirical findings concerning combinatorial properties of optimal means.
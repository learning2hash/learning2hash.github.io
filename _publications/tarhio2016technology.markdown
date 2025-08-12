---
layout: publication
title: Technology Beats Algorithms (in Exact String Matching)
authors: Jorma Tarhio, Jan Holub, Emanuele Giaquinta
conference: 'Software: Practice and Experience'
year: 2017
bibkey: tarhio2016technology
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1612.01506'}]
tags: []
short_authors: Jorma Tarhio, Jan Holub, Emanuele Giaquinta
---
More than 120 algorithms have been developed for exact string matching within
the last 40 years. We show by experiments that the \naive\{\} algorithm
exploiting SIMD instructions of modern CPUs (with symbols compared in a special
order) is the fastest one for patterns of length up to about 50 symbols and
extremely good for longer patterns and small alphabets. The algorithm compares
16 or 32 characters in parallel by applying SSE2 or AVX2 instructions,
respectively. Moreover, it uses loop peeling to further speed up the searching
phase. We tried several orders for comparisons of pattern symbols and the
increasing order of their probabilities in the text was the best.
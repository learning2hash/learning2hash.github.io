---
layout: publication
title: A Faster Implementation Of Online Run-length Burrows-wheeler Transform
authors: Tatsuya Ohno, Yoshimasa Takabatake, Tomohiro I, Hiroshi Sakamoto
conference: Lecture Notes in Computer Science
year: 2018
bibkey: ohno2017faster
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1704.05233'}]
tags: ["Efficiency"]
short_authors: Ohno et al.
---
Run-length encoding Burrows-Wheeler Transformed strings, resulting in
Run-Length BWT (RLBWT), is a powerful tool for processing highly repetitive
strings. We propose a new algorithm for online RLBWT working in run-compressed
space, which runs in \\(O(n\lg r)\\) time and \\(O(r\lg n)\\) bits of space, where \\(n\\)
is the length of input string \\(S\\) received so far and \\(r\\) is the number of runs
in the BWT of the reversed \\(S\\). We improve the state-of-the-art algorithm for
online RLBWT in terms of empirical construction time. Adopting the dynamic list
for maintaining a total order, we can replace rank queries in a dynamic wavelet
tree on a run-length compressed string by the direct comparison of labels in a
dynamic list. The empirical result for various benchmarks show the efficiency
of our algorithm, especially for highly repetitive strings.
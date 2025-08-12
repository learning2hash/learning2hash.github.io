---
layout: publication
title: Improved Lower Bounds On The Expected Length Of Longest Common Subsequences
authors: "George T. Heineman, Chase Miller, Daniel Reichman, Andrew Salls, G\xE1bor\
  \ S\xE1rk\xF6zy, Duncan Soiffer"
conference: Arxiv
year: 2024
bibkey: heineman2024improved
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.10925'}]
tags: []
short_authors: Heineman et al.
---
It has been proven that, when normalized by \(n\), the expected length of a
longest common subsequence of \(d\) random strings of length \(n\) over an alphabet
of size \(\sigma\) converges to some constant that depends only on \(d\) and
\(\sigma\). These values are known as the Chv\'\{a\}tal-Sankoff constants, and
determining their exact values is a well-known open problem. Upper and lower
bounds are known for some combinations of \(\sigma\) and \(d\), with the best lower
and upper bounds for the most studied case, \(\sigma=2, d=2\), at \(0.788071\) and
\(0.826280\), respectively. Building off previous algorithms for lower-bounding
the constants, we implement runtime optimizations, parallelization, and an
efficient memory reading and writing scheme to obtain an improved lower bound
of \(0.792665992\) for \(\sigma=2, d=2\). We additionally improve upon almost all
previously reported lower bounds for the Chv\'\{a\}tal-Sankoff constants when
either the size of alphabet, the number of strings, or both are larger than 2.
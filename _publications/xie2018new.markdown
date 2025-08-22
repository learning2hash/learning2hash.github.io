---
layout: publication
title: A New Algorithm For Finding Closest Pair Of Vectors
authors: Ning Xie, Shuai Xu, Yekun Xu
conference: Arxiv
year: 2018
bibkey: xie2018new
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1802.09104'}]
tags: ["Uncategorized"]
short_authors: Ning Xie, Shuai Xu, Yekun Xu
---
Given \(n\) vectors \(x_0, x_1, \ldots, x_\{n-1\}\) in \(\\{0,1\\}^\{m\}\), how to find
two vectors whose pairwise Hamming distance is minimum? This problem is known
as the *Closest Pair Problem*. If these vectors are generated uniformly at
random except two of them are correlated with Pearson-correlation coefficient
\(\rho\), then the problem is called the *Light Bulb Problem*. In this work,
we propose a novel coding-based scheme for the Closest Pair Problem. We design
both randomized and deterministic algorithms, which achieve the best-known
running time when the length of input vectors \(m\) is small and the minimum
distance is very small compared to \(m\). Specifically, the running time of our
randomized algorithm is \(O(nlog^\{2\}n\cdot 2^\{c m\} \cdot \mathrm\{poly\}(m))\) and
the running time of our deterministic algorithm is \(O(nlog\{n\}\cdot 2^\{c' m\}
\cdot \mathrm\{poly\}(m))\), where \(c\) and \(c'\) are constants depending only on
the (relative) distance of the closest pair. When applied to the Light Bulb
Problem, our result yields state-of-the-art deterministic running time when the
Pearson-correlation coefficient \(\rho\) is very large. Specifically, when \(\rho
\geq 0.9933\), our deterministic algorithm runs faster than the previously best
deterministic algorithm (Alman, SOSA 2019).
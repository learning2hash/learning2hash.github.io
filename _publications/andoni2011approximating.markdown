---
layout: publication
title: Approximating Edit Distance In Near-linear Time
authors: Alexandr Andoni, Krzysztof Onak
conference: SIAM Journal on Computing
year: 2012
bibkey: andoni2011approximating
citations: 54
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1109.5635'}]
tags: ["Distance Metric Learning", "Efficiency", "Scalability"]
short_authors: Alexandr Andoni, Krzysztof Onak
---
We show how to compute the edit distance between two strings of length n up
to a factor of 2^\{\~O(sqrt(log n))\} in n^(1+o(1)) time. This is the first
sub-polynomial approximation algorithm for this problem that runs in
near-linear time, improving on the state-of-the-art n^(1/3+o(1)) approximation.
Previously, approximation of 2^\{\~O(sqrt(log n))\} was known only for embedding
edit distance into l_1, and it is not known if that embedding can be computed
in less than quadratic time.
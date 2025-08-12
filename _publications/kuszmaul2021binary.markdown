---
layout: publication
title: Binary Dynamic Time Warping In Linear Time
authors: William Kuszmaul
conference: Arxiv
year: 2021
bibkey: kuszmaul2021binary
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.01108'}]
tags: []
short_authors: William Kuszmaul
---
Dynamic time warping distance (DTW) is a widely used distance measure between
time series \(x, y \in \Sigma^n\). It was shown by Abboud, Backurs, and Williams
that in the *binary case*, where \(|\Sigma| = 2\), DTW can be computed in
time \(O(n^\{1.87\})\). We improve this running time \(O(n)\). Moreover, if \(x\) and
\(y\) are run-length encoded, then there is an algorithm running in time
\(\tilde\{O\}(k + \ell)\), where \(k\) and \(\ell\) are the number of runs in \(x\) and
\(y\), respectively. This improves on the previous best bound of \(O(k\ell)\) due
to Dupont and Marteau.
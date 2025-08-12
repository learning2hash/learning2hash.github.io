---
layout: publication
title: Approximating Text-to-pattern Distance Via Dimensionality Reduction
authors: "Przemys\u0142aw Uzna\u0144ski"
conference: Arxiv
year: 2020
bibkey: "uzna\u0144ski2020approximating"
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.03459'}]
tags: ["Distance Metric Learning"]
short_authors: "Przemys\u0142aw Uzna\u0144ski"
---
Text-to-pattern distance is a fundamental problem in string matching, where
given a pattern of length \(m\) and a text of length \(n\), over an integer
alphabet, we are asked to compute the distance between pattern and the text at
every location. The distance function can be e.g. Hamming distance or \(\ell_p\)
distance for some parameter \(p > 0\). Almost all state-of-the-art exact and
approximate algorithms developed in the past \(\sim 40\) years were using FFT as
a black-box. In this work we present \(\widetilde\{O\}(n/\epsilon^2)\) time
algorithms for \((1\pm\epsilon)\)-approximation of \(ℓ₂\) distances, and
\(\widetilde\{O\}(n/\epsilon^3)\) algorithm for approximation of Hamming and
\(\ell_1\) distances, all without use of FFT. This is independent to the very
recent development by Chan et al. [STOC 2020], where \(O(n/\epsilon^2)\)
algorithm for Hamming distances not using FFT was presented -- although their
algorithm is much more "combinatorial", our techniques apply to other norms
than Hamming.
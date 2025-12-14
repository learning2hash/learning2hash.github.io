---
layout: publication
title: An Illuminating Algorithm For The Light Bulb Problem
authors: Josh Alman
conference: Arxiv
year: 2018
bibkey: alman2018an
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1810.06740'}]
tags: [Hashing Methods, Locality Sensitive Hashing]
short_authors: Josh Alman
---
The Light Bulb Problem is one of the most basic problems in data analysis.
One is given as input \(n\) vectors in \(\\{-1,1\\}^d\), which are all independently
and uniformly random, except for a planted pair of vectors with inner product
at least \(\rho \cdot d\) for some constant \(\rho > 0\). The task is to find the
planted pair. The most straightforward algorithm leads to a runtime of
\(Ω(n^2)\). Algorithms based on techniques like Locality-Sensitive Hashing
achieve runtimes of \(n^\{2 - O(\rho)\}\); as \(\rho\) gets small, these approach
quadratic.
  Building on prior work, we give a new algorithm for this problem which runs
in time \(O(n^\{1.582\} + nd),\) regardless of how small \(\rho\) is. This matches
the best known runtime due to Karppa et al. Our algorithm combines techniques
from previous work on the Light Bulb Problem with the so-called `polynomial
method in algorithm design,' and has a simpler analysis than previous work. Our
algorithm is also easily derandomized, leading to a deterministic algorithm for
the Light Bulb Problem with the same runtime of \(O(n^\{1.582\} + nd),\) improving
previous results.
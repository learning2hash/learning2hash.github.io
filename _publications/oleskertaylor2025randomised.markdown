---
layout: publication
title: A Randomised Approach To Distributed Sorting
authors: Sam Olesker-Taylor
conference: Arxiv
year: 2025
bibkey: oleskertaylor2025randomised
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.05082'}]
tags: []
short_authors: Sam Olesker-Taylor
---
We introduce and analyse a new, extremely simple, randomised sorting
algorithm:
  - choose a pair of indices \(\\{i, j\\}\) according to some distribution \(q\);
  - sort the elements in positions \(i\) and \(j\) of the array in ascending order.
  Choosing \(q_\{\\{i,j\\}\} \propto 1/|j - i|\) yields an order-\(n (log n)^2\)
sorting time. We call it the harmonic sorter.
  The sorter trivially parallelises in the asynchronous setting, yielding a
linear speed-up. We also exhibit a low-communication, synchronous version with
a linear speed-up.
  We compare and contrast this algorithm with other sorters, and discuss some
of its benefits, particularly its robustness and amenability to parallelisation
and distributed computing.
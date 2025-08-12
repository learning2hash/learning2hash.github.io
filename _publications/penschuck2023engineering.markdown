---
layout: publication
title: Engineering Shared-memory Parallel Shuffling To Generate Random Permutations
  In-place
authors: Manuel Penschuck
conference: Arxiv
year: 2023
bibkey: penschuck2023engineering
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.03317'}]
tags: []
short_authors: Manuel Penschuck
---
Shuffling is the process of rearranging a sequence of elements into a random
order such that any permutation occurs with equal probability. It is an
important building block in a plethora of techniques used in virtually all
scientific areas. Consequently considerable work has been devoted to the design
and implementation of shuffling algorithms.
  We engineer, -- to the best of our knowledge -- for the first time, a
practically fast, parallel shuffling algorithm with \(\Oh\{\sqrt\{n\}log n\}\)
parallel depth that requires only poly-logarithmic auxiliary memory. Our
reference implementations in Rust are freely available, easy to include in
other projects, and can process large data sets approaching the size of the
system's memory. In an empirical evaluation, we compare our implementations
with a number of existing solutions on various computer architectures. Our
algorithms consistently achieve the highest through-put on all machines.
Further, we demonstrate that the runtime of our parallel algorithm is
comparable to the time that other algorithms may take to acquire the memory
from the operating system to copy the input.
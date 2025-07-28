---
layout: publication
title: Faster Tuple Lattice Sieving Using Spherical Locality-sensitive Filters
authors: Thijs Laarhoven
conference: Arxiv
year: 2017
bibkey: laarhoven2017faster
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.02828'}]
tags: ["Hashing Methods"]
short_authors: Thijs Laarhoven
---
To overcome the large memory requirement of classical lattice sieving
algorithms for solving hard lattice problems, Bai-Laarhoven-Stehl\'\{e\} [ANTS
2016] studied tuple lattice sieving, where tuples instead of pairs of lattice
vectors are combined to form shorter vectors. Herold-Kirshanova [PKC 2017]
recently improved upon their results for arbitrary tuple sizes, for example
showing that a triple sieve can solve the shortest vector problem (SVP) in
dimension \\(d\\) in time \\(2^\{0.3717d + o(d)\}\\), using a technique similar to
locality-sensitive hashing for finding nearest neighbors.
  In this work, we generalize the spherical locality-sensitive filters of
Becker-Ducas-Gama-Laarhoven [SODA 2016] to obtain space-time tradeoffs for near
neighbor searching on dense data sets, and we apply these techniques to tuple
lattice sieving to obtain even better time complexities. For instance, our
triple sieve heuristically solves SVP in time \\(2^\{0.3588d + o(d)\}\\). For
practical sieves based on Micciancio-Voulgaris' GaussSieve [SODA 2010], this
shows that a triple sieve uses less space and less time than the current best
near-linear space double sieve.
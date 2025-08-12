---
layout: publication
title: Fast Scalable Construction Of (minimal Perfect Hash) Functions
authors: Marco Genuzio, Giuseppe Ottaviano, Sebastiano Vigna
conference: Lecture Notes in Computer Science
year: 2016
bibkey: genuzio2016fast
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1603.04330'}]
tags: ["Hashing Methods"]
short_authors: Marco Genuzio, Giuseppe Ottaviano, Sebastiano Vigna
---
Recent advances in random linear systems on finite fields have paved the way
for the construction of constant-time data structures representing static
functions and minimal perfect hash functions using less space with respect to
existing techniques. The main obstruction for any practical application of
these results is the cubic-time Gaussian elimination required to solve these
linear systems: despite they can be made very small, the computation is still
too slow to be feasible.
  In this paper we describe in detail a number of heuristics and programming
techniques to speed up the resolution of these systems by several orders of
magnitude, making the overall construction competitive with the standard and
widely used MWHC technique, which is based on hypergraph peeling. In
particular, we introduce broadword programming techniques for fast equation
manipulation and a lazy Gaussian elimination algorithm. We also describe a
number of technical improvements to the data structure which further reduce
space usage and improve lookup speed.
  Our implementation of these techniques yields a minimal perfect hash function
data structure occupying 2.24 bits per element, compared to 2.68 for MWHC-based
ones, and a static function data structure which reduces the multiplicative
overhead from 1.23 to 1.03.
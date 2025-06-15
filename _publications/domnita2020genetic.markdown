---
layout: publication
title: 'A Genetic Algorithm For Obtaining Memory Constrained Near-perfect Hashing'
authors: Dan Domnita, Ciprian Oprisa
conference: "Arxiv"
year: 2020
citations: 1
bibkey: domnita2020genetic
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2007.08311'}
tags: ['Hashing Fundamentals', 'Indexing and Efficiency', 'Hashing Methods', 'Applications']
---
The problem of fast items retrieval from a fixed collection is often
encountered in most computer science areas, from operating system components to
databases and user interfaces. We present an approach based on hash tables that
focuses on both minimizing the number of comparisons performed during the
search and minimizing the total collection size. The standard open-addressing
double-hashing approach is improved with a non-linear transformation that can
be parametrized in order to ensure a uniform distribution of the data in the
hash table. The optimal parameter is determined using a genetic algorithm. The
paper results show that near-perfect hashing is faster than binary search, yet
uses less memory than perfect hashing, being a good choice for
memory-constrained applications where search time is also critical.

---
layout: publication
title: Designing A Parallel Suffix Sort
authors: Kunal Chowdhury
conference: Arxiv
year: 2022
bibkey: chowdhury2022designing
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.01475'}]
tags: ["Efficiency", "Scalability"]
short_authors: Kunal Chowdhury
---
Suffix sort plays a critical role in various computational algorithms
including genomics as well as in frequently used day to day software
applications. The sorting algorithm becomes tricky when we have lot of repeated
characters in the string for a given radix. Various innovative implementations
are available in this area e.g., Manber Myers. We present here an analysis that
uses a concept around generalized polynomial factorization to sort these
suffixes. The initial generation of these substring specific polynomial can be
efficiently done using parallel threads and shared memory. The set of distinct
factors and their order are known beforehand, and this helps us to sort the
polynomials (equivalent of strings) accordingly.
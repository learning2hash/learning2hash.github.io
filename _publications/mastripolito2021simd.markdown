---
layout: publication
title: Simd-optimized Search Over Sorted Data
authors: Benjamin Mastripolito, Nicholas Koskelo, Dylan Weatherred, David A. Pimentel,
  Daniel Sheppard, Anna Pietarila Graham, Laura Monroe, Robert Robey
conference: Journal of Computing and Information Science in Engineering
year: 2021
bibkey: mastripolito2021simd
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.03229'}]
tags: ["Efficiency"]
short_authors: Mastripolito et al.
---
Applications often require a fast, single-threaded search algorithm over
sorted data, typical in table-lookup operations. We explore various search
algorithms for a large number of search candidates over a relatively small
array of logarithmically-distributed sorted data. These include an innovative
hash-based search that takes advantage of floating point representation to bin
data by the exponent. Algorithms that can be optimized to take advantage of
SIMD vector instructions are of particular interest. We then conduct a case
study applying our results and analyzing algorithmic performance with the
EOSPAC package. EOSPAC is a table look-up library for manipulation and
interpolation of SESAME equation-of-state data. Our investigation results in a
couple of algorithms with better performance with a best case 8x speedup over
the original EOSPAC Hunt-and-Locate implementation. Our techniques are
generalizable to other instances of search algorithms seeking to get a
performance boost from vectorization.
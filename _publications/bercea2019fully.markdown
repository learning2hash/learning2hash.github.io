---
layout: publication
title: Fully-dynamic Space-efficient Dictionaries And Filters With Constant Number
  Of Memory Accesses
authors: Ioana O. Bercea, Guy Even
conference: Arxiv
year: 2019
bibkey: bercea2019fully
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.05060'}]
tags: []
short_authors: Ioana O. Bercea, Guy Even
---
A fully-dynamic dictionary is a data structure for maintaining sets that
supports insertions, deletions and membership queries. A filter approximates
membership queries with a one-sided error. We present two designs:
  1. The first space-efficient fully-dynamic dictionary that maintains both
sets and random multisets and supports queries, insertions, and deletions with
a constant number of memory accesses in the worst case with high probability.
The comparable dictionary of Arbitman, Naor, and Segev [FOCS 2010] works only
for sets.
  2. By a reduction from our dictionary for random multisets, we obtain a
space-efficient fully-dynamic filter that supports queries, insertions, and
deletions with a constant number of memory accesses in the worst case with high
probability (as long as the false positive probability is \(2^\{-O(w)\}\), where
\(w\) denotes the word length). This is the first in-memory space-efficient
fully-dynamic filter design that provably achieves these properties.
  We also present an application of the techniques used to design our
dictionary to the static Retrieval Problem.
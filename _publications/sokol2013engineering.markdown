---
layout: publication
title: Engineering Small Space Dictionary Matching
authors: Shoshana Marcus Dina Sokol
conference: Arxiv
year: 2013
bibkey: sokol2013engineering
citations: 3
additional_links: [{name: Code, url: 'http://www.sci.brooklyn.cuny.edu/~sokol/dictmatch.html'},
  {name: Paper, url: 'https://arxiv.org/abs/1301.6428'}]
tags: []
short_authors: Shoshana Marcus Dina Sokol
---
The dictionary matching problem is to locate occurrences of any pattern among
a set of patterns in a given text. Massive data sets abound and at the same
time, there are many settings in which working space is extremely limited. We
introduce dictionary matching software for the space-constrained environment
whose running time is close to linear. We use the compressed suffix tree as the
underlying data structure of our algorithm, thus, the working space of our
algorithm is proportional to the optimal compression of the dictionary. We also
contribute a succinct tool for performing constant-time lowest marked ancestor
queries on a tree that is succinctly encoded as a sequence of balanced
parentheses, with linear time preprocessing of the tree. This tool should be
useful in many other applications. Our source code is available at
http://www.sci.brooklyn.cuny.edu/~sokol/dictmatch.html
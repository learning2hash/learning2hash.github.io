---
layout: publication
title: Extending The Burrows-wheeler Transform For Cartesian Tree Matching And Constructing
  It
authors: "Eric M. Osterkamp, Dominik K\xF6ppl"
conference: Arxiv
year: 2024
bibkey: osterkamp2024extending
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.12241'}]
tags: []
short_authors: "Eric M. Osterkamp, Dominik K\xF6ppl"
---
Cartesian tree matching is a form of generalized pattern matching where a
substring of the text matches with the pattern if they share the same Cartesian
tree. This form of matching finds application for time series of stock prices
and can be of interest for melody matching between musical scores. For the
indexing problem, the state-of-the-art data structure is a Burrows-Wheeler
transform based solution due to [Kim and Cho, CPM'21], which uses nearly
succinct space and can count the number of substrings that Cartesian tree match
with a pattern in time linear in the pattern length. The authors address the
construction of their data structure with a straight-forward solution that,
however, requires pointer-based data structures, which asymptotically need more
space than compact solutions [Kim and Cho, CPM'21, Section A.4]. We address
this bottleneck by a construction that requires compact space and has a time
complexity linear in the product of the text length with some logarithmic
terms. Additionally, we can extend this index for indexing multiple circular
texts in the spirit of the extended Burrows-Wheeler transform without
sacrificing the time and space complexities. We present this index in a dynamic
variant, where we pay a logarithmic slowdown and need compact space for the
extra functionality that we can incrementally add texts. Our extended setting
is of interest for finding repetitive motifs common in the aforementioned
applications, independent of offsets and scaling.
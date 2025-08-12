---
layout: publication
title: A Space Lower Bound For Approximate Membership With Duplicate Insertions Or
  Deletions Of Nonelements
authors: Aryan Agarwala, Guy Even
conference: Arxiv
year: 2024
bibkey: agarwala2024space
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.19249'}]
tags: []
short_authors: Aryan Agarwala, Guy Even
---
Designs of data structures for approximate membership queries with
false-positive errors that support both insertions and deletions stipulate the
following two conditions: (1) Duplicate insertions are prohibited, i.e., it is
prohibited to insert an element \(x\) if \(x\) is currently a member of the
dataset. (2) Deletions of nonelements are prohibited, i.e., it is prohibited to
delete \(x\) if \(x\) is not currently a member of the dataset. Under these
conditions, the space required for the approximate representation of a datasets
of cardinality \(n\) with a false-positive probability of \(\epsilon^\{+\}\) is at
most \((1+o(1))n\cdotlog_2 (1/\epsilon^\{+\}) + O(n)\) bits [Bender et al., 2018;
Bercea and Even, 2019].
  We prove that if these conditions are lifted, then the space required for the
approximate representation of datasets of cardinality \(n\) from a universe of
cardinality \(u\) is at least \(\frac 12 \cdot (1-\epsilon^\{+\} -\frac 1n)\cdot
log \binom\{u\}\{n\} -O(n)\) bits.
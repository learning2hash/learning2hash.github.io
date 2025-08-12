---
layout: publication
title: 'Iceberg Hashing: Optimizing Many Hash-table Criteria At Once'
authors: "Michael A. Bender, Alex Conway, Mart\xEDn Farach-colton, William Kuszmaul,\
  \ Guido Tagliavini"
conference: Journal of the ACM
year: 2023
bibkey: bender2021iceberg
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.04548'}]
tags: ["Efficiency", "Hashing Methods"]
short_authors: Bender et al.
---
Despite being one of the oldest data structures in computer science, hash
tables continue to be the focus of a great deal of both theoretical and
empirical research. A central reason for this is that many of the fundamental
properties that one desires from a hash table are difficult to achieve
simultaneously; thus many variants offering different trade-offs have been
proposed.
  This paper introduces Iceberg hashing, a hash table that simultaneously
offers the strongest known guarantees on a large number of core properties.
Iceberg hashing supports constant-time operations while improving on the state
of the art for space efficiency, cache efficiency, and low failure probability.
Iceberg hashing is also the first hash table to support a load factor of up to
\\(1 - o(1)\\) while being stable, meaning that the position where an element is
stored only ever changes when resizes occur. In fact, in the setting where keys
are \\(\Theta(log n)\\) bits, the space guarantees that Iceberg hashing offers,
namely that it uses at most \\(log \binom\{|U|\}\{n\} + O(n log log n)\\) bits to
store \\(n\\) items from a universe \\(U\\), matches a lower bound by Demaine et al.
that applies to any stable hash table.
  Iceberg hashing introduces new general-purpose techniques for some of the
most basic aspects of hash-table design. Notably, our indirection-free
technique for dynamic resizing, which we call waterfall addressing, and our
techniques for achieving stability and very-high probability guarantees, can be
applied to any hash table that makes use of the front-yard/backyard paradigm
for hash table design.
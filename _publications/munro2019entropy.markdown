---
layout: publication
title: Entropy Trees And Range-minimum Queries In Optimal Average-case Space
authors: J. Ian Munro, Sebastian Wild
conference: Arxiv
year: 2019
bibkey: munro2019entropy
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1903.02533'}]
tags: ["Efficiency"]
short_authors: J. Ian Munro, Sebastian Wild
---
The range-minimum query (RMQ) problem is a fundamental data structuring task
with numerous applications. Despite the fact that succinct solutions with
worst-case optimal \(2n+o(n)\) bits of space and constant query time are known,
it has been unknown whether such a data structure can be made adaptive to the
reduced entropy of random inputs (Davoodi et al. 2014). We construct a succinct
data structure with the optimal \(1.736n+o(n)\) bits of space on average for
random RMQ instances, settling this open problem.
  Our solution relies on a compressed data structure for binary trees that is
of independent interest. It can store a (static) binary search tree generated
by random insertions in asymptotically optimal expected space and supports many
queries in constant time. Using an instance-optimal encoding of subtrees, we
furthermore obtain a "hyper-succinct" data structure for binary trees that
improves upon the ultra-succinct representation of Jansson, Sadakane and Sung
(2012).
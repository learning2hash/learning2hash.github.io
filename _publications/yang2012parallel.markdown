---
layout: publication
title: Parallel And Sequential In-place Permuting And Perfect Shuffling Using Involutions
authors: Qingxuan Yang, John Ellis, Khalegh Mamakani, Frank Ruskey
conference: Arxiv
year: 2012
bibkey: yang2012parallel
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1204.1958'}]
tags: []
short_authors: Yang et al.
---
We show that any permutation of \(\{1,2,...,N\}\) can be written as the product
of two involutions. As a consequence, any permutation of the elements of an
array can be performed in-place in parallel in time O(1). In the case where the
permutation is the \(k\)-way perfect shuffle we develop two methods for
efficiently computing such a pair of involutions.
  The first method works whenever \(N\) is a power of \(k\); in this case the time
is O(N) and space \(O(log^2 N)\). The second method applies to the general case
where \(N\) is a multiple of \(k\); here the time is \(O(N log N)\) and the space is
\(O(log^2 N)\). If \(k=2\) the space usage of the first method can be reduced to
\(O(log N)\) on a machine that has a SADD (population count) instruction.
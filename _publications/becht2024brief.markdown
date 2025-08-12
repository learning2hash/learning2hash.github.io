---
layout: publication
title: 'Brief Announcement: Parallel Construction Of Bumped Ribbon Retrieval'
authors: Matthias Becht, Hans-Peter Lehmann, Peter Sanders
conference: Arxiv
year: 2024
bibkey: becht2024brief
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.12365'}]
tags: []
short_authors: Matthias Becht, Hans-Peter Lehmann, Peter Sanders
---
A retrieval data structure stores a static function f : S -> \{0,1\}^r . For
all x in S, it returns the r-bit value f(x), while for other inputs it may
return an arbitrary result. The structure cannot answer membership queries, so
it does not have to encode S. The information theoretic space lower bound for
arbitrary inputs is r|S| bits. Retrieval data structures have widespread
applications. They can be used as an approximate membership filter for S by
storing fingerprints of the keys in S, where they are faster and more space
efficient than Bloom filters. They can also be used as a basic building block
of succinct data structures like perfect hash functions.
  Bumped Ribbon Retrieval (BuRR) [Dillinger et al., SEA'22] is a recently
developed retrieval data structure that is fast to construct with a space
overhead of less than 1%. The idea is to solve a nearly diagonal system of
linear equations to determine a matrix that, multiplied with the hash of each
key, gives the desired output values. During solving, BuRR might bump lines of
the equation system to another layer of the same data structure. While the
paper describes a simple parallel construction based on bumping the keys on
thread boundaries, it does not give an implementation. In this brief
announcement, we now fill this gap.
  Our parallel implementation is transparent to the queries. It achieves a
speedup of 14 on 32 cores for 8-bit filters. The additional space overhead is
105 bytes per thread, or 105 slots. This matches 0.0007% of the total space
consumption when constructing with 1 billion input keys. A large portion of the
construction time is spent on parallel sorting.
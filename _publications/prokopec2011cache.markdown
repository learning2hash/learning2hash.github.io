---
layout: publication
title: Cache-aware Lock-free Concurrent Hash Tries
authors: Aleksandar Prokopec, Phil Bagwell, Martin Odersky
conference: Arxiv
year: 2011
bibkey: prokopec2011cache
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1709.06056'}]
tags: []
short_authors: Aleksandar Prokopec, Phil Bagwell, Martin Odersky
---
This report describes an implementation of a non-blocking concurrent
shared-memory hash trie based on single-word compare-and-swap instructions.
Insert, lookup and remove operations modifying different parts of the hash trie
can be run independent of each other and do not contend. Remove operations
ensure that the unneeded memory is freed and that the trie is kept compact. A
pseudocode for these operations is presented and a proof of correctness is
given -- we show that the implementation is linearizable and lock-free.
Finally, benchmarks are presented which compare concurrent hash trie operations
against the corresponding operations on other concurrent data structures,
showing their performance and scalability.
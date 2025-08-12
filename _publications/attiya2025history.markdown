---
layout: publication
title: History-independent Concurrent Hash Tables
authors: "Hagit Attiya, Michael A. Bender, Mart\xEDn Farach-Colton, Rotem Oshman,\
  \ Noa Schiller"
conference: Proceedings of the 57th Annual ACM Symposium on Theory of Computing
year: 2025
bibkey: attiya2025history
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2503.21016'}]
tags: ["Hashing Methods"]
short_authors: Attiya et al.
---
A history-independent data structure does not reveal the history of
operations applied to it, only its current logical state, even if its internal
state is examined. This paper studies history-independent concurrent
dictionaries, in particular, hash tables, and establishes inherent bounds on
their space requirements.
  This paper shows that there is a lock-free history-independent concurrent
hash table, in which each memory cell stores two elements and two bits, based
on Robin Hood hashing. Our implementation is linearizable, and uses the shared
memory primitive LL/SC. The expected amortized step complexity of the hash
table is \(O(c)\), where \(c\) is an upper bound on the number of concurrent
operations that access the same element, assuming the hash table is not
overpopulated. We complement this positive result by showing that even if we
have only two concurrent processes, no history-independent concurrent
dictionary that supports sets of any size, with wait-free membership queries
and obstruction-free insertions and deletions, can store only two elements of
the set and a constant number of bits in each memory cell. This holds even if
the step complexity of operations on the dictionary is unbounded.
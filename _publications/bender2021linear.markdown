---
layout: publication
title: 'Linear Probing Revisited: Tombstones Mark The Death Of Primary Clustering'
authors: Michael A. Bender, Bradley C. Kuszmaul, William Kuszmaul
conference: "Arxiv"
year: 2021
citations: 3
bibkey: bender2021linear
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2107.01250'}
tags: ['Unsupervised', 'Unimodal', 'Shallow', 'Hashing']
---
First introduced in 1954, linear probing is one of the oldest data structures
in computer science, and due to its unrivaled data locality, it continues to be
one of the fastest hash tables in practice. It is widely believed and taught,
however, that linear probing should never be used at high load factors; this is
because primary-clustering effects cause insertions at load factor \\(1 - 1 /x\\)
to take expected time \\(\Theta(x^2)\\) (rather than the ideal \\(\Theta(x)\\)). The
dangers of primary clustering, first discovered by Knuth in 1963, have been
taught to generations of computer scientists, and have influenced the design of
some of many widely used hash tables.
  We show that primary clustering is not a foregone conclusion. We demonstrate
that small design decisions in how deletions are implemented have dramatic
effects on the asymptotic performance of insertions, so that, even if a hash
table operates continuously at a load factor \\(1 - \Theta(1/x)\\), the expected
amortized cost per operation is \\(\tilde\{O\}(x)\\). This is because tombstones
created by deletions actually cause an anti-clustering effect that combats
primary clustering.
  We also present a new variant of linear probing (which we call graveyard
hashing) that completely eliminates primary clustering on *any* sequence
of operations: if, when an operation is performed, the current load factor is
\\(1 - 1/x\\) for some \\(x\\), then the expected cost of the operation is \\(O(x)\\). One
corollary is that, in the external-memory model with a data blocks of size \\(B\\),
graveyard hashing offers the following remarkable guarantee: at any load factor
\\(1 - 1/x\\) satisfying \\(x = o(B)\\), graveyard hashing achieves \\(1 + o(1)\\) expected
block transfers per operation. Past external-memory hash tables have only been
able to offer a \\(1 + o(1)\\) guarantee when the block size \\(B\\) is at least
\\(Ω(x^2)\\).

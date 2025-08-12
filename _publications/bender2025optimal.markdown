---
layout: publication
title: Optimal Non-oblivious Open Addressing
authors: Michael A. Bender, William Kuszmaul, Renfei Zhou
conference: Proceedings of the 57th Annual ACM Symposium on Theory of Computing
year: 2025
bibkey: bender2025optimal
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2503.13628'}]
tags: ["Hashing Methods"]
short_authors: Michael A. Bender, William Kuszmaul, Renfei Zhou
---
A hash table is said to be open-addressed (or non-obliviously open-addressed)
if it stores elements (and free slots) in an array with no additional metadata.
Intuitively, open-addressed hash tables must incur a space-time tradeoff: The
higher the load factor at which the hash table operates, the longer
insertions/deletions/queries should take.
  In this paper, we show that no such tradeoff exists: It is possible to
construct an open-addressed hash table that supports constant-time operations
even when the hash table is entirely full. In fact, it is even possible to
construct a version of this data structure that: (1) is dynamically resized so
that the number of slots in memory that it uses, at any given moment, is the
same as the number of elements it contains; (2) supports \(O(1)\)-time
operations, not just in expectation, but with high probability; and (3)
requires external access to just \(O(1)\) hash functions that are each just
\(O(1)\)-wise independent.
  Our results complement a recent lower bound by Bender, Kuszmaul, and Zhou
showing that oblivious open-addressed hash tables must incur \(Ω(log log
\epsilon^\{-1\})\)-time operations. The hash tables in this paper are
non-oblivious, which is why they are able to bypass the previous lower bound.
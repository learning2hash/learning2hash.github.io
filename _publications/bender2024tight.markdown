---
layout: publication
title: Tight Bounds For Classical Open Addressing
authors: Michael A. Bender, William Kuszmaul, Renfei Zhou
conference: 2024 IEEE 65th Annual Symposium on Foundations of Computer Science (FOCS)
year: 2024
bibkey: bender2024tight
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.11280'}]
tags: []
short_authors: Michael A. Bender, William Kuszmaul, Renfei Zhou
---
We introduce a classical open-addressed hash table, called rainbow hashing,
that supports a load factor of up to \(1 - \epsilon\), while also supporting
\(O(1)\) expected-time queries, and \(O(log log \epsilon^\{-1\})\) expected-time
insertions and deletions. We further prove that this tradeoff curve is optimal:
any classical open-addressed hash table that supports load factor \(1 -
\epsilon\) must incur \(Ω(log log \epsilon^\{-1\})\) expected time per
operation.
  Finally, we extend rainbow hashing to the setting where the hash table is
dynamically resized over time. Surprisingly, the addition of dynamic resizing
does not come at any time cost -- even while maintaining a load factor of \(\ge
1 - \epsilon\) at all times, we can support \(O(1)\) queries and \(O(log log
\epsilon^\{-1\})\) updates.
  Prior to our work, achieving any time bounds of the form
\(o(\epsilon^\{-1\})\) for all of insertions, deletions, and queries
simultaneously remained an open question.
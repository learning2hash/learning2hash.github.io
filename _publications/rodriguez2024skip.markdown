---
layout: publication
title: 'Skip Hash: A Fast Ordered Map Via Software Transactional Memory'
authors: Matthew Rodriguez, Vitaly Aksenov, Michael Spear
conference: Arxiv
year: 2024
bibkey: rodriguez2024skip
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.07466'}]
tags: ["Scalability"]
short_authors: Matthew Rodriguez, Vitaly Aksenov, Michael Spear
---
Scalable ordered maps must ensure that range queries, which operate over many
consecutive keys, provide intuitive semantics (e.g., linearizability) without
degrading the performance of concurrent insertions and removals. These goals
are difficult to achieve simultaneously when concurrent data structures are
built using only locks and compare-and-swap objects. However, recent
innovations in software transactional memory (STM) allow programmers to assume
that multi-word atomic operations can be fast and simple.
  This paper introduces the skip hash, a new ordered map designed around that
assumption. It combines a skip list and a hash map behind a single abstraction,
resulting in \(O(1)\) overheads for most operations. The skip hash makes use of a
novel range query manager -- again leveraging STM -- to achieve fast,
linearizable range queries that do not inhibit scalability. In performance
evaluation, we show that the skip hash outperforms the state of the art in
almost all cases. This places the skip hash in the uncommon position of being
both exceedingly fast and exceedingly simple.
---
layout: publication
title: Per-bucket Concurrent Rehashing Algorithms
authors: Malakhov Anton
conference: "Arxiv"
year: 2015
bibkey: malakhov2015per
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1509.02235"}
tags: ['ARXIV']
---
This paper describes a generic algorithm for concurrent resizing and on-demand per-bucket rehashing for an extensible hash table. In contrast to known lock-based hash table algorithms the proposed algorithm separates the resizing and rehashing stages so that they neither invalidate existing buckets nor block any concurrent operations. Instead the rehashing work is deferred and split across subsequent operations with the table. The rehashing operation uses bucket-level synchronization only and therefore allows a race condition between lookup and moving operations running in different threads. Instead of using explicit synchronization the algorithm detects the race condition and restarts the lookup operation. In comparison with other lock-based algorithms the proposed algorithm reduces high-level synchronization on the hot path improving performance concurrency and scalability of the table. The response time of the operations is also more predictable. The algorithm is compatible with cache friendly data layouts for buckets and does not depend on any memory reclamation techniques thus potentially achieving additional performance gain with corresponding implementations.

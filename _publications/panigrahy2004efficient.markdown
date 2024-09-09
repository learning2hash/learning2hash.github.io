---
layout: publication
title: "Efficient Hashing with Lookups in two Memory Accesses"
authors: Panigrahy Rina
conference: Arxiv
year: 2004
bibkey: panigrahy2004efficient
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/cs/0407023"}
tags: ['ARXIV']
---
The study of hashing is closely related to the analysis of balls and bins. It is well-known that instead of using a single hash function if we randomly hash a ball into two bins and place it in the smaller of the two, then this dramatically lowers the maximum load on bins. This leads to the concept of two-way hashing where the largest bucket contains $O(\log\log n)$ balls with high probability. The hash look up will now search in both the buckets an item hashes to. Since an item may be placed in one of two buckets, we could potentially move an item after it has been initially placed to reduce maximum load. with a maximum load of We show that by performing moves during inserts, a maximum load of 2 can be maintained on-line, with high probability, while supporting hash update operations. In fact, with $n$ buckets, even if the space for two items are pre-allocated per bucket, as may be desirable in hardware implementations, more than $n$ items can be stored giving a high memory utilization. We also analyze the trade-off between the number of moves performed during inserts and the maximum load on a bucket. By performing at most $h$ moves, we can maintain a maximum load of $O(\frac{\log \log n}{h \log(\log\log n/h)})$. So, even by performing one move, we achieve a better bound than by performing no moves at all.
---
layout: publication
title: Mementohash A Stateful Minimal Memory Best Performing Consistent Hash Algorithm
authors: Coluzzi Massimo, Brocco Amos, Antonucci Alessandro, Leidi Tiziano
conference: "Arxiv"
year: 2023
citations: 1
bibkey: coluzzi2023mementohash
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2306.09783"}
tags: ['ARXIV', 'Independent']
---
Consistent hashing is used in distributed systems and networking applications
to spread data evenly and efficiently across a cluster of nodes. In this paper,
we present MementoHash, a novel consistent hashing algorithm that eliminates
known limitations of state-of-the-art algorithms while keeping optimal
performance and minimal memory usage. We describe the algorithm in detail,
provide a pseudo-code implementation, and formally establish its solid
theoretical guarantees. To measure the efficacy of MementoHash, we compare its
performance, in terms of memory usage and lookup time, to that of
state-of-the-art algorithms, namely, AnchorHash, DxHash, and JumpHash. Unlike
JumpHash, MementoHash can handle random failures. Moreover, MementoHash does
not require fixing the overall capacity of the cluster (as AnchorHash and
DxHash do), allowing it to scale indefinitely. The number of removed nodes
affects the performance of all the considered algorithms. Therefore, we conduct
experiments considering three different scenarios: stable (no removed nodes),
one-shot removals (90% of the nodes removed at once), and incremental removals.
We report experimental results that averaged a varying number of nodes from ten
to one million. Results indicate that our algorithm shows optimal lookup
performance and minimal memory usage in its best-case scenario. It behaves
better than AnchorHash and DxHash in its average-case scenario and at least as
well as those two algorithms in its worst-case scenario. However, the
worst-case scenario for MementoHash occurs when more than 70% of the nodes
fail, which describes a unlikely scenario. Therefore, MementoHash shows the
best performance during the regular life cycle of a cluster.

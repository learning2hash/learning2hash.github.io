---
layout: publication
title: 'Binomialhash: A Constant Time, Minimal Memory Consistent Hash Algorithm'
authors: Massimo Coluzzi, Amos Brocco, Alessandro Antonucci, Tiziano Leidi
conference: "Arxiv"
year: 2024
citations: 0
bibkey: coluzzi2024constant
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2406.19836'}
tags: ['Unimodal', 'Supervised', 'Shallow', 'Hashing']
---
Consistent hashing is a technique for distributing data across a network of
nodes in a way that minimizes reorganization when nodes join or leave the
network. It is extensively applied in modern distributed systems as a
fundamental mechanism for routing and data placement. Similarly, distributed
storage systems rely on consistent hashing for scalable and fault-tolerant data
partitioning. This paper introduces BinomialHash, a consistent hashing
algorithm that executes in constant time and requires minimal memory. We
provide a detailed explanation of the algorithm, present a pseudo-code
implementation, and formally establish its strong theoretical guarantees.
Finally, we compare its performance against state-of-the-art constant-time
consistent hashing algorithms, demonstrating that our solution is both highly
competitive and effective, while also validating the theoretical boundaries.

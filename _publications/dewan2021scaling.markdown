---
layout: publication
title: 'Scaling Shared-memory Data Structures As Distributed Global-view Data Structures In The Partitioned Global Address Space Model'
authors: Garvit Dewan, Louis Jenkins
conference: "Arxiv"
year: 2021
citations: 0
bibkey: dewan2021scaling
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2112.00068'}
tags: ['Indexing and Efficiency', 'Evaluation Metrics', 'Tools and Libraries']
---
The Partitioned Global Address Space (PGAS), a memory model in which the
global address space is explicitly partitioned across compute nodes in a
cluster, strives to bridge the gap between shared-memory and distributed-memory
programming. To further bridge this gap, there has been an adoption of
global-view distributed data structures, such as 'global arrays' or
'distributed arrays'. This work demonstrates how shared-memory data structures
can be modified to scale in distributed memory. Presented in this work is the
Distributed Interlocked Hash Table (DIHT), a global-view distributed map data
structure inpired by the Interlocked Hash Table (IHT). At 64 nodes with 44
cores per node, DIHT provides upto 110x the performance of the Chapel
standard-library HashedDist.

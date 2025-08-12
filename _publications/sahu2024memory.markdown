---
layout: publication
title: Memory-efficient Community Detection On Large Graphs Using Weighted Sketches
authors: Subhajit Sahu
conference: Arxiv
year: 2024
bibkey: sahu2024memory
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.02268'}]
tags: []
short_authors: Subhajit Sahu
---
Community detection in graphs identifies groups of nodes with denser
connections within the groups than between them, and while existing studies
often focus on optimizing detection performance, memory constraints become
critical when processing large graphs on shared-memory systems. We recently
proposed efficient implementations of the Louvain, Leiden, and Label
Propagation Algorithms (LPA) for community detection. However, these incur
significant memory overhead from the use of collision-free per-thread
hashtables. To address this, we introduce memory-efficient alternatives using
weighted Misra-Gries (MG) sketches, which replace the per-thread hashtables,
and reduce memory demands in Louvain, Leiden, and LPA implementations - while
incurring only a minor quality drop (up to 1%) and moderate runtime penalties.
We believe that these approaches, though slightly slower, are well-suited for
parallel processing and could outperform current memory-intensive techniques on
systems with many threads.
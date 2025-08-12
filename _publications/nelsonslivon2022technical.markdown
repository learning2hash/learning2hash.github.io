---
layout: publication
title: 'Technical Report: Bundling Linked Data Structures For Linearizable Range Queries'
authors: Jacob Nelson-Slivon, Ahmed Hassan, Roberto Palmieri
conference: Arxiv
year: 2022
bibkey: nelsonslivon2022technical
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.00874'}]
tags: ["Evaluation"]
short_authors: Jacob Nelson-Slivon, Ahmed Hassan, Roberto Palmieri
---
We present bundled references, a new building block to provide linearizable
range query operations for highly concurrent lock-based linked data structures.
Bundled references allow range queries to traverse a path through the data
structure that is consistent with the target atomic snapshot. We demonstrate
our technique with three data structures: a linked list, skip list, and a
binary search tree. Our evaluation reveals that in mixed workloads, our design
can improve upon the state-of-the-art techniques by 1.2x-1.8x for a skip list
and 1.3x-3.7x for a binary search tree. We also integrate our bundled data
structure into the DBx1000 in-memory database, yielding up to 40% gain over the
same competitors.
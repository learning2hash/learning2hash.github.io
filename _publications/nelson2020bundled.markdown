---
layout: publication
title: 'Bundled References: An Abstraction For Highly-concurrent Linearizable Range
  Queries'
authors: Jacob Nelson, Ahmed Hassan, Roberto Palmieri
conference: Arxiv
year: 2020
bibkey: nelson2020bundled
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.15438'}]
tags: []
short_authors: Jacob Nelson, Ahmed Hassan, Roberto Palmieri
---
We present bundled references, a new building block to provide linearizable
range query operations for highly concurrent linked data structures. Bundled
references allow range queries to traverse a path through the data structure
that is consistent with the target atomic snapshot and is made of the minimal
amount of nodes that should be accessed to preserve linearizability. We
implement our technique into a skip list, a binary search tree, and a linked
list data structure. Our evaluation reveals that in mixed workloads, our design
improves upon the state-of-the-art techniques by 3.9x for a skip list and 2.1x
for a binary search tree. We also integrate our bundled data structure into the
DBx1000 in-memory database, yielding up to 20% gain over the same competitors.
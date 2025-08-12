---
layout: publication
title: Indexing Variation Graphs
authors: "Jouni Sir\xE9n"
conference: 2017 Proceedings of the Ninteenth Workshop on Algorithm Engineering and
  Experiments (ALENEX)
year: 2017
bibkey: "sir\xE9n2016indexing"
citations: 88
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1604.06605'}]
tags: ["Graph Based ANN", "Vector Indexing"]
short_authors: "Jouni Sir\xE9n"
---
Variation graphs, which represent genetic variation within a population, are
replacing sequences as reference genomes. Path indexes are one of the most
important tools for working with variation graphs. They generalize text indexes
to graphs, allowing one to find the paths matching the query string. We propose
using de Bruijn graphs as path indexes, compressing them by merging redundant
subgraphs, and encoding them with the Burrows-Wheeler transform. The resulting
fast, space-efficient, and versatile index is used in the variation graph
toolkit vg.
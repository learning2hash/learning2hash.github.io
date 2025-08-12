---
layout: publication
title: Faster Repetition-aware Compressed Suffix Trees Based On Block Trees
authors: "Manuel C\xE1ceres, Gonzalo Navarro"
conference: Lecture Notes in Computer Science
year: 2019
bibkey: "c\xE1ceres2019faster"
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1902.03274'}]
tags: ["Tree Based ANN"]
short_authors: "Manuel C\xE1ceres, Gonzalo Navarro"
---
Suffix trees are a fundamental data structure in stringology, but their space
usage, though linear, is an important problem for its applications. We design
and implement a new compressed suffix tree targeted to highly repetitive texts,
such as large genomic collections of the same species. Our suffix tree tree
builds on Block Trees, a recent Lempel-Ziv-bounded data structure that captures
the repetitiveness of its input. We use Block Trees to compress the topology of
the suffix tree, and augment the Block Tree nodes with data that speeds up
suffix tree navigation.
  Our compressed suffix tree is slightly larger than previous repetition-aware
suffix trees based on grammars, but outperforms them in time, often by orders
of magnitude. The component that represents the tree topology achieves a speed
comparable to that of general-purpose compressed trees, while using 2.3--10
times less space, and might be of interest in other scenarios.
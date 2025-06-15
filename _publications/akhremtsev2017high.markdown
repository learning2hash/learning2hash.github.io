---
layout: publication
title: 'High-quality Shared-memory Graph Partitioning'
authors: Yaroslav Akhremtsev, Peter Sanders, Christian Schulz
conference: "Arxiv"
year: 2017
citations: 27
bibkey: akhremtsev2017high
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1710.08231'}
tags: ['Cross-Modal', 'Independent', 'Shallow']
---
Partitioning graphs into blocks of roughly equal size such that few edges run
between blocks is a frequently needed operation in processing graphs. Recently,
size, variety, and structural complexity of these networks has grown
dramatically. Unfortunately, previous approaches to parallel graph partitioning
have problems in this context since they often show a negative trade-off
between speed and quality. We present an approach to multi-level shared-memory
parallel graph partitioning that guarantees balanced solutions, shows high
speed-ups for a variety of large graphs and yields very good quality
independently of the number of cores used. For example, on 31 cores, our
algorithm partitions our largest test instance into 16 blocks cutting less than
half the number of edges than our main competitor when both algorithms are
given the same amount of time. Important ingredients include parallel label
propagation for both coarsening and improvement, parallel initial partitioning,
a simple yet effective approach to parallel localized local search, and fast
locality preserving hash tables.

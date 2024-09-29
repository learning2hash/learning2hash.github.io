---
layout: publication
title: Practical Near Neighbor Search Via Group Testing
authors: Joshua Engels, Benjamin Coleman, Anshumali Shrivastava
conference: "Neural Information Processing Systems"
year: 2021
bibkey: engels2021practical
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2021/hash/5248e5118c84beea359b6ea385393661-Abstract.html"}
tags: ['Independent', 'LSH', 'NEURIPS']
---
We present a new algorithm for the approximate near neighbor problem that combines classical ideas from group testing with locality45;sensitive hashing (LSH). We reduce the near neighbor search problem to a group testing problem by designating neighbors as positives non45;neighbors as negatives and approximate membership queries as group tests. We instantiate this framework using distance45;sensitive Bloom Filters to Identify Near45;Neighbor Groups (FLINNG). We prove that FLINNG has sub45;linear query time and show that our algorithm comes with a variety of practical advantages. For example FLINNG can be constructed in a single pass through the data consists entirely of efficient integer operations and does not require any distance computations. We conduct large45;scale experiments on high45;dimensional search tasks such as genome search URL similarity search and embedding search over the massive YFCC100M dataset. In our comparison with leading algorithms such as HNSW and FAISS we find that FLINNG can provide up to a 10x query speedup with substantially smaller indexing time and memory.

---
layout: publication
title: Toward Metric Indexes For Incremental Insertion And Querying
authors: Raff Edward, Nicholas Charles
conference: Arxiv
year: 2018
bibkey: raff2018toward
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1801.05055'}]
tags: ["Efficiency", "Vector-Indexing", "Distance-Metric-Learning", "Datasets"]
short_authors: Raff Edward, Nicholas Charles
---
In this work we explore the use of metric index structures, which accelerate
nearest neighbor queries, in the scenario where we need to interleave
insertions and queries during deployment. This use-case is inspired by a
real-life need in malware analysis triage, and is surprisingly understudied.
Existing literature tends to either focus on only final query efficiency, often
does not support incremental insertion, or does not support arbitrary distance
metrics. We modify and improve three algorithms to support our scenario of
incremental insertion and querying with arbitrary metrics, and evaluate them on
multiple datasets and distance metrics while varying the value of \\(k\\) for the
desired number of nearest neighbors. In doing so we determine that our improved
Vantage-Point tree of Minimum-Variance performs best for this scenario.
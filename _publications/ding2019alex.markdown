---
layout: publication
title: 'ALEX: An Updatable Adaptive Learned Index'
authors: Ding et al.
conference: Proceedings of the 2020 ACM SIGMOD International Conference on Management
  of Data
year: 2019
bibkey: ding2019alex
citations: 224
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.08898'}]
tags: [DATASETS, Evaluation, Efficiency And Optimization]
---
Recent work on "learned indexes" has changed the way we look at the
decades-old field of DBMS indexing. The key idea is that indexes can be thought
of as "models" that predict the position of a key in a dataset. Indexes can,
thus, be learned. The original work by Kraska et al. shows that a learned index
beats a B+Tree by a factor of up to three in search time and by an order of
magnitude in memory footprint. However, it is limited to static, read-only
workloads.
  In this paper, we present a new learned index called ALEX which addresses
practical issues that arise when implementing learned indexes for workloads
that contain a mix of point lookups, short range queries, inserts, updates, and
deletes. ALEX effectively combines the core insights from learned indexes with
proven storage and indexing techniques to achieve high performance and low
memory footprint. On read-only workloads, ALEX beats the learned index from
Kraska et al. by up to 2.2X on performance with up to 15X smaller index size.
Across the spectrum of read-write workloads, ALEX beats B+Trees by up to 4.1X
while never performing worse, with up to 2000X smaller index size. We believe
ALEX presents a key step towards making learned indexes practical for a broader
class of database workloads with dynamic updates.
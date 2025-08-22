---
layout: publication
title: Scalable Blocking For Very Large Databases
authors: Andrew Borthwick, Stephen Ash, Bin Pang, Shehzad Qureshi, Timothy Jones
conference: Communications in Computer and Information Science
year: 2020
bibkey: borthwick2020scalable
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.08285'}]
tags: ["Datasets", "Evaluation", "Hashing Methods", "Locality-Sensitive-Hashing"]
short_authors: Borthwick et al.
---
In the field of database deduplication, the goal is to find approximately
matching records within a database. Blocking is a typical stage in this process
that involves cheaply finding candidate pairs of records that are potential
matches for further processing. We present here Hashed Dynamic Blocking, a new
approach to blocking designed to address datasets larger than those studied in
most prior work. Hashed Dynamic Blocking (HDB) extends Dynamic Blocking, which
leverages the insight that rare matching values and rare intersections of
values are predictive of a matching relationship. We also present a novel use
of Locality Sensitive Hashing (LSH) to build blocking key values for huge
databases with a convenient configuration to control the trade-off between
precision and recall. HDB achieves massive scale by minimizing data movement,
using compact block representation, and greedily pruning ineffective candidate
blocks using a Count-min Sketch approximate counting data structure. We
benchmark the algorithm by focusing on real-world datasets in excess of one
million rows, demonstrating that the algorithm displays linear time complexity
scaling in this range. Furthermore, we execute HDB on a 530 million row
industrial dataset, detecting 68 billion candidate pairs in less than three
hours at a cost of $307 on a major cloud service.
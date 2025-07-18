---
layout: publication
title: Learning Multi-dimensional Indexes
authors: Nathan et al.
conference: Proceedings of the 2020 ACM SIGMOD International Conference on Management
  of Data
year: 2019
bibkey: nathan2019learning
citations: 166
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.01668'}]
tags: [Vector Indexing, Tools & Libraries, Evaluation, DATASETS]
---
Scanning and filtering over multi-dimensional tables are key operations in
modern analytical database engines. To optimize the performance of these
operations, databases often create clustered indexes over a single dimension or
multi-dimensional indexes such as R-trees, or use complex sort orders (e.g.,
Z-ordering). However, these schemes are often hard to tune and their
performance is inconsistent across different datasets and queries. In this
paper, we introduce Flood, a multi-dimensional in-memory index that
automatically adapts itself to a particular dataset and workload by jointly
optimizing the index structure and data storage. Flood achieves up to three
orders of magnitude faster performance for range scans with predicates than
state-of-the-art multi-dimensional indexes or sort orders on real-world
datasets and workloads. Our work serves as a building block towards an
end-to-end learned database system.
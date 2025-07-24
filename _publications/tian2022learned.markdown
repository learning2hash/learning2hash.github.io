---
layout: publication
title: A Learned Index For Exact Similarity Search In Metric Spaces
authors: Yao Tian, Tingyun Yan, Xi Zhao, Kai Huang, Xiaofang Zhou
conference: IEEE Transactions on Knowledge and Data Engineering
year: 2022
bibkey: tian2022learned
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.10028'}]
tags: ["Datasets", "Similarity Search", "Vector Indexing"]
short_authors: Tian et al.
---
Indexing is an effective way to support efficient query processing in large
databases. Recently the concept of learned index, which replaces or complements
traditional index structures with machine learning models, has been actively
explored to reduce storage and search costs. However, accurate and efficient
similarity query processing in high-dimensional metric spaces remains to be an
open challenge. In this paper, we propose a novel indexing approach called LIMS
that uses data clustering, pivot-based data transformation techniques and
learned indexes to support efficient similarity query processing in metric
spaces. In LIMS, the underlying data is partitioned into clusters such that
each cluster follows a relatively uniform data distribution. Data
redistribution is achieved by utilizing a small number of pivots for each
cluster. Similar data are mapped into compact regions and the mapped values are
totally ordinal. Machine learning models are developed to approximate the
position of each data record on disk. Efficient algorithms are designed for
processing range queries and nearest neighbor queries based on LIMS, and for
index maintenance with dynamic updates. Extensive experiments on real-world and
synthetic datasets demonstrate the superiority of LIMS compared with
traditional indexes and state-of-the-art learned indexes.
---
layout: publication
title: On The Merge Of K-nn Graph
authors: Wan-lei Zhao, Hui Wang, Peng-cheng Lin, Chong-wah Ngo
conference: IEEE Transactions on Big Data
year: 2021
bibkey: zhao2019merge
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.00814'}]
tags: ["Datasets", "Evaluation", "Scalability"]
short_authors: Zhao et al.
---
k-nearest neighbor graph is a fundamental data structure in many disciplines
such as information retrieval, data-mining, pattern recognition, and machine
learning, etc. In the literature, considerable research has been focusing on
how to efficiently build an approximate k-nearest neighbor graph (k-NN graph)
for a fixed dataset. Unfortunately, a closely related issue of how to merge two
existing k-NN graphs has been overlooked. In this paper, we address the issue
of k-NN graph merging in two different scenarios. In the first scenario, a
symmetric merge algorithm is proposed to combine two approximate k-NN graphs.
The algorithm facilitates large-scale processing by the efficient merging of
k-NN graphs that are produced in parallel. In the second scenario, a joint
merge algorithm is proposed to expand an existing k-NN graph with a raw
dataset. The algorithm enables the incremental construction of a hierarchical
approximate k-NN graph. Superior performance is attained when leveraging the
hierarchy for NN search of various data types, dimensionality, and distance
measures.
---
layout: publication
title: Search Efficient Binary Network Embedding
authors: Zhang Daokun, Yin Jie, Zhu Xingquan, Zhang Chengqi
conference: ACM Transactions on Knowledge Discovery from Data
year: 2021
bibkey: zhang2019search
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1901.04097'}]
tags: ["Hashing-Methods", "Distance-Metric-Learning", "Scalability", "Similarity-Search", "Memory-Efficiency", "Compact-Codes", "Evaluation"]
short_authors: Zhang et al.
---
Traditional network embedding primarily focuses on learning a continuous
vector representation for each node, preserving network structure and/or node
content information, such that off-the-shelf machine learning algorithms can be
easily applied to the vector-format node representations for network analysis.
However, the learned continuous vector representations are inefficient for
large-scale similarity search, which often involves finding nearest neighbors
measured by distance or similarity in a continuous vector space. In this paper,
we propose a search efficient binary network embedding algorithm called
BinaryNE to learn a binary code for each node, by simultaneously modeling node
context relations and node attribute relations through a three-layer neural
network. BinaryNE learns binary node representations through a stochastic
gradient descent based online learning algorithm. The learned binary encoding
not only reduces memory usage to represent each node, but also allows fast
bit-wise comparisons to support faster node similarity search than using
Euclidean distance or other distance measures. Extensive experiments and
comparisons demonstrate that BinaryNE not only delivers more than 25 times
faster search speed, but also provides comparable or better search quality than
traditional continuous vector based network embedding methods. The binary codes
learned by BinaryNE also render competitive performance on node classification
and node clustering tasks. The source code of this paper is available at
https://github.com/daokunzhang/BinaryNE.
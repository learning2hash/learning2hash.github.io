---
layout: publication
title: 'Hashnwalk: Hash And Random Walk Based Anomaly Detection In Hyperedge Streams'
authors: Geon Lee, Minyoung Choe, Kijung Shin
conference: Proceedings of the Thirty-First International Joint Conference on Artificial
  Intelligence
year: 2022
bibkey: lee2022hashnwalk
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.13822'}]
tags: ["IJCAI"]
short_authors: Geon Lee, Minyoung Choe, Kijung Shin
---
Sequences of group interactions, such as emails, online discussions, and
co-authorships, are ubiquitous; and they are naturally represented as a stream
of hyperedges. Despite their broad potential applications, anomaly detection in
hypergraphs (i.e., sets of hyperedges) has received surprisingly little
attention, compared to that in graphs. While it is tempting to reduce
hypergraphs to graphs and apply existing graph-based methods, according to our
experiments, taking higher-order structures of hypergraphs into consideration
is worthwhile. We propose HashNWalk, an incremental algorithm that detects
anomalies in a stream of hyperedges. It maintains and updates a constant-size
summary of the structural and temporal information about the stream. Using the
summary, which is the form of a proximity matrix, HashNWalk measures the
anomalousness of each new hyperedge as it appears. HashNWalk is (a) Fast: it
processes each hyperedge in near real-time and billions of hyperedges within a
few hours, (b) Space Efficient: the size of the maintained summary is a
predefined constant, (c) Effective: it successfully detects anomalous
hyperedges in real-world hypergraphs.
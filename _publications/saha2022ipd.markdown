---
layout: publication
title: Ipd:an Incremental Prototype Based DBSCAN For Large-scale Data With Cluster
  Representatives
authors: Jayasree Saha, Jayanta Mukherjee
conference: Arxiv
year: 2022
bibkey: saha2022ipd
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2202.07870'}]
tags: ["Scalability"]
short_authors: Jayasree Saha, Jayanta Mukherjee
---
DBSCAN is a fundamental density-based clustering technique that identifies
any arbitrary shape of the clusters. However, it becomes infeasible while
handling big data. On the other hand, centroid-based clustering is important
for detecting patterns in a dataset since unprocessed data points can be
labeled to their nearest centroid. However, it can not detect non-spherical
clusters. For a large data, it is not feasible to store and compute labels of
every samples. These can be done as and when the information is required. The
purpose can be accomplished when clustering act as a tool to identify cluster
representatives and query is served by assigning cluster labels of nearest
representative. In this paper, we propose an Incremental Prototype-based DBSCAN
(IPD) algorithm which is designed to identify arbitrary-shaped clusters for
large-scale data. Additionally, it chooses a set of representatives for each
cluster.
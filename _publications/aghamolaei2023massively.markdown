---
layout: publication
title: Massively-parallel Heat Map Sorting And Applications To Explainable Clustering
authors: Aghamolaei Sepideh, Ghodsi Mohammad
conference: "Arxiv"
year: 2023
bibkey: aghamolaei2023massively
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2309.07486"}
tags: ['ARXIV', 'Graph', 'Unsupervised']
---
Given a set of points labeled with \(k\) labels, we introduce the heat map sorting problem as reordering and merging the points and dimensions while preserving the clusters (labels). A cluster is preserved if it remains connected, i.e., if it is not split into several clusters and no two clusters are merged. We prove the problem is NP-hard and we give a fixed-parameter algorithm with a constant number of rounds in the massively parallel computation model, where each machine has a sublinear memory and the total memory of the machines is linear. We give an approximation algorithm for a NP-hard special case of the problem. We empirically compare our algorithm with k-means and density-based clustering (DBSCAN) using a dimensionality reduction via locality-sensitive hashing on several directed and undirected graphs of email and computer networks.

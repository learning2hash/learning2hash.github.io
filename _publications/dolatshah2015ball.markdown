---
layout: publication
title: Ball-tree Efficient Spatial Indexing For Constrained Nearest-neighbor Search In Metric Spaces
authors: Dolatshah Mohamad, Hadian Ali, Minaei-bidgoli Behrouz
conference: "Arxiv"
year: 2015
bibkey: dolatshah2015ball
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1511.00628"}
tags: ['ARXIV']
---
Emerging location-based systems and data analysis frameworks requires
efficient management of spatial data for approximate and exact search. Exact
similarity search can be done using space partitioning data structures, such as
Kd-tree, R*-tree, and Ball-tree. In this paper, we focus on Ball-tree, an
efficient search tree that is specific for spatial queries which use euclidean
distance. Each node of a Ball-tree defines a ball, i.e. a hypersphere that
contains a subset of the points to be searched.
  In this paper, we propose Ball*-tree, an improved Ball-tree that is more
efficient for spatial queries. Ball*-tree enjoys a modified space partitioning
algorithm that considers the distribution of the data points in order to find
an efficient splitting hyperplane. Also, we propose a new algorithm for KNN
queries with restricted range using Ball*-tree, which performs better than both
KNN and range search for such queries. Results show that Ball*-tree performs
39%-57% faster than the original Ball-tree algorithm.

---
layout: publication
title: Optimization Of Indexing Based On K-nearest Neighbor Graph For Proximity Search
  In High-dimensional Data
authors: Masajiro Iwasaki, Daisuke Miyazaki
conference: Arxiv
year: 2018
bibkey: iwasaki2018optimization
citations: 39
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1810.07355'}]
tags: ["Efficiency", "Graph Based ANN", "Similarity Search", "Vector Indexing"]
short_authors: Masajiro Iwasaki, Daisuke Miyazaki
---
Searching for high-dimensional vector data with high accuracy is an
inevitable search technology for various types of data. Graph-based indexes are
known to reduce the query time for high-dimensional data. To further improve
the query time by using graphs, we focused on the indegrees and outdegrees of
graphs. While a sufficient number of incoming edges (indegrees) are
indispensable for increasing search accuracy, an excessive number of outgoing
edges (outdegrees) should be suppressed so as to not increase the query time.
Therefore, we propose three degree-adjustment methods: static degree adjustment
of not only outdegrees but also indegrees, dynamic degree adjustment with which
outdegrees are determined by the search accuracy users require, and path
adjustment to remove edges that have alternative search paths to reduce
outdegrees. We also show how to obtain optimal degree-adjustment parameters and
that our methods outperformed previous methods for image and textual data.
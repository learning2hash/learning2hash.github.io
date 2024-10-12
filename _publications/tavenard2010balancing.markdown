---
layout: publication
title: Balancing Clusters To Reduce Response Time Variability In Large Scale Image Search
authors: Tavenard Romain Inria - Irisa, Amsaleg Laurent Inria - Irisa, Jégou Hervé Inria - Irisa
conference: "Arxiv"
year: 2010
bibkey: tavenard2010balancing
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1009.4739"}
tags: ['ARXIV']
---
Many algorithms for approximate nearest neighbor search in high-dimensional spaces partition the data into clusters. At query time, in order to avoid exhaustive search, an index selects the few (or a single) clusters nearest to the query point. Clusters are often produced by the well-known \{&#37; raw &#37;\}\\(k\\)\{&#37; endraw &#37;\}-means approach since it has several desirable properties. On the downside, it tends to produce clusters having quite different cardinalities. Imbalanced clusters negatively impact both the variance and the expectation of query response times. This paper proposes to modify \{&#37; raw &#37;\}\\(k\\)\{&#37; endraw &#37;\}-means centroids to produce clusters with more comparable sizes without sacrificing the desirable properties. Experiments with a large scale collection of image descriptors show that our algorithm significantly reduces the variance of response times without seriously impacting the search quality.

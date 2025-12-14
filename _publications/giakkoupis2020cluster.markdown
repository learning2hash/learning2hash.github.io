---
layout: publication
title: 'Cluster-and-conquer: When Randomness Meets Graph Locality'
authors: "George Giakkoupis, Anne-Marie Kermarrec, Olivier Ruas, Fran\xE7ois Ta\xEF\
  ani"
conference: Arxiv
year: 2020
bibkey: giakkoupis2020cluster
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.11497'}]
tags: [Evaluation, Distance Metric Learning, Locality Sensitive Hashing, Datasets]
short_authors: Giakkoupis et al.
---
K-Nearest-Neighbors (KNN) graphs are central to many emblematic data mining
and machine-learning applications. Some of the most efficient KNN graph
algorithms are incremental and local: they start from a random graph, which
they incrementally improve by traversing neighbors-of-neighbors links.
Paradoxically, this random start is also one of the key weaknesses of these
algorithms: nodes are initially connected to dissimilar neighbors, that lie far
away according to the similarity metric. As a result, incremental algorithms
must first laboriously explore spurious potential neighbors before they can
identify similar nodes, and start converging. In this paper, we remove this
drawback with Cluster-and-Conquer (C 2 for short). Cluster-and-Conquer boosts
the starting configuration of greedy algorithms thanks to a novel lightweight
clustering mechanism, dubbed FastRandomHash. FastRandomHash leverages
random-ness and recursion to pre-cluster similar nodes at a very low cost. Our
extensive evaluation on real datasets shows that Cluster-and-Conquer
significantly outperforms existing approaches, including LSH, yielding
speed-ups of up to x4.42 while incurring only a negligible loss in terms of KNN
quality.
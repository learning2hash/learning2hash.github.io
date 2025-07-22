---
layout: publication
title: Solving \(k\)-nearest Neighbor Problem On Multiple Graphics Processors
authors: Kato Kimikazu, Hosino Tikara
conference: 2010 10th IEEE/ACM International Conference on Cluster, Cloud and Grid
  Computing
year: 2010
bibkey: kato2009solving
citations: 37
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/0906.0231'}]
tags: ["Recommender-Systems"]
short_authors: Kato Kimikazu, Hosino Tikara
---
The recommendation system is a software system to predict customers' unknown
preferences from known preferences. In the recommendation system, customers'
preferences are encoded into vectors, and finding the nearest vectors to each
vector is an essential part. This vector-searching part of the problem is
called a \\(k\\)-nearest neighbor problem. We give an effective algorithm to solve
this problem on multiple graphics processor units (GPUs).
  Our algorithm consists of two parts: an \\(N\\)-body problem and a partial sort.
For a algorithm of the \\(N\\)-body problem, we applied the idea of a known
algorithm for the \\(N\\)-body problem in physics, although another trick is need
to overcome the problem of small sized shared memory. For the partial sort, we
give a novel GPU algorithm which is effective for small \\(k\\). In our partial
sort algorithm, a heap is accessed in parallel by threads with a low cost of
synchronization. Both of these two parts of our algorithm utilize maximal power
of coalesced memory access, so that a full bandwidth is achieved.
  By an experiment, we show that when the size of the problem is large, an
implementation of the algorithm on two GPUs runs more than 330 times faster
than a single core implementation on a latest CPU. We also show that our
algorithm scales well with respect to the number of GPUs.
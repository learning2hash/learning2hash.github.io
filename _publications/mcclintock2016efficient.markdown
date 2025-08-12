---
layout: publication
title: Efficient Parallel Algorithms For K-center Clustering
authors: Jessica McClintock, Anthony Wirth
conference: 2016 45th International Conference on Parallel Processing (ICPP)
year: 2016
bibkey: mcclintock2016efficient
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1604.03228'}]
tags: ["Efficiency"]
short_authors: Jessica McClintock, Anthony Wirth
---
The k-center problem is one of several classic NP-hard clustering questions.
For contemporary massive data sets, RAM-based algorithms become impractical.
And although there exist good sequential algorithms for k-center, they are not
easily parallelizable.
  In this paper, we design and implement parallel approximation algorithms for
this problem. We observe that Gonzalez's greedy algorithm can be efficiently
parallelized in several MapReduce rounds; in practice, we find that two rounds
are sufficient, leading to a 4-approximation. We contrast this with an existing
parallel algorithm for k-center that runs in a constant number of rounds, and
offers a 10-approximation. In depth runtime analysis reveals that this scheme
is often slow, and that its sampling procedure only runs if k is sufficiently
small, relative to the input size. To trade off runtime for approximation
guarantee, we parameterize this sampling algorithm, and find in our experiments
that the algorithm is not only faster, but sometimes more effective. Yet the
parallel version of Gonzalez is about 100 times faster than both its sequential
version and the parallel sampling algorithm, barely compromising solution
quality.
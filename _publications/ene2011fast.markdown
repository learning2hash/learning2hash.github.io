---
layout: publication
title: Fast Clustering Using Mapreduce
authors: Alina Ene, Sungjin Im, Benjamin Moseley
conference: Proceedings of the 17th ACM SIGKDD international conference on Knowledge
  discovery and data mining
year: 2011
bibkey: ene2011fast
citations: 221
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1109.1579'}]
tags: ["KDD"]
short_authors: Alina Ene, Sungjin Im, Benjamin Moseley
---
Clustering problems have numerous applications and are becoming more
challenging as the size of the data increases. In this paper, we consider
designing clustering algorithms that can be used in MapReduce, the most popular
programming environment for processing large datasets. We focus on the
practical and popular clustering problems, \(k\)-center and \(k\)-median. We
develop fast clustering algorithms with constant factor approximation
guarantees. From a theoretical perspective, we give the first analysis that
shows several clustering algorithms are in \(\mathcal\{MRC\}^0\), a theoretical
MapReduce class introduced by Karloff et al. \cite\{KarloffSV10\}. Our algorithms
use sampling to decrease the data size and they run a time consuming clustering
algorithm such as local search or Lloyd's algorithm on the resulting data set.
Our algorithms have sufficient flexibility to be used in practice since they
run in a constant number of MapReduce rounds. We complement these results by
performing experiments using our algorithms. We compare the empirical
performance of our algorithms to several sequential and parallel algorithms for
the \(k\)-median problem. The experiments show that our algorithms' solutions are
similar to or better than the other algorithms' solutions. Furthermore, on data
sets that are sufficiently large, our algorithms are faster than the other
parallel algorithms that we tested.
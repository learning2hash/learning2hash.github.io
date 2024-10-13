---
layout: publication
title: A Faster Algorithm For Cuckoo Insertion And Bipartite Matching In Large Graphs
authors: Khosla Megha, Anand Avishek
conference: "Algorithmica"
year: 2016
bibkey: khosla2016faster
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1611.07786"}
tags: ['Graph', 'Independent']
---
Hash tables are ubiquitous in computer science for efficient access to large datasets. However, there is always a need for approaches that offer compact memory utilisation without substantial degradation of lookup performance. Cuckoo hashing is an efficient technique of creating hash tables with high space utilisation and offer a guaranteed constant access time. We are given \(n\) locations and \(m\) items. Each item has to be placed in one of the \(k\ge2\) locations chosen by \(k\) random hash functions. By allowing more than one choice for a single item, cuckoo hashing resembles multiple choice allocations schemes. In addition it supports dynamically changing the location of an item among its possible locations. We propose and analyse an insertion algorithm for cuckoo hashing that runs in \emph\\{linear time\\} with high probability and in expectation. Previous work on total allocation time has analysed breadth first search, and it was shown to be linear only in \emph\\{expectation\\}. Our algorithm finds an assignment (with probability 1) whenever it exists. In contrast, the other known insertion method, known as \emph\\{random walk insertion\\}, may run indefinitely even for a solvable instance. We also present experimental results comparing the performance of our algorithm with the random walk method, also for the case when each location can hold more than one item. As a corollary we obtain a linear time algorithm (with high probability and in expectation) for finding perfect matchings in a special class of sparse random bipartite graphs. We support this by performing experiments on a real world large dataset for finding maximum matchings in general large bipartite graphs. We report an order of magnitude improvement in the running time as compared to the \emph\\{Hopkraft-Karp\\} matching algorithm.

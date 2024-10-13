---
layout: publication
title: Similarity Search In High Dimensions Via Hashing
authors: Gionis A., Indyk, Motwani
conference: "Arxiv"
year: 2024
bibkey: gionis2024similarity
additional_links:
  - {name: "Paper", url: "https://dl.acm.org/citation.cfm?id=997857"}
tags: ['ARXIV']
---
The nearest- or near-neighbor query problems arise in a large variety of database applications, usually in the context of similarity searching. Of late, there has been increasing interest in building search/index structures for performing similarity search over high-dimensional data, e.g., image databases, document collections, time-series databases, and genome databases. Unfortunately,
all known techniques for solving this problem fall prey to the curse of dimensionality. That is, the data structures scale poorly with data dimensionality;
in fact, if the number of dimensions exceeds 10 to 20, searching in k-d trees and related structures involves the inspection of a large fraction of the database, thereby doing no better than brute-force linear search. It has been suggested that since the selection of features and the choice of a distance metric in typical applications is rather heuristic, determining an approximate nearest neighbor should suffice for most practical purposes. In this paper, we examine a novel scheme for approximate similarity search based on hashing. The basic idea is to hash the points from the database so as to ensure that the probability of collision is much higher for objects that are close to each other than for those that are far apart. We provide experimental evidence that our
method gives significant improvement in running time over other methods for searching in highdimensional spaces based on hierarchical tree decomposition.
Experimental results also indicate that our scheme scales well even for a relatively large number of dimensions (more than 50).
